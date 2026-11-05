# Apigee Operator for kubernetes

## 2026-11-04

### Announcement

On November 4, 2026, we released an updated version of Apigee.

### Feature

**The Apigee Operator for Kubernetes version 1.1.2 is now available.**

### Security

| Bug ID | Description |
| --- | --- |
| **521387476, 521388685, 521389473, 521389648, 521390401, 521390431, 521418315, 521467563, 521470029, 521523106, 521532318, 522502328, 522502515, 522502723, 522508097, 522515015, 522515987, 523406508, 524990439, 525000385, 525013469, 545525835, 545535262, 545546643, 545547894, 545594793, 545595426, 545604082, 545605504, 545613200, 545619209, 546865118, 549708263, 572097689, 572100132** | **Security fixes for Netty in the Apigee Operator for Kubernetes.** Upgraded Netty to 4.1.137.Final. This addresses the following vulnerabilities:   * [CVE-2026-33870](https://nvd.nist.gov/vuln/detail/CVE-2026-33870) * [CVE-2026-33871](https://nvd.nist.gov/vuln/detail/CVE-2026-33871) * [CVE-2026-41417](https://nvd.nist.gov/vuln/detail/CVE-2026-41417) * [CVE-2026-42578](https://nvd.nist.gov/vuln/detail/CVE-2026-42578) * [CVE-2026-42579](https://nvd.nist.gov/vuln/detail/CVE-2026-42579) * [CVE-2026-42580](https://nvd.nist.gov/vuln/detail/CVE-2026-42580) * [CVE-2026-42581](https://nvd.nist.gov/vuln/detail/CVE-2026-42581) * [CVE-2026-42583](https://nvd.nist.gov/vuln/detail/CVE-2026-42583) * [CVE-2026-42584](https://nvd.nist.gov/vuln/detail/CVE-2026-42584) * [CVE-2026-42585](https://nvd.nist.gov/vuln/detail/CVE-2026-42585) * [CVE-2026-42587](https://nvd.nist.gov/vuln/detail/CVE-2026-42587) * [CVE-2026-44249](https://nvd.nist.gov/vuln/detail/CVE-2026-44249) * [CVE-2026-45416](https://nvd.nist.gov/vuln/detail/CVE-2026-45416) * [CVE-2026-45673](https://nvd.nist.gov/vuln/detail/CVE-2026-45673) * [CVE-2026-45674](https://nvd.nist.gov/vuln/detail/CVE-2026-45674) * [CVE-2026-47244](https://nvd.nist.gov/vuln/detail/CVE-2026-47244) * [CVE-2026-47691](https://nvd.nist.gov/vuln/detail/CVE-2026-47691) * [CVE-2026-48043](https://nvd.nist.gov/vuln/detail/CVE-2026-48043) * [CVE-2026-50010](https://nvd.nist.gov/vuln/detail/CVE-2026-50010) * [CVE-2026-50020](https://nvd.nist.gov/vuln/detail/CVE-2026-50020) * [CVE-2026-50560](https://nvd.nist.gov/vuln/detail/CVE-2026-50560) * [CVE-2026-55831](https://nvd.nist.gov/vuln/detail/CVE-2026-55831) * [CVE-2026-55833](https://nvd.nist.gov/vuln/detail/CVE-2026-55833) * [CVE-2026-56745](https://nvd.nist.gov/vuln/detail/CVE-2026-56745) * [CVE-2026-56746](https://nvd.nist.gov/vuln/detail/CVE-2026-56746) * [CVE-2026-56819](https://nvd.nist.gov/vuln/detail/CVE-2026-56819) * [CVE-2026-59898](https://nvd.nist.gov/vuln/detail/CVE-2026-59898) * [CVE-2026-59899](https://nvd.nist.gov/vuln/detail/CVE-2026-59899) * [CVE-2026-59900](https://nvd.nist.gov/vuln/detail/CVE-2026-59900) * [CVE-2026-59901](https://nvd.nist.gov/vuln/detail/CVE-2026-59901) * [CVE-2026-59903](https://nvd.nist.gov/vuln/detail/CVE-2026-59903) * [CVE-2026-59921](https://nvd.nist.gov/vuln/detail/CVE-2026-59921) * [CVE-2026-73508](https://nvd.nist.gov/vuln/detail/CVE-2026-73508) * [CVE-2026-75595](https://nvd.nist.gov/vuln/detail/CVE-2026-75595) * [CVE-2026-75596](https://nvd.nist.gov/vuln/detail/CVE-2026-75596) |
| **527492626, 527495614, 527497578, 527498733, 545553137, 572096453, 572096754, 572096884, 572097054, 572097090, 572097183, 572098198, 572098299, 572099894, 572100881, 578504005** | **Security fixes for Jackson in the Apigee Operator for Kubernetes.** Upgraded Jackson to 2.21.7. This addresses the following vulnerabilities:   * [CVE-2026-18401](https://nvd.nist.gov/vuln/detail/CVE-2026-18401) * [CVE-2026-19032](https://nvd.nist.gov/vuln/detail/CVE-2026-19032) * [CVE-2026-54512](https://nvd.nist.gov/vuln/detail/CVE-2026-54512) * [CVE-2026-54513](https://nvd.nist.gov/vuln/detail/CVE-2026-54513) * [CVE-2026-54514](https://nvd.nist.gov/vuln/detail/CVE-2026-54514) * [CVE-2026-54515](https://nvd.nist.gov/vuln/detail/CVE-2026-54515) * [CVE-2026-59888](https://nvd.nist.gov/vuln/detail/CVE-2026-59888) * [CVE-2026-59889](https://nvd.nist.gov/vuln/detail/CVE-2026-59889) * [CVE-2026-68494](https://nvd.nist.gov/vuln/detail/CVE-2026-68494) * [CVE-2026-68497](https://nvd.nist.gov/vuln/detail/CVE-2026-68497) * [CVE-2026-77310](https://nvd.nist.gov/vuln/detail/CVE-2026-77310) * [CVE-2026-83557](https://nvd.nist.gov/vuln/detail/CVE-2026-83557) * [CVE-2026-89407](https://nvd.nist.gov/vuln/detail/CVE-2026-89407) * [CVE-2026-89425](https://nvd.nist.gov/vuln/detail/CVE-2026-89425) * [CVE-2026-91776](https://nvd.nist.gov/vuln/detail/CVE-2026-91776) * [CVE-2026-91777](https://nvd.nist.gov/vuln/detail/CVE-2026-91777) |
| **521477919, 545546100, 545555197, 545603496, 545608493** | **Security fixes for Jetty in the Apigee Operator for Kubernetes.** Upgraded Jetty to 12.0.36. This addresses the following vulnerabilities:   * [CVE-2025-11143](https://nvd.nist.gov/vuln/detail/CVE-2025-11143) * [CVE-2026-1605](https://nvd.nist.gov/vuln/detail/CVE-2026-1605) * [CVE-2026-2332](https://nvd.nist.gov/vuln/detail/CVE-2026-2332) * [CVE-2026-6790](https://nvd.nist.gov/vuln/detail/CVE-2026-6790) * [CVE-2026-8384](https://nvd.nist.gov/vuln/detail/CVE-2026-8384) * [CVE-2026-10050](https://nvd.nist.gov/vuln/detail/CVE-2026-10050) * [CVE-2026-10051](https://nvd.nist.gov/vuln/detail/CVE-2026-10051) |
| **522503039** | **Security fixes for Vert.x in the Apigee Operator for Kubernetes.** Upgraded Vert.x to 4.5.35. This addresses the following vulnerabilities:   * [CVE-2026-1002](https://nvd.nist.gov/vuln/detail/CVE-2026-1002) * [CVE-2026-6860](https://nvd.nist.gov/vuln/detail/CVE-2026-6860) |
| **579151884** | **Security fixes for Guava in the Apigee Operator for Kubernetes.** Upgraded Guava to 33.7.2-jre. This addresses the following vulnerabilities:   * [CVE-2026-102554](https://nvd.nist.gov/vuln/detail/CVE-2026-102554) |

---
## 2026-01-07

### Announcement

On January 7, 2026, we released an updated version of Apigee.

### Security

| Bug ID | Description |
| --- | --- |
| **471150886, 471150271, 471150102, 426783172** | **Security fixes for the Apigee Operator for Kubernetes.** This addresses the following vulnerabilities:   * [CVE-2025-55163](https://nvd.nist.gov/vuln/detail/CVE-2025-55163) * [CVE-2025-67735](https://nvd.nist.gov/vuln/detail/CVE-2025-67735) * [CVE-2025-58057](https://nvd.nist.gov/vuln/detail/CVE-2025-58057) * [CVE-2025-58056](https://nvd.nist.gov/vuln/detail/CVE-2024-58056) |

### Feature

**The Apigee Operator for Kubernetes version 1.1.1 is now available.**

---
