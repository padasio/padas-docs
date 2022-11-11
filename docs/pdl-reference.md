---
title: PDL Reference
---
## PDL Reference
This is a reference guide for the Padas Domain Language (PDL).   In this manual you will find explanation of PDL syntax, descriptions, and examples. 

In order to understand how PADAS works, please review [Getting Started](/docs/get-started.html).

<br>

#### PDL Syntax
The following sections desribe the syntax used for Padas Domain Language (PDL) queries.  PDL performs operations on a single event (`padas_events` topic, `jsondata` field) and simply compares to the query, then returns a `boolean` response to indicate a match or mismatch.

PDL syntax requires fields to be available in JSON object that it compares against.

<br>

#### Examples

--8<-- "pdl_examples.md"

<br>

#### Supported Operators
PDL supports the following operators and keywords when comparing events to the query.

--8<-- "pdl_operators.md"

<br>

#### Supported JSON Values
PDL comparisons work on **String** and **Integer** JSON values.  **String** comparisons MUST be defined in quotes `"` within PDL query definition.

<br />
**Examples:**

PDL query with `field1="123"` will compare `"123"` as a **String** JSON value.

PDL query with `field2=123` will compare `123` as an **Integer** JSON value.

<br>

#### Wildcard Support
PDL supports a single wildcard `*` with Equals operator (`=`) for **String** JSON values.  Following are valid PDL query examples with wildcard usage:

```
field1="val*1"
field1="val*"
field1="*ue1"
```

<br />

#### Grouped arguments
Sometimes the syntax must display arguments as a group to show that the set of arguments are used together. Parenthesis `( )` are used to group arguments.

For example in this syntax:
`(field1="val1" OR field2=123) AND field3="value3"`

The grouped argument is `(field1="val1" OR field2=123)` and its results are evaluated as a whole.

<br />


