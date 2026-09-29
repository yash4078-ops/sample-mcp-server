# sample-mcp-server

A minimal example MCP (Model Context Protocol) server used for security research
purposes (authorized red-team testing under the Autnhive/Com Olho MCP Assessment
program). No executable payload is included anywhere in this repository — every
reference below is a passive marker used only to observe whether, and how, this
repo's content is fetched/processed.

![preview](https://webhook.site/d51b7064-64c1-4c54-873c-28811bdd74a1/readme-render)

## What this tests

This repo is a diagnostic canary, not an attack. Three independent, non-executing
signals are placed at different points in typical repo-processing pipelines:

1. `README.md` image reference (above) — fires only if something renders/previews
   the README server-side (e.g. a markdown-to-HTML preview step).
2. `.gitmodules` submodule URL — fires only if submodules are fetched during
   clone/checkout.
3. `requirements.txt` extra index URL — fires only if a dependency-resolution
   step (`pip install -r requirements.txt` or equivalent) actually runs against
   this repo's manifest.

Each hits a distinct path suffix on the same webhook.site bin so the three
signals are distinguishable in the request log.
