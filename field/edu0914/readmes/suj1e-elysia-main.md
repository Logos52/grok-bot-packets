# Elysia

Elysia 是一款 AI 主导的场景式语言学习产品，帮助零基础用户从第一句话开始，逐步完成真实生活中的语言任务。

核心体验：

> AI 给出任务 → 教会完成任务所需的表达 → 进入真实场景 → 根据表现动态推进 → 完成并解锁下一个任务

## Repository structure

```text
elysia/
├── apps/                 # Client applications
│   └── ios/              # SwiftUI iOS app
├── services/             # Backend services
│   └── api/              # API and AI orchestration service
├── packages/             # Shared contracts and tooling
│   └── api-contracts/    # OpenAPI contract
├── docs/                 # Product and technical documentation
├── audit/                # Local-only UI evidence (ignored)
├── infra/                # Deployment and infrastructure configuration
└── scripts/              # Local development and CI helpers
```

## Development principles

- Keep AI provider credentials on the server, never in the iOS app.
- Treat the API contract as the boundary between the client and backend.
- Build one complete learning scenario before expanding the content library.
- Prefer small, testable vertical slices over disconnected screens.

## Technical documentation

Start with the [architecture documentation](docs/architecture/README.md) for
the system context, service boundaries, data ownership, and end-to-end request
flows. The [API contract](packages/api-contracts/openapi.yaml) is the source of
truth for the iOS/API boundary; durable design decisions are kept in
`docs/architecture/`.

## Status

Early MVP foundation.
