# reCAPTCHA

## 2026-01-30

### Change

The updated reCAPTCHA Mobile SDK improves the risk score. You should review
and adjust your reCAPTCHA action thresholds as needed.

---
## 2026-01-14

### Change

reCAPTCHA Mobile SDK v18.9.0-beta01 is available for iOS. This version includes
improvements to SDK latency and reliability.

---
## 2026-01-06

### Change

reCAPTCHA Mobile SDK v18.9.0-beta01 is available for Android. This version includes improvements to SDK latency and reliability.

---
## 2025-12-01

### Change

reCAPTCHA Mobile SDK v18.8.2 is available for iOS. This version fixes a race
condition affecting multiple simultaneous calls to execute.

---
## 2025-10-28

### Feature

reCAPTCHA policy-based challenge keys are available in [GA](https://cloud.google.com/products#product-launch-stages). With policy-based challenge keys, you can configure reCAPTCHA to deterministically trigger CAPTCHA challenges based on a score threshold and challenge difficulty.
For more information about the policy-based challenge keys, see [reCAPTCHA keys overview](https://docs.cloud.google.com/recaptcha/docs/keys).

---
## 2025-10-22

### Changed

reCAPTCHA Mobile SDK v18.8.1 is available for iOS. This version fixes an issue
with iOS 26 screen time showing use from recaptcha.net

---
## 2025-09-17

### Changed

reCAPTCHA Mobile SDK v18.8.0 is available for Android. This version contains reliability improvements and bug fixes.

---
## 2025-09-15

### Changed

reCAPTCHA Mobile SDK 18.8.0 is available for iOS. This version contains the following changes:

* Reliability improvements and bug fixes
* Swift 6 and Xcode 26.0 support
* The minimum supported version is iOS 15. This is in accordance with the [compatibility guidelines for Xcode 16](https://developer.apple.com/support/xcode/).

---
## 2025-09-04

### Changed

reCAPTCHA Mobile SDK v18.8.0-beta03 is available for Android. This version contains reliability improvements and bug fixes.

### Changed

reCAPTCHA Mobile SDK 18.8.0-beta02 is now available for iOS. This version contains reliability improvements and bug fixes.

---
## 2025-08-28

### Feature

Transaction Defense Reasons [is generally available](https://cloud.google.com/products?#product-launch-stages). This feature enhances transparency by providing clear, human-readable explanations for why a particular transaction receives a high transaction risk score. The reasons help you better understand the risk assessments and take more informed actions to protect against fraud.

For more information, see [Risk reason](https://cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments#riskreason).

### Feature

We've enhanced the reCAPTCHA Admin console to provide a more intuitive interface for configuring risk score thresholds. These improvements help you define how to act on different risk scores. You can also get a better understanding of the transactions that will exceed the threshold which can help in deciding what you allow, block or further reviewing transactions.

For more information, see [Protect payment transactions with Fraud Prevention](https://cloud.google.com/recaptcha/docs/fraud-prevention).

---
## 2025-07-31

### Feature

reCAPTCHA policy-based challenge keys are now available in [Preview](https://cloud.google.com/products#product-launch-stages). With policy-based challenge keys, you can configure reCAPTCHA to deterministically trigger CAPTCHA challenges based on a score threshold and challenge difficulty.
For more information about the policy-based challenge keys, see [reCAPTCHA keys overview](https://cloud.google.com/recaptcha/docs/keys).

### Changed

reCAPTCHA Mobile SDK v18.8.0-beta02 is available for Android.

This version contains the following changes:

* Reliability improvements and bug fixes.
* The minimum supported version of Android is 23.

---
## 2025-07-02

### Changed

reCAPTCHA Mobile SDK 18.8.0-beta01 is now available for iOS.

This version contains the following changes:

* Support for Swift 6 and Xcode 26.0 beta01.
* Minimum supported version is set to iOS 15 in accordance with <https://developer.apple.com/support/xcode/> for Xcode 16.

---
## 2025-06-04

### Changed

reCAPTCHA Mobile SDK v18.8.0-beta01 is now available for Android

This version contains reliability improvements and bug fixes.

---
