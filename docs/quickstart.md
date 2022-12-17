---
title: Quick Start
layout: documentation
---

Use Padas to perform streaming event data transformations and apply specific rules to filter out sample data.  This quick start guide assumes all components (Confluent Kafka and Padas) will be installed on the same machine.  In production, it is recommended to separate out these components on different nodes/hosts.

### Prerequisites
- Internet connectivity
- Supported [Operating System](/installation.html#operating-systems)
- A supported version of [Java](https://www.oracle.com/technetwork/java/javase/downloads/index.html). Java 8 and Java 11 are supported in this version.
- Confluent Kafka must be installed and running (locally) as described in [Quick Start for Confluent Platform](https://docs.confluent.io/platform/current/quickstart).  
- You should have at least Kafka and Zookeeper services up and running.
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

#### Step 1: Download
1. [Download](http://padas.io/index.html#download) the latest version of Padas Engine and UI components applicable to your platform.

    ```bash 
    wget https://padas.io/assets/downloads/padas-{{ current_version }}.tgz
    wget https://padas.io/assets/downloads/padas-ui-{{ current_version }}-linux-x64.tgz
    ```

2. Use the `tar` command to decompress the archive file

    ```sh
  
    tar -xzf padas-{{ current_version }}.tgz
    tar -xzf padas-ui-{{ current_version }}-linux-x64.tgz
    ```

3. Once extracted, you should have `padas` and `padas-ui` directories.  By default, Padas Engine expects Kafka to be running on `localhost`.  If that's not the case, edit `padas/etc/padas.properties` accordingly.

At this stage, make sure you have Confluent Kafka running locally as mentioned in prerequisites.

#### Step 2: Start Engine
1. Start engine node on the console.  The script will ask you to accept the license agreement (enter `y`)
    ```bash
    cd padas/
    ```
    --8<-- "padas_engine_start_console.md"

    **NOTE**: Unless you created all required topics, you should receive a warning as following on the console.  We'll create these topics on the next steps.
    ```bash
    ...
    WARN  Unable to describe required topics for Padas.  Please create these topics in order to run the engine.
    ...
    ```

#### Step 3: Start UI
1. Start UI component on the console.  Default configuration connects to `localhost` for Padas Engine.
    ```bash
    cd padas-ui/
    ```
    --8<-- "padas_ui_start_console.md"

2. **Initialize User**: Go to [https://localhost:9000](https://localhost:9000) and since this is the first time, click the link below and create an administrator user.

    <figure markdown>
      <p>
      <img src="../assets/img/padas_ui_preinit.png" class="w-50 img-fluid py-5">
      </p>
      <p>
      <img src="../assets/img/padas_ui_init.png" class="w-50 img-fluid py-5">
      </p>
    </figure>

3. **Login**: After initial user creation you will be redrected to Login screen; Login with the newly created user credentials.

#### Step 3: Create Topics
In addition to required (Padas) topics we will create `test_input` and `test_output` topics for demo purposes.  You can create these topics according to your preference (e.g. Confluent Control Center) and below steps simply provide one way of doing so.

1. **Create Padas Topics**: After initial login, from the left menu, click on [Topics](https://localhost:9000/topics).  For this demo, you can simply accept the defaults and click <span class="btn btn-padas">Create Topics</span> button

    <figure markdown>
      <p>
      <img src="../assets/img/padas_ui_topics_pre.png" class="w-50 img-fluid py-5">
      </p>
    </figure>

    **IMPORTANT NOTE**: If you created the required topics from Padas UI, you will need to restart the Padas Engine so that it can read/write to these topics.  Stop the running Padas Engine via `CTRL-C`, and start it again.  You'll need to logout/login from the UI as well.
    ```bash
    bin/padas start-console
    ```

2. **Create Test Topics**: From the console, simply run the following commands to create `test_input` and `test_output` test topics with defaults.
    ```bash
    kafka-topics --bootstrap-server localhost:9092 --create --topic "test_input"
    kafka-topics --bootstrap-server localhost:9092 --create --topic "test_output"
    ```

#### Step 4: Configure Padas

---

**TLDR;**
Upload the configurations from the corresponding menus.  Each of the views provide a way to bulk upload configurations from a file.

  - For [Tasks](https://localhost:9000/tasks) upload [PadasQuickStartTasks.json](../assets/config/PadasQuickStartTasks.json)
  - For [Pipelines](https://localhost:9000/pipelines) upload [PadasQuickStartPipelines.json](../assets/config/PadasQuickStartPipelines.json)
  - For [Rules](https://localhost:9000/rules) upload [PadasQuickStartRules.json](../assets/config/PadasQuickStartRules.json)
    
    **NOTE**: You will need to create the topology manually, please go to step 4 below.

    <figure markdown>
      <p>
      <img src="../assets/img/padas_ui_upload_config.png" class="w-50 img-fluid py-5">
      </p>
    </figure>
  
---

1. **Create Tasks**: We will create 2 tasks.  First one will simply perform some enrichment and add a new field `group_name` based on a condition.  The second one will run all relevant PDL rules for `mydata` data model (arbitrary name).  From [Tasks](https://localhost:9000/tasks) menu, click <span class="btn btn-padas">New Task</span> button and fill in the details.
    <figure markdown>
      <p>
      <img src="../assets/img/padas_ui_task_eval_create.png" class="w-50 img-fluid py-5">
      </p>
      <p>
      <img src="../assets/img/padas_ui_task_rule_create.png" class="w-50 img-fluid py-5">
      </p>
    </figure>

2. **Create Pipeline**: Create a pipeline with the above tasks.  From [Pipelines](https://localhost:9000/pipelines) menu, click <span class="btn btn-padas">New Pipeline</span> button and fill in the details.  Note that the output of a task becomes an input for the following task in the pipeline.
    <figure markdown>
      <p>
      <img src="../assets/img/padas_ui_pipeline_create.png" class="w-50 img-fluid py-5">
      </p>
    </figure>

3. **Create Rules**: Create couple of rules for `mydata` data model. with the above tasks.  From [Rules](https://localhost:9000/rules) menu, click <span class="btn btn-padas">New Rule</span> button and fill in the details.
    <figure markdown>
      <p>
      <img src="../assets/img/padas_ui_rule_create_1.png" class="w-50 img-fluid py-5">
      </p>
      <p>
      <img src="../assets/img/padas_ui_rule_create_2.png" class="w-50 img-fluid py-5">
      </p>
    </figure>

4. **Create Topology**: Create a topology with the above pipeline that reads from `test_input` topic and writes to `test_output` topic.  From [Topologies](https://localhost:9000/topologies) menu, click <span class="btn btn-padas">New Topology</span> button and fill in the details.
    <figure markdown>
      <p>
      <img src="../assets/img/padas_ui_topology_create.png" class="w-50 img-fluid py-5">
      </p>
    </figure>

4. **Restart Node**: Once a new topology is created we need to let Padas Engine know about it by restarting the node.  You can do this from the console (`CTRL-C` and start, or stop/start the service, etc.) or you can also do this from the UI from [Nodes](https://localhost:9000/nodes) menu, click <span class="btn btn-padas">Start</span> button and you should see the state change to `RUNNING` for this node.
    <figure markdown>
      <p>
      <img src="../assets/img/padas_ui_nodes.png" class="w-50 img-fluid py-5">
      </p>
    </figure>

#### Step 5: Test & Play

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
      "padas_rules": [
        {
          "id": 1,
          "name": "Test Rule for Evil",
          "description": "Match for group name that starts with evil",
          "pdl": "group_name=\"evil*\"",
          "datamodel": "mydata",
          "annotations": [
            "T1234",
            "T2345"
          ]
        },
        {
          "id": 2,
          "name": "Test Rule for Failure",
          "description": "Match when action is failure",
          "pdl": "action=\"failure\"",
          "datamodel": "mydata",
          "annotations": [
            "T9876"
          ]
        }
      ]
    }
    ```


#### Next Steps
- <a href="/docs/installation.html">Install</a> in production.
- <a href="/docs/user-guide.html">Utilize PADAS</a> with out-of-the-box [padasRules.json](/assets/config/padasRules.json)
- <a href="/docs/admin-guide.html#integrate-to-external-systems">Integrations</a> with ingest pipelines ([Sample Sysmon Config with Winlogbeat](/assets/config/sysmonconfig-export-exclude-winlogbeat.xml)) and ready-to-use transformations ([Winlogbeat Sysmon and Security](/assets/config/padas_transformation.properties))