# Copyright 2016 Casey Jaymes

# This file is part of PySCAP.
#
# PySCAP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PySCAP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PySCAP.  If not, see <http://www.gnu.org/licenses/>.

import logging

from expatriate.model.Model import Model
from expatriate.model.decorators import *
from .BenchmarkIdPattern import BenchmarkIdPattern
from expatriate.model.xs.IdType import IdType
from expatriate.model.xs.BooleanType import BooleanType
from expatriate.model.xs.StringType import StringType
from expatriate.model.xs.AnyUriType import AnyUriType
from .StatusType import StatusType
from .TextType import TextType
from .HtmlTextWithSubType import HtmlTextWithSubType
from .NoticeType import NoticeType
from .ReferenceType import ReferenceType
from .PlainTextType import PlainTextType
from .Cpe2IdRefType import Cpe2IdRefType
from .VersionType import VersionType
from .MetadataType import MetadataType
from .ModelType import ModelType
from .ProfileType import ProfileType
from .ValueType import ValueType
from .GroupType import GroupType
from .RuleType import RuleType
from .TestResultType import TestResultType
from .SignatureType import SignatureType

logger = logging.getLogger(__name__)

@attribute(local_name='id', required=True, type=BenchmarkIdPattern)
@attribute(local_name='Id', type=IdType)
@attribute(local_name='resolved', type=BooleanType, default=False)
@attribute(local_name='style', type=StringType)
@attribute(local_name='style-href', type=AnyUriType)
@element(local_name='status', list='statuses', cls=StatusType, min=1, max=None)
@element(namespace='http://purl.org/dc/elements/1.1/', local_name='dc-status', list='dc_statuses', min=0, max=None)
@element(local_name='title', list='titles', cls=TextType, min=0, max=None)
@element(local_name='description', list='descriptions', cls=HtmlTextWithSubType, min=0, max=None)
@element(local_name='notice', dict='notices', cls=NoticeType, min=0, max=None)
@element(local_name='front-matter', list='front_matter', cls=HtmlTextWithSubType, min=0, max=None)
@element(local_name='rear-matter', list='rear_matter', cls=HtmlTextWithSubType, min=0, max=None)
@element(local_name='reference', list='references', cls=ReferenceType, min=0, max=None)
@element(local_name='plain-text', list='plain_texts', cls=PlainTextType, min=0, max=None)
@element(namespace='http://cpe.mitre.org/language/2.0', local_name='platform-specification', min=0, max=1)
@element(local_name='platform', cls=Cpe2IdRefType, min=0, max=None)
@element(local_name='version', cls=VersionType, min=1, max=1)
@element(local_name='metadata', list='metadata', cls=MetadataType, min=0, max=None)
@element(local_name='model', list='models', cls=ModelType, min=0, max=None)
@element(local_name='Profile', cls=ProfileType, min=0, max=None, dict='profiles')
@element(local_name='Value', cls=ValueType, min=0, max=None, dict='values')
@element(local_name='Group', cls=GroupType, min=0, max=None, dict='groups')
@element(local_name='Rule', cls=RuleType, min=0, max=None, dict='rules')
@element(local_name='TestResult', cls=TestResultType, min=0, max=None, dict='tests')
@element(local_name='signature', cls=SignatureType, min=0, max=1)
class BenchmarkType(Model):
    def noticing(self):
        ### Loading.Noticing

        # For each notice property of the Benchmark object, add the notice to
        # the tool’s set of legal notices. If a notice with an identical id
        # value is already a member of the set, then replace it. If the
        # Benchmark’s resolved property is set, then Loading succeeds, otherwise
        # go to the next step: Loading.Resolve.Items.

        for notice in list(self.notices.values()):
            logger.info('Notice: \n' + str(notice))

    def resolve(self):
        if self.resolved:
            return

        ### Loading.Resolve.Items

        for item_id in self.items:
            logger.debug('Resolving item: ' + item_id)
            self.items[item_id].resolve(self)

        ### Loading.Resolve.Profiles

        for profile_id in self.profiles:
            if self.profiles[profile_id].extends:
                logger.debug('Resolving profile: ' + profile_id)
                self.profiles[profile_id].resolve(self)

        ### Loading.Resolve.Abstract

        # For each Item in the Benchmark for which the abstract property is
        # true, remove the Item.
        for item_id in self.items:
            if self.items[item_id].abstract:
                logger.debug('Deleting abstract item: ' + item_id)
                del self.items[item_id]

        # For each Profile in the Benchmark for which the abstract property is
        # true, remove the Profile. Go to the next step:
        # Loading.Resolve.Finalize
        for profile_id in self.profiles:
            if self.profiles[profile_id].abstract:
                logger.debug('Deleting abstract profile: ' + profile_id)
                del self.profiles[profile_id]

        ### Loading.Resolve.Finalize

        # Set the Benchmark resolved property to true; Loading succeeds.
        self.resolved = True

    def process(self, host):
        ### Benchmark.Front

        if 'checklist' not in host.facts:
            host.facts['checklist'] = {}

        if self.id not in host.facts['checklist']:
            host.facts['checklist'][self.id] = {
                'start_time': datetime.datetime.utcnow(),
                'profile': {},
            }

        # Process the properties of the Benchmark object

        # TODO check that if this benchmark has a platform specification identified,
        # that the  target system matches

        # TODO check that if this benchmark has a platform identified, that the
        # target system matches

        ### Benchmark.Profile

        if not hasattr(self, 'selected_profiles'):
            raise ValueError('No profiles have been selected for Benchmark ' + self.id)

        for profile_id in self.selected_profiles:
            logger.info('Selecting profile ' + str(profile_id))
            if profile_id not in host.facts['checklist'][self.id]['profile']:
                host.facts['checklist'][self.id]['profile'][profile_id] = {
                    'start_time': datetime.datetime.utcnow(),
                    'rule': {},
                    'value': {},
                    'scores': [],
                }
            self.profiles[profile_id].apply(host, self)

            ### Benchmark.Content

            # For each Item in the Benchmark object’s items property, initiate
            # Item.Process
            for item in self.items.values():
                item.process(host, self, profile_id)

            if len(self.models) == 0:
                def_model = ModelType(tag_name='model')
                def_model.system = 'urn:xccdf:scoring:default'
                self.models.append(def_model)

            for model in self.models:
                model.score(host, self, profile_id)

            host.facts['checklist'][self.id]['profile'][profile_id]['end_time'] =  datetime.datetime.utcnow()
        ### Benchmark.Back

        # Perform any additional processing of the Benchmark object properties
        host.facts['checklist'][self.id]['end_time'] =  datetime.datetime.utcnow()
