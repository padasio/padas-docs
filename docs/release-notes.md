---
title: Release Notes
layout: documentation
---

### Version {{ current_version }}

**Release Date**: 06.05.2024

#### What's New?

| Feature                         | Description |
| ----------------------          | ----------------------       
| `PDL_EXPRESSION` task supports correlation queries | Correlation support was only available in rules (i.e. `APPLY_RULES` function) but by adding this feature to `PDL_EXPRESSION`, it's possible to perform aggregation and related solutions (e.g. joining results of 2 separate topologies aggregated over a field) 
| Confluent Streams Security Integration | Stream configuration via `padas.properties` supports TLS/SSL related security settings as per [Secure Deployment for Kafka Streams in Confluent Platform](https://docs.confluent.io/platform/current/streams/developer-guide/security.html#kstreams-security)


#### Known Issues

| Date Filed    | Issue Number      | Description |
| ------------- | ----------------  | ----------------------       
| 06.11.2023    | PADAS-201	        | Cannot delete multiple configuration items from UI.

#### Fixed Issues

| Date Fixed    | Issue Number      | Description |
| ------------- | ----------------  | ----------------------   
| 15.03.2024    | PADAS-95         | Padas Engine start script to display proper notification.
| 01.04.2024    | PADAS-173         | Padas UI start script to display proper notification.

---
