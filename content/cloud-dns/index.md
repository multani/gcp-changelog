# Cloud DNS

## 2026-10-27

### Announcement

Starting January 5, 2027, CNAME chasing behavior will change so that Cloud DNS
follows CNAME chains between public and private zones. If your private zones or
response policies have overlapping domain names with public CNAME targets,
queries might resolve to unintended internal IP addresses or return resolution
errors.

The following table outlines the current and updated behaviors.

| Source of CNAME answer | Current behavior (until January 5, 2027) | New behavior (starting January 5, 2027) |
| --- | --- | --- |
| Cloud DNS public zone | Subsequent queries search only public DNS zones and internal DNS. Private zones, forwarding zones, and response policies are ignored. | Subsequent queries follow the complete VPC name resolution order: response policies, private zones, forwarding or peering zones, internal DNS, and public zones. |
| Cloud DNS private zone | Subsequent queries search only authorized private zones. Public DNS zones are ignored. | Subsequent queries follow the complete VPC name resolution order. If the target isn't found in authorized private zones, Cloud DNS queries public DNS zones. |
| Cloud DNS response policy zone | Cloud DNS systems don't perform queries for CNAME answers received from response policy local data rules. | Subsequent queries follow the complete VPC name resolution order. If the target isn't found in response policies or private zones, Cloud DNS queries public DNS zones. |

Review your CNAME chasing needs before January 5, 2027. Test your DNS query paths
using `dig` or `nslookup` to identify CNAME chasing scenarios.

* **Look for private-to-public CNAME chasing scenarios**: Look for CNAME answers
  from response policies or private zones that don't match any response policy
  or record in a private zone. Previously, these queries resulted in a `NXDOMAIN`
  answer but after January 5, 2027, these scenarios might match a record in a
  public zone or continue to be `NXDOMAIN` responses.
* **Look for public-to-private CNAME chasing scenarios**: Look for CNAME answers
  from public zones that don't match any record in a public zone. Previously,
  these CNAME chasing scenarios would have resulted in a `NXDOMAIN` response.
  After January 5, 2027, these scenarios might match a response policy or record
  in a private zone or continue to be `NXDOMAIN` responses if the private zone
  doesn't have the record.
* **For CNAME chasing scenarios under your control**: As best practice, configure
  matching time-to-live (TTL) values for all records in the CNAME chain.

### Announcement

Starting January 5, 2027, Cloud DNS will disable full responses to DNS queries of
type `ANY` (`QTYPE=ANY`) in [public authoritative zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview).
Instead, a single resource record will return for `ANY` queries, chosen from the
existing resource record sets that match the query.

Standard traffic from web browsers, applications, and API traffic query specific
record types directly and are therefore unaffected with no action required.

However, certain legacy scripts, automated health checkers, debugging commands
(for example, `dig example.com ANY`), or custom third-party monitoring systems
that explicitly query `ANY` records will receive the first available record
instead of a full zone inventory. You must complete the following configuration
updates before January 5, 2027:

* **Identify legacy queries**: Review internal tools, deployment scripts, or
  third-party DNS monitoring configurations for commands or API calls that
  request the `ANY` record type. Cloud DNS logs in Cloud Logging can be helpful
  with this.
* **Transition to specific queries**: Update the tools to query the specific,
  individual record types they require (for example, querying for `A`,
  `AAAA`, `MX`, or `TXT` records separately).
* **Retrieve full zone records**: If you use `ANY` queries to retrieve all records
  in a zone, use the Cloud DNS REST API (`resourceRecordSets.list`), the gcloud
  CLI (`gcloud dns record-sets list`), or the Google Cloud Console instead.

Risks associated with not making these changes include the following:

* **False monitoring alarms**: Automated uptime or DNS monitoring tools checking
  `ANY` responses may misinterpret the new response as a system failure and
  trigger false alerts.
* **Broken automation pipelines**: Internal deployment or CI/CD scripts that
  rely on parsing a full zone dump with an `ANY` query will fail to retrieve the
  expected data payload and may crash.
* **Disrupted IT diagnostics**: Network administrators running manual legacy
  troubleshooting commands will no longer see a quick summary of all domain
  records, which could delay active network incident diagnostics.

---
## 2026-10-12

### Feature

Outbound Endpoints for Cloud DNS is available in [Preview](https://cloud.google.com/products#product-launch-stages).

Attach Outbound Endpoints to forwarding zones or server policies to
enable direct DNS query forwarding from VPC networks to external
and on-premises DNS resolvers using private IP addresses. For more information,
see [Outbound Endpoints overview](https://docs.cloud.google.com/dns/docs/outbound-endpoints-overview).

---
## 2026-03-15

### Feature

The `filter` query parameter for [`resourceRecordSets.list`](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets/list#query-parameters) is generally available ([GA](https://cloud.google.com/products?e=48754805#product-launch-stages)).

You can filter records to match a specified domain using the API.

---
## 2026-01-16

### Feature

Monitoring your internet-bound DNS queries for malicious activity using DNS Armor is generally available ([GA](https://cloud.google.com/products?e=48754805#product-launch-stages)).

For more information, see [Advanced threat detection with DNS Armor](https://docs.cloud.google.com/dns/docs/threat-detection).

---
## 2025-09-30

### Feature

[Alias records](https://cloud.google.com/dns/docs/records-overview#alias-records) are available in [GA](https://cloud.google.com/products#product-launch-stages).

This custom record type provides CNAME-like functionality at the zone apex, mapping the apex domain name to a canonical target.

---
## 2025-08-29

### Feature

Monitoring your internet-bound DNS queries for malicious activity using advanced threat detection from DNS Armor is now available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Advanced threat detection overview](https://cloud.google.com/dns/docs/threat-detection).

---
## 2025-08-26

### Feature

DNS64 is available in [GA](https://cloud.google.com/products#product-launch-stages).

DNS64 provides synthesized IPv6 addresses for IPv4 destinations. For more information, see the following:

* [DNS64 overview](https://cloud.google.com/dns/docs/overview#dns64-overview)
* [Configure DNS64 server policies](https://cloud.google.com/dns/docs/configure-dns64)

---
## 2025-06-30

### Feature

Using a fully qualified domain name (FQDN) [forwarding target](https://cloud.google.com/dns/docs/zones/forwarding-zones) is available for outbound DNS forwarding in [GA](https://cloud.google.com/products#product-launch-stages).

---
