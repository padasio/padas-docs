<br />
<span class="fw-bold">Datamodel Name: </span><code>endpointService</code>
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
      <td><code>action</code></td>
      <td>string</td>
      <td>The action performed on the service.</td>
      <td><code>create<br/>delete<br/>pause<br/>start<br/>stop</code></td>
    </tr>
    <tr>
      <td><code>dest</code></td>
      <td>string</td>
      <td>The endpoint on which the service is installed.</td>
      <td><code>10.10.1.1</code></td>
    </tr>
    <tr>
      <td><code>name</code></td>
      <td>string</td>
      <td>The name of the service.</td>
      <td><code>RpcSs</code></td>
    </tr>
    <tr>
      <td><code>parentProcessId</code></td>
      <td>string</td>
      <td>The numeric identifier of the parent process assigned by the operating system.</td>
      <td><code>837</code></td>
    </tr>
    <tr>
      <td><code>process</code></td>
      <td>string</td>
      <td>All of the arguments passed to the process upon execution.</td>
      <td><code>C:\path\example.exe /flag1</code></td>
    </tr>
    <tr>
      <td><code>processExec</code></td>
      <td>string</td>
      <td>The executable name of the process</td>
      <td><code>example.exe</code></td>
    </tr>
    <tr>
      <td><code>processGuid</code></td>
      <td>string</td>
      <td>The globally unique identifier of the process assigned by the vendor_product.</td>
      <td><code>{f81d4fae-7dec-11d0-a765-00a0c91e6bf6}</code></td>
    </tr>
    <tr>
      <td><code>processHash</code></td>
      <td>string</td>
      <td>The digests of the contents of the file located at <code>processPath</code> by using md5, sha1, etc.</td>
      <td><code>5eb63bbbe01eeed093cb22bb8f5acdc3<br/>2aae6c35c94fcfb415dbe95f408b9ce91ee846ed</code></td>
    </tr>
    <tr>
      <td><code>processId</code></td>
      <td>string</td>
      <td>The numeric identifier of the process assigned by the operating system.</td>
      <td><code>837</code></td>
    </tr>
    <tr>
      <td><code>processPath</code></td>
      <td>string</td>
      <td>The file path of the executable associated with this process.</td>
      <td><code>C:\path\to\example.exe</code></td>
    </tr>
    <tr>
      <td><code>startMode</code></td>
      <td>string</td>
      <td>The start mode for the service.</td>
      <td><code>disabled<br/>manual<br/>auto</code></td>
    </tr>
    <tr>
      <td><code>status</code></td>
      <td>string</td>
      <td>The status of the service.</td>
      <td><code>started<br/>stopped<br/>warning<br/>critical</code></td>
    </tr>
    <tr>
      <td><code>user</code></td>
      <td>string</td>
      <td>The user account that spawned the process.</td>
      <td><code>LOCALUSER</code></td>
    </tr>
    <tr>
      <td><code>userId</code></td>
      <td>string</td>
      <td>The unique identifier of the user account which spawned the process. For Windows, this is the security identifier, <code>sid</code></td>
      <td><code>S-1-5-18</code></td>
    </tr>
  </tbody>
</table>