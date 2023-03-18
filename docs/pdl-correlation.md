---
title: PDL Correlation
---

## Correlation Statement
PDL provides several correlation statements for analyzing and aggregating data over time, including:

- `event_count`: Calculates the count of events over a given timespan and stores the results under `padasAggregation` field.
- `value_count`: Calculates the count of specific field values over a given timespan and stores the results under `padasAggregation` field.
- `temporal`: Evaluates a list of events over a given timespan based on query expressions and stores the results under `padasTemporal` field.

Correlation statements have the following generic structure:
```bash
<function-command> [<function-specific-params>] <timespan-param> <group-by-clause> <where-clause>
```

Some example correlation statements:
```
event_count timespan=5m group_by field1 where field3 > 100
value_count(myfield) timespan=30s
temporal(ordered=true) [ padasRule="internal_error" || padasRule="new_network_connection" ] timespan=1m group_by internal_ip, remote_ip
```

### Common Parameters for Functions
All correlation statements evaluate streaming events for a given time window (defined via `timespan` parameter) and optionally groups them according to selected fields (defined via `group_by` clause).  For counting aggregation/correlation statements it's also possible to limit the results by providing a query expression (defined via `where` clause).

#### Argument Order
Correlation statements must start with the one of the available functions, followed by function specific parameters (if any).  Common argument order and descriptions are provided in the following table.


| Order | Keyword     | Required | Description                    | Example                    |
| ----- | ----------- | -------- | ------------------------------ | -------------------------- |
| 1     | `timespan`  | Yes      | Specifies time window to perform aggregated function.<br/>The value should be an integer followed by one of the following identifiers:<br/>`s` for second(s)<br/>`m` for minute(s)<br/>`h` for hour(s)<br/>`d` for day(s)| `timespan=5m`<br/>`timespan=1h` | 
| 2     | `group_by`  | No       | Group correlation results according to specified field(s). | `group_by field1, field2` |
| 3     | `where`     | No       | Filter events according to specified query expression. | `where field1 > 100` |



### Event Count
--8<-- "pdl_eventcount_details.md"

### Value Count
--8<-- "pdl_valuecount_details.md"

### Temporal
--8<-- "pdl_temporal_details.md"

