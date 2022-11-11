---
title: Release Notes
---

### <a name="anchor1"></a>

### Version 0.0.1

<br />

#### What's New?

<table class="table table-striped w-75">
  <thead>
    <tr>
      <th scope="col">Feature</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
  {% for item in site.data.release_notes_100.features %}
    <tr>
      <td>{{ item.feature }}</td>
      <td>{{ item.description }}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>

<br />

#### Known Issues

<table class="table table-striped w-75">
  <thead>
    <tr>
      <th scope="col">Date Filed</th>
      <th scope="col">Issue Number</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
  {% for item in site.data.release_notes_100.known_issues %}
    <tr>
      <td>{{ item.date }}</td>
      <td>{{ item.number }}</td>
      <td>{{ item.description }}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>

<br />

#### Fixed Issues

<table class="table table-striped w-75">
  <thead>
    <tr>
      <th scope="col">Date Fixed</th>
      <th scope="col">Issue Number</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
  {% for item in site.data.release_notes_100.fixed_issues %}
    <tr>
      <td>{{ item.date }}</td>
      <td>{{ item.number }}</td>
      <td>{{ item.description }}</td>
    </tr>
  {% endfor %}
  </tbody>
</table>