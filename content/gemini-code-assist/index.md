# Gemini Code Assist

## 2025-09-26

### Feature



### Next Edit Predictions in VS Code (Preview)

[Next Edit Predictions](https://cloud.google.com/gemini/docs/codeassist/write-code-gemini#use_next_edit_predictions),
which predicts the next code suggestions throughout the code file that you're
currently in, are now available in VS Code Gemini Code Assist, in
[Preview](https://cloud.google.com/terms/service-terms).

You can cycle through multiple suggestions, dismiss suggestions, or ignore them
and continue coding.

[Enable Next Edit Predictions](https://cloud.google.com/gemini/docs/codeassist/write-code-gemini#use_next_edit_predictions)
in your IDE to get started.

![Next Edit Predictions in VS Code Gemini Code Assist.](https://cloud.google.com/gemini/images/release-notes-images/vscode-next-edit.gif)

---
## 2025-09-23

### Feature



### Inline diff is generally available (GA) for VS Code

[Inline diff](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#view_code_diffs)
is generally available for VS Code Gemini Code Assist. With the inline diff
view, chat generated code suggestions are visually highlighted directly in your
editor—green for additions, red for deletions. This feature boosts productivity
by offering immediate visibility on modifications, streamlining reviews, and
enabling precise control over integrating new code, all without leaving your
current view.

If preferred, you can also
[change the diff view settings to have a side-by-side diff window](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#change_diff_view_settings)
instead of the inline diff.

![Inline diff in VS Code Gemini Code Assist.](https://cloud.google.com/gemini/images/release-notes-images/vscode-inline-diff.gif)

### Feature



### Revert to a checkpoint in IntelliJ (GA)

[Reverting to a checkpoint for chat code suggestions](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#revert_to_a_checkpoint_in_chat)
with IntelliJ Gemini Code Assist is now generally available. Reverting to a
checkpoint lets you revert affected source files to a point before any code
suggestions were applied.

### Feature



### Access saved prompts in the Prompt Library

You can [access saved prompts](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#create_custom_commands)
in the Prompt Library when you type `@` in Gemini chat and select the prompt you
want.

To view the Prompt Library settings, go to **Settings** > **Tools** >
**Gemini** > **Prompt Library**.

![Saved prompt in Prompt Library in IntelliJ Gemini Code Assist.](https://cloud.google.com/gemini/images/release-notes-images/intellij-saved-prompt.png)

### Feature



### Copy sign-in link

As an alternative to clicking **Sign in** when signing into your Google Account
to use IntelliJ Gemini Code Assist, you can [click **Copy link**](https://cloud.google.com/gemini/docs/discover/set-up-gemini#sign-in-select-gcp-project)
and manually paste the link in your browser's URL bar.

---
## 2025-09-18

### See code customization status directly in IDE

You'll now get a one-time notification the first time code customization is
enabled for you, so you know right away that the feature is active.
Additionally, you can now check the status of code customization directly by
clicking on the Gemini icon in your IDE. This makes it simple to confirm that
the feature is configured correctly and ready to go. For more information, see
[Code customization overview](https://cloud.google.com/gemini/docs/codeassist/code-customization-overview).

---
## 2025-09-11

### Delete prompt and response pair in VS Code

You can [delete your prompt and Gemini's response to that prompt](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#delete_prompt_and_response_pairs) in your chat with
Gemini Code Assist. This works as an alternative to deleting your entire chat
history, allowing you to remove a single prompt and response within a chat,
while maintaining the rest of your chat history with Gemini Code Assist.

### Introducing Release Channels in Gemini Code Assist

We're rolling out Release Channels in Gemini Code Assist Standard and Enterprise
to give you more control over the features and models you access, helping us
deliver new capabilities faster. This means direct access to our latest features,
minimizing the need for sign-ups.

You can choose between the Preview Channel for early access to cutting-edge
features (no SLA) or the GA Channel for stable, fully supported features with a
standard Google Cloud SLA. Project leads and administrators can easily configure
these settings at the Google Cloud Platform project level within the Admin for
Gemini settings, making it simple to opt in your entire team to the Preview
channel if desired. Note that at launch, the two release channels have
identical features. For more information, see
[Configure Gemini Code Assist release channels](https://cloud.google.com/gemini/docs/codeassist/configure-release-channels).

![Configure a Gemini Code Assist release channel in the Google Cloud console](https://cloud.google.com/gemini/images/release-notes-images/gemini-code-assist-release-channel-setting.png)

### Performance and stability improvements for VS Code

Numerous performance and stability improvements have been made to the Gemini
Code Assist extension, further reducing extension crashes and related adverse
functional events.

### Edit a prior prompt in VS Code

You can [edit a prior prompt](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#edit_a_prior_prompt) in Gemini Code Assist and receive a regenerated
response based on your edited prompt.

### Regenerate a prompt response in VS Code

You can [regenerate a prompt response](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#regenerate_a_prompt_response) to your most recent prompt, where
Gemini Code Assist re-evaluates your prompt and provides a new response.

---
## 2025-09-10

### Deploy apps to Cloud Run in Gemini Code Assist agent mode (Preview)

Leverage the power of Gemini CLI extensions in VS Code Gemini Code Assist agent
mode with the `/deploy` custom slash command. The `/deploy` command lets you deploy
your existing web application to Cloud Run directly from agent mode. `/deploy`
takes care of what used to be a multi-step process of building, containerizing,
pushing, and configuring, and then returns a public URL for your live
application.

![Use the /deploy command to deploy to Cloud Run](https://cloud.google.com/gemini/images/release-notes-images/vscode-agent-mode-deploy.gif)

To get started using the `/deploy` command, create a web application
in your workspace, install the
[Cloud Run MCP server](https://github.com/GoogleCloudPlatform/cloud-run-mcp),
turn on agent mode, and then type `/deploy`. Your app is deployed in minutes and
accessible through a public URL. For more information, see
[Use commands](https://cloud.google.com/gemini/docs/codeassist/use-agentic-chat-pair-programmer#use-commands).

---
## 2025-09-09

### Add terminal output to context in IntelliJ

You can [attach terminal output to the chat context](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#prompt_with_selected_terminal_output_using_chat) with IntelliJ
Gemini Code Assist. You can now ask Gemini Code Assist questions about terminal
commands and output.

### Regenerate a prompt response in IntelliJ

You can [regenerate a prompt response](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#regenerate_a_prompt_response)
to your most recent prompt, where Gemini Code Assist re-evaluates your prompt
and provides a new response.

---
## 2025-09-04

### Monitor Gemini Code Assist usage

You can now monitor your organization's usage of Gemini Code Assist with a
dashboard that is automatically available when you enable and use Gemini Code
Assist. The dashboard includes some of the most important metrics, giving you a
quick way to view aggregated usage data. For more information, see
[Monitor Gemini Code Assist usage](https://cloud.google.com/gemini/docs/codeassist/monitor-gemini-code-assist).

---
## 2025-09-03

### Mention a remote repository to prioritize context

You can now start your prompt with the `@` symbol and select a specific
remote repository from a list to ensure Gemini prioritizes that context. This
feature is designed to give you more relevant and precise suggestions by
explicitly directing Gemini's focus to the codebase you care about most,
allowing you to get more tailored and accurate results. For more information,
see
[Code customization overview](https://cloud.google.com/gemini/docs/codeassist/code-customization-overview).

---
## 2025-09-02

### Create and manage multiple chats in IntelliJ

You can [create and manage multiple chats](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#create_multiple_chats) in IntelliJ Gemini Code Assist.
Each chat contains its own context separate from other chats.

### Edit a prior prompt in IntelliJ

You can [edit a prior prompt](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#edit_a_prior_prompt)
in IntelliJ Gemini Code Assist and receive a regenerated response based on your
edited prompt.

---
## 2025-08-29

### Full Remote Codebase Awareness

Comprehensive understanding of your entire remote codebase directly within the
chat interface. This new capability improves the quality of suggestions and
answers to general questions about your project. To use it, ask an abstract
question about your remote context, such as "What does this repository do?" and
Gemini uses its deep knowledge of the codebase to provide a detailed and
accurate response. For more information, see
[Code customization overview](https://cloud.google.com/gemini/docs/codeassist/code-customization-overview).

### Get suggestions from your documentation stored in Markdown files

Gemini Code Assist code customization can now index and understand your
organization's internal documentation, stored in Markdown files. This means that
when you ask a question or request a code snippet, Gemini will use the context
available in your team's documentation to provide more accurate and tailored
responses, improving both the quality of the suggestions and the overall
relevance of the information you receive. To take advantage of this, ask a
question that is related to the context available in your remote Markdown files,
and Gemini will use that knowledge to assist you. For more information, see
[Code customization overview](https://cloud.google.com/gemini/docs/codeassist/code-customization-overview).

---
## 2025-08-27

### Change in telemetry setting behavior for VS Code Gemini Code Assist

Gemini Code Assist telemetry log settings now override the VS Code telemetry
setting. For example, if the Gemini Code Assist telemetry log setting is turned
on but the VS Code telemetry setting is turned off, then telemetry data is still
collected. For more information, see
[Configure Gemini for Google Cloud logs](https://cloud.google.com/gemini/docs/configure-logging).

---
## 2025-08-15

### Numerous IDE performance improvements

Numerous improvements to VS Code Gemini Code Assist performance, including
reductions in CPU usage, memory usage, and extension slowdown.

### Release channel name in VS Code chat banner

VS Code Gemini Code Assist shows the configured **Release Channel** when you're
opted into an experimental channel and are using a Standard or Enterprise
license.

![Release channel name in VS Code chat banner.](https://cloud.google.com/gemini/images/release-notes-images/vscode-release-channel-info.png)

### Delete prompt and response pair in IntelliJ

You can [delete your prompt and Gemini's response to that prompt](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#delete_prompt_and_response_pairs) in your chat with IntelliJ Gemini
Code Assist. This works as an alternative to deleting your entire chat history,
allowing you to remove a single prompt and response within a chat, while
maintaining the rest of your chat history with Gemini Code Assist.

![Delete prompt and response pair in IntelliJ Gemini Code Assist.](https://cloud.google.com/gemini/images/intellij-delete-prompt-response-pair.png)

---
## 2025-08-12

### Configure Gemini Code Assist code customization in the Google Cloud Console

You can now set up and manage code customization within the Google Cloud Console,
including creating a code repository index, adding repositories to be indexed,
and managing repository groups for granular access control. For more information,
see
[Configure Gemini Code Assist code customization](https://cloud.google.com/gemini/docs/codeassist/code-customization).

---
## 2025-08-08

### Quick Preview of chat code suggestions across multiple files

#### VS Code Gemini Code Assist `2.44.0`

Gemini Code Assist chat provides a [quick preview](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#view_code_diffs)
of the collective code suggestions across multiple files in the chat. Selecting
a particular file opens the corresponding file in the editor with the first
suggestion selected by default.

![Quick Preview in VS Code Gemini Code Assist.](https://cloud.google.com/gemini/images/vscode-quick-preview.png)

---
## 2025-08-01

### Clickable filenames in chat output

#### IntelliJ Gemini Code Assist `1.23.3`

IntelliJ Gemini Code Assist provides clickable filenames when it references a
file in your workspace as part of its chat response. Clicking the filename opens
the file in your workspace.

### Chat banner shows release channel information

#### IntelliJ Gemini Code Assist `1.23.3`

The IntelliJ Gemini Code Assist chat banner shows the release channel that
you're currently working in.

![IntelliJ Gemini Code Assist chat banner shows release channel info.](https://cloud.google.com/gemini/images/release-notes-images/intellij-release-channel-info.png)

### View code diff in IntelliJ chat

#### IntelliJ Gemini Code Assist `1.23.3`

With the [code diff view](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#view_code_diffs)
in IntelliJ Gemini Code Assist, you can view suggested code changes directly in
your chat with Gemini Code Assist. This feature boosts productivity by offering
immediate visibility on modifications, streamlining reviews, and enabling
precise control over integrating new code, all within the Gemini Code Assist
chat interface.

![Accept code diff in IntelliJ Gemini Code Assist.](https://cloud.google.com/gemini/images/intellij-accept-diff.png)

### Multi-part chat code suggestions

#### IntelliJ Gemini Code Assist `1.23.3`

IntelliJ Gemini Code Assist now supports streamlined multi-part chat code
suggestions. You have the option to accept a single code change or all suggested
changes.

![Structured chat edits in IntelliJ Gemini Code Assist](https://cloud.google.com/gemini/images/release-notes-images/intellij-structured-chat-edits.png)

---
## 2025-07-31

### Use Gemini Code Assist agent mode in IntelliJ (Preview)

![IntelliJ Gemini Code Assist agent mode in action](https://cloud.google.com/gemini/images/release-notes-images/intellij-agent-mode-in-action.gif)

#### Stay in control with interactive reviews and approvals

You can use Gemini Code Assist chat in agent mode to complete complex,
multi-step tasks and goals with complete control over every change. Before
making any modifications, the agent will present a plan for your review. You can
edit, ask for changes, approve, or deny any suggested changes. This
collaborative approach combines the power of AI with your expertise, resulting
in better code and a more efficient workflow.

To get started with agent mode, restart your IDE and follow the instructions in
[Use agentic chat as a pair programmer](https://cloud.google.com/gemini/docs/codeassist/use-agentic-chat-pair-programmer).

### Auto Approve mode lets the agent act on your behalf (Preview)

Enable auto approve mode to let the agent act on your behalf. Once the agent is
done you can review and roll back changes as you see fit.

![auto-approve mode in action](https://cloud.google.com/gemini/images/release-notes-images/intellij-auto-approve-in-action.gif)

### Use agent mode in Gemini Code Assist for VS Code (Preview)

![Agent mode in VS Code](https://cloud.google.com/gemini/images/release-notes-images/vscode-agent-mode-toggle.png)

#### Tackle complex tasks with Gemini Code Assist agent mode for VS Code

Gemini Code Assist agent mode is available for all users. Describe your goal,
and Gemini will create a plan for you to review and approve before any code is
changed. This update removes the insiders channel requirement, and includes
persistent agent mode or interactive chat state between IDE restarts, real-time
shell command output, and faster UI performance. This collaborative approach
combines AI power with your expertise, enabling you to complete multi-step tasks
with complete control and efficiency.

To get started with agent mode, see
[Use agentic chat as a pair programmer](https://cloud.google.com/gemini/docs/codeassist/use-agentic-chat-pair-programmer).

### Effectively collaborate with your agent with the improved diff view functionality (Preview)

We've enhanced Gemini Code Assist agent mode with powerful new
editing capabilities. You can edit code changes directly in the integrated Diff
view for precise, on-the-fly adjustments. To improve clarity, we've also added
inline diffs directly in the chat, making it easier to see proposed changes at a
glance. These features give you unparalleled control and a more efficient way to
refine AI-suggested code.

![Agent mode diff view in VS Code](https://cloud.google.com/gemini/images/release-notes-images/vscode-agent-mode-diff-view.png)

---
## 2025-07-28

### Inline diff (Preview)

#### VS Code Gemini Code Assist `2.42.0`

[Inline diff](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#view_code_diffs)
is available for VS Code Gemini Code Assist `2.42.0` in
[Preview](https://cloud.google.com/terms/service-terms). With the inline diff
view, you can visually highlight code changes directly in your editor—green for
additions, red for deletions. This feature boosts productivity by offering
immediate visibility on modifications, streamlining reviews, and enabling
precise control over integrating new code, all without leaving your current
view.

If preferred, you can
[change the diff view settings to have a side-by-side diff window](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#change_diff_view_settings)
instead of the inline diff.

![Inline diff in VS Code Gemini Code Assist.](https://cloud.google.com/gemini/images/release-notes-images/vscode-inline-diff.gif)

---
## 2025-07-24

### Stop in-progress chat responses with IntelliJ

#### IntelliJ Gemini Code Assist `1.22.1`

You can
[stop chat responses](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#stop_in-progress_chat)
with IntelliJ Gemini Code Assist `1.22.1`. Undesired long running or errant chat
responses are immediately halted.

### Thinking tokens

#### IntelliJ Gemini Code Assist `1.22.1`

You'll see thinking insights into Gemini's thought process before IntelliJ
Gemini Code Assist produces a response, to show you that Gemini is actively
working on your request.

![Thinking tokens in IntelliJ Code Gemini Code Assist.](https://cloud.google.com/gemini/images/release-notes-images/intellij-thinking-tokens.png)

---
## 2025-07-18

### Improved code completion speed

#### VS Code Gemini Code Assist `2.41.0`

Code completion suggestion speed is improved with VS Code Extension `2.41.0`.

---
## 2025-07-17

### Checkpoints, selected code snippets and terminal output, and other features are now Generally Available (GA)

The following features, which launched in Preview in May and June 2025, are now
[Generally Available](https://cloud.google.com/terms/service-terms):

* [Revert to checkpoints](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#revert_to_a_checkpoint_in_chat)
* [Add selected code snippets to context](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#add_selected_code_snippets_to_context)
* [Prompt Gemini Code Assist with selected terminal output](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#prompt_with_selected_terminal_output_using_chat)
* [Specify filenames in your workspace](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#specify_files_and_folders_in_your_workspace_context)
* [Exclude files from Gemini Code Assist use](https://cloud.google.com/gemini/docs/codeassist/create-aiexclude-file)

---
## 2025-07-15

### Announcement



### Thinking tokens

You'll see thinking insights into Gemini's thought process before Gemini Code
Assist produces a response, to show you that Gemini is actively working on your
request.

![Thinking tokens in VS Code Gemini Code Assist.](/gemini/images/release-notes-images/vscode-thinking-tokens.gif)

---
## 2025-07-01

### Gemini 2.5 Pro and Gemini 2.5 Flash models are Generally Available (GA)

Gemini 2.5 Pro and Gemini 2.5 Flash are [Generally Available (GA)](https://cloud.google.com/terms/service-terms). These models are used for Gemini Code Assist Standard and Enterprise, and power Gemini Code Assist's chat, code generation, and code transformation capabilities.

With the integration of these stable versions of Gemini 2.5 Pro and Gemini 2.5 Flash, you'll experience a boost in how Gemini Code Assist handles complex tasks. These models excel in areas like coding, mathematics, science, and intricate reasoning, leading to more accurate and helpful suggestions.

![Gemini Code Assist 2.5 Flash and Pro comparison chart.](https://cloud.google.com/gemini/images/release-notes-images/gca-flash-pro-chart.png)

---
## 2025-06-25

### Use agent mode in Gemini Code Assist Standard and Enterprise insiders channel for VS Code (Preview)

![Review and approve](https://cloud.google.com/gemini/images/release-notes-images/vscode-agent-mode-approve-changes.gif)

**Stay in control with interactive reviews and approvals**.

You can use Gemini Code Assist chat in agent mode to complete complex, multi-step tasks and goals with complete control over every change. Before making any modifications, the agent will present a plan for your review. You can edit, ask for changes, approve, or deny any suggested changes. This collaborative approach combines the power of AI with your expertise, resulting in better code and a more efficient workflow.

To get started with agent mode, see [Use agentic chat as a pair programmer](https://cloud.google.com/gemini/docs/codeassist/use-agentic-chat-pair-programmer).

### Use multi file editing in Gemini Code Assist Standard and Enterprise insiders channel in agent mode for VS Code (Preview)

![Multi-file edits](https://cloud.google.com/gemini/images/release-notes-images/vscode-agent-mode-multi-file-edit.gif)

**Say goodbye to single-file edits and hello to project-wide changes**.

With multi-file edits in agent mode, the agent can make concurrent changes across your entire codebase in response to a single prompt. This powerful new capability streamlines large-scale refactoring, feature implementation, and bug fixes. Simply describe the changes you need, and the agent will intelligently identify and modify all relevant files, saving you time and effort.
You will also have the option to undo changes to local files in case you want to revert the changes to an earlier state.

### Use full project context in Gemini Code Assist Standard and Enterprise insiders channel in agent mode for VS Code (Preview)

![Explain my codebase](https://cloud.google.com/gemini/images/release-notes-images/vscode-agent-mode-explain-codebase.gif)

**Smarter, more accurate code suggestions with full project awareness**.

Agent mode has a comprehensive understanding of your entire project. The agent analyzes your whole codebase and requests files and folders as needed based on your goals. Full project context lets the agent create more accurate and context-aware code completions, suggestions, and refactorings. This deeper understanding of your project's architecture, dependencies, and coding patterns means you get higher-quality, more consistent code with less effort.

---
## 2025-06-18

### Feature



### Chat code suggestion preview

Chat code suggestions are [displayed in a preview block](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#configure_preview_pane) by default with VS Code Gemini Code Assist `2.37.0`, improving the readability of generated chat responses. You can [configure preview pane settings](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#configure_preview_pane) to alternatively display chat code suggestions as fully collapsed or expanded.

![Preview pane in VS Code Gemini Code Assist.](https://cloud.google.com/gemini/images/release-notes-images/vscode-preview-pane.gif)

### Feature



### Revert to a checkpoint (Preview)

You can [revert to a checkpoint for chat code suggestions](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#revert_to_a_checkpoint_in_chat) with VS Code Gemini Code Assist `2.37.0`, in [Preview](https://cloud.google.com/terms/service-terms). Reverting to a checkpoint enables you to revert affected source files to a point before any code suggestions were applied.

![Preview pane in VS Code Gemini Code Assist.](https://cloud.google.com/gemini/images/release-notes-images/vscode-revert-to-checkpoint.gif)

### Feature



### Configure local codebase awareness

You can [configure local codebase awareness](https://cloud.google.com/gemini/docs/codeassist/configure-local-codebase-awareness) with VS Code Gemini Code Assist `2.37.0`.

---
## 2025-06-12

### Feature



### Configure AI exclusion files

You can now [configure the use of `.aiexclude` and `.gitignore` files](https://cloud.google.com/gemini/docs/codeassist/create-aiexclude-file#configure_context_exclusion_settings) to exclude files from the local context with VS Code Gemini Code Assist (version `2.36.0`).

### Feature



### Add code snippets to the chat context

You can now select, attach, and direct Gemini to focus on code snippets with VS Code Gemini Code Assist (version `2.36.0`). [Code snippet selection](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#add_selected_code_snippets_to_context) enables discrete analysis of smaller code blocks instead of entire files, as [Preview](https://cloud.google.com/terms/service-terms).

![Selected code snippets in VS Code Gemini Code Assist](https://cloud.google.com/gemini/images/release-notes-images/vscode-code-snippets.gif)

### Feature



### Add terminal output to the chat context

Terminal output can now be [attached to the chat context](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#prompt_with_selected_terminal_output_using_chat) with VS Code Gemini Code Assist (version `2.36.0`). You can now ask Gemini Code Assist questions about terminal commands and output, as [Preview](https://cloud.google.com/terms/service-terms).

![Selected terminal output in VS Code Gemini Code Assist](https://cloud.google.com/gemini/images/release-notes-images/vscode-terminal-snippets.gif)

---
## 2025-06-05

### Feature



### Automatic scrolling

VS Code Gemini Code Assist (version `2.35.0`) now [automatically scrolls through chat responses](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#configure_automatic_scrolling), enabling easier and faster readability. You can disable automatic scrolling in the Gemini Code Assist settings.

![Automatic scrolling in VS Code Gemini Code Assist.](https://cloud.google.com/gemini/images/release-notes-images/vscode-automatic-scrolling.gif)

### Feature



### Stop in-progress chat responses

You can now [stop chat responses](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#stop_in-progress_chat) with VS Code Gemini Code Assist (version `2.35.0`). Undesired long running or errant chat responses are immediately halted.

![Stop chat responses in VS Code.](https://cloud.google.com/gemini/images/release-notes-images/vscode-stop-chat.png)

### Feature



### Clickable filenames in chat (Preview)

You can now click filenames referenced in a chat response to open the file in the IDE with VS Code Gemini Code Assist (`2.35.0`), as [Preview](https://cloud.google.com/terms/service-terms#1).

![Clickable filenames in VS Code.](https://cloud.google.com/gemini/images/release-notes-images/vscode-clickable-filenames.png)

### Feature



### Exclude files from local context (Preview)

[Context exclusion of files using `.gitIgnore` is now enforced](https://cloud.google.com/gemini/docs/codeassist/create-aiexclude-file). Files present in `.gitignore` are now excluded from the local context with chat, code generation, code completion, and code transformation, as [Preview](https://cloud.google.com/terms/service-terms#1).

---
## 2025-05-28

### Feature



### Manage files and folders in the Context Drawer

You can now [view and manage files and folders requested to be included in Gemini Code Assist's context, using the Context Drawer](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#manage_files_and_folders_in_the_context_drawer). After you specify a file or folder to be used as context for your Gemini Code Assist prompts, these files and folders are placed in the Context Drawer, where you can review and remove them from the prompt context.

This gives you more control over which information Gemini Code Assist considers when responding to your prompts.

![Context Drawer for Gemini Code Assist for VS Code](https://cloud.google.com/gemini/images/vscode-context-drawer.png)

---
