####################################
# This file provides all possible options for padas.properties file.
# Use this file to configure PADAS instances and their properties.
####################################

####################################
# SETTINGS FOR ALL INSTANCES
####################################

####################################
# Required Settings
# These settings must be defined for each instance regardless of its role.
####################################

padas.instance.role=detect
# Required - detect | transform | manager
# Defines PADAS Component to run for this instance
# Default: detect

bootstrap.servers=localhost:9092
# Required - <string>
# Kafka bootstrap server list with port information.  Multiple servers can be separated by comma.
# Default: localhost:9092

schema.registry.url=http://localhost:8081
# Required - <string>
# Confluent Schema Registry URL
# Default: http://localhost:8081

####################################
# Optional Settings
####################################

padas.application.id=padas-client
# Optional - <string>
# Unique ID for this application cluster.  Used as consumer group ID as well.
# Default: padas-client

padas.home=/opt/padas
# Optional - <string>
# Root folder where PADAS is installed
# Default: /opt/padas

padas.uuid=
# N/A - Automatically assigned
# Universally Unique Identifier for this instance.  Created upon initial start.


####################################
# Advanced Settings
####################################
padas.state.dir=/opt/padas/var/padas-streams-global-stores
# Optional - <string>
# State store directory to keep local RocksDB data
# Default: ${padas.home}/var/padas-streams-global-stores

padas.log.dir=/opt/padas/var/logs
# Optional - <string>
# Directory for logs
# Default: ${padas.home}/var/logs

num.stream.threads=1
# Optional - <integer>
# Number of threads to run in parallel for this streaming instance.  
# This setting is only applicable for 'detect' and 'transform' roles
# Default: 1

####################################
# SETTINGS FOR MANAGER
# Following settings are only used by manager instance
####################################

####################################
# Required Settings
####################################

padas.license=
# Required - <string>
# This setting is only used by 'manager' role.
# License string should be a pipe '|' delimeted string containing 
# version, entitlement, startdate, enddate, quota, type, and signature
# Default: none

####################################
# Web Settings
####################################
server.port=9000
# Optional - <integer>
# Port number for Manager web interface
# Default: 9000

server.ssl.enabled=true
# Optional - <boolean>
# Enable SSL for Manager web interface with the server.ssl.* configuration
# Default: true

server.ssl.key-alias=padas_ssl_cert
# Optional - <string>
# SSL Key alias for certificate
# Default: padas_ssl_cert

server.ssl.key-password=password
# Optional - <string>
# SSL Key password
# Default: password

server.ssl.key-store-password=password
# Optional - <string>
# SSL Key Store password
# Default: password

server.ssl.key-store=classpath:ssl-server.jks
# Optional - <string>
# SSL Key Store path, this should be the full path (e.g. /opt/padas/etc/certs/my.jks)
# Default: reads from built-in classpath

server.ssl.key-store-provider=SUN
# Optional - <string>
# SSL Key Store provider
# Default: SUN

server.ssl.key-store-type=JKS
# Optional - <string>
# SSL Key Store type
# Default: padas_ssl_cert


####################################
####################################
# Informational Settings
# Following settings are provided here for informational purposes only and any
# configuration changes made here will NOT be read.  All configuration changes
# should be done via Manager Web Interface, which also allows changing/updating 
# the following properties.  Please refer to PADAS Documentation for details.
####################################

####################################
# SETTINGS FOR DETECT
# Following settings are only used to detect role where matching events are converted to alerts
####################################
event.datetime.pattern=yyyy-MM-dd'T'HH:mm:ss.SSSZ
# Optional - <string>
# Padas Events timestamp pattern.  It is recommended to leave this at its default value.
# You may play with the pattern, but ALWAYS include the Zone Offset (Z)
# Example timestamp: 2021-05-19T09:05:01.337+0300
# It is used to create a java.time.ZonedDateTime by parsing the event in the value message
# For more details on pattern formatting, please visit https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html
# Default: yyyy-MM-dd'T'HH:mm:ss.SSSZ

alerts.topic.omit.rawdata=false
# Optional - <boolean>
# Define whether to omit raw data from Events when generating alerts
# Default: false

alerts.topic.omit.jsondata=false
# Optional - <boolean>
# Define whether to omit JSON data from Events when generating alerts
# Default: false


####################################
# SETTINGS FOR TRANFORM
# Following settings are only used to transform input topics to PADAS Events
####################################

####################################
# Required Settings
####################################

# N must start with 0 and must be incremented by 1 (e.g. 0,1,2,3, etc.)

input.topic.N.name= 
# Required - <string>
# Input topic name to read from
# Default: none

####################################
# Optional Settings
# While the following settings are optional, we recommend reviewing them for production.
# Each input may be expected to behave differently with various fields.
####################################

input.topic.N.enabled=true
# Required - <boolean>
# Defines whether this transformation is enabled or not
# Default: true

input.topic.N.rawdata.field=
# Optional - <string>
# Defines the extracted field that has the raw event data.  If undefined, all event value is used.
# Default: event value

input.topic.N.omit.rawdata=false 
# Optional - <boolean>
# Defines whether to omit raw data when populating PADAS Events
# Default: false

input.topic.N.extraction=json
# Optional - json | regex
# Defines how to extract fields from input topic.  If regex is specified, regex definition is used for extraction.
# Default: json

input.topic.N.regex=
# Optional - <string>
# Defines a regular expression on how to extract fields from the topic's value.  Applicable only when extraction is set to regex.
# Only named-capturing groups are allowed currently.  Please refer to https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/regex/Pattern.html for details.
# Example for apache: ^(?<host>[^ ]*) [^ ]* (?<user>[^ ]*) \[(?<time>[^\]]*)\] "(?<method>\S+)(?: +(?<path>[^\"]*?)(?: +\S*)?)?" (?<code>[^ ]*) (?<size>[^ ]*)(?: "(?<referer>[^\"]*)" "(?<agent>[^\"]*)")?$
# Default: none

input.topic.N.timestamp.field=
# Optional - <string>
# Defines the extracted field to be used as the timestamp of the event.  If left empty or unspecified, current time is used.
# Default: none

input.topic.N.timestamp.pattern=yyyy-MM-dd'T'HH:mm:ss.SSSZ
# Optional - <string>
# Defines the pattern for timestamp field, if specified.
# Default: "yyyy-MM-dd'T'HH:mm:ss.SSSZ"

input.topic.N.host.name=
# Optional - <string>
# Defines the hostname for this event (static).  This setting is only applicable if host.field is NOT specified.
# Default: current hostname

input.topic.N.host.field=
# Optional - <string>
# Defines the field to be used as hostname for this event (dynamic).  This setting overwrites host.name
# Default: none

input.topic.N.source.name=
# Optional - <string>
# Defines the source for this event (static).  This setting is only applicable if source.field is NOT specified.
# Default: topic name

input.topic.N.source.field=
# Optional - <string>
# Defines the field to be used as source for this event (dynamic).  This setting overwrites source.name
# Default: none

input.topic.N.datamodel.name=
# Optional - <string>
# Defines the datamodel for this event (static).  This setting is only applicable if datamodel.field is NOT specified.
# Default: topic name

input.topic.N.datamodel.field=
# Optional - <string>
# Defines the field to be used as datamodel for this event (dynamic).  This setting overwrites datamodel.name
# Default: none

input.topic.N.src.value=
# Optional - <string>
# Defines the source host/IP address for this event (static).  This setting is only applicable if src.field is NOT specified.
# Default: none

input.topic.N.src.field=
# Optional - <string>
# Defines the field to be used as source host/IP address for this event (dynamic).  This setting overwrites src.value
# Default: none

input.topic.N.dest.value=
# Optional - <string>
# Defines the destination host/IP address for this event (static).  This setting is only applicable if dest.field is NOT specified.
# Default: none

input.topic.N.dest.field=
# Optional - <string>
# Defines the field to be used as destination host/IP address for this event (dynamic).  This setting overwrites dest.value
# Default: none

input.topic.N.user.value=
# Optional - <string>
# Defines the user associated with this event (static).  This setting is only applicable if user.field is NOT specified.
# Default: none

input.topic.N.user.field=
# Optional - <string>
# Defines the field to be used as the user identifer for this event (dynamic).  This setting overwrites user.value
# Default: none