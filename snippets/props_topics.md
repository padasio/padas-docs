<table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">Topic Name</th>
      <th scope="col">Description</th>
      <th scope="col">Topic Settings</th>
      <th scope="col">Avro Schema</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>padas_alerts</code></td>
      <td>Streaming events topic, all events that match the rules (PDL) will populate this topic.  Alerts can be consumed by one or more endpoint systems.</td>
      <td><code>cleanup.policy: delete</code></td>
      <td><a href="/assets/config/padas_alert.avsc">padas_alert.avsc</a></td>
    </tr>
    <tr>
      <td><code>padas_events</code></td>
      <td>Streaming events topic, all events from transformations or direct ingest pipeline populates this topic for analysis by Padas rules.</td>
      <td><code>cleanup.policy: delete</code></td>
      <td><a href="/assets/config/padas_event.avsc">padas_event.avsc</a></td>
    </tr>
    <tr>
      <td><code>padas_rules</code></td>
      <td>Log compacted topic, keeps an up-to-date list of Padas rules.</td>
      <td>
        <code>cleanup.policy: compact</code>
        <code>retention.bytes: -1</code>
      </td>
      <td><a href="/assets/config/padas_rule.avsc">padas_rule.avsc</a></td>
    </tr>
    <tr>
      <td><code>padas_nodes</code></td>
      <td>Log compacted topic, keeps an up-to-date list of running Padas instances.</td>
      <td>
        <code>cleanup.policy: compact</code>
        <code>retention.bytes: -1</code>
      </td>
      <td>none</td>
    </tr>
    <tr>
      <td><code>padas_properties</code></td>
      <td>Log compacted topic, keeps properties for detect and transform engine.</td>
      <td>
        <code>cleanup.policy: compact</code>
        <code>retention.bytes: -1</code>
      </td>
      <td>none</td>
    </tr>
  </tbody>
</table>