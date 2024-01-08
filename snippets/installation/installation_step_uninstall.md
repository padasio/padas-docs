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
