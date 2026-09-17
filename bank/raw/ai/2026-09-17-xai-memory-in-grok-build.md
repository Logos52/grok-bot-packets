---
id: 2026-09-17-xai-memory-in-grok-build
kind: article
title: Memory in Grok Build
source: "https://x.ai/news/grok-build-memory"
author: xAI
published: 2026-09-16
captured: 2026-09-17
via: grok-bot/Brief
lane: ai
status: raw
private: false
---

Memory in Grok Build
Grok Build now carries conventions, decisions, and project facts from one session to the next. Notes are written in the background as you work and read back when you return to the project.
$
curl -fsSL https://x.ai/cli/install.sh
| bash
Try Free
Grok Build now has memory. As you work, it keeps notes on the conventions, decisions, and project facts that come up, and later sessions read those notes before touching related code. Grok Build gets better the more you use it.
~/dev/orbit
|
7.42%
|
❯
run the test suite
◆
Run
cargo test
error: connection refused (postgres at localhost:5432)
test result: FAILED. 143 passed; 5 failed; 0 ignored
❯
use just test, not cargo test. it starts the test database first.
◆
Run
just test
Starting postgres on :5433 ... ready
test result: ok. 148 passed; 0 failed; 0 ignored
All 148 tests pass with just test.
workspaces
›
orbit-3f9c2a1d
›
topics
›
testing.md
Testing
How tests are run and organized in orbit.
Commands
•
Run the suite with
just test
. It starts the test database and then runs
cargo test
; plain
cargo test
fails the integration tests.
•
just test <crate>
runs a single crate.
Fixtures
•
Integration tests seed from
tests/fixtures/seed.sql
.
~/dev/orbit
|
1.08%
|
❯
add a retry with backoff to the webhook sender
◆
Edit
src/webhooks.rs
43
for attempt in 0..MAX_ATTEMPTS {
44
if self.post(event).await.is_ok() {
45
return Ok(());
46
}
47
sleep(backoff(attempt)).await;
48
}
◆
Thought for
1.9s
The testing topic says the suite runs through just test.
◆
Run
just test
Starting postgres on :5433 ... ready
test result: ok. 151 passed; 0 failed; 0 ignored
Added the retry in src/webhooks.rs. 151 tests pass with just test.
Capture
Topic files
Recall
Captured after the turn
After a turn completes, Grok reviews it in the background and records anything durable: conventions, decisions, and project facts. Capture runs on every completed turn and does not interrupt the session.
Stored as markdown
Notes are markdown files, one topic per subject. Each project has its own workspace scope, and a global scope holds preferences that apply everywhere.
/dream
merges new observations into the topic they belong to, and
/memory
shows the files as they are on disk.
Read back in later sessions
Before starting related work, Grok reads the topics that cover the area and applies them, including in sessions where the subject never comes up. Instructions in the current conversation take precedence over anything in a note.
Captured after the turn
After a turn completes, Grok reviews it in the background and records anything durable: conventions, decisions, and project facts. Capture runs on every completed turn and does not interrupt the session.
What it remembers
Memory holds the details most likely to matter in a later session: how the team writes and reviews code, decisions and the reasoning behind them, and durable facts about the project, from where a subsystem lives to which command runs the suite. Task state, tentative conclusions, secrets, and anything the repository or its docs already cover are left out.
Notes are kept per project, plus a global set for preferences that apply everywhere.
Written in the background
Capture runs after a turn completes and never blocks the session. Grok reviews the finished turn, writes anything worth keeping as a markdown note, and continues. Over time,
/dream
folds those notes into topic files, one per subject, so each project ends up with a small set of organized references.
When you return to a project, Grok reads the topics that cover the area it is about to work in. Instructions in the current conversation take precedence over anything in a note.
Browsing memory
/memory
opens a read-only browser of every memory file, grouped by scope, with a preview of the selected file. It is the fastest way to see what a session produced, and to find the file to edit when a note is wrong.
~/dev/orbit
|
4.36%
|
❯
add a retry with backoff to the webhook sender
◆
Edit
src/webhooks.rs
◆
Thought for
1.9s
The testing topic says the suite runs through just test.
◆
Run
just test
Starting postgres on :5433 ... ready
test result: ok. 151 passed; 0 failed; 0 ignored
Added the retry in src/webhooks.rs. 151 tests pass with just test.
❯
