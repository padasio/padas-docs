
Description of fields and state details can be found below.

| Field   | Description                                           | Example      |
| ------- | -----------------------------------                   | ------------------- |
| UUID    | Unique identifier for this instance. | `26ee88e3-a753-4c8b-9adf-e0432abbbded` |
| Host    | Hostname of the instance.               | `padas.local` |
| REST    | REST API endpoint where UI will connect to.      | `https://padas.local:8999` |
| Group   | Consumer group associated with this instance.     | `default`  |
| State   | Current state of this streaming application. See below table for details. | `RUNNING` |


_State Details_

Padas Engine is built as a Kafka Streams application and the state information is inherited from [KafkaStreams.State](https://kafka.apache.org/11/javadoc/org/apache/kafka/streams/KafkaStreams.State.html). The following is a section from this link.  Padas Engine instance must only be in one state at a time.  The expected state transition is defined as:

<figure markdown>
  <p>
  <img src="../assets/img/props_nodes_states.png" class="img-fluid py-5 w-75">
  </p>
</figure>
 
 **NOTE**: In order to reach a `RUNNING` state, you need at least 1 enabled Topology configuration that is assigned to the same group as the Padas Engine.