<p class="padas-important-color">At this stage, make sure you have Confluent Kafka is running as mentioned in prerequisites.</p>

1. Start engine node on the console.  The script will ask you to accept the license agreement (enter `y or yes`)
    ```bash
    cd padas/engine
    ```
    --8<-- "padas/padas_engine_start_console.md"

    **NOTE**: If Padas is configured to utilize Kafka (`padas.config.store=kafka` in properties file) to store configurations you will need to create the required topics (configuration namespaces).  If not, you will receive a warning as following on the console.  

    ```bash
    ...
    WARN  Unable to describe required topics for Padas.  Please create these topics in order to run the engine.
    ...
    ```
