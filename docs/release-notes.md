---
title: Release Notes
layout: documentation
latest_version: 0.0.4
---

### Version 0.0.4

**Release Date**: 11.09.2023

#### What's New?

| Feature                         | Description |
| ----------------------          | ----------------------       
| Topics initialization REST API  | New API endpoint that describes all required topics and returns `true` or `false`.


#### Known Issues

| Date Filed    | Issue Number      | Description |
| ------------- | ----------------  | ----------------------       
| 14.04.2023    | PADAS-71	        | After initial login, check for required topics is not performed. 
| 26.07.2023    | PADAS-137	        | For `PARSE_KV`, `PARSE_CSV`, and `EXTRACT` Task definitions, `field` option is unused.  This option performs extraction/parsing on a specific field value. 


#### Fixed Issues

| Date Fixed    | Issue Number      | Description |
| ------------- | ----------------  | ----------------------       
| 07.07.2023    | PADAS-78	        | UI lookup definition CRUD functionality is missing.
| 28.08.2023    | PADAS-135         | Error occurs when running multiple topologies.
| 04.09.2023    | PADAS-161         | Updated JSON Schema for FILTER Task REST API to make `action` field mandatory.
| 12.07.2023    | PADAS-103	        | Default and optional values should not be required in the forms.
| 11.09.2023    | N/A multiple      | Created and updated unit and integration tests to cover multiple scenarios.

---
