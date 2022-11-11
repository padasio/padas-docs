<table class="table table-striped w-75">
  <thead>
    <tr>
      <th scope="col">Component</th>
      <th scope="col">Storage</th>
      <th scope="col">Memory</th>
      <th scope="col">CPU</th>
      <th scope="col">Nodes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Manager</td>
      <td>100GB, preferably SSD</td>
      <td>8GB RAM</td>
      <td>2 cores or more</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Detect Engine</td>
      <td>SSD.  Sizing depends on the number of queries.  For evaluation/test/dev 10-20GB should be sufficient.</td>
      <td>12GB to 64GB RAM.</td>
      <td>4 cores or more</td>
      <td>1 to many, depends on <code>padas_events</code> partition count and scalability requirements</td>
    </tr>
    <tr>
      <td>Transform Engine</td>
      <td>100GB, preferably SSD</td>
      <td>12GB to 64GB RAM.  Sizing depends on the number of transformations.</td>
      <td>4 cores or more</td>
      <td>1 to many, depends on input topic(s) and scalability requirements</td>
    </tr>
  </tbody>
</table>