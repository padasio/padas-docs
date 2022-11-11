<span class="fw-bold">Detection Rules Configuration</span>
<table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">Display Name</th>
      <th scope="col">JSON Field Name</th>
      <th scope="col">Type</th>
      <th scope="col">Required</th>
      <th scope="col">Default Value</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Rule Name</td>
      <td><code>name</code></td>
      <td><code>string</code></td>
      <td>yes</td>
      <td></td>
      <td>Rule name(e.g. Attack Detection - Successful Local Account Login).</td>
    </tr>
    <tr>
      <td>Rule Description</td>
      <td><code>description</code></td>
      <td><code>string</code></td>
      <td>yes</td>
      <td></td>
      <td>A brief description for this rule. (e.g. The successful use of Pass The Hash for lateral movement between workstations).</td>
    </tr>
    <tr>
      <td>PDL Query</td>
      <td><code>pdl</code></td>
      <td><code>string</code></td>
      <td>yes</td>
      <td></td>
      <td>PDL Query to match the event. (e.g. <code>event_id=4624 AND event_data.TargetUserName!='ANONYMOUS LOGON'</code>). Go to <a href="/docs/pdl-reference.html">PDL Reference</a> for details.</td>
    </tr>
    <tr>
      <td>Enabled</td>
      <td><code>enabled</code></td>
      <td><code>boolean</code></td>
      <td>yes</td>
      <td><code>true</code></td>
      <td>Defines whether this rule is enabled and active.</td>
    </tr>
    <tr>
      <td>Datamodel List</td>
      <td><code>datamodelList</code></td>
      <td><code>string array</code></td>
      <td>yes</td>
      <td></td>
      <td>Comma separated list of Datamodels where this rule will be applicable to.  These MUST match the datamodels in Padas Events (<code>padas_events</code>) topic, probably populated via Padas Transformation(s). (e.g. <code>sysmon, wineventlog</code>).</td>
    </tr>
    <tr>
      <td colspan=6>Additional/Optional Configuation <i class="bi bi-chevron-down"></i> </td>
    </tr>
    <tr>
      <td>Omit Raw Data from alerts</td>
      <td><code>omitRawdataFromAlerts</code></td>
      <td><code>boolean</code></td>
      <td>yes</td>
      <td><code>false</code></td>
      <td>Defines whether to omit raw data from generated alert(s), i.e. <code>padas_alerts</code> topic.</td>
    </tr>
    <tr>
      <td>Omit JSON Data from alerts</td>
      <td><code>omitJsondataFromAlerts</code></td>
      <td><code>boolean</code></td>
      <td>yes</td>
      <td><code>false</code></td>
      <td>Defines whether to omit JSON data from generated alert(s), i.e. <code>padas_alerts</code> topic.</td>
    </tr>
    <tr>
      <td>References</td>
      <td><code>references</code></td>
      <td><code>string array</code></td>
      <td>no</td>
      <td></td>
      <td>Comma separated list of references for this rule.</td>
    </tr>
    <tr>
      <td>Platform</td>
      <td><code>platforms</code></td>
      <td><code>string</code></td>
      <td>no</td>
      <td></td>
      <td>Applicable platform(s) for this rule. (e.g. <code>Windows</code>)</td>
    </tr>
    <tr>
      <td>Domain</td>
      <td><code>domain</code></td>
      <td><code>string</code></td>
      <td>yes</td>
      <td><code>mitre_attack</code></td>
      <td>Applicable domain for this rule. (e.g. mitre_attack)</td>
    </tr>
    <tr>
      <td>Severity</td>
      <td><code>severity</code></td>
      <td><code>string</code></td>
      <td>no</td>
      <td></td>
      <td>String representing severity of this detection (e.g. <code>medium</code>)</td>
    </tr>
    <tr>
      <td>Custom Annotations</td>
      <td><code>customAnnotations</code></td>
      <td><code>string array</code></td>
      <td>no</td>
      <td></td>
      <td>Please enter any custom annotations (e.g. <code>CIS20, KillChain, NIST</code>, etc.) as a comma separated list pertinent to this rule</td>
    </tr>
    <tr>
      <td colspan=6>MITRE ATT&amp;CK Annotations <i class="bi bi-chevron-down"></i></td>
    </tr>
    <tr>
      <td>(sub)Technique ID List</td>
      <td><code>mitreAnnotations</code></td>
      <td><code>string array</code></td>
      <td>no</td>
      <td></td>
      <td>MITRE ATT&amp;CK Technique and Subtechnique IDs as a comma separated list. (e.g. <code>T1550, T1550.001, T1550.002</code>).</td>
    </tr>
    <tr>
      <td>Analytic Type</td>
      <td><code>analyticType</code></td>
      <td><code>string</code></td>
      <td>no</td>
      <td></td>
      <td>Applicable analytic type for this rule according to MITRE Cyber Analytics Repository (e.g. <code>Situational Awareness</code>)</td>
    </tr>
    <tr>
      <td>Datamodel References</td>
      <td><code>datamodelReferences[] PadasDatamodelReference</code></td>
      <td><code>string</code></td>
      <td>no</td>
      <td></td>
      <td>List of datamodel reference triplets (object|action|field) separated by commas. (e.g. <code>process|create|command_line, process|create|exe</code>)</td>
    </tr>                                                                                 
  </tbody>
</table>