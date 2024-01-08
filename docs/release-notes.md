---
title: Release Notes
layout: documentation
---

### Version {{ current_version }}

**Release Date**: 08.01.2024

#### What's New?

| Feature                         | Description |
| ----------------------          | ----------------------       
| Update topics view to support new features.  | Topics view now has an overview (summary of important settings), messages (ability to create and view topic content), and settings (view all topic settings) tabs.
| Topology configuration allows custom stream configuration options. | Stream topology configuration supports Avro SerDe (Serializer/Deserializer) information to be specified and administrators can provide further resiliency parameters as per [Confluent Documentation](https://docs.confluent.io/platform/current/streams/developer-guide/config-streams.html#recommended-configuration-parameters-for-resiliency)
| A new Task, `OUTPUT_FIELD` is added. | From a given JSON input streaming event, a single field value can be output as an event (e.g. only output a matching `_raw` field value to be consumed by endpoint analytics system).


#### Known Issues

| Date Filed    | Issue Number      | Description |
| ------------- | ----------------  | ----------------------       
| 06.11.2023    | PADAS-201	        | Cannot delete multiple configuration items from UI.

#### Fixed Issues

| Date Fixed    | Issue Number      | Description |
| ------------- | ----------------  | ----------------------   
| 01.11.2023    | PADAS-175	        | Fix typo and update streams and admin configuration in documentation.
| 01.01.2024    | PADAS-216	        | User can be created without a role.

---
