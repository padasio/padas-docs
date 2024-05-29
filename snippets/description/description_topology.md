A topology is simply a group of one or more ordered pipelines where it reads from a single input topic and writes to one or more output topic(s).  Both input and output topic(s) are mandatory requirements for a topology that Padas engine runs.  A topology consists of one or more ordered pipelines where an output from one pipeline becomes an input for the next pipeline definition.

It's possible to define any number of topologies per Padas Engine, where each topology starts a different processing task within one or more threads.  For more detailed architectural description on Kafka streams processor topology please refer to [Confluent Documentation](https://docs.confluent.io/platform/current/streams/architecture.html#processor-topology).