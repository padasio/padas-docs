Java 17 is the recommended version in this version of Padas. Java 11 and later versions are also supported.  From a security perspective, we recommend the latest released patch version as older freely available versions may have disclosed security vulnerabilities.

For more information regarding Confluent Platform, please visit [here](https://docs.confluent.io/platform/current/installation/versions-interoperability.html#java).

**NOTE**: You need to separately install the correct version of Java before you start the installation process.

JVM Heap Options can be set via `PADAS_HEAP_OPTS` environment variable.  Default value is: `-Xmx1G -Xms1G`

**NOTE**: When using `systemctl` to start the service, you'll need to edit `padas.service` file to make a change in JVM heap options.

