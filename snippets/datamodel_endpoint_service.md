Datamodel Name: `EndpointService`

| Field Name                  | Data Type | Description                                           | Example                   |
| -----------                 | ---       |--------------------------------------                 | ------------------------- |
| `action` 	                  | string 	  | The action performed on the service. 	                | `create`<br>`delete`<br>`pause`<br>`start`<br>`stop`
| `dest` 	                    | string 	  | The endpoint on which the service is installed. 	    | `10.10.1.1`
| `name` 	                    | string 	  | The name of the service. 	                            | `RpcSs`
| `parent_process_id` 	      | string 	  | The numeric identifier of the parent process assigned by the operating system. | `837`
| `process` 	                | string 	  | All of the arguments passed to the process upon execution. | `C:\path\example.exe /flag1`
| `process_exec` 	            | string 	  | The executable name of the process 	                  | `example.exe`
| `process_guid` 	            | string 	  | The globally unique identifier of the process assigned by the vendor_product. | `{f81d4fae-7dec-11d0-a765-00a0c91e6bf6}`
| `process_hash`              | string 	  | The digests of the contents of the file located at processPath by using md5, sha1, etc. | `2aae6c35c94fcfb415dbe95f408b9ce91ee846ed`
| `process_id` 	              | string 	  | The numeric identifier of the process assigned by the operating system. | `837`
| `process_path` 	            | string 	  | The file path of the executable associated with this process. | `C:\path\to\example.exe`
| `start_mode` 	              | string 	  | The start mode for the service. 	                    | `disabled`<br>`manual`<br>`auto`
| `status` 	                  | string 	  | The status of the service. 	                          | `started`<br>`stopped`<br>`warning`<br>`critical`
| `user` 	                    | string 	  | The user account that spawned the process. 	          | `LOCALUSER`
| `user_id` 	                | string 	  | The unique identifier of the user account which spawned the process. For Windows, this is the security identifier, `sid` 	| `S-1-5-18`
