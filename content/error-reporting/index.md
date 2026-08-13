# Error Reporting

## 2026-08-13

### Announcement

Error Reporting can report stack traces collected from Rust applications
using [`std::backtrace`](https://doc.rust-lang.org/std/backtrace/index.html).
To enable, set the `RUST_BACKTRACE=1` environment variable and
make sure debug symbols are enabled.

For more information, see
[ReportedErrorEvent](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/report.html?rep_location=global#reportederrorevent).

---
## 2026-05-28

### Announcement

You can view the available regional endpoints for the
Error Reporting API on the REST reference pages. For an example, see
[Method: projects.events.list](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/list?rep_location=global).

---
## 2026-03-26

### Feature

You can use the
[Error Reporting API MCP server](https://docs.cloud.google.com/error-reporting/reference_mcp/mcp)
to let agents and AI applications interact with your error data.
This feature is in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

---
