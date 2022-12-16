---
title: User Guide
---
## User Guide

<br>

### Account Settings
<br>
You can view and edit current user's account settings (Display Name, Email address and password) via this view.

<br/>
<img src="/assets/img/account_settings.png" width="67%">

---

### About Overview
<br>
Overview provides information regarding license information and registered nodes.  Note that licensing quota is based on number of Detect nodes with an expiration date.

Registered Node Information table provides details on actively running PADAS instances (other than this manager).

<br/>
<img src="/assets/img/overview_sample.png" width="67%">

---

### Topics
<br>
Upon initial login, PADAS Manager checks whether all required topics are created and available.  If any one of the required topics is missing, you'll be redirected to Topics view in order to view and update existing settings. This is a simple interface to create required Kafka topics through PADAS Manager interface.

**Important Note**: Number of partitions can NOT be changed/updated once a topic is created.  This value depends on your data volume and scalability requirements.  If you need to change/update this value for any reason, the topic will need to be deleted and created again with new values.  For more information regarding topics, please refer to [Topic Properties](/docs/admin-guide.html#anchor3)

If you need more control over topic creation, please consult your Kafka/PADAS administrator; you can also refer to [Confluent Documentation](https://docs.confluent.io/platform/current/control-center/topics/overview.html).

<br/>
<img src="/assets/img/topics_pre_sample.png" width="67%">

---

### Properties
<br>
Properties view provides configuration entries for Detect and Transform Engine components.  You can click <span class="btn btn-padas">Edit</span> button to enter in edit mode and make changes.  Following table provides information on the form fields.

**NOTE**: You can upload (click <span class="btn btn-padas"><i class="bi bi-chevron-right"></i> Upload Properties from File</span> button) and/or download (click <span class="btn btn-padas"><i class="bi bi-download"></i> Download Properties </span> button) properties as a file.  A sample properties file for Winlogbeat transformations can be found here: [Winlogbeat Sysmon and Security](/assets/config/padas_transformation.properties)

**NOTE**: You can click <span class="btn btn-padas"><i class="bi bi-plus-lg"></i> Add New Transformation</span> button to add new input topics for analysis.  The input topic *must* exist prior to starting PADAS Transform Engine.

**NOTE**: After any configuration changes, you will need to restart the corresponding component(s) (i.e. Detect and/or Transform Engine(s)).  PADAS instances read and load the configuration upon starting.

<br />

--8<-- "props_detect.md"

<br /><br />

--8<-- "props_transform.md"

<br/>

**Properties View Sample**
<br/>

<img src="/assets/img/props_pre_sample.png" width="67%">

<br/>

---

### Rules
<br>
Rules view provides configuration entries for Detect Engine rules that are applicable to various data models (as specified in transformations or `padas_events` topic).  Relevant schema for PADAS topics can be found [here](/docs/admin-guide.html#topic-properties).

**NOTE**: You can upload (click <span class="btn btn-padas"><i class="bi bi-chevron-right"></i> Upload Rules from File</span> button) and/or download (click <span class="btn btn-padas"><i class="bi bi-download"></i> Download Rules</span> button) rules as a JSON file.  An out-of-the-box JSON rule file is provided for Winlogbeat according to MITRE ATT&amp;CK framework and can be found here: [padasRules.json](/assets/config/padasRules.json)

**NOTE**: You can click <span class="btn btn-padas"><i class="bi bi-plus-lg"></i> Add New Rule</span> button to add new detection rule.

**NOTE**: Any change in detection rules is effective immediately (updates `padas_rules` topic) and does NOT require any restart/refresh.

<br />

--8<-- "props_rules.md"

<br />

**Rules View Sample**
<br/>
<img src="/assets/img/rules_pre_sample.png" width="67%">
