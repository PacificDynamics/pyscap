#!/bin/bash

. lib/db.sh
error_if_no_db
if [[ "x$STIG_DATABASE" == "xmysql" ]]; then
	echo '<result>fail</result><message>The DBMS does not limit the use of resources by priority and not impede the host from servicing processes designated as a higher-priority.</message>'
else
	echo '<result>notchecked</result>'
fi