---
title: Converting Sigma Rules
layout: documentation
---

### What is Sigma

[Sigma](https://github.com/SigmaHQ/sigma) rules are a simple, yet powerful way for security teams to detect and respond to threats using SIEM systems. They are written in a YAML-based format and allow teams to identify suspicious patterns and behaviors across multiple systems and data sources, providing a unified view of security events.

Sigma rules offer several advantages over traditional detection rules, including platform-agnosticism, easy customization, and easy modification. They can be used with various SIEM systems, allowing teams to standardize their detection capabilities across their security stack and improve their overall security posture. 

While Sigma rules are platform-agnostic and can be used with various SIEM systems, it is also possible to convert them to other formats, such as Padas rules by utilizing [PDL](pdl-quick-reference.md). Padas [Sigma converter script](https://github.com/padasinc/padas-tools/tree/main/sigma_v2_to_padas) is a new open-source tool that allows users to convert Sigma rules into Padas PDL. The ability to convert Sigma rules to Padas rules offers significant benefits for security teams looking to enhance their detection and response capabilities.

### Sigma to Padas

Please see [Quick Start](/quickstart.md) **before** going through the steps below. In this section, only converting Sigma rules to Padas will be explained. After conversion, rest of steps will be the same as Padas Quick Start.

This conversion tool is designed to be used with [Sigma Specification version 2](https://github.com/SigmaHQ/sigma-specification/tree/version_2).

### Prerequisites
- Python (version 3 or above)

### Overview of Quickstart

#### Step 1: Download
1. [Download](https://github.com/padasinc/padas-tools/tree/main/sigma_v2_to_padas) the latest version of the script in padas-tools repository.

2. If it is downloaded as compressed, it is needed to uncompress properly such as `unzip` command or using verious zip tools. Else, skip this step.

3. You should see `sigma_v2_to_padas` directory. 

At this stage, make sure you have downloaded proper Python version.


#### Step 2: Start Padas
* You need to complete [Quick Start](/quickstart.md); step 6 is optional.

#### Step 3: Converting Sigma to Padas Rules

Following files should be available with your download under `sigma_v2_to_padas` directory:

- `sigma_v2_to_padas.py`
- `test/expected_output.json`
- `test/input_sigma_rule.yml`
- `test/test_to_rules.py`

<br/>
1. Convert: `sigma_v2_to_padas.py` is the converter script. This gives proper Sigma v2 (yml) to Padas (json) conversion.
<br>
**Usage : ** `python3 path/sigma_v2_to_padas.py input_path/input.yml output_path/ouput.json`

<br>
2. Test: You can try `test/test_to_rules.py` script for testing. This script checks if `test/input_sigma_rule.yml` file is converted as `test/expected_output.json`. You can add your own Sigma v2 rules in `test/input_sigma_rule.yml` and their properly converted outputs in `test/expected_output.json`.
<br>
    **Usage : ** `python3 path/test/test_to_rules.py`

#### Step 4: Create Rules

1. **Create Rule** : You can add your converted rules either manually by copying the generated PDL or uploading the JSON file from [Rules](https://localhost:3000/rules) menu.

    <br>
    __*Adding manually*__ : 
    <br> 
    Click <span class="btn btn-padas">New Rule</span> button and fill in the details from generated JSON file.


    <figure markdown>
      <p>
      <img src="../assets/img/padas_ui_rule_create_1.png" class="w-50 img-fluid py-5">
      </p>
    </figure>

    __*Uploading JSON*__ : 
    <br>

    1. Click top of the <span class="btn btn-padas">Upload</span> button.
    2. Click <span class="btn btn-padas">Choose File</span> button. If you add same rule previously, you need to check `Overwrite existing configuration.` box.
    3. Click bottom of the <span class="btn btn-padas">Upload</span> button.

    <figure markdown>
      <p>
      <img src="../assets/img/padas_add_rule_upload.png" class="w-50 img-fluid py-5">
      </p>
    </figure>

#### Step 5: Test & Play

** Test : ** You can generate some matching data and test your rules as described in Quick Start [Step 6](/quickstart/#step-6-test-play).
