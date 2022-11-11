<span class="fw-bold">Detect Engine Properties</span>
<table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">Display Name</th>
      <th scope="col">Property Name</th>
      <th scope="col">Required</th>
      <th scope="col">Default Value</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Omit Raw Data</td>
      <td><code>alerts.topic.omit.rawdata</code></td>
      <td>yes</td>
      <td><code>false</code></td>
      <td>Define whether to omit raw data when generating PADAS Alerts.</td>
    </tr>
    <tr>
      <td>Omit Json Data</td>
      <td><code>alerts.topic.omit.jsondata</code></td>
      <td>yes</td>
      <td><code>false</code></td>
      <td>Define whether to omit JSON data when generating PADAS Alerts.</td>
    </tr>
    <tr>
      <td>Event Datetime Pattern</td>
      <td><code>event.datetime.pattern</code></td>
      <td>yes</td>
      <td><code>yyyy-MM-dd'T'HH:mm:ss.SSSZ</code></td>
      <td>Timestamp pattern to extract from Padas Events.  It is recommended use the default value.</td>
    </tr>
  </tbody>
</table>