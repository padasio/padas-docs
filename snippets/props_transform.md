<span class="fw-bold">Transform Engine Properties (for each Input Topic)</span>
<br />
<span class="fst-italic text-muted">N starts with 0 and incremented by 1 (e.g. 0,1,2,3, etc.)</span>
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
      <td>Topic Name</td>
      <td><code>input.topic.N.name</code></td>
      <td>yes</td>
      <td></td>
      <td>Define whether to omit raw data when generating PADAS Alerts.</td>
    </tr>
    <tr>
      <td>Enabled</td>
      <td><code>input.topic.N.enabled</code></td>
      <td>no</td>
      <td><code>true</code></td>
      <td>Defines whether this transformation is enabled or not</td>
    </tr>
    <tr>
      <td>Raw Data Field</td>
      <td><code>input.topic.N.rawdata.field</code></td>
      <td>no</td>
      <td>event value</td>
      <td>Defines the extracted field that has the raw event data.  If undefined, all event value is used.</td>
    </tr>
    <tr>
      <td>Omit Raw Data</td>
      <td><code>input.topic.N.omit.rawdata</code></td>
      <td>no</td>
      <td><code>false</code></td>
      <td>Defines whether to omit raw data when populating PADAS Events</td>
    </tr>
    <tr>
      <td>Extraction</td>
      <td><code>input.topic.N.extraction</code></td>
      <td>no</td>
      <td><code>json</code></td>
      <td>Defines how to extract fields from input topic.  Available values are <code>json</code> and <code>regex</code>.  If <code>regex</code> is specified, Regex definition is used for extraction.</td>
    </tr>
    <tr>
      <td>Regex</td>
      <td><code>input.topic.N.regex</code></td>
      <td>no</td>
      <td></td>
      <td>Defines a regular expression on how to extract fields from the topic's value.  Applicable only when extraction is set to regex.
      For regular expressions, only named-capturing groups are allowed currently for field extractions.  Please refer to <a href="https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/regex/Pattern.html" target="_blank">Java Regex Pattern</a> for details.
      <br /><br />
      Example for apache: <br />
      <code>^(?&lt;host&gt;[^ ]*) [^ ]* (?&lt;user&gt;[^ ]*) \[(?&lt;time&gt;[^\]]*)\] "(?&lt;method&gt;\S+)(?: +(?&lt;path&gt;[^\"]*?)(?: +\S*)?)?" (?&lt;code&gt;[^ ]*) (?&lt;size&gt;[^ ]*)(?: "(?&lt;referer&gt;[^\"]*)" "(?&lt;agent&gt;[^\"]*)")?$
      </code>
      </td>
    </tr>
    <tr>
      <td>Timestamp Field</td>
      <td><code>input.topic.N.timestamp.field</code></td>
      <td>no</td>
      <td></td>
      <td>Defines the extracted field to be used as the timestamp of the event.  If left empty or unspecified, current time is used.</td>
    </tr>
    <tr>
      <td>Timestamp Pattern</td>
      <td><code>input.topic.N.timestamp.pattern</code></td>
      <td>no</td>
      <td><code>yyyy-MM-dd'T'HH:mm:ss.SSSZ</code></td>
      <td>Defines the pattern for timestamp field, if specified.</td>
    </tr>
    <tr>
      <td>Host Name</td>
      <td><code>input.topic.N.host.name</code></td>
      <td>no</td>
      <td>current hostname</td>
      <td>Defines the hostname for this event (static).  This setting is only applicable if <code>host.field</code> is NOT specified.</td>
    </tr>
    <tr>
      <td>Host Field</td>
      <td><code>input.topic.N.host.field</code></td>
      <td>no</td>
      <td></td>
      <td>Defines the field to be used as hostname for this event (dynamic).  This setting overwrites <code>host.name</code></td>
    </tr>
    <tr>
      <td>Source Name</td>
      <td><code>input.topic.N.source.name</code></td>
      <td>no</td>
      <td>input topic name</td>
      <td>Defines the source for this event (static).  This setting is only applicable if <code>source.field</code> is NOT specified.</td>
    </tr>
    <tr>
      <td>Source Field</td>
      <td><code>input.topic.N.source.field</code></td>
      <td>no</td>
      <td></td>
      <td>Defines the field to be used as source for this event (dynamic).  This setting overwrites <code>source.name</code></td>
    </tr>
    <tr>
      <td>Datamodel Name</td>
      <td><code>input.topic.N.datamodel.name</code></td>
      <td>no</td>
      <td>input topic name</td>
      <td>Defines the datamodel for this event (static).  This setting is only applicable if <code>datamodel.field</code> is NOT specified.</td>
    </tr>
    <tr>
      <td>Datamodel Field</td>
      <td><code>input.topic.N.datamodel.field</code></td>
      <td>no</td>
      <td></td>
      <td>Defines the field to be used as datamodel for this event (dynamic).  This setting overwrites <code>datamodel.name</code></td>
    </tr>
    <tr>
      <td>Event src Value</td>
      <td><code>input.topic.N.src.value</code></td>
      <td>no</td>
      <td></td>
      <td>Defines the source host/IP address for this event (static).  This setting is only applicable if <code>src.field</code> is NOT specified.</td>
    </tr>
    <tr>
      <td>Event src Field</td>
      <td><code>input.topic.N.src.field</code></td>
      <td>no</td>
      <td></td>
      <td>Defines the field to be used as source host/IP address for this event (dynamic).  This setting overwrites <code>src.value</code></td>
    </tr>
    <tr>
      <td>Event dest Value</td>
      <td><code>input.topic.N.dest.value</code></td>
      <td>no</td>
      <td></td>
      <td>Defines the destination host/IP address for this event (static).  This setting is only applicable if <code>dest.field</code> is NOT specified.</td>
    </tr>
    <tr>
      <td>Event dest Field</td>
      <td><code>input.topic.N.dest.field</code></td>
      <td>no</td>
      <td></td>
      <td>Defines the field to be used as destination host/IP address for this event (dynamic).  This setting overwrites <code>dest.value</code></td>
    </tr>
    <tr>
      <td>Event user Value</td>
      <td><code>input.topic.N.user.value</code></td>
      <td>no</td>
      <td></td>
      <td>Defines the user associated with this event (static).  This setting is only applicable if <code>user.field</code> is NOT specified.</td>
    </tr>
    <tr>
      <td>Event user Field</td>
      <td><code>input.topic.N.user.field</code></td>
      <td>no</td>
      <td></td>
      <td>Defines the field to be used as the user identifer for this event (dynamic).  This setting overwrites <code>user.value</code></td>
    </tr>
  </tbody>
</table>