<br />
<span class="fw-bold">Datamodel Name: </span><code>endpointListeningPort</code>
<br />
<table class="table table-striped w-75">
  <thead>
    <tr>
      <th scope="col">Field Name</th>
      <th scope="col">Data Type</th>
      <th scope="col">Description</th>
      <th scope="col">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>dest</code></td>
      <td>string</td>
      <td>The endpoint on which the port is listening.</td>
      <td><code>10.10.1.1</code></td>
    </tr>
    <tr>
      <td><code>destPort</code></td>
      <td>string</td>
      <td>Network port listening on the endpoint</td>
      <td><code>80</code></td>
    </tr>
    <tr>
      <td><code>processGuid</code></td>
      <td>string</td>
      <td>The globally unique identifier of the process assigned by the vendor_product.</td>
      <td><code>{f81d4fae-7dec-11d0-a765-00a0c91e6bf6}</code></td>
    </tr>
    <tr>
      <td><code>processId</code></td>
      <td>string</td>
      <td>The numeric identifier of the process assigned by the operating system.</td>
      <td><code>456</code></td>
    </tr>
    <tr>
      <td><code>src</code></td>
      <td>string</td>
      <td>The "remote" system connected to the listening port (if applicable).</td>
      <td><code>192.168.1.10</code></td>
    </tr>
    <tr>
      <td><code>srcPort</code></td>
      <td>string</td>
      <td>The "remote" port connected to the listening port (if applicable).</td>
      <td><code>4567</code></td>
    </tr>
    <tr>
      <td><code>state</code></td>
      <td>string</td>
      <td>The status of the listening port</td>
      <td><code>listening<br/>established</code></td>
    </tr>
    <tr>
      <td><code>transport</code></td>
      <td>string</td>
      <td>The network transport protocol associated with the listening port</td>
      <td><code>tcp<br/>udp</code></td>
    </tr>
    <tr>
      <td><code>user</code></td>
      <td>string</td>
      <td>The user account associated with the listening port.</td>
      <td><code></code></td>
    </tr>
  </tbody>
</table>