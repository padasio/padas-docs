---
title: Quick Start
layout: documentation
padas_version: 0.0.1
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

 <img src="/assets/img/padas_quickstart_setup.png" width="67%">

#### Step 1: Download and define components
1. [Download](http://padas.io/index.html#download) the latest version of Padas Engine and Manager components applicable to your platform.
2. Use the `tar` command to decompress the archive file

    ```sh
    --> site_name
    tar -xvzf padas-{{ padas_version }}.tgz
    ```
3. Since we have everything on a single host, make a copy of the extracted folder for manager, transform engine, and detect engine

    ```sh
    cp -r padas padas-manager
    cp -r padas padas-transform
    mv padas padas-detect
    ```
    **NOTE**: Last renaming step is not necessary but gives a descriptive name to the folder's functionality.
4. Edit manager properties (`padas-manager/etc/padas.properties`) to make sure the `padas.instance.role` is set to `manager` and `padas.license` is set to the license you received.

    ```sh
    vi padas-manager/etc/padas.properties
    ...
    ```

    After editing, properties file (`padas-manager/etc/padas.properties`) entries should be:
    ```properties
    padas.instance.role=manager
    bootstrap.servers=localhost:9092
    schema.registry.url=http://localhost:8081
    padas.license=<LICENSE KEY SHOULD GO HERE>
    ```
5. Edit transform properties (`padas-transform/etc/padas.properties`) to make sure the `padas.instance.role` is set to `transform`.

    ```sh
    vi padas-transform/etc/padas.properties
    ...
    ```

    After editing, properties file (`padas-transform/etc/padas.properties`) entries should be:
    ```properties
    padas.instance.role=transform
    bootstrap.servers=localhost:9092
    schema.registry.url=http://localhost:8081
    ```
6. From your current working directory, now you should have 3 PADAS folders, e.g.

    ```sh
    ls
    padas-detect   padas-manager   padas-transform
    ```
    Note that you don't have to make any configuration changes to `padas-detect` folder, as the default behavior is set to Detect Engine with localhost.

At this stage, make sure you have Confluent Kafka running locally as mentioned in prerequisites.

#### Step 2: Start Manager
1. Start manager node on the console.  The script will ask you to accept the license agreement (enter `y`) and define an administrator user to login; enter the desired password to continue
```
cd padas-manager/
```
--8<-- "padas_manager_start_console.md"

2. **Login**: Go to [http://localhost:9000](http://localhost:9000) and login with the credentials used in previous step (e.g. admin)

    <img src="/assets/img/login_sample.png" width="67%">

3. **Create Topics**: Upon initial login, Manager will go to Topics menu in order to create necessary Kafka topics.  

    <img src="/assets/img/topics_pre_sample.png" width="67%">
    <br/>
    Hit <span class="btn btn-padas">Save</span> button to continue with defaults.
    <br/>
    <img src="/assets/img/topics_post_sample.png" width="67%">

4. **Create a Rule**: Go to <span class="fw-bold"><i class="bi bi-file-ruled"></i>Rules</span> menu link in order to add a sample rule.  Enter the following values for the required fields:
    - **Rule Name**: `Test Rule`
    - **PDL Query**: `field1="value"`
    - **Datamodel List**: `testdm`

    Other provided fields are optional but feel free to review and add/modify as needed.  A list of rules for MITRE ATT&CK can be found here: [padasRules.json](/assets/config/padasRules.json)

    <br/>
    Hit <span class="btn btn-padas">Save</span> button to continue. 

    <img src="/assets/img/rules_pre_sample.png" width="67%">

    <br/>
    You should be able to view the rule you specified, similar to the following screenshot.

    <img src="/assets/img/rules_post_sample.png" width="67%">

5. **Add a Transformation**: Go to <span class="fw-bold"><i class="bi bi-filter"></i>Properties</span> and first hit <span class="btn btn-padas">Edit</span>, then select <span class="btn btn-padas"><i class="bi bi-plus-lg"></i>Add New Transformation</span>.  Expand "Input Topic: 0" and enter the following values for the required fields:
    - **Topic Name**: `testtopic`
    - **Datamodel Name**: `testdm`

    <br/>
    <img src="/assets/img/props_pre_sample.png" width="67%">

    <br/>
    You should be able to view the newly added property (Input Topic: testtopic, similar to the following screenshot.

    <img src="/assets/img/props_post_sample.png" width="67%">

#### Step 3: Start Detect Engine
1. Start Detect Engine on the console (separate window, since Manager is running on the console as well).  The script will ask you to accept the license agreement (enter `y`). 
```
cd padas-detect/
```
--8<-- "padas_detect_start_console.md"

#### Step 4: Start Transform Engine
1. Before starting Transform Engine we must first create the specified input topic (i.e. `testtopic`) in Kafka.  You can do this from [Confluent Control Center](https://docs.confluent.io/platform/current/control-center/topics/create.html) or from the console as shown below.

    ```sh
    kafka-topics --create --bootstrap-server localhost:9092 --topic testtopic --partitions 1 --replication-factor 1
    Created topic testtopic.
    ```
    
2. Start Transform Engine on the console (separate window, since Manager and Detect Engine are running on the console as well).  The script will ask you to accept the license agreement (enter `y`). 
```
cd padas-transform/
```
--8<-- "padas_transform_start_console.md"

#### Step 5: Generate Sample Event

1. Let's generate a sample event with a simple JSON message.  Note that this JSON will match the PDL (`field1="value1"`) specified above.
```sh
echo '{"field1":"value1","field2":"value1"}' |  kafka-console-producer --bootstrap-server localhost:9092 --topic testtopic
```

#### Step 6: View Alerts

1. Once the sample event is ingested, PADAS Detect Engine will run the rules for matching datamodels in real-time and populate `padas_alerts` topic with matching event and alert information.  You can simply view this alert with the following command:

    ```sh
    kafka-avro-console-consumer --bootstrap-server localhost:9092 --topic padas_alerts --from-beginning | jq
    ```

    Output will be similar to the following.  Note the use of `jq` above for pretty display of JSON data.
    ```json
    {
      "timestamp": "2021-11-28T14:25:23.199+0300",
      "name": "Test Rule",
      "description": "",
      "references": null,
      "customAnnotations": null,
      "mitreAnnotations": null,
      "platforms": {
        "string": ""
      },
      "domain": "mitre_attack",
      "analyticType": {
        "string": ""
      },
      "severity": {
        "string": ""
      },
      "datamodelReferences": null,
      "events": [
        {
          "timestamp": "2021-11-28T14:18:30.309+0300",
          "datamodel": "testdm",
          "source": "unknown",
          "host": "padas.local",
          "src": null,
          "dest": null,
          "user": null,
          "rawdata": "{\"field1\":\"value1\",\"field2\":\"value1\"}",
          "jsondata": "{\"field1\":\"value1\",\"field2\":\"value1\"}"
        }
      ]
    }
    ```


#### Next Steps
- <a href="/docs/installation.html">Install</a> in production.
- <a href="/docs/user-guide.html">Utilize PADAS</a> with out-of-the-box [padasRules.json](/assets/config/padasRules.json)
- <a href="/docs/admin-guide.html#integrate-to-external-systems">Integrations</a> with ingest pipelines ([Sample Sysmon Config with Winlogbeat](/assets/config/sysmonconfig-export-exclude-winlogbeat.xml)) and ready-to-use transformations ([Winlogbeat Sysmon and Security](/assets/config/padas_transformation.properties))