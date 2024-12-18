1. [Contact](mailto:info@padas.io) with us to get the latest version of Padas Engine and UI components applicable to your platform. 

    ```bash 
    padas-engine-1.0.0.tgz
    padas-ui-1.0.0-linux-x64.tgz (or darwin)
    ```

2. Use the `tar` command to decompress the archive file

    ```sh
    tar -xzf padas-engine-1.0.0.tgz
    tar -xzf padas-ui-1.0.0-linux-x64.tgz (or darwin)
    ```

3. After extraction, combine the two `padas` folders. By default, two `padas` directories are created:  
    One containing the `ui` folder  
    The other containing the `engine` folder  

    To organize them into a single `padas` directory, use the following structure:

    ```text
    padas/
    ├── engine/    # Contents of padas-engine
    └── ui/        # Contents of padas-ui
    ```

4. By default, Padas Engine expects Kafka to be running on `localhost`.  If that's not the case, edit `padas/engine/etc/padas.properties` accordingly. If the `padas.properties` file does not exist, copy the `padas.properties.example` file to create it.

