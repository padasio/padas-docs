---
title: Installation
---
## Installation

<br>

### System Requirements

<br>

##### Hardware
The following machine recommendations are for installing individual PADAS components:
{% include docs/sysreq_hardware.md %}

<br>
##### Software
{% include docs/sysreq_confluent.md %}

<br>
##### Operating Systems
PADAS supports the following operating systems.
{% include docs/sysreq_os.md %}

<br>
##### Java
{% include docs/sysreq_java.md %}

<br>

---

### Manual Install Using TAR Archive
<br>

#### Download the software
1. Download the latest version here: [padas-{{ site.data.versions.latest_version }}.tgz](/assets/downloads/padas-{{ site.data.versions.latest_version }}.tgz) or via command line:
```sh
curl -O https://www.padas.io/assets/downloads/padas-{{ site.data.versions.latest_version }}.tgz
```
NOTE: You can verify the integrity by checking against its SHA512 checksum: [padas-{{ site.data.versions.latest_version }}.tgz.sha512](/assets/downloads/padas-{{ site.data.versions.latest_version }}.tgz.sha512)
2. Extract contents of the archive (default `/opt` is assumed for `$PADAS_HOME`)
```sh
cd /opt
tar xvf padas-{{ site.data.versions.latest_version }}.tgz
```
<br>
You should have these directories:
{% include docs/padas_folders.md %}
<br>

**IMPORTANT NOTE**: It is recommended to create a separate user to run Padas, other than `root`.  In our examples, we use `padas` as both the user and group name.  Following is an example on how to create such user:
```
sudo useradd -d /opt/padas -U padas
```

---

### Register as a Service

1. Run Padas to create a service file. (Note: following examples assume `$PADAS_HOME` to be `/opt/padas` directory)
```sh
bin/padas set-service
Systemd unit file has been created as '/opt/padas/libs/padas.service'
```
2. Review the generated service file (`libs/padas.service`) and edit as necessary (e.g. user & group information, JVM memory options according to your system settings)
```properties
[Unit]
Description=PADAS - Alert Detection for Streaming Events
Documentation=https://www.padas.io/docs
After=network.target
#
[Service]
Type=simple
User=padas
Group=padas
ExecStart=java -Xmx1G -Xms1G -Dconfig.file=/opt/padas/etc/padas.properties -Dlogging.config=/opt/padas/etc/logback.xml -jar /opt/padas/libs/padas-{{ site.data.versions.latest_version }}.jar
TimeoutStopSec=180
Restart=no
#
[Install]
WantedBy=multi-user.target
```
3. Copy the service file under system
```sh
sudo cp /opt/padas/libs/padas.service /etc/systemd/system/
```
4. Reload systemd process
```sh
sudo systemctl daemon-reload
```


<br>

---

#### Start For the First Time

**IMPORTANT NOTE**: You need a running Kafka environment (Broker(s) and Schema Registry) and a PADAS license key. [Request a license key](/index.html#download) if you don't have one.

##### Manager
1. Edit `etc/padas.properties` file to reflect your environment and enter the license key.  Note that `padas.instance.role` **MUST** be `manager`.
```properties
padas.instance.role=manager
bootstrap.servers=localhost:9092
schema.registry.url=http://localhost:8081
padas.license=<ENTER YOUR LICENSE KEY HERE>
```
2. Use command-line interface (CLI) to start PADAS:
```sh
cd $PADAS_HOME/bin
./padas start
```
3. PADAS displays the license agreement and prompts you to accept in order to continue.
{% include docs/padas_licenseagreement_start.md %}
4. Create admin username.  This is the user that you log into PADAS Manager with.
```sh
Please enter an administrator username? [admin]:
```
5. Create the password for the user that you just created.
```sh
Password must contain at least 8 total printable ASCII characters.
Please enter a new password:
Please repeat the password:
Successfully saved password.
```
6. By default, Manager web interface starts on tcp/9000 port.  Open a browser and access PADAS Manager (e.g. http://localhost:9000).  For any custom configurations please go to [Admin Guide](/docs/admin-guide.html#anchor1)
7. Once logged in, unless the topics are created separately, Manager will prompt you to create the required Kafka topics.
    <img src="/assets/img/topics_pre_sample.png" width="67%">
    <br/>
    **IMPORTANT NOTE**: Number of partitions for each topic needs to be determined based on the expected event data load, performance requirements and your Kafka cluster setup.  Please consult your Kafka administrator or PADAS representative for assistance.  Once set, number of partitions can not be changed (the topic needs to be deleted and re-created).
8. Go to <span class="fw-bold"><i class="bi bi-file-ruled"></i>Rules</span> menu link and click <span class="btn btn-padas">Edit</span> button in order to add rules. You can upload our out-of-the-box MITRE ATT&CK compatible rules, [padasRules.json](/assets/config/padasRules.json), that work with Winlogbeat eventlog from `winlogbeat-sysmon` and `winlogbeat-security` datamodels in `padas_events`

    <img src="/assets/img/rules_upload_sample.png" width="67%">
    <br/>
9. Go to <span class="fw-bold"><i class="bi bi-filter"></i>Properties</span> menu link and click <span class="btn btn-padas">Edit</span> button in order to add properties.  You can upload out-of-the-box transformations for Winlogbeat, [padas_transformation.properties](/assets/config/padas_transformation.properties), which are configured for getting `winlogbeat-sysmon` and `winlogbeat-security` topics transformed into `padas_events`

    <img src="/assets/img/transform_upload_sample.png" width="67%">
    <br/>
<br/>
##### Detect Engine
1. Edit `etc/padas.properties` file to reflect your environment.  Note that `padas.instance.role` **MUST** be `detect` (default setting).
```properties
padas.instance.role=detect
bootstrap.servers=localhost:9092
schema.registry.url=http://localhost:8081
```
2. Use command-line interface (CLI) to start PADAS:
```sh
cd $PADAS_HOME/bin
./padas start
```
3. PADAS displays the license agreement and prompts you to accept in order to continue.
{% include docs/padas_licenseagreement_start.md %}

<br/>
##### Transform Engine
1. Edit `etc/padas.properties` file to reflect your environment.  Note that `padas.instance.role` **MUST** be `transform`.
```properties
padas.instance.role=detect
bootstrap.servers=localhost:9092
schema.registry.url=http://localhost:8081
```
2. Use command-line interface (CLI) to start PADAS:
```sh
cd $PADAS_HOME/bin
./padas start
```
3. PADAS displays the license agreement and prompts you to accept in order to continue.
{% include docs/padas_licenseagreement_start.md %}

<br>

---

### PADAS Command Line Interface
A wrapper script is provided to manage PADAS service: `$PADAS_HOME/bin/padas`
{% include docs/padas_cli.md %}

<br>
Example outputs when components are started for the first time.

<br>
Manager:
{% include docs/padas_manager_start_console.md %}

<br>
Detect Engine:
{% include docs/padas_detect_start_console.md %}

<br>
Transform Engine:
{% include docs/padas_transform_start_console.md %}

<br>

---

### Uninstall
1. Remove Padas directory.  For example:
```sh
rm -rf /opt/padas
```

<br>

---

### Docker
*TBD*


