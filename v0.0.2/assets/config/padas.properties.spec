####################################
# This file provides all possible options for padas.properties file.
# Use this file to configure PADAS instances and their properties.
####################################

####################################
# Required Settings
# These settings must be defined for each instance regardless of its role.
####################################

bootstrap.servers=localhost:9092
# Required - <string>
# Kafka bootstrap server list with port information.  Multiple servers can be separated by comma.
# Default: localhost:9092

padas.uuid=
# N/A - Automatically assigned
# Universally Unique Identifier for this instance.  Created upon initial start.

padas.license=
# Required - <string>
# License string should be a pipe '|' delimited string containing
# version, entitlement, start date, end date, quota, type, and signature
# Default: none


####################################
# Optional Settings
####################################

padas.application.id=padas-engine
# Optional - <string>
# Unique ID for this application cluster.  Used as consumer group ID as well.
# Default: padas-engine

padas.home=/opt/padas
# Optional - <string>
# Root folder where PADAS is installed
# Default: /opt/padas

padas.group=default
# Optional - <string>
# Group name that this instance belongs to.  This is used to distribute running topologies to different instances.


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
# SETTINGS FOR REST API
####################################

server.port=8999
# Optional - <integer>
# Port number for Manager web interface
# Default: 8999

server.ssl.enabled=true
# Optional - <boolean>
# Enable SSL for Manager web interface with the server.ssl.* configuration
# Default: true

server.ssl.key-alias=padas
# Optional - <string>
# SSL Key alias for certificate
# Default: padas

server.ssl.key-store-password=password
# Optional - <string>
# SSL Key Store password
# Default: password

server.ssl.key-store=classpath:padas-ssl.p12
# Optional - <string>
# SSL Key Store path, this should be the full path (e.g. /opt/padas/etc/certs/my.jks)
# Default: reads from built-in classpath

server.ssl.key-store-type=PKCS12
# Optional - <string>
# SSL Key Store type
# Default: PKCS12

