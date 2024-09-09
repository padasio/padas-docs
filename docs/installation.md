---
title: Install Using TAR Archive
---

**IMPORTANT NOTE**: It is recommended to create a separate user to run Padas, other than `root`.  In our examples, we use `padas` as both the user and group name.  Following is an example on how to create such user:
```bash
sudo useradd -d /opt/padas -U padas
```

Padas installation folder structure:
--8<-- "padas/padas_folders.md"

---

#### Step 1: Acquiring Padas
--8<-- "installation/installation_step_acquire.md"

**NOTE:** You can install these components in a distributed environment.  For possible configuration options, please refer to [Configuration File Reference](config-reference.md).

---

#### Step 2: Start Engine
--8<-- "installation/installation_step_engine.md"

---

#### Step 3: Start UI
--8<-- "installation/installation_step_ui.md"

---

### Step 4: Register as a Service
--8<-- "installation/installation_step_registerservice.md"

---

### Command Line Interface
Comman Lince Interface (CLI) is a wrapper script is provided to manage PADAS service: `$PADAS_HOME/bin/padas`
--8<-- "padas/padas_cli.md"

---

### Uninstall
--8<-- "installation/installation_step_uninstall.md"

