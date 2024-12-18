---
title: Quick Start
layout: documentation
---

Use Padas to perform streaming event data transformations and apply specific rules to filter out sample data.  This quick start guide assumes all components (Confluent Kafka and Padas) will be installed on the same machine.  In production, it is recommended to separate out these components on different nodes/hosts.

### Prerequisites
- Internet connectivity
- Review [System Requirements](system-requirements.md)
- Kafka (Apache, Confluent Community, etc.) must be installed and running (locally) (e.g. [Quick Start for Confluent Platform](https://docs.confluent.io/platform/current/quickstart)).  
- You should have at least Kafka Broker and Controller (or Zookeeper) services up and running.
    ```sh
    confluent local services status
    ...
    Kafka is [UP]
    ZooKeeper is [UP]
    ...
    ```

<br>

### Overview of Quickstart

Below diagram shows what will be accomplished with this quick start guide.

<figure markdown>
  <p>
  <img src="../assets/img/padas_quickstart_setup.png" class="img-fluid py-5">
  </p>
</figure>

We will play with some mock data such as the following.  Our goal will be to transform sample event data and apply a set of rules to generate alerts.

Sample input:
```json
{
  "user": "user_1",
  "group_id": 5,
  "action": "success"
}
```

We will have a couple of simple rules that will trigger when `group_name` (soon to be enriched field) matches `"evil*"` or when `action` results in `failure`.

**NOTE**: For the purposes of demo, the goal is carried with multiple tasks, where as a simple `FILTER` function can be utilized as well.

---
#### Step 1: Acquiring Padas
--8<-- "installation/installation_step_acquire.md"

---

#### Step 2: Start Engine
--8<-- "installation/installation_step_engine.md"

---

#### Step 3: Start UI
--8<-- "installation/installation_step_ui.md"

---

#### Step 4: Configuration & Namespaces
--8<-- "installation/installation_step_configuration.md"

---

#### Step 5: Configure Padas

##### Option 1: Configure Padas Using Stream Configs JSON File

For [Stream Configs](https://localhost:9000/stream-configs){:target="_blank"} upload [PadasQuickStartStreamConfigurations.json](../assets/config/PadasQuickStartStreamConfigurations.json)

To configure the stream settings, follow the steps below:  

1. Navigate to [Stream Configs](https://localhost:9000/stream-configs){:target="_blank"}.  
2. Click on the **Upload** button. This will open a dialog window.
<figure markdown>
  <p>
    <img src="../assets/img/padas_ui_upload_config1.png" class="w-60 img-fluid py-5">
  </p>
</figure>  
3. In the dialog, select the file **PadasQuickStartStreamConfigurations.json** from your local system.
<figure markdown>
  <p>
    <img src="../assets/img/padas_ui_upload_config2.png" class="w-60 img-fluid py-5">
  </p>
</figure>  
4. Once selected, click the **Upload** button.
<figure markdown>
  <p>
    <img src="../assets/img/padas_ui_upload_config.png" class="w-60 img-fluid py-5">
  </p>
</figure> 
Upon a successful upload, the following components will be configured automatically:  
- Rules  
- Tasks  
- Pipeline  
- Topology   

---
     
##### Option 2: Configure Padas Manually  

The following steps will guide you on how to manually create the necessary configuration items instead of uploading a JSON file.  

<span class='padas-important-color'>**1. Create Rules**</span>

   - Click on the **Create New** dropdown and select **Rule**.  
   - Fill in the fields in the dialog as shown in the examples below.
       <figure markdown>
      <p>
      <img src="../assets/img/padas_ui_rule_create_1.png" class="w-50 img-fluid py-5">
      </p>
      <p>
      <img src="../assets/img/padas_ui_rule_create_2.png" class="w-50 img-fluid py-5">
      </p>
    </figure>  
   - Click on **Create Rule**.  
   - Repeat this process to create **2 rules**.  

<span class='padas-important-color'>**2. Create Tasks**</span>  

   - Click on the **Create New** dropdown and select **Task**.  
   - Fill in the fields in the dialog as shown in the examples below.
       <figure markdown>
      <p>
      <img src="../assets/img/padas_ui_task_eval_create.png" class="w-50 img-fluid py-5">
      </p>
      <p>
      <!-- TODO: INSERT NEW SCREENSHOT HERE -->
      <img src="../assets/img/padas_ui_task_apply_rules_create.png" class="w-50 img-fluid py-5">
      </p>
    </figure>  
   - Click on **Create Task**.  
   - Repeat this process to create **2 tasks**. 
   
   First one will simply perform some enrichment and add a new field `group_name` based on a condition.  The second one will run all selected PDL rules.

<span class='padas-important-color'>**3. Create a Pipeline**</span> 

   - Click on the **Create New** dropdown and select **Pipeline**.  
   - Fill in the fields in the dialog as shown in the example below.
       <figure markdown>
      <p>
      <img src="../assets/img/padas_ui_pipeline_create.png" class="w-50 img-fluid py-5">
      </p>
    </figure>  
   - Click on **Create Pipeline**.

   Note that the output of a task becomes an input for the following task in the pipeline.  

<span class='padas-important-color'>**4. Create a Topology**</span> 

  Create a topology with the above pipeline that reads from `test_input` topic and writes to `test_output` topic. 

   - Click on the **Create New** dropdown and select **Topology**.  
   - Fill in the fields in the dialog as shown in the example below.
       <figure markdown>
      <p>
      <img src="../assets/img/padas_ui_topology_create.png" class="w-50 img-fluid py-5">
      </p>
    </figure>  
   - Click on **Create Topology**.

      `keySerde:` topic key SerDe, if not specified default is "org.apache.kafka.common.serialization.Serdes$StringSerde".

      `valueSerde:` topic value SerDe, if not specified default is "org.apache.kafka.common.serialization.Serdes$StringSerde". 

<span class='padas-important-color'>**5. Restart Node**</span>

##### Option 1: From Console 

Once a new topology is created we need to let Padas Engine know about it by restarting the node.  You can do this from the console (`CTRL-C` and start, or stop/start the service, etc.)

##### Option 2: From UI 

 You can also do this from the UI from [Engines](https://localhost:9000/nodes) menu, click <span class="btn btn-padas">Start</span> button and you should see the state change to `RUNNING` for this node.
    <figure markdown>
      <p>
      <img src="../assets/img/padas_ui_nodes.png" class="w-50 img-fluid py-5">
      </p>
    </figure>

#### Step 6: Test & Play

##### Option 1: Testing with Padas UI

1. **Navigate to the Test Page:** Open your web browser and access the Padas UI. Once logged in, locate and click on the "Test" option in the navigation to open the Test page.

    <figure markdown>
      <p>
      <img src="../assets/img/padas_ui_open_test_page.png" class="w-50 img-fluid py-5">
      </p>
    </figure>

2. **Configure and Run Your Test:** On the Test page, locate the dropdown menu for selecting a Test Function and choose "pipeline" as it pertains to our example.
In the provided field, paste the sample event data that corresponds to the pipeline function you are testing. Click the "Test" button.

    <figure markdown>
      <p>
      <img src="../assets/img/padas_ui_select_test_function.png" class="w-50 img-fluid py-5">
      </p>
    </figure>

    ```json
    {"user": "user_1","group_id": 5,"action": "success", "user": "user_1","group_id": 1,"action": "success", "user": "user_1","group_id": 1,"action": "failure"}
    ```

    <figure markdown>
      <p>
      <img src="../assets/img/padas_ui_apply_test_function.png" class="w-50 img-fluid py-5">
      </p>
    </figure>



##### Option 2: Testing using Kafka CLI Tools

1. **Generate Data**: Let's generate a few sample event with a simple JSON message.  Note that the last 2 events will match the rules specified above.
    ```bash
    echo '{"user": "user_1","group_id": 5,"action": "success"}' |  kafka-console-producer --bootstrap-server localhost:9092 --topic test_input
    echo '{"user": "user_1","group_id": 1,"action": "success"}' |  kafka-console-producer --bootstrap-server localhost:9092 --topic test_input
    echo '{"user": "user_1","group_id": 1,"action": "failure"}' |  kafka-console-producer --bootstrap-server localhost:9092 --topic test_input
    ```

2. **View output**: Once the sample event is ingested, rules for matching datamodels in real-time and populate `padas_alerts` topic with matching event and alert information.  You can simply view this alert with the following command:

    ```bash
    kafka-console-consumer --bootstrap-server localhost:9092 --topic test_output --from-beginning | jq
    ```

    Output will be similar to the following, this example output is from the last input from above.  Note the use of `jq` above for pretty display of JSON data.
    ```json
    {
      "user": "user_1",
      "group_id": 1,
      "action": "failure",
      "group_name": "evil group",
      "padasRule":
      {
        "id": "test_rule_for_evil",
        "name": "Test Rule for Evil",
        "description": "Match for group name that starts with evil",
        "pdl": "group_name=\"evil*\"",
        "datamodel": "mydata",
        "annotations": [
          "T1234",
          "T2345"
        ]
      }
    }

    {
      "user": "user_1",
      "group_id": 1,
      "action": "failure",
      "group_name": "evil group",
      "padasRule":
      {
        "id": "test_rule_for_failure",
        "name": "Test Rule for Failure",
        "description": "Match when action is failure",
        "pdl": "action=\"failure\"",
        "datamodel": "mydata",
        "annotations": [
          "T9876"
        ]
      }
    }
    ```

---

#### Next Steps
- [Install](installation.md) in production.
- [Utilize PADAS](stream-config.md) with out-of-the-box [PadasRules_sample.json](../assets/config/PadasRules_sample.json)
- [Integrations](admin-guide.md#integrate-to-external-systems) with ingest pipelines ([Sample Sysmon Config with Winlogbeat](../assets/config/sysmonconfig-export-exclude-winlogbeat.xml)).
