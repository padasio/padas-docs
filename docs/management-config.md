---
title: Management Configuration
---

### Users
As an administrator user, you can view and edit all configuration items including user account settings. Currently there are 2 roles available for a user: `admin` and `user`, where `user` has read-only access to configurations.  "Users" view can be accessed via "Settings --> Users" menu.

<figure markdown>
  <p>
  <img src="../assets/img/padas_ui_users.png" class="img-fluid py-5 w-75">
  </p>
</figure>

---

### Nodes
Node Information table provides details on registered Padas engine instances.

<figure markdown>
  <p>
  <img src="../assets/img/padas_ui_nodes.png" class="img-fluid py-5 w-75">
  </p>
</figure>

--8<-- "props/props_node.md"


---

### Topics

The Topic view provides an overview of all created topics, and it also allows you to create new topics directly from this page. 

**NOTE:** If padas.config.store=kafka is set in padas.properties file, required Kafka topics must be created for keeping centralized configuration entries. Details can be found in [Topic Properties](admin-guide.md#topic-properties) section in Admin Guide.

<figure markdown>
  <p>
  <img src="../assets/img/padas_ui_topics_post.png" class="img-fluid py-5 w-75">
  </p>
</figure>

---

