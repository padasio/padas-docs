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

schema.registry.url="http://localhost:8081"
# Optional - <string>
# Schema registry URL for SerDe (e.g. Avro).  If not provided, it will use the default value.
# Default: http://localhost:8081

padas.uuid=
# N/A - Automatically assigned
# Universally Unique Identifier for this instance.  Created upon initial start.

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
padas.config.store=rocksdb
# Optional - <string>
# Configuration store setting, possible options: rocksdb, kafka
# Default: rocksdb

padas.config.location=/opt/padas/var/config
# Optional - <string>
# State store directory to keep local RocksDB data.  If it is a clustered RocksDB, provide the URL (e.g. "http://localhost:2379")
# Default: ${padas.home}/var/config

# Following settings are for streams only
state.dir=/opt/padas/var/state
# Optional - <string>
# State store directory for any streaming topologies to utilize.
# Default: ${padas.home}/var/state


num.stream.threads=10
# Optional - <integer>
# Number of threads to run in parallel for this streaming instance.  
# Default: 10

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

####################################
# SETTINGS FOR CLIENT AUTHENTICATION AND TLS/SSL - CONFLUENT KAFKA
####################################
security.protocol=PLAINTEXT
# Optional - <string>
# Security protocol for Kafka.  Possible options: PLAINTEXT, SSL, SASL_PLAINTEXT, SASL_SSL
# Default: PLAINTEXT

ssl.truststore.location=
# Optional - <string>
# Truststore location for SSL, e.g. /etc/security/tls/kafka.client.truststore.jks
# Default: None

ssl.truststore.password=
# Optional - <string>
# Truststore password for SSL, e.g. test1234
# Default: None

ssl.keystore.location=
# Optional - <string>
# Keystore location for SSL, e.g. /etc/security/tls/kafka.client.keystore.jks
# Default: None

ssl.keystore.password=
# Optional - <string>
# Keystore password for SSL, e.g. test1234
# Default: None

ssl.key.password=
# Optional - <string>
# Key password for SSL, e.g. test1234
# Default: None