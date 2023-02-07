---
name: New repo suggestion form
about: 'To suggest a GitHub repo for inclusion in the Serverless Repo Collection,
  please complete the following form in full:'
title: "[New repo]: "
labels: ''
assignees: jbesw

body:
  - type: markdown
  attributes:
    value: |
      To suggest a GitHub repo for inclusion in the Serverless Repo Collection, please complete the following form in full:
  - type: textarea 
    id: description
    attributes:
      label: Description
      description: Describe what this repo does (max 100 chars)
    validations:
      required: true

---

