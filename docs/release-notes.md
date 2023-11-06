---
title: Release Notes
layout: documentation
---

### Version {{ current_version }}

**Release Date**: 06.11.2023

#### What's New?

| Feature                         | Description |
| ----------------------          | ----------------------       
| PDL Expression commands for field extraction.  | New PDL commands perform additional field extractions on specific JSON fields: `rex`, `parse_csv`, `parse_kv`
| PDL Operator for regex based query matching.   | New operator, `~=`, allows query matching based on regular expression patterns.
| Topics UI and API update        | Topics UI and API allow Create, Read, Delete operations on Kafka topics.
| Produce messages to a topic.    | Produce a message to a given topic from UI.
| Consume messages from a topic.  | Subscribe and consume messages from a topic to visualize streaming event activity.
| Embedded configuration without topic creation. | No need to create topics upon initial installation.  Padas configuration attribute `padas.config.store` supports both local (`rocksdb`) and compacted topic (`kafka`) based setup.
| Define SerDe information for Topology topics.  | When creating Topologies, it's possible to specify SerDe (Serializer/Deserializer) information for both key and value.


#### Known Issues

| Date Filed    | Issue Number      | Description |
| ------------- | ----------------  | ----------------------       


#### Fixed Issues

| Date Fixed    | Issue Number      | Description |
| ------------- | ----------------  | ----------------------   
| 20.09.2023    | PADAS-71	        | After initial login, check for required topics is not performed.     
| 29.09.2023    | PADAS-137	        | For `PARSE_KV`, `PARSE_CSV`, and `EXTRACT` Task definitions, `field` option is unused.  This option performs extraction/parsing on a specific field value. 
| 20.09.2023    | PADAS-164         | The engine does not start if there are no topics.
| 30.10.2023    | PADAS-172         | UI fails to start with emtpy `local.json` configuration file.

---
