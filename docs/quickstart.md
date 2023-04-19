---
title: Quick Start
layout: documentation
---

Use Padas to perform streaming event data transformations and apply specific rules to filter out sample data.  This quick start guide assumes all components (Confluent Kafka and Padas) will be installed on the same machine.  In production, it is recommended to separate out these components on different nodes/hosts.

### Prerequisites
- Internet connectivity
- Review [System Requirements](system-requirements.md)
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

--8<-- "installation_step_download.md"

--8<-- "installation_step_engine.md"

--8<-- "installation_step_ui.md"

#### Step 4: Create Topics
In addition to required (Padas) topics we will create `test_input` and `test_output` topics for demo purposes.  You can create these topics according to your preference (e.g. Confluent Control Center) and below steps simply provide one way of doing so.

1. **Create Padas Topics**: After initial login, from the left menu, click on [Topics](https://localhost:9000/topics).  For this demo, you can simply accept the defaults and click <span class="btn btn-padas">Create Topics</span> button

    <figure markdown>
      <p>
      <img src="../assets/img/padas_ui_topics_pre.png" class="w-50 img-fluid py-5">
      </p>
    </figure>

    **IMPORTANT NOTE**: If you created the required topics from Padas UI, you will need to restart the Padas Engine so that it can read from and write to these topics.  Stop the running Padas Engine via `CTRL-C`, and start it again.  You'll need to logout/login from the UI as well.
    ```bash
    bin/padas start-console
    ```

2. **Create Test Topics**: From the console, simply run the following commands to create `test_input` and `test_output` test topics with defaults.
    ```bash
    kafka-topics --bootstrap-server localhost:9092 --create --topic "test_input"
    kafka-topics --bootstrap-server localhost:9092 --create --topic "test_output"
    ```

#### Step 5: Configure Padas

---

**TLDR;**
Upload the configurations from the corresponding menus.  Each of the views provide a way to bulk upload configurations from a file.

  - For [Tasks](https://localhost:9000/tasks) upload [PadasQuickStartTasks.json](../assets/config/PadasQuickStartTasks.json)
  - For [Pipelines](https://localhost:9000/pipelines) upload [PadasQuickStartPipelines.json](../assets/config/PadasQuickStartPipelines.json)
  - For [Rules](https://localhost:9000/rules) upload [PadasQuickStartRules.json](../assets/config/PadasQuickStartRules.json)
  - For [Topologies](https://localhost:9000/topologies) upload [PadasQuickStartTopologies.json](../assets/config/PadasQuickStartTopologies.json)

    <figure markdown>
      <p>
      <img src="../assets/img/padas_ui_upload_config.png" class="w-50 img-fluid py-5">
      </p>
    </figure>

---
Following steps will guide you through how to manually create these configuration items instead of uploading.

1. **Create Rules**: Create couple of rules for `mydata` data model. with the above tasks.  From [Rules](https://localhost:9000/rules) menu, click <span class="btn btn-padas">New Rule</span> button and fill in the details.
    <figure markdown>
      <p>
      <img src="../assets/img/padas_ui_rule_create_1.png" class="w-50 img-fluid py-5">
      </p>
      <p>
      <img src="../assets/img/padas_ui_rule_create_2.png" class="w-50 img-fluid py-5">
      </p>
    </figure>

2. **Create Tasks**: We will create 2 tasks.  First one will simply perform some enrichment and add a new field `group_name` based on a condition.  The second one will run all selected PDL rules.  From [Tasks](https://localhost:9000/tasks) menu, click <span class="btn btn-padas">New Task</span> button and fill in the details.
    <figure markdown>
      <p>
      <img src="../assets/img/padas_ui_task_eval_create.png" class="w-50 img-fluid py-5">
      </p>
      <p>
      <!-- TODO: INSERT NEW SCREENSHOT HERE -->
      <img src="../assets/img/padas_ui_task_apply_rules_create.png" class="w-50 img-fluid py-5">
      </p>
    </figure>

3. **Create Pipeline**: Create a pipeline with the above tasks.  From [Pipelines](https://localhost:9000/pipelines) menu, click <span class="btn btn-padas">New Pipeline</span> button and fill in the details.  Note that the output of a task becomes an input for the following task in the pipeline.
    <figure markdown>
      <p>
      <img src="../assets/img/padas_ui_pipeline_create.png" class="w-50 img-fluid py-5">
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

#### Step 6: Test & Play

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

#### Next Steps
- [Install](installation.md) in production.
- [Utilize PADAS](stream-config.md) with out-of-the-box [PadasRules_sample.json](../assets/config/PadasRules_sample.json)
- [Integrations](admin-guide.md#integrate-to-external-systems) with ingest pipelines ([Sample Sysmon Config with Winlogbeat](../assets/config/sysmonconfig-export-exclude-winlogbeat.xml)).
