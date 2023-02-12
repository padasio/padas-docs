Datamodel Name: `EndpointProcess`

| Field Name                  | Data Type | Description                                           | Example                   |
| -----------                 | ---       |--------------------------------------                 | ------------------------- |
| `action` 	                  | string 	  | The action taken by the endpoint 	                    | `access`<br>`create`<br>`terminate`<br>`allowed`<br>`blocked`
| `access_level` 	            | string 	  | Permissions level at which the target process is accessed. |	`0x40`
| `call_trace` 	              | string 	  | The stack trace showing the context of a process open/access call. | `C:\Windows\SYSTEM32\ntdll.dll+a5594`<br>`C:\Windows\system32\KERNELBASE.dll+1e865`
| `dest` 	                    | string 	  | The endpoint for which the process was spawned. 	    | `10.10.1.1`
| `parent_process` 	          | string 	  | All of the arguments passed to the parent process upon execution. | `C:\path\example.exe /flag1`
| `parent_process_exec` 	    | string 	  | The executable name of the parent process 	          | `example.exe`
| `parent_process_guid` 	    | string 	  | The globally unique identifier of the parent process assigned by the vendor_product. | `{f81d4fae-7dec-11d0-a765-00a0c91e6bf6}`
| `parent_process_id` 	      | string 	  | The numeric identifier of the parent process assigned by the operating system. | `837`
| `parent_process_path` 	    | string 	  | The file path of the executable associated with this parent process. | `C:\path\to\example.exe`
| `process` 	                | string 	  | All of the arguments passed to the process upon execution. | `C:\path\example.exe /flag1`
| `process_current_directory` | string 	  | The absolute path to the current working directory of the process. | `c:\windows\system32\`
| `process_exec` 	            | string 	  | The executable name of the process 	                   | `example.exe`
| `process_guid` 	            | string 	  | The globally unique identifier of the process assigned by the vendor_product. | `{f81d4fae-7dec-11d0-a765-00a0c91e6bf6}`
| `process_hash` 	            | string 	  | The digests of the contents of the file located at processPath by using md5, sha1, etc. | `5eb63bbbe01eeed093cb22bb8f5acdc3`
| `process_id` 	              | string 	  | The numeric identifier of the process assigned by the operating system. | `837`
| `process_integrity_level` 	| string 	  | The Windows integrity level associated with the process. MUST be one of: `low`, `medium`, `high`, or `system`. | `medium`
| `process_path` 	            | string 	  | The file path of the executable associated with this process.	| `C:\path\to\example.exe`
| `user` 	                    | string 	  | The user account that spawned the process. 	          | `LOCALUSER`
| `user_id` 	                | string 	  | The unique identifier of the user account which spawned the process. For Windows, this is the security identifier, `sid` | `S-1-5-18`

