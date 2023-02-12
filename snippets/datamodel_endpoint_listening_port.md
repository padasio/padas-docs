Datamodel Name: `EndpointListeningPort`

| Field Name     | Data Type | Description                                           | Example                   |
| -----------    | ---       |--------------------------------------                 | ------------------------- |
| `dest`         | string    | The endpoint on which the port is listening.          |`10.10.1.1`                |
| `dest_port` 	 | string 	 | Network port listening on the endpoint 	             | `80`
| `process_guid` | string 	 | The globally unique identifier of the process assigned by the vendor_product. | `{f81d4fae-7dec-11d0-a765-00a0c91e6bf6}` |
| `process_id` 	 | string    | The numeric identifier of the process assigned by the operating system. | `456` |
| `src` 	       | string	   | The "remote" system connected to the listening port (if applicable). | `192.168.1.10` |
| `src_port` 	 | string 	 | The "remote" port connected to the listening port (if applicable). 	| `4567` |
| `state` 	     | string 	 | The status of the listening port 	listening          | `established` |
| `transport` 	 | string    | The network transport protocol associated with the listening port | 	`tcp`<br>`udp` |
| `user` 	       | string	   | The user account associated with the listening port.  | `LOCALSYSTEM` |


