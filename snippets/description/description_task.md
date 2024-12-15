A task is the single unit of work performed on event data.  Each task has the following built-in functions that can perform processing on an event:

- `APPLY_RULES`: Apply predefined rules (per event and/or correlated/aggregated) to streaming events. The input must be `JSON`.
- `EXTRACT`: Extract any event input with provided Regular Expression defition (named groups). The output is `JSON`.
- `FILTER`: Filter an event (keep or drop) based on [PDL](../pdl-quick-reference) or regex definition.  For PDL, the input must be `JSON`.
- `OUTPUT_FIELD`: Outputs the value of a given field.  The input must be `JSON` and the output is `String` representation of the selected field value.
- `PARSE_CEF`: Parse input CEF (Common Event Format) event into `JSON`.
- `PARSE_CSV`: Parse input `CSV` event into `JSON`.
- `PARSE_KV`: Parse input key-value pairs event into `JSON`.
- `PDL_EXPRESSION`: Allows event data transformation and enrichment via [PDL](../pdl-quick-reference) expressions. The input must be `JSON`.
- `TIMESTAMP`: Define a field from within the event data (`JSON` formatted) to use as the timestamp.