Datamodel Name: `EndpointFile`

| Field Name                  | Data Type | Description                                           | Example                   |
| ----------------------      | ---       |--------------------------------------                 | ------------------------- |
| `action` 	                  | string 	  | The action performed on the resource.                 | `create`<br>`delete`<br>`modify`<br>`read`<br>`write`
| `dest` 	                    | string 	  | The endpoint on which the filesystem activity takes place. | `10.10.1.1`
| `file_creation_time` 	      | string 	  | The creation time of the file 	                      | `05/14/2015 12:47:06`
| `file_hash` 	              | string 	  | The digests of the contents of the file located at filePath by using md5, sha1, etc. | `2aae6c35c94fcfb415dbe95f408b9ce91ee846ed`
| `file_group` 	              | string 	  | The group owner of the file 	                        | `admin`
| `file_group_id` 	          | string 	  | The group ID of the file 	                            | `801`
| `file_mode` 	              | string 	  | The mode or permissions set of the file. 	            | `0644` (linux) or NTFS ACL
| `file_name` 	              | string 	  | The name of the file. 	                              | `MyWordDoc.docx`
| `file_owner` 	              | string 	  | The username of the owner of the file. 	              | `adam`
| `file_owner_id` 	          | string 	  | The user ID or SID of the owner of the file. 	        | `501`
| `file_path` 	              | string 	  | The full path to the file on the file system. 	      | `C:\users\fakeuser\documents\MyFile.docx`
| `parent_process_id` 	      | string 	  | The numeric identifier of the parent process assigned by the operating system. 	| `837`
| `process` 	                | string 	  | All of the arguments passed to the process upon execution. 	| `C:\path\example.exe /flag1`
| `process_exec` 	            | string 	  | The executable name of the process 	| `example.exe`
| `process_guid` 	            | string 	  | The globally unique identifier of the process assigned by the vendor_product. | `{f81d4fae-7dec-11d0-a765-00a0c91e6bf6}`
| `process_id` 	              | string 	  | The numeric identifier of the process assigned by the operating system. 	| `837`
| `process_path` 	            | string 	  | The file path of the executable associated with this process. 	| `C:\path\to\example.exe`
| `user` 	                    | string 	  | The user account that spawned the process. 	          | `LOCALUSER`
| `userId` 	                  | string 	  | The unique identifier of the user account which spawned the process. For Windows, this is the security identifier, `sid` 	| `S-1-5-18`
