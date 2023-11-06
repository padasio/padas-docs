**NOTE**: Following steps are applicable for both Engine and UI components.  For UI, simply use `bin/padas-ui` as the command.

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