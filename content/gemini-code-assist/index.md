# Gemini Code Assist

## 2025-07-24

### Feature



### Stop in-progress chat responses with IntelliJ

#### IntelliJ Gemini Code Assist `1.22.1`

You can
[stop chat responses](/gemini/docs/codeassist/chat-gemini#stop_in-progress_chat)
with IntelliJ Gemini Code Assist `1.22.1`. Undesired long running or errant chat
responses are immediately halted.

### Announcement



### Thinking tokens

You'll see thinking insights into Gemini's thought process before IntelliJ
Gemini Code Assist produces a response, to show you that Gemini is actively
working on your request.

![Thinking tokens in IntelliJ Code Gemini Code Assist.](/gemini/images/release-notes-images/intellij-thinking-tokens.png)

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

* [Revert to checkpoints](/gemini/docs/codeassist/chat-gemini#revert_to_a_checkpoint_in_chat)
* [Add selected code snippets to context](/gemini/docs/codeassist/chat-gemini#add_selected_code_snippets_to_context)
* [Prompt Gemini Code Assist with selected terminal output](/gemini/docs/codeassist/chat-gemini#prompt_with_selected_terminal_output_using_chat)
* [Specify filenames in your workspace](/gemini/docs/codeassist/chat-gemini#specify_files_and_folders_in_your_workspace_context)
* [Exclude files from Gemini Code Assist use](/gemini/docs/codeassist/create-aiexclude-file)

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
