**NOTE**: All required topics enable [log compaction](https://kafka.apache.org/documentation.html#compaction) since they keep relevant configuration entries.  Proper retention policy should be implemented in order to avoid any loss of configuration.


| Topic Name       | Description                                           | Kafka Settings      |
| -------------    | -----------------------------------                   | ------------------- |
| padas_nodes      | Up-to-date list of registered Padas Engine instances. | `cleanup.policy: compact`<br/>`retention.bytes: -1` |
| padas_tasks      | List of transformation and apply tasks.               | `cleanup.policy: compact`<br/>`retention.bytes: -1` |
| padas_pipelines  | List of pipelines that contain task information.      | `cleanup.policy: compact`<br/>`retention.bytes: -1` |
| padas_topologies | List of topologies that contain pipeline information. | `cleanup.policy: compact`<br/>`retention.bytes: -1` |
| padas_rules      | List of rules to be utilized by APPLY_RULES task.     | `cleanup.policy: compact`<br/>`retention.bytes: -1` |
