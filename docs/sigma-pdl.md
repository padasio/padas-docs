---
title: Sigma Rule Reference
---

This reference section provides explanations on inner workings of [Sigma v2 to Padas converter script](https://github.com/padasinc/padas-tools/tree/main/sigma_v2_to_padas).

### Field Mapping (Padas : Sigma)
The table below provides field mapping information of Padas [Rule](/stream-config/#rules) vs. Sigma Rule. There is a tiny difference between Simple and Meta mapping. Padas creates PDL with `detection` field from Simple Rule but `action` field from Meta.

<table>
  <thead>
    <tr>
      <th style="text-align: center;" scope="col">Padas Rule : Simple Sigma v2 Rule</th>
      <th style="text-align: center;" scope="col">Padas Rule : Meta Sigma v2 Rule</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="align-middle">
        ```
            id          : id / title / name
            name        : title / name
            description : description
            datamodel   : logsource
            annotations : tags
            pdl         : detection
        ```
        <b>
        &emsp;
        </b>
      </td>
      <td class="align-middle">
        ````
            id          : id / title / name
            name        : title / name
            description : description
            datamodel   : "padas_alert"
            annotations : tags
            pdl         : type, field, group-by, timespan, condition, ordered, aliases *
          
        ````
<small>* See below for details. </small>
      </td>
    </tr>
  </tbody>
  </table>

---
### Conversion of Fields
#### id   
The first matching Sigma field ise used from the following list, in order of precedence: `id`, `title`, `name`

#### name   
The first matching Sigma field ise used from the following list, in order of precedence: `title`, `name`

#### description 
The `description` Sigma field is used.

#### datamodel 
For Simple Rules, `logsource` Sigma field is used.  For Meta Rules `padas_alert` is assigned for this value.  Following table shows the subfields used to construct `datamodel` field in Padas Rule.

| Simple Rule                                | Meta Rule |
| ------------------------------------------ | ------------- |
| `category + "_" + product + "_" + service` | `padas_alert` |


#### annotations  
The `tags` Sigma field is used.

#### pdl 
This field is where the actual conversion happens to make it meaningful for Padas. The `condition` field works similarly for both Simple and Meta rules as it gives information about modifiers, conditions, etc. and their relationships for desired fields. There are some modifiers for field conditions rules. The following table provides information regarding Simple Rule modifier conversion.

<table>
  <thead>
    <tr>
      <th style="text-align: center;" scope="col">Sigma Rule Field  Modifiers</th>
        <th style="text-align: center;" scope="col">PDL Field Modifiers</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="align-middle">
        contains
        </td>
      <td class="align-middle">
        ```
        ?=
        ```
        </td>
    </tr>
  </tbody>
     <tbody>
    <tr>
      <td class="align-middle">
        startswith
        </td>
      <td class="align-middle">
        ```
        "...*"
        ```
        </td>
    </tr>
  </tbody>
     <tbody>
    <tr>
      <td class="align-middle">
        endswith
        </td>
      <td class="align-middle">
        ```
        "*..."
        ```
        </td>
    </tr>
  </tbody>
     <tbody>
    <tr>
      <td class="align-middle">
        gt
        </td>
      <td class="align-middle">
        ```
        >
        ```
        </td>
    </tr>
  </tbody>
     <tbody>
    <tr>
      <td class="align-middle">
        gte
        </td>
      <td class="align-middle">
        ```
        >=
        ```
        </td>
    </tr>
  </tbody>
     <tbody>
    <tr>
      <td class="align-middle">
        lt
        </td>
      <td class="align-middle">
        ```
        <
        ```
        </td>
    </tr>
  </tbody>
     <tbody>
    <tr>
      <td class="align-middle">
        lte
        </td>
      <td class="align-middle">
        ```
        <=
        ```
        </td>
    </tr>
  </tbody>
</table>

<br>
###### Simple Rule Examples
--8<-- "sigma/sigma_pdl_simple.md"
<br>
###### Meta Rule Examples
--8<-- "sigma/sigma_pdl_meta.md"
