<br />
<span class="fw-bold">Datamodel Name: </span><code>endpointRegistry</code>
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
      <td>The action performed on the resource.</td>
      <td><code>create<br/>delete<br/>modify<br/>read</code></td>
    </tr>
    <tr>
      <td><code>dest</code></td>
      <td>string</td>
      <td>The endpoint on which the port is listening.</td>
      <td><code>10.10.1.1</code></td>
    </tr>
    <tr>
      <td><code>process</code></td>
      <td>string</td>
      <td>All of the arguments passed to the process upon execution.</td>
      <td><code>C:\path\example.exe /flag1</code></td>
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
      <td><code>registryHive</code></td>
      <td>string</td>
      <td>The logical group of keys, subkeys, and values in the registry.</td>
      <td><code>HKEY_CURRENT_USER<br/>HKEY_LOCAL_MACHINE</code></td>
    </tr>
    <tr>
      <td><code>registryKey</code></td>
      <td>string</td>
      <td>The registry key specified in the event. Similar to a folder in a traditional file system.</td>
      <td><code>HKLM\SYSTEM\CurrentControlSet\services\RpcSs</code></td>
    </tr>
    <tr>
      <td><code>registryValueName</code></td>
      <td>string</td>
      <td>The descriptive name for the data being stored in the key.</td>
      <td><code>InstalledVersion</code></td>
    </tr>
    <tr>
      <td><code>registryValueData</code></td>
      <td>string</td>
      <td>The contents of the value, typically a text string.</td>
      <td><code>%SystemRoot%\system32\svchost.exe -k rpcss</code></td>
    </tr>
    <tr>
      <td><code>registryValueType</code></td>
      <td>string</td>
      <td>The type of data being stored in the value. Types include binary data, 32 bit numbers, strings, etc.</td>
      <td><code>REG_SZ<br/>REG_MULTI_SZ<br/>REG_DWORD<br/>REG_BINARY<br/>REG_QWORD</code></td>
    </tr>
    <tr>
      <td><code>status</code></td>
      <td>string</td>
      <td>The outcome of the registry action.</td>
      <td><code>failure<br/>success</code></td>
    </tr>
    <tr>
      <td><code>user</code></td>
      <td>string</td>
      <td>The user account associated with the listening port.</td>
      <td><code></code></td>
    </tr>
  </tbody>
</table>