---
name: workspace-context-helper
description: Workspace context aggregation, memory indexing, and document lifecycle assistance. Use when synthesizing documents, managing project memory notes, or organizing Google Workspace resources.
---

# 📑 Workspace Context Helper (`workspace-context-helper`)

Aggregates workspace context, indexes project memory, and manages document lifecycles across Google Workspace applications.

---

## 🎯 When to Use
Use this skill when:
- Synthesizing information across multiple Google Docs, Sheets, Calendar events, and Gmail threads
- Structuring workspace document organization and search queries
- Managing project memory notes, decision logs, and cross-source research synthesis
- Compressing token contexts and orchestrating multi-task workspace DAGs

---

## 📋 Workflow Steps

### Step 1: Context Gathering & Search
- Query relevant Workspace resources (Gmail, Drive, Docs, Sheets, Calendar) using structured search.
- Retrieve full thread details and document content for high-relevance items.
- Scan local directory trees and file schemas using `wc-scan`.

### Step 2: Context Indexing & Synthesis
- Extract key milestones, project updates, and stakeholder communications.
- Cross-reference facts across sources while maintaining strict recency and source attribution.
- Index extracted entities and memory facts into local SQLite store via `wc-agent-memory`.

### Step 3: Workspace Document Management
- Update or draft structured Google Docs, Sheets trackers, or project memory files.
- Pack and compress dense logs into token-efficient payloads via `wc-context-pack`.
- Orchestrate multi-task document workflows via `wc-task-dag`.

---

## 🛠️ Required & Associated Workspace Tools
When aggregating workspace context, managing memory, and synthesizing documents, activate these tools from [`AI-Agents-Workspace-Tools-Library`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library):

- [`wc-context-pack`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-context-pack) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-context-pack.md)): Token density optimizer and document context compressor.
- [`wc-agent-memory`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-agent-memory) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-agent-memory.md)): Local SQLite persistent store for entity indexing and memory facts.
- [`wc-task-dag`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-task-dag) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-task-dag.md)): Multi-task DAG scheduler for automated synthesis pipelines.
- [`wc-scan`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-scan) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-scan.md)): Fast filesystem metadata and tree structure extractor.
- [`wc-resource-lock`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-resource-lock) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-resource-lock.md)): File lock mutex preventing concurrent write conflicts across agents.
