# Backup and DR

## 2025-07-31

### Announcement

Announcing the **Public Preview launch of Cloud SQL enhanced backups** with Backup and DR. This enables advanced data protection capabilities offered by Backup and DR including backup vault support, granular scheduling through backup plans, and centralized management.

---
## 2025-07-11

### Announcement

We're excited to announce the launch of Editable Backup Plans, a new feature designed to give you more flexibility and control over your data protection strategy. You can now modify your existing backup plans directly, eliminating the need to create new plans and reassign them when your requirements change. This makes it easier than ever to adapt to evolving business needs, optimize for cost, and correct configuration errors on the fly.

What's new:

* Directly Edit Key Settings: You can now change the description, schedule, backup window, and retention periods of your existing backup plans. You can also add or remove backup rules as needed.
* Automatic Updates: Once a plan is edited, the changes are automatically applied to all resources protected by that plan for all future backups. There's no need to manually detach and reattach the plan.
* Backward Compatibility: This new capability is available for all backup plans, including those created before this update.

Important Note: While most settings in a backup plan are now editable, the assigned backup vault cannot be changed. To store backups in a different vault, a new backup plan must be created.

---
