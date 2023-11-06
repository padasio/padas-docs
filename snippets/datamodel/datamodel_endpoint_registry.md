Datamodel Name: `EndpointRegistry`

| Field Name                  | Data Type | Description                                           | Example                   |
| ----------------------      | ---       |--------------------------------------                 | ------------------------- |
| `action` 	                  | string 	  | The action performed on the resource. 	              | `create`<br>`delete`<br>`modify`<br>`read`
| `dest` 	                    | string 	  | The endpoint on which the port is listening. 	        | `10.10.1.1`
| `process` 	                | string 	  | All of the arguments passed to the process upon execution. 	| `C:\path\example.exe /flag1`
| `process_guid` 	            | string 	  | The globally unique identifier of the process assigned by the vendor_product. | `{f81d4fae-7dec-11d0-a765-00a0c91e6bf6}`
| `process_id` 	              | string 	  | The numeric identifier of the process assigned by the operating system. 	| `456`
| `registry_hive` 	          | string 	  | The logical group of keys, subkeys, and values in the registry. 	| `HKEY_CURRENT_USER`<br>`HKEY_LOCAL_MACHINE`
| `registry_key` 	            | string 	  | The registry key specified in the event. Similar to a folder in a traditional file system. | `HKLM\SYSTEM\CurrentControlSet\services\RpcSs`
| `registry_value_name` 	    | string 	  | The descriptive name for the data being stored in the key. 	| `InstalledVersion`
| `registry_value_data` 	    | string 	  | The contents of the value, typically a text string. 	| `%SystemRoot%\system32\svchost.exe -k rpcss`
| `registry_value_type` 	    | string 	  | The type of data being stored in the value. Types include binary data, 32 bit numbers, strings, etc. | `REG_SZ`<br>`REG_MULTI_SZ`<br>`REG_DWORD`<br>`REG_BINARY`<br>`REG_QWORD`
| `status` 	                  | string 	  | The outcome of the registry action. 	                | `failure`<br>`success`
| `user` 	                    | string 	  | The user account associated with the listening port. 	| `LOCALSYSTEM`

