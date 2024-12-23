1. [Contact](mailto:info@padas.io) with us to get the latest version of Padas Engine and UI components applicable to your platform. 

    ```bash 
    padas-{{ current_version }}.tgz
    padas-ui-{{ current_version }}-linux-x64.tgz
    ```

2. Use the `tar` command to decompress the archive file

    ```sh
    tar -xzf padas-{{ current_version }}.tgz
    tar -xzf padas-ui-{{ current_version }}-linux-x64.tgz
    ```

3. Once extracted, you should have `padas` and `padas-ui` directories.  By default, Padas Engine expects Kafka to be running on `localhost`.  If that's not the case, edit `padas/etc/padas.properties` accordingly.

At this stage, make sure you have Confluent Kafka is running as mentioned in prerequisites.

