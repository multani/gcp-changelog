# Gemini

## 2026-01-08

### Feature

[VPC Service Controls for Gemini Cloud Assist investigations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_cloud_assist)
is now available in [Preview](https://cloud.google.com/products#product-launch-stages).

---
## 2025-12-16

### VS Code model selection issue fixed as of version 2.63.1

The [model selection issue](#known_issue_for_the_model_selection_feature_in_vs_code_gemini_code_assist)
affecting free tier customers using Gemini Code Assist releases 2.56 and later
is fixed as of version 2.63.1.

### VS Code model selection issue fixed as of version 2.63.1

The [model selection issue](#known_issue_for_the_model_selection_feature_in_vs_code_gemini_code_assist)
affecting free tier customers using Gemini Code Assist releases 2.56 and later
is fixed as of version 2.63.1.

---
## 2025-12-12

### Known issue for the model selection feature in VS Code Gemini Code Assist

The VS Code Gemini Code Assist
[model selection feature](https://docs.cloud.google.com/gemini/docs/codeassist/chat-gemini#select-model)
incorrectly appears for users of the free tier of Gemini Code Assist for
individuals.

* The feature shouldn't appear for such users and does not function for them.

### Known issue for the model selection feature in VS Code Gemini Code Assist

The VS Code Gemini Code Assist
[model selection feature](https://docs.cloud.google.com/gemini/docs/codeassist/chat-gemini#select-model)
incorrectly appears for users of the free tier of Gemini Code Assist for
individuals.

* The feature shouldn't appear for such users and does not function for them.

---
## 2025-12-05

### Outline in IntelliJ (Preview)

The [outline feature](https://docs.cloud.google.com/gemini/docs/codeassist/chat-gemini#outline) automatically
creates AI-assisted documentation by generating short, English summaries of code
blocks within the **Outline** tab of the Gemini Code Assist plugin. Outlines
help developers to achieve rapid understanding and to focus on abstraction,
without getting bogged down by syntactical details.

You can [change the settings](https://docs.cloud.google.com/gemini/docs/codeassist/chat-gemini#outline-settings)
to disable automatic outline generation, which instead lets you generate
outlines of files manually.

![Outline in IntelliJ Gemini Code Assist.](https://docs.cloud.google.com/gemini/images/release-notes-images/intellij-outline.png)

### Finish Changes in IntelliJ (Preview)

The [finish changes](https://docs.cloud.google.com/gemini/docs/codeassist//write-code-gemini#finish-changes)
feature acts as an AI pair programmer that observes your in-progress work and
completes the job, eliminating the need to write complex prompts. The core
strength of the finish changes feature lies in its flexibility, allowing you to
use a mix of input styles, such as pseudocode, #TODOs, or half-written code.
This combination minimizes distraction and ensures you remain in control of the
high-level design.

### Outline in IntelliJ (Preview)

The [outline feature](https://docs.cloud.google.com/gemini/docs/codeassist/chat-gemini#outline) automatically
creates AI-assisted documentation by generating short, English summaries of code
blocks within the **Outline** tab of the Gemini Code Assist plugin. Outlines
help developers to achieve rapid understanding and to focus on abstraction,
without getting bogged down by syntactical details.

You can [change the settings](https://docs.cloud.google.com/gemini/docs/codeassist/chat-gemini#outline-settings)
to disable automatic outline generation, which instead lets you generate
outlines of files manually.

![Outline in IntelliJ Gemini Code Assist.](https://docs.cloud.google.com/gemini/images/release-notes-images/intellij-outline.png)

### Finish Changes in IntelliJ (Preview)

The [finish changes](https://docs.cloud.google.com/gemini/docs/codeassist//write-code-gemini#finish-changes)
feature acts as an AI pair programmer that observes your in-progress work and
completes the job, eliminating the need to write complex prompts. The core
strength of the finish changes feature lies in its flexibility, allowing you to
use a mix of input styles, such as pseudocode, #TODOs, or half-written code.
This combination minimizes distraction and ensures you remain in control of the
high-level design.

---
## 2025-12-04

### Model selection for VS Code Gemini Code Assist

The following VS Code Gemini Code Assist users can now
[manually select the model](https://docs.cloud.google.com/gemini/docs/codeassist/chat-gemini#select-model)
used by Gemini Code Assist:

* Gemini Code Assist Enterprise users
* Gemini Code Assist Standard users
* Gemini Code Assist for individuals, if you have a Google AI Pro or Ultra
  subscription

### Model selection for VS Code Gemini Code Assist

The following VS Code Gemini Code Assist users can now
[manually select the model](https://docs.cloud.google.com/gemini/docs/codeassist/chat-gemini#select-model)
used by Gemini Code Assist:

* Gemini Code Assist Enterprise users
* Gemini Code Assist Standard users
* Gemini Code Assist for individuals, if you have a Google AI Pro or Ultra
  subscription

---
## 2025-11-20

### Other



### Bug fixes in IntelliJ

Various bug fixes and minor product enhancements.

---
## 2025-11-13

### Known issue in VS Code 2.57 and later

The Gemini Code Assist 2.57 and later releases for VS Code have a known issue
that prevents the extension from connecting to the server if you are using a
gnc c runtime version that's earlier than 2.36.

* You can permanently fix this issue by upgrading your gnu c runtime version to
  2.36 or higher.
* Alternatively, you can downgrade the Gemini Code Assist VS Code extension
  to version 2.56 until a fix is released.

### VS Code server connection issue fixed as of version 2.58.1

The [server connection issue](#known_issue_in_vs_code_257_and_later) affecting
Gemini Code Assist 2.57 and 2.58 releases is fixed as of version 2.58.1

### Known issue in VS Code 2.57 and later

The Gemini Code Assist 2.57 and later releases for VS Code have a known issue
that prevents the extension from connecting to the server if you are using a
gnc c runtime version that's earlier than 2.36.

* You can permanently fix this issue by upgrading your gnu c runtime version to
  2.36 or higher.
* Alternatively, you can downgrade the Gemini Code Assist VS Code extension
  to version 2.56 until a fix is released.

### VS Code server connection issue fixed as of version 2.58.1

The [server connection issue](#known_issue_in_vs_code_257_and_later) affecting
Gemini Code Assist 2.57 and 2.58 releases is fixed as of version 2.58.1

---
## 2025-11-12

### Chat performance metrics

Gain deeper insights into Gemini for Google Cloud's chat performance with
metrics for chat acceptance rate and lines of chat accepted, including
interactions in Agent mode and non-agentic chat. Combine these metrics with
existing code metrics to calculate total acceptance and total lines of code
accepted, providing a complete picture of Gemini's performance. For more
information, see
[View Gemini for Google Cloud logs](https://docs.cloud.google.com/gemini/docs/log-gemini).

### Code customization available in agent mode and Gemini CLI (Preview)

[Code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization-overview) is now
supported when using [Gemini CLI](https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli) and
[agent mode](https://docs.cloud.google.com/gemini/docs/codeassist/agent-mode) in Gemini Code Assist.

### Chat performance metrics

Gain deeper insights into Gemini for Google Cloud's chat performance with
metrics for chat acceptance rate and lines of chat accepted, including
interactions in Agent mode and non-agentic chat. Combine these metrics with
existing code metrics to calculate total acceptance and total lines of code
accepted, providing a complete picture of Gemini's performance. For more
information, see
[View Gemini for Google Cloud logs](https://docs.cloud.google.com/gemini/docs/log-gemini).

### Code customization available in agent mode and Gemini CLI (Preview)

[Code customization](https://docs.cloud.google.com/gemini/docs/codeassist/code-customization-overview) is now
supported when using [Gemini CLI](https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli) and
[agent mode](https://docs.cloud.google.com/gemini/docs/codeassist/agent-mode) in Gemini Code Assist.

### Inline diff is generally available (GA) for IntelliJ

[Inline diff](https://docs.cloud.google.com/gemini/docs/codeassist/chat-gemini#view_code_diffs) is generally
available for IntelliJ Gemini Code Assist. With the inline diff view, chat
generated code suggestions are visually highlighted directly in your editor.
This feature can boost productivity by offering immediate visibility on
modifications, streamlining reviews and enabling precise control over
integrating new code, all without leaving your current view.

If preferred, you can also
[change the diff view settings](https://docs.cloud.google.com/gemini/docs/codeassist/chat-gemini#change_diff_view_settings)
to have a side-by-side diff window instead of the inline diff.

![Inline diff in IntelliJ Gemini Code Assist.](https://cloud.google.com/gemini/images/release-notes-images/intellij-inline-diff.gif)

### Inline diff is generally available (GA) for IntelliJ

[Inline diff](https://docs.cloud.google.com/gemini/docs/codeassist/chat-gemini#view_code_diffs) is generally
available for IntelliJ Gemini Code Assist. With the inline diff view, chat
generated code suggestions are visually highlighted directly in your editor.
This feature can boost productivity by offering immediate visibility on
modifications, streamlining reviews and enabling precise control over
integrating new code, all without leaving your current view.

If preferred, you can also
[change the diff view settings](https://docs.cloud.google.com/gemini/docs/codeassist/chat-gemini#change_diff_view_settings)
to have a side-by-side diff window instead of the inline diff.

![Inline diff in IntelliJ Gemini Code Assist.](https://cloud.google.com/gemini/images/release-notes-images/intellij-inline-diff.gif)

---
## 2025-11-10

### Persistent memory for Gemini Code Assist on GitHub (Preview)

* [Gemini Code Assist on GitHub](https://developers.google.com/gemini-code-assist/docs/review-github-code#versions)
  now supports persistent memory, which stores your previous interactions with
  Gemini Code Assist on GitHub so that it has context during your future
  interactions.
* For users of the enterprise version, persistent memory is enabled from the
  connection settings within the Google Cloud console. For users of the consumer
  version, persistent memory is enabled from the Gemini Code Assist site. For
  more information, see
  [manage configuration files across multiple repositories](https://developers.google.com/gemini-code-assist/docs/customize-gemini-behavior-github#bulk-config).

### Persistent memory for Gemini Code Assist on GitHub (Preview)

* [Gemini Code Assist on GitHub](https://developers.google.com/gemini-code-assist/docs/review-github-code#versions)
  now supports persistent memory, which stores your previous interactions with
  Gemini Code Assist on GitHub so that it has context during your future
  interactions.
* For users of the enterprise version, persistent memory is enabled from the
  connection settings within the Google Cloud console. For users of the consumer
  version, persistent memory is enabled from the Gemini Code Assist site. For
  more information, see
  [manage configuration files across multiple repositories](https://developers.google.com/gemini-code-assist/docs/customize-gemini-behavior-github#bulk-config).

---
## 2025-11-07

### Other



### Bug fixes in VS Code

Various bug fixes and minor product enhancements.

---
