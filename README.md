# Website

My personal website.

https://k7a-tomohiro.github.io/

## Run

This website uses [MkDocs](https://www.mkdocs.org/).

Generate the contribution page (Not necessary for local development).

```sh
pip install requests httpx github_oss_contributions mkdocs-issues-plugin
export GITHUB_TOKEN=******
python generate_contributions.py
```

Install MkDocs and run pages.

```sh
pip install mkdocs mkdocs-material mkdocs-material-extensions mkdocs-static-i18n mkdocs-issues-plugin
mkdocs serve
```

## Page Template

```markdown
---
title: Document Title
summary: A brief description of my document.
date: 2025-12-22
tags: ["Go", "Rust", "lang/go"]
---

# h1

This is the first paragraph of the document.

## h2

This is the second paragraph of the document.
```
