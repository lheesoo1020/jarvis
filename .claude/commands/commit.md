Analyze staged changes and commit with an appropriate message.

## Steps
1. Run `git diff --staged` to understand the changes
2. Suggest an appropriate type and message
3. Execute the commit after user confirmation

## Commit Message Rules
- Format: `type: description`
- Types: `feat, fix, refactor, chore, docs, test`
- Description should be concise and imperative (e.g. `implement user login`)
- Start with lowercase, no trailing period

## Handling Multiple Changes
- If types are mixed, use the most significant type
- If changes can be separated, suggest splitting into multiple commits