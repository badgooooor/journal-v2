# Blog Writer Skill — Sanitize & Translate

You are helping process a blog post through two steps: sanitize the English source, then translate it to Thai.

## Arguments

The user may pass a file path as `$ARGUMENTS` (e.g. `content/en/articles/my-post.md`).
- If a path is provided, use it directly.
- If no path is provided, list the files in `content/en/articles/` and ask the user which one to process.

---

## Step 1: Sanitize the English source

Read the file at `content/en/articles/<filename>`.

Fix the frontmatter to match this exact schema:

```yaml
---
title: "..."        # must be a quoted string
description: "..."  # must be a quoted string
published: YYYY/MM/DD
slug: "..."         # must be a quoted, kebab-case string
tags:
  - tag1            # must be a YAML block list, not inline
  - tag2
---
```

Rules:
- `title` and `description`: wrap bare values in double quotes. Escape any `"` inside the value with `\"`.
- `published`: normalize to `YYYY/MM/DD` (e.g. `2025-06-12` → `2025/06/12`).
- `slug`: must be quoted and kebab-case (lowercase, words separated by hyphens).
- `tags`: convert inline arrays `[tag1, tag2]` to a block list.
- Body: remove trailing whitespace on each line. Ensure there is a blank line after every heading (`##`, `###`, etc.) before the next paragraph.

Write the sanitized file back to its original path (`content/en/articles/<filename>`).

---

## Step 2: Translate to Thai

Using the sanitized English source, produce a Thai translation:

- **Frontmatter**: copy it exactly as-is (title, description, slug, tags all stay in English — do not translate them).
- **Body**: translate to Thai.
  - Use a **natural, informal, conversational** tone — first-person, relaxed, as if writing to a friend. This matches the style of existing Thai articles in this blog.
  - Preserve all markdown formatting: headings, bold, italic, blockquotes, code blocks, inline code, images, and links must remain intact with the same structure.
  - Do not translate code blocks or inline code.
  - Do not translate image URLs or link URLs.
  - Technical terms (framework names, tool names, protocol names, etc.) can stay in English within the Thai text.

Write the translated file to `content/th/articles/<same-filename>`.

---

## Output

After completing both steps, briefly confirm:
1. Sanitized: `content/en/articles/<filename>` — list any frontmatter fields that were fixed
2. Translated: `content/th/articles/<filename>` — created
