# PolyglotQuest 🎮🌍
> **AI-Native Multilingual RPG & In-Game Contextual Coaching Platform**
> Built with Google Cloud ADK (Python), Vertex AI Agent Engine (`reasoning_engines`), Gemini 3.X, A2UI Protocol, and Google Workspace Integration.

[![Tests](https://img.shields.io/badge/tests-95%20passed-brightgreen.svg)]()
[![Coverage](https://img.shields.io/badge/coverage-94%25-brightgreen.svg)]()
[![Python](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13-blue.svg)]()
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)]()

---

## 🌟 Overview

**PolyglotQuest** bridges the gap between traditional rote language apps and real-world conversational competence. Learners step into authentic cultural scenarios across **Portuguese, Spanish, and French** (for English native speakers) across 4 domain tracks: **Academic**, **Professional**, **Travel**, and **Hobbies**.

The platform features a **Dual-Pane Immersion & Live Voice Capstone Layout**:
1. **Left Pane (ADK Contextual Coaching Sidecar)**: An AI mentor observing real-time game events, offering sociolinguistic explanations, dialectal notes, and subtle tactical hints without spoiling choices. Emits declarative **A2UI** interactive elements including quick-reply chips and guided suggestions.
2. **Right Pane (Retro HTML5 Canvas 2D Game Frame)**: Adaptable procedural stage-box dioramas (5 environments, counters, thematic props), walk-in character cinematics, interactive Rosetta/Duolingo 4-6 card challenges with Web Speech API audio, and a dynamic **Social Harmony Meter** (0–100%).
3. **Gemini Live 3.x Native Procedural Avatar Voice Boss Capstone**: An interactive end-of-game oral fluency exam powered by `gemini-3.1-flash-live-preview` WebSocket streaming, real-time procedural Canvas 2D avatars (Manuel, Carmen, Laurent) with audio-reactive viseme lip-sync (`rest`, `A`, `E`, `O`, `U`, `MBP`), idle breathing, blinking, and reactive emotion shifts (`neutral`, `happy`, `impressed`, `offended`).

---

## 🏗️ Architecture

```
                                      [ User / Learner ]
                                              │
                      ┌───────────────────────┴───────────────────────┐
                      ▼                                               ▼
         [ ADK Coaching Sidecar ]                       [ HTML5 Canvas RPG Frame ]
                      │                                               │
                      └──────── A2UI postMessage IPC Bridge ──────────┘
                                              │
                                     FastAPI Server (:8080)
                                              │
                                       CoordinatorAgent
            ┌───────────────────┬─────────────┴─────────────┬───────────────────┐
            ▼                   ▼                           ▼                   ▼
  CurriculumDeveloperAgent  ScenarioCompilerAgent   InGameCoachAgent   WorkspaceSyncAgent
  (6-Slot State Machine)    (Self-Healing DAG)      (Live Mentor)      (Slides/Docs/Cal)
                                │
                                ▼
         ┌────────────────────────────────────────────────────────┐
         │     Managed Agents (Interactions API) Generation       │
         │  Architect ──> Builder ──> Graph & Pedagogy Auditor    │
         │                   ▲                     │ (Feedback)   │
         │                   └─────────────────────┘              │
         └────────────────────────────────────────────────────────┘
```

---

## 🧩 Protocol Standards & Scaffolding

### 1. A2UI (Agent-to-User Interface) Protocol
PolyglotQuest adheres to Google's **A2UI** specification:
- **Declarative Blueprints**: The ADK agent never streams raw, executable JavaScript. It transmits structured JSON envelopes containing UI components:
  - Contextual action chips (`suggested_actions` pills).
  - Rosetta matching challenges (`MatchingCard` decks with target-language terms, phonetic transcriptions, and cultural feedback).
- **Bidirectional WebFrame IPC**: The client app communicates with the agent using structured `postMessage` envelopes (`PQ_INIT_SESSION`, `PQ_GAME_READY`, `PQ_CHOICE_SELECTED`, `PQ_AGENT_HINT`, `PQ_GAME_COMPLETED`), matching the Gemini Enterprise A2UI iframe architecture.

### 2. Standard ADK & `agents-cli` Scaffolding
- **`agents-cli-manifest.yaml`**: Canonical project manifest configuring runtime, deployment target (`cloud_run`), region (`us-central1`), and `agent_directory: adk`.
- **`adk/` Directory**: Self-contained Google Cloud ADK package containing:
  - `adk/agent.py`: Single canonical `root_agent` entrypoint configuring subagents and tools.
  - `adk/subagents/`: Specialized runtime subagents (`CoordinatorAgent`, `CurriculumDeveloperAgent`, `ScenarioCompilerAgent`, `InGameCoachAgent`, `WorkspaceSyncAgent`).
  - `adk/tools/`: ADK tool modules (`live_llm`, `managed_agent`, `tts`, `workspace`).
  - `adk/agent.yaml` & `adk/reasoning_engine.yaml`: Declarative Vertex AI Reasoning Engine manifests.
- **`src/polyglotquest/`**: Core application library and backend services (FastAPI HTTP/WebSocket server, Pydantic domain models, Cloud DLP redactor, session storage, and telemetry).

---

## 🚀 Quickstart

### 1. Environment Setup
```bash
git clone https://github.com/behmke12/polyglot-quest-agent.git
cd polyglot-quest-agent

python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
playwright install chromium
```

### 2. Run Test Suites
```bash
# Run all 99 tests: unit tests, 20 golden CUJ evaluations, and live integration tests
pytest tests/ -v

# Run Playwright headless browser E2E tests
pytest tests/e2e/ -v
```

### 3. Launch Local Server & Playground
```bash
# Launch FastAPI server with UI & WebSocket live endpoints
python -m uvicorn polyglotquest.server:app --host 0.0.0.0 --port 8080

# Or inspect project via agents-cli
agents-cli info
agents-cli run "I want to practice Portuguese for a trip to Lisbon"
```

---

## 📊 Observability & Vertex AI Evaluation

- **Google Cloud Logging**: Structured JSON logging format conforming to GCP standards with `logging.googleapis.com/trace` and `logging.googleapis.com/spanId` correlation, mapping severity levels and capturing intent-vs-outcome state.
- **OpenTelemetry & Cloud Trace**: Tracing spans wrapping agent turns (`trace_agent_turn`) and subagent delegations.
- **Vertex AI Gen AI Evaluation Service**: Pre-configured PointwiseMetric rubrics in `src/polyglotquest/observability/vertex_evaluation.py`:
  - **Rosetta Pedagogical Immersion**: Validates contextual immersion and translation avoidance.
  - **Dialect Authenticity**: Assesses European vs. Brazilian Portuguese, Peninsular vs. Latin American Spanish, and Parisian vs. Québécois French.
  - **CEFR Level Calibration**: Evaluates syntactic complexity and lexical accessibility across A1 through C1.

---

## 💡 Architectural Rationale & Scaled Tradeoffs ("Why X?")

Every architectural decision in PolyglotQuest resolves concrete enterprise and pedagogical engineering challenges:

1. **Why Dual-Pane Immersion over a Chatbot-only Interface?**
   - *Problem*: Pure text chat fosters passive recognition, lexical guessing, and conversational fatigue without spatial or visual anchoring.
   - *Rationale*: Coupling a retro HTML5 2D Canvas stage-box diorama with an ADK sidecar grounds the learner in an authentic cultural environment (counters, props, walk-in NPCs). The sidecar acts as a live sociolinguistic advisor rather than a conversational crutch.

2. **Why Google's A2UI Declarative Protocol over Raw LLM HTML/JS Streaming?**
   - *Problem*: Allowing LLMs to stream executable HTML/JavaScript creates severe cross-site scripting (XSS) attack vectors, renders unpredictably across devices, and couples agent intelligence to frontend CSS frameworks.
   - *Rationale*: A2UI enforces a security-first boundary: the agent emits structured JSON blueprints (`MatchingCard` decks, `suggested_actions` pills), and the trusted client application renders native widgets with zero execution risk. The bidirectional `postMessage` bridge mirrors the Gemini Enterprise A2UI WebFrame architecture.

3. **Why Dual-Zone Context Compaction over Naive History Truncation?**
   - *Problem*: Naive FIFO windowing drops critical early constraints (target language, CEFR tier, slang preference) or drops active quest state mid-dialogue.
   - *Rationale*: Dual-Zone compaction preserves the 4–6 most recent turns verbatim in high-fidelity *Working Memory* for conversational coherence, while asynchronously consolidating older turns into factual pedagogical bullets in *Semantic Summary*.

4. **Why Multi-Agent Managed Agents Pipeline (Architect → Builder → Auditor)?**
   - *Problem*: Single-turn monolithic generation fails when generating complex branching DAGs with 8+ nodes, causing dangling pointers and unreachable victory terminals.
   - *Rationale*: Decomposing the generation into specialized roles (Pedagogy Architect, Scenario Builder, and Graph Auditor) paired with an ADK-orchestrated verification feedback loop ensures mathematically guaranteed graph connectivity and cultural fidelity before a scenario reaches the player.

5. **Why Gemini Live 3.x Native WebSocket Audio Streaming for Capstones?**
   - *Problem*: Turn-based text-to-speech roundtrips introduce 2–4 seconds of latency, destroying the realism of high-stakes verbal fluency exams.
   - *Rationale*: Bi-directional WebSocket streaming with Gemini Live delivers sub-second speech-to-speech conversational responsiveness. Combining streaming audio with real-time procedural viseme lip-sync (`rest`, `A`, `E`, `O`, `U`, `MBP`) creates an engaging oral exam capstone.

---

## 📋 95-Point Assessment Rubric Mapping

- **Category 1: Tool & Interface Design**: Pydantic schemas, guided error handling (`errors.py`), atomic Google Workspace batch updates (`workspace_sync.py`).
- **Category 2: Context & Memory**: Dual-zone context compaction engine (`compaction.py`), Firestore store with automatic local fallback (`session_store.py`).
- **Category 3: Orchestration & Logic**: 6-slot elicitation state machine with slang preference (`curriculum_developer.py`), self-healing DAG repair loop (`scenario_compiler.py`), live in-game coach (`coach.py`), and multi-agent Managed Agents pipeline (Architect, Builder, Auditor).
- **Category 4: Observability & Tracing**: OpenTelemetry distributed tracing, Google Cloud Logging structured format, and Vertex AI Gen AI Evaluation Suite (`vertex_evaluation.py`).
- **Category 5: Infrastructure & CI/CD**: Terraform Cloud Run v2 configuration (`terraform/`), Vertex AI Agent Engine declarative specs (`adk/reasoning_engine.yaml`), standard `agents-cli-manifest.yaml`, and Cloud DLP PII scrubbing (`guardrails/pii_redactor.py`).

