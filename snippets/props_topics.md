This section is only applicable if `padas.config.store=kafka` is set in `padas.properties` file.  The following Kafka topics must be created for keeping centralized configuration entries. You can create these topics according to your preference (e.g. Padas UI, Confluent Control Center) and below steps simply provide one way of doing so.

**NOTE**: While it's possible to create these topics either via REST API or from Padas UI, it is **highly recommended** to review [Topic Configuration](https://docs.confluent.io/platform/current/installation/configuration/topic-configs.html) and tune settings for each Padas topic (specially for `partitions` and `replication_factor`) according to expected volume and performance requirements.

**NOTE**: All required topics must enable [log compaction](https://kafka.apache.org/documentation.html#compaction) since they keep relevant configuration entries.  Proper retention policy should be implemented in order to avoid any loss of configuration.


| Topic Name       | Description                                           | Kafka Settings      |
| -------------    | -----------------------------------                   | ------------------- |
| padas_nodes      | Up-to-date list of registered Padas Engine instances. | `cleanup.policy: compact`<br/>`retention.bytes: -1` |
| padas_tasks      | List of transformation and apply tasks.               | `cleanup.policy: compact`<br/>`retention.bytes: -1` |
| padas_pipelines  | List of pipelines that contain task information.      | `cleanup.policy: compact`<br/>`retention.bytes: -1` |
| padas_topologies | List of topologies that contain pipeline information. | `cleanup.policy: compact`<br/>`retention.bytes: -1` |
| padas_rules      | List of rules to be utilized by APPLY_RULES task.     | `cleanup.policy: compact`<br/>`retention.bytes: -1` |
| padas_lookups    | List of lookup files for data enrichment.             | `cleanup.policy: compact`<br/>`retention.bytes: -1` |
