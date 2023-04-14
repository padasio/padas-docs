---
title: Sigma Rule Reference
---
### Fields
Padas Rule is needed 5 basic keys that are created by different fields in Simple/Meta Rules. <br> These are `id`, `name`, `description`, `datamodel`, `annotations`, `pdl`. 

---
### Field Mapping (Padas : Sigma)
Mapping of Padas vs. Sigma Rule can be seen below table. There is a tiny difference between Simple and Meta mapping. Padas creates PDL with `detection` field from Simple Rule but `action` field from Meta.

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
            pdl         : type, fieled, group-by, timespan, condition, ordered, aliases *
          
        ````
<small>* This will be explained under [ Conversion of Fields / pdl / Meta Rule ] section </small>
      </td>
    </tr>
  </tbody>
  </table>

---
### Conversion of Fields
#### id   
It is directly coming from the **id** field as `str`. If there is no id in the Sigma Rule, it uses the **title** field. Also, uses the **name** field as the last option. This rule of the field is same in both Simple and Meta Rules.
<br>
#### name   
It is directly coming from the **title** field as `str`. If there is no title in the Sigma Rule, it uses the **name** field. This rule of the field is same in both Simple and Meta Rules.
<br>
#### description 
It is directly coming from the **description** field as `str` in both Simple and Meta Rules.
<br>
#### datamodel 
It is coming from logsource field as `str` in **Simple Rule**, and created as `str` for **Meta Rule**.
    <br> 
        <table>
          <thead>
            <tr>
              <th style="text-align: center;" scope="col">Simple Rule</th>
              <th style="text-align: center;" scope="col">Meta Rule</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="align-middle">
                ```
                category + "_" + product + "_" + service
                ```
              </td>
              <td class="align-middle">
                ```
                "padas_alert"
                ```
              </td>
            </tr>
          </tbody>
        </table>
<br>
#### annotations  
It is directly coming from **tags** field as `list` in both Simple and Meta Rules.
<br>
#### pdl 
This field is completely different for Simple and Meta Rules, but the "condition" field works similarly for both. `condition` field gives information about modifiers, conditions, etc. and their relationships for desired fields. There are some modifiers for field conditions rules. They and their PDL equivalents can be found in below table.
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
###### Simple Rule
--8<-- "sigma_pdl_simple.md"
<br>
###### Meta Rule
--8<-- "sigma_pdl_meta.md"
