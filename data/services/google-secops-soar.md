# Google SecOps SOAR

## 2025-07-06

### Announcement

Release 6.3.52 is being rolled out to the first phase of regions as listed [here](https://cloud.google.com/chronicle/docs/soar/overview-and-introduction/soar-gradual-release).

This release contains the following feature:

### Feature

**Share Case Queue Filters**

You can now share case queue filters with other users. These filters can be saved with specific criteria, such as assignee roles, and shared with individual users, SOC roles, or all users in your organization for quick access..

For more information, see [Apply and save filters](https://cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/apply-and-save-filters).

---
## 2025-07-05

### Announcement

[Release 6.3.51](https://cloud.google.com/chronicle/docs/soar/release-notes#June_29_2025) is now available for all regions.

---
## 2025-06-29

### Announcement

Release 6.3.51 is being rolled out to the first phase of regions as listed [here](https://cloud.google.com/chronicle/docs/soar/overview-and-introduction/soar-gradual-release).

This release contains the following change.

### Changed

**Bulk Playbook Duplication Behavior Updated**

When duplicating playbooks in bulk, the original selection is now preserved. Newly created copies are no longer automatically selected in the platform.

---
## 2025-06-28

### Announcement

[Release 6.3.50](https://cloud.google.com/chronicle/docs/soar/release-notes#June_22_2025) is now available for all regions.

---
## 2025-06-22

### Announcement

Release 6.3.50 is being rolled out to the first phase of regions as listed [here](https://cloud.google.com/chronicle/docs/soar/overview-and-introduction/soar-gradual-release).

This release contains internal and customer bug fixes.

---
## 2025-06-21

### Announcement

[Release 6.3.49](https://cloud.google.com/chronicle/docs/soar/release-notes#June_14_2025) is now available for all regions.

---
## 2025-06-14

### Announcement

Release 6.3.49 is being rolled out to the first phase of regions as listed [here](https://cloud.google.com/chronicle/docs/soar/release-notes#March_03_2025).

This release contains internal and customer bug fixes.

---
## 2025-06-13

### Announcement

[Release 6.3.48](https://cloud.google.com/chronicle/docs/soar/release-notes#June_07_2025) is now available for all regions.

---
## 2025-06-08

### Announcement

[Release 6.3.47](https://cloud.google.com/chronicle/docs/soar/release-notes#May_24_2025) is now available for all regions.

---
## 2025-06-07

### Announcement

Release 6.3.48 is being rolled out to the first phase of regions.

### Feature

**Playbook Permissions: Support for API Key Roles**

The platform has been updated to extend playbook permissions to also support the SOC Roles associated with API keys, in addition to the user SOC Roles.

This enhancement affects how integrations using API keys interact with playbooks that have specific permission configurations. For example, GitSync now uses this capability to synchronize playbooks with restricted permissions.

For more information on how playbook permissions work with users and API keys, see [Playbook permissions](http://cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/playbook-permissions).

For specific instructions on configuring GitSync with restricted playbooks, see [GitSync - Work with playbook permissions](https://cloud.google.com/chronicle/docs/soar/marketplace/power-ups/gitsync#work-with-playbook-permissions).

### Feature

**Advanced Reports: Case Custom Fields**

Advanced Reports (Looker) has been enhanced to include support for custom fields created for Cases.

This enhancement allows users to leverage organization-specific data captured in custom fields to gain deeper insights and create tailored visualizations within Looker reports. Specific LookML formulas and filtering guidance are now available.

For more information on how to use custom fields in Advanced Reports, see [Use Custom Fields in Advanced Reports](https://cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/adding-custom-fields#use-custom-fields-in-advanced-reports).

---
