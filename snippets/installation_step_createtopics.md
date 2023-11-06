
--8<-- "props_topics.md"

<figure markdown>
<p>
    <img src="../assets/img/padas_ui_topics_pre.png" class="w-50 img-fluid py-5">
</p>
</figure>

**IMPORTANT NOTE**: If you created the required topics from Padas UI, you will need to **restart** the Padas Engine so that it can read from and write to these topics.  Stop the running Padas Engine via `CTRL-C` or `/opt/padas/bin/padas stop`, and start it again.  You'll need to logout/login from the UI as well.
    ```bash
    bin/padas start-console
    ```