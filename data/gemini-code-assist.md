# Gemini Code Assist

## 2025-06-25 00:00:00-07:00

### Feature

**Agent mode is available in preview in Gemini Code Assist Standard and Enterprise Edition for VS Code**.

![Review and approve](https://cloud.google.com/gemini/images/release-notes-images/vscode-agent-mode-approve-changes.gif)

**Stay in control with interactive reviews and approvals**.

You can use Gemini Code Assist chat in agent mode to complete complex, multi-step tasks and goals with complete control over every change. Before making any modifications, the agent will present a plan for your review. You can edit, ask for changes, approve, or deny any suggested changes. This collaborative approach combines the power of AI with your expertise, resulting in better code and a more efficient workflow.

To get started with agent mode, see [Use agentic chat as a pair programmer](https://cloud.google.com/gemini/docs/codeassist/use-agentic-chat-pair-programmer).### Feature

**Multi file editing is available in preview in Gemini Code Assist Standard and Enterprise Edition chat agent mode**.

![Multi-file edits](https://cloud.google.com/gemini/images/release-notes-images/vscode-agent-mode-multi-file-edit.gif)

**Say goodbye to single-file edits and hello to project-wide changes**.

With multi-file edits in agent mode, the agent can make concurrent changes across your entire codebase in response to a single prompt. This powerful new capability streamlines large-scale refactoring, feature implementation, and bug fixes. Simply describe the changes you need, and the agent will intelligently identify and modify all relevant files, saving you time and effort.
You will also have the option to undo changes to local files in case you want to revert the changes to an earlier state.### Feature

**Full Project Context is available in preview in Gemini Code Assist Standard and Enterprise Edition chat agent mode**.

![Explain my codebase](https://cloud.google.com/gemini/images/release-notes-images/vscode-agent-mode-explain-codebase.gif)

**Smarter, more accurate code suggestions with full project awareness**.

Agent mode has a comprehensive understanding of your entire project. The agent analyzes your whole codebase and requests files and folders as needed based on your goals. Full project context lets the agent create more accurate and context-aware code completions, suggestions, and refactorings. This deeper understanding of your project's architecture, dependencies, and coding patterns means you get higher-quality, more consistent code with less effort.## 2025-06-18 00:00:00-07:00

### Feature

### Chat code suggestion preview

Chat code suggestions are [displayed in a preview block](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#configure_preview_pane) by default with VS Code Gemini Code Assist `2.37.0`, improving the readability of generated chat responses. You can [configure preview pane settings](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#configure_preview_pane) to alternatively display chat code suggestions as fully collapsed or expanded.

![Preview pane in VS Code Gemini Code Assist.](https://cloud.google.com/gemini/images/release-notes-images/vscode-preview-pane.gif)### Feature

### Revert to a checkpoint (Preview)

You can [revert to a checkpoint for chat code suggestions](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#revert_to_a_checkpoint_in_chat) with VS Code Gemini Code Assist `2.37.0`, in [Preview](https://cloud.google.com/terms/service-terms). Reverting to a checkpoint enables you to revert affected source files to a point before any code suggestions were applied.

![Preview pane in VS Code Gemini Code Assist.](https://cloud.google.com/gemini/images/release-notes-images/vscode-revert-to-checkpoint.gif)### Feature

### Configure local codebase awareness

You can [configure local codebase awareness](https://cloud.google.com/gemini/docs/codeassist/configure-local-codebase-awareness) with VS Code Gemini Code Assist `2.37.0`.## 2025-06-12 00:00:00-07:00

### Feature

### Configure AI exclusion files

You can now [configure the use of `.aiexclude` and `.gitignore` files](https://cloud.google.com/gemini/docs/codeassist/create-aiexclude-file#configure_context_exclusion_settings) to exclude files from the local context with VS Code Gemini Code Assist (version `2.36.0`).### Feature

### Add code snippets to the chat context

You can now select, attach, and direct Gemini to focus on code snippets with VS Code Gemini Code Assist (version `2.36.0`). [Code snippet selection](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#add_selected_code_snippets_to_context) enables discrete analysis of smaller code blocks instead of entire files, as [Preview](https://cloud.google.com/terms/service-terms).

![Selected code snippets in VS Code Gemini Code Assist](https://cloud.google.com/gemini/images/release-notes-images/vscode-code-snippets.gif)### Feature

### Add terminal output to the chat context

Terminal output can now be [attached to the chat context](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#prompt_with_selected_terminal_output_using_chat) with VS Code Gemini Code Assist (version `2.36.0`). You can now ask Gemini Code Assist questions about terminal commands and output, as [Preview](https://cloud.google.com/terms/service-terms).

![Selected terminal output in VS Code Gemini Code Assist](https://cloud.google.com/gemini/images/release-notes-images/vscode-terminal-snippets.gif)## 2025-06-05 00:00:00-07:00

### Feature

### Automatic scrolling

VS Code Gemini Code Assist (version `2.35.0`) now [automatically scrolls through chat responses](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#configure_automatic_scrolling), enabling easier and faster readability. You can disable automatic scrolling in the Gemini Code Assist settings.

![Automatic scrolling in VS Code Gemini Code Assist.](https://cloud.google.com/gemini/images/release-notes-images/vscode-automatic-scrolling.gif)### Feature

### Stop in-progress chat responses

You can now [stop chat responses](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#stop_in-progress_chat) with VS Code Gemini Code Assist (version `2.35.0`). Undesired long running or errant chat responses are immediately halted.

![Stop chat responses in VS Code.](https://cloud.google.com/gemini/images/release-notes-images/vscode-stop-chat.png)### Feature

### Clickable filenames in chat (Preview)

You can now click filenames referenced in a chat response to open the file in the IDE with VS Code Gemini Code Assist (`2.35.0`), as [Preview](https://cloud.google.com/terms/service-terms#1).

![Clickable filenames in VS Code.](https://cloud.google.com/gemini/images/release-notes-images/vscode-clickable-filenames.png)### Feature

### Exclude files from local context (Preview)

[Context exclusion of files using `.gitIgnore` is now enforced](https://cloud.google.com/gemini/docs/codeassist/create-aiexclude-file). Files present in `.gitignore` are now excluded from the local context with chat, code generation, code completion, and code transformation, as [Preview](https://cloud.google.com/terms/service-terms#1).## 2025-05-28 00:00:00-07:00

### Feature

### Manage files and folders in the Context Drawer

You can now [view and manage files and folders requested to be included in Gemini Code Assist's context, using the Context Drawer](https://cloud.google.com/gemini/docs/codeassist/chat-gemini#manage_files_and_folders_in_the_context_drawer). After you specify a file or folder to be used as context for your Gemini Code Assist prompts, these files and folders are placed in the Context Drawer, where you can review and remove them from the prompt context.

This gives you more control over which information Gemini Code Assist considers when responding to your prompts.

![Context Drawer for Gemini Code Assist for VS Code](https://cloud.google.com/gemini/images/vscode-context-drawer.png)