# Certificate Authority Service

## 2025-06-27

### Feature

You can backdate the `not_before_time` of certificates by specifying the `backdate_duration` field within the issuance policy of your CA Pool. This new optional field in the issuance policy allows you to control the `not_before_time` of all certificates issued from a given CA Pool.

If `backdate_duration` is not set: Certificates are issued with a `not_before_time` equal to the current issuance time.

If `backdate_duration` is set: Certificates are issued with a `not_before_time` equal to the issuance time minus the specified `backdate_duration`. The `not_after_time` automatically adjusts to maintain the requested certificate lifetime.

---
