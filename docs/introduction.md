---
title: Introduction
layout: documentation
---

### What is PADAS?
--8<-- "whatispadas.md"
<br>

---

### Components
Padas has 2 main components:

1. **Manager UI**: All configuration changes (CRUD - Create, Read, Update, Delete operations) can be performed through Manager web interface.  This is an optional but recommended component to manage configurations through Engine API.
2. **Engine**: Reads configurations from existing Padas topics and runs assigned (based on `group` setting) and enabled topologies.  Each topology reads from a single source topic, runs one or more pipeline(s), and writes the resulting outputs to one or more output topic(s).  Each pipeline consists of one or more task(s) where each task can perform a filter, transform, enrichment, or detection (rules) function.  Please see below for details on concepts.

A Manager UI can be configured to connect to a single Engine component.  Engine components can be scaled up or down as needed with group assignments to distribute work-load.
<figure markdown>
  <p>
  <img src="/assets/img/padas_design_details.png" class="img-fluid py-5">
  </p>
</figure>

### Basic Concepts
Let's take a closer look at Padas configuration and engine's processing concepts.  At a high-level, Padas Engine reads an input topic, processes data (pipelines and tasks) and writes to one or more output topics.

<figure markdown>
  <p>
  <img src="/assets/img/padas_topology_pipeline_task.png" class="img-fluid py-5">
  </p>
</figure>

#### Topology
A topology is simply a group of one or more ordered pipelines where it reads from a single input topic and writes to one or more output topic(s).  Both input and output topic(s) are mandatory requirements for a topology that Padas engine runs.  A topology consists of one or more ordered pipelines where an output from one pipeline becomes an input for the next pipeline definition.

It's possible to define any number of topologies per Padas Engine, where each topology starts a different processing task within one or more threads.  For more detailed architectural descriptions please refer to [Confluent Documentation](https://docs.confluent.io/platform/current/streams/architecture.html#processor-topology).

#### Pipeline
A pipeline consists of one or more ordered tasks where an output from one task becomes an input for the next task definition.  A pipeline is a logical grouping of tasks for specific goals.  For example, in terms of processing takss, a single pipeline with 12 different tasks is the same as having 3 consecutive pipelines with 4 different tasks each.

#### Task
A task is the single unit of work performed on event data.  Each task has the following built-in functions that can perform processing on an event:

- `FILTER`: Filter an event (keep or drop) based on [PDL](/pdl-reference) or regex definition.  For PDL, the input must be `JSON`.
- `EXTRACT`: Extract any event input with provided Regular Expression defition (named groups). The output is `JSON`.
- `PARSE_CSV`: Parse input `CSV` event into `JSON`.
- `PARSE_KV`: Parse input key-value pairs event into `JSON`.
- `EVAL`: Add, remove or rename fields within `JSON` data.  Both input and output are `JSON`.
- `TIMESTAMP`: Define a field from within the event data (`JSON` formatted) to use as the timestamp.
- `APPLY_RULES`: Apply predefined rules (see below for [Rule](#rule)) to matching events tagged with specific data models.  This requires events to have `datamodels` field (an array of strings).
- `CONVERT_TO_CSV`: Convert existing `JSON` event into `CSV`.


#### Rule
A rule is a PDL query that matches an event.  The goal is to associate a rule with a specific data model and assign one or more annotations (e.g. MITRE ATT&amp;CK technique IDs) for further processing by other analytics systems.