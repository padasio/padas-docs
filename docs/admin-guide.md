---
title: Admin Guide
---
## Admin Guide

<br>

### JVM Settings
--8<-- "sysreq_java.md"

<br>

### Topic Properties
Following Kafka topics are required for PADAS to operate properly.  Upon initial access to Padas Manager, Topics View allows changing partition and replication counts.

**NOTE**: For production, it is highly recommended to review [Topic Configuration](https://docs.confluent.io/platform/current/installation/configuration/topic-configs.html) and tune settings for each Padas topic according to expected volume and performance requirements.

{% include docs/props_topics.md %}

<br>

### Configuration Properties
For any PADAS instance all configuration is read from `$PADAS_HOME/etc/padas.properties` file; and details regarding the properties settings can be found in [padas.properties.spec](/assets/config/padas.properties.spec), also available with any installation at `$PADAS_HOME/etc/padas.properties.spec`

At a minimum, following settings are required for any PADAS instance:
```
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
```

<br />

For Manager instance, license entry is required and the following settings are also applicable:
```
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
```

<br>

### Logging
PADAS utilizes [Logback](https://logback.qos.ch/manual/configuration.html) for logging application activity.  By default, `$PADAS_HOME/etc/logback.xml` file is used; log files are created based on the following settings and can be changed according to your requirements.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <!-- Stop output INFO at start -->
    <statusListener class="ch.qos.logback.core.status.NopStatusListener" />

    <property name="LOGS" value="${PADAS_HOME}/logs" />

    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%yellow(%d{yyyy-MM-dd HH:mm:ss.SSS}) %cyan(${HOSTNAME}) %magenta([%thread]) %highlight(%-5level) %logger{36}.%M - %msg%n</pattern>
        </encoder>
    </appender>
    <appender name="DISPLAY" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%highlight(%-5level) %msg%n</pattern>
        </encoder>
    </appender>
    <appender name="FILE-ROLLING" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>${LOGS}/padas.log</file>

        <rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
            <fileNamePattern>${LOGS}/padas.%d{yyyy-MM-dd}.%i.log</fileNamePattern>
            <!-- each archived file, size max 100MB -->
            <maxFileSize>100MB</maxFileSize>
            <!-- total size of all archive files, if total size > 20GB, it will delete old archived file -->
            <totalSizeCap>20GB</totalSizeCap>
            <!-- 60 days to keep -->
            <maxHistory>60</maxHistory>
        </rollingPolicy>

        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} ${HOSTNAME} [%thread] %-5level %logger{36}.%M - %msg%n</pattern>
        </encoder>
    </appender>
    <logger name="ch.qos.logback" level="WARN" />
    <logger name="org.springframework" level="WARN" />
    <logger name="org.apache" level="WARN" />
    <logger name="io.confluent" level="WARN" />
    <logger name="io.padas" level="INFO">
        <!--<appender-ref ref="STDOUT" />-->
    </logger>
    <logger name="io.padas.app.management.Manager" level="INFO">
        <appender-ref ref="DISPLAY" />
    </logger>
    <logger name="io.padas.app.App" level="INFO">
        <appender-ref ref="DISPLAY" />
    </logger>
    <root level="info">
        <appender-ref ref="FILE-ROLLING" />
    </root>
</configuration>
```

<br>

### Integrate to External Systems
It is possible to integrate any external system either as a [Kafka Producer](https://docs.confluent.io/platform/current/clients/producer.html) (source, generating and ingesting event data) or [Kafka Consumer](https://docs.confluent.io/platform/current/clients/consumer.html) (sink, consuming `padas_alerts` topic for further analysis/alerting).  [Confluent Hub](https://www.confluent.io/hub/) can be utilized to implement any specific source and/or sink connector for integration. 

<br />

#### Winlogbeat (Elastic Stack)
[Winlogbeat (OSS)](https://www.elastic.co/downloads/beats/winlogbeat-oss) can be utilized as a Kafka Producer to ingest Windows event data.  You can find relevant example information below.

*Winlogbeat examples*:
- [Sample Sysmon Config with Winlogbeat](/assets/config/sysmonconfig-export-exclude-winlogbeat.xml): This example sysmon configuration is based on [Swift On Security sysmon config](https://github.com/SwiftOnSecurity/sysmon-config) and it focuses on default high-quality event tracing while excluding any Winlogbeat generated activity from event logs.

- [Winlogbeat configuration (`winlogbeat.yml`)](/assets/config/winlogbeat.yml): This is an example winlogbeat configuration that reads both Security and Sysmon event logs on the installed Windows system and sends events to relevant Kafka topics (i.e. `winlogbeat-sysmon` and `winlogbeat-security`).

*PADAS configurations*:

- [Winlogbeat Sysmon and Security](/assets/config/padas_transformation.properties): This example properties file is for PADAS and can be uploaded via [Properties view](/docs/user-guide.html#properties) to quickly start transformations on Winlogbeat generated events as specified with the above examples.

- [Out-of-the-box PADAS Rules](/assets/config/padasRules.json): This JSON configuration contains MITRE ATT&amp;CK relevant rules, which are tested and verified with the above example configurations.  You can upload this file via [Rules view](/docs/user-guide.html#rules) to quickly get started.  For any other input, it's recommended to review the applicable data model and PDL query of each rule for accuracy.

<br />

#### Splunk
[Splunk](https://www.splunk.com) can act as a Kafka Consumer for further analysis of Padas Alerts.  Padas and Splunk integration can be accomplished seamlessly with [Splunk Sink Connector](https://www.confluent.io/hub/splunk/kafka-connect-splunk) and [Technology Add-on for Padas](https://github.com/seynur/TA-padas).  Splunk Sink Connector needs to be installed on Confluent Kafka and TA-Padas will need to be installed on Splunk Search Head(s).  Please follow the instructions within the links on how to properly install.

An example configuration for Splunk Sink Connector can be found here: [splunk-sink-connector-example.json](/assets/config/splunk-sink-connector-example.json)
```json
{
  "name": "SplunkSinkConnectorConnector_Padas",
  "config": {
    "connector.class": "com.splunk.kafka.connect.SplunkSinkConnector",
    "value.converter": "io.confluent.connect.avro.AvroConverter",
    "topics": "padas_alerts",
    "splunk.hec.token": "e8de5f0e-97b1-4485-b416-9391cbf89392",
    "splunk.hec.uri": "https://splunk-server:8088",
    "splunk.indexes": "padas",
    "splunk.sourcetypes": "padas:alert",
    "splunk.hec.ssl.validate.certs": "false",
    "value.converter.schema.registry.url": "http://confluent-kafka-schema-registry-server:8081"
  }
}
```

If the Splunk installation has [MITRE ATT&amp;CK App for Splunk](https://splunkbase.splunk.com/app/4617/), then any alert with MITRE ATT&amp;CK annotations are automatically integrated also.

