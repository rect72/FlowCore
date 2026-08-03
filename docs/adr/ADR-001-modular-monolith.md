# ADR-001: Use a Modular Monolith

**Status:** Accepted  
**Date:** 2026-08-03  
**Decision Owner:** FlowCore Architecture

---

# Context

FlowCore is an open-source low-code platform for business process automation.

The platform is designed as a multi-tenant system and includes several business domains:

- Identity
- Organizations
- Projects
- Forms
- Submissions
- CRM
- Workflows
- Integrations
- Notifications
- Audit

The first version of the project is developed by a single developer.

The architecture should:

- remain simple to develop;
- remain easy to deploy;
- support business growth;
- clearly separate business domains;
- support future scaling;
- avoid unnecessary infrastructure complexity.

---

# Decision

FlowCore will use a **feature-first modular monolith architecture**.

The application will consist of one backend application and one PostgreSQL database.

Business logic will be divided into independent modules.

Each module owns its own business rules.

The project structure is:

```text
flowcore/
└── modules/
    ├── identity/
    ├── organizations/
    ├── projects/
    ├── forms/
    ├── submissions/
    ├── crm/
    ├── workflows/
    ├── integrations/
    ├── notifications/
    └── audit/
```

Every module contains four layers:

```text
module/
├── domain/
├── application/
├── infrastructure/
└── presentation/
```

Dependency direction:

```text
Presentation
        ↓
Application
        ↓
Domain
        ↑
Infrastructure
```

The Domain layer must not depend on:

- FastAPI
- SQLAlchemy
- Redis
- Celery
- aiogram
- PostgreSQL
- external APIs

Modules communicate only through:

- public application services;
- domain events;
- documented contracts.

Direct access to another module's internal implementation is prohibited.

---

# Consequences

## Positive

- Simple deployment.
- Simple local development.
- Easy debugging.
- Strong transaction support.
- Clear module boundaries.
- Lower infrastructure cost.
- Faster development.
- Easier testing.
- Future migration to microservices remains possible.

## Negative

- One backend process contains all modules.
- Independent deployment of modules is not possible.
- Strong architectural discipline is required.
- Incorrect dependencies may increase coupling.

---

# Alternatives Considered

## Microservices

Rejected because:

- the project is developed by one developer;
- business boundaries are still evolving;
- operational complexity would increase significantly;
- distributed transactions are unnecessary for the first version.

---

## Traditional Layered Monolith

Rejected because it mixes business domains into common folders such as:

```text
controllers/
services/
repositories/
models/
```

This structure becomes difficult to maintain as the project grows.

---

## Serverless

Rejected because:

- workflows require shared business state;
- local development becomes more difficult;
- vendor lock-in increases;
- transactions become harder to manage.

---

# Rules

- Every new feature must belong to a business module.
- Business logic belongs only to the Domain layer.
- Infrastructure must never contain business rules.
- Modules must not access another module's infrastructure directly.
- Circular dependencies are forbidden.
- Shared code should contain only reusable utilities.

---

# Review Conditions

This decision should be reviewed if:

- multiple development teams work on the project;
- independent deployment becomes necessary;
- one module requires separate scaling;
- database contention becomes a significant problem;
- business domains become completely independent.