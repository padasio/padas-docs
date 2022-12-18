---
title: Installation
---
### System Requirements

#### Hardware
--8<-- "sysreq_hardware.md"

#### Software
--8<-- "sysreq_confluent.md"

#### Operating Systems
--8<-- "sysreq_os.md"

#### Java
--8<-- "sysreq_java.md"

---

### Install Using TAR Archive

**IMPORTANT NOTE**: It is recommended to create a separate user to run Padas, other than `root`.  In our examples, we use `padas` as both the user and group name.  Following is an example on how to create such user:
```bash
sudo useradd -d /opt/padas -U padas
```

Padas installation folder structure:
--8<-- "padas_folders.md"

--8<-- "installation_step_download.md"

**NOTE:** You can install these components in a distributed environment.  For possible configuration options, please refer to [Configuration File Reference](config-reference.md).

--8<-- "installation_step_engine.md"

--8<-- "installation_step_ui.md"



---

### Create Topics
The following Kafka topics must be created for keeping centralized configuration entries. You can create these topics according to your preference (e.g. Confluent Control Center) and below steps simply provide one way of doing so.

--8<-- "props_topics.md"

**Create Padas Topics**: After initial login, from the left menu, click on [Topics](https://localhost:9000/topics).   In this view you can ONLY change replication or partition information.  For further detailed configuration on topics, please refer to [Topic Properties](admin-guide.md#topic-properties) and/or consult your Kafka administrator.

<figure markdown>
<p>
    <img src="../assets/img/padas_ui_topics_pre.png" class="w-50 img-fluid py-5">
</p>
</figure>

**IMPORTANT NOTE**: If you created the required topics from Padas UI, you will need to **restart** the Padas Engine so that it can read from and write to these topics.  Stop the running Padas Engine via `CTRL-C`, and start it again.  You'll need to logout/login from the UI as well.
    ```bash
    bin/padas start-console
    ```


---

### Register as a Service

1. Run Padas to create a service file. (Note: following examples assume `$PADAS_HOME` to be `/opt/padas` directory)
    ```bash
    bin/padas set-service
    Systemd unit file has been created as '/opt/padas/libs/padas.service'
    ```
2. Review the generated service file (`libs/padas.service`) and edit as necessary (e.g. user & group information, JVM memory options according to your system settings)
    ```properties
    [Unit]
    Description=PADAS - Engine for Streaming Events
    Documentation=https://docs.padas.io/
    After=network.target
    #
    [Service]
    Type=simple
    User=padas
    Group=padas
    ExecStart=java -Xmx1G -Xms1G -Dconfig.file=/opt/padas/etc/padas.properties -Dlogging.config=/opt/padas/etc/logback.xml -jar /opt/padas/libs/padas-{{ current_version }}.jar
    TimeoutStopSec=180
    Restart=no
    #
    [Install]
    WantedBy=multi-user.target
    ```
3. Copy the service file under system
    ```bash
    sudo cp /opt/padas/libs/padas.service /etc/systemd/system/
    ```
4. Reload systemd process
    ```bash
    sudo systemctl daemon-reload
    ```
5. You can control the service (start/stop) via `systemctl` or from `$PADAS_HOME/bin/padas` script, which internally utilizes `systemctl`.
    ```bash
    /opt/padas/bin/padas start
    ```

---

### PADAS Command Line Interface
A wrapper script is provided to manage PADAS service: `$PADAS_HOME/bin/padas`
--8<-- "padas_cli.md"

---

### Uninstall

1. Stop Padas service(s).
    ```bash
    /opt/padas/bin/padas stop
    ```
2. Remove any system service definition.  For example
    ```bash
    rm /etc/systemd/system/padas.service
    ```
3. Remove Padas installation directory.  For example:
    ```sh
    rm -rf /opt/padas
    ```

