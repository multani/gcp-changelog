# Confidential VM

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
