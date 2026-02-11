# Confidential VM

## 2026-02-10

### Security

A vulnerability affecting Intel TDX firmware was discovered and is
being addressed. For more information, see the
[GCP-2026-008 security bulletin](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/security-bulletins#gcp-2026-008).

---
## 2025-10-27

### Breaking

Following a firmware update, Confidential VM instances with AMD SEV-SNP generate v4
attestation reports. Attestation report parsers that are designed for v3
attestation reports might break.

Customers using [`go-sev-guest`](https://github.com/google/go-sev-guest) to
parse attestation reports can resolve attestation failures by updating to
`go-sev-guest` v0.14.0 or above.

If you're writing your own parser, the attestation report format is defined by
the
[SEV Secure Nested Paging Firmware ABI Specification](https://www.amd.com/en/developer/sev.html).

---
## 2025-10-20

### Security

A vulnerability affecting AMD Zen 5 processors (Turin) was discovered and is
being addressed. For more information, see the
[GCP-2025-058 security bulletin](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/security-bulletins#gcp-2025-058).

---
## 2025-07-31

### Feature

Support for [accelerator-optimized a3-highgpu-1g](https://cloud.google.com/compute/docs/accelerator-optimized-machines#a3-standard-vms) machine type for securely running AI and ML workloads is now generally available, with the following specifications:

* 4th Generation Intel Xeon Scalable processor (Sapphire Rapids)
* Intel TDX
* 1 NVIDIA H100 GPU

---
## 2025-07-14

### Issue

As of June 20, 2025, Confidential VM instances using AMD SEV-SNP or Intel TDX do not support remote attestation when running the following guest OS images:

* SLES 15 SP7
* Ubuntu 25.04

To restore remote attestation, use an earlier guest OS version such as SLES 15 SP6 or Ubuntu 24.04.

---
## 2025-06-13

### Feature

Support for general purpose [C4D machine types](https://cloud.google.com/compute/docs/general-purpose-machines?utm_source=cloud_console&utm_medium=release_notes&utm_campaign=dec029572dce3d0d9991dd094856fdd9&_gl=1*1odqac9*_ga*OTY1OTE3MjM4LjE3NTA3ODgyNTg.*_ga_WH2QY8WWF5*czE3NTA4Mzg4MTkkbzE3JGcwJHQxNzUwODM4ODIwJGo1OSRsMCRoMA..#c4d_series) is now generally available, featuring:

* 5th generation AMD EPYC processors (Turin) and Google Titanium
* AMD [Secure Encrypted Virtualization (SEV)](https://www.amd.com/en/developer/sev.html) which can encrypt the memory of the VM to protect data in-use

---
