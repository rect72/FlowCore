# FlowCore Module Architecture

**Version:** 1.0  
**Status:** Draft  
**Last Updated:** 2026-08-03

---

# Purpose

This document describes the business modules of FlowCore.

Each module owns a specific business domain.

Modules communicate only through public application interfaces, domain events, or documented contracts.

Internal implementation details must remain private.

---

# Module Overview

FlowCore consists of the following modules:

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

---

# Identity

## Purpose

Manages authentication, authorization, user accounts, sessions, and security.

## Owns

- Users
- Credentials
- Sessions
- Refresh Tokens
- Roles
- Permissions

## Public Interface

- Register User
- Login User
- Logout User
- Refresh Token
- Verify Email
- Reset Password

## Incoming Dependencies

- Web API
- Organizations

## Outgoing Dependencies

None

---

# Organizations

## Purpose

Manages organizations and memberships.

## Owns

- Organizations
- Members
- Invitations

## Public Interface

- Create Organization
- Invite Member
- Remove Member
- Change Role

## Incoming Dependencies

- Identity

## Outgoing Dependencies

- Notifications
- Audit

---

# Projects

## Purpose

Organizes business processes inside an organization.

## Owns

- Projects

## Public Interface

- Create Project
- Update Project
- Archive Project

## Incoming Dependencies

- Organizations

## Outgoing Dependencies

- Audit

---

# Forms

## Purpose

Provides a dynamic form builder.

## Owns

- Forms
- Form Fields
- Form Versions

## Public Interface

- Create Form
- Publish Form
- Update Form

## Incoming Dependencies

- Projects

## Outgoing Dependencies

- Audit

---

# Submissions

## Purpose

Stores customer requests.

## Owns

- Submissions
- Submission Answers

## Public Interface

- Create Submission
- View Submission
- Update Submission

## Incoming Dependencies

- Forms

## Outgoing Dependencies

- CRM
- Workflows
- Notifications
- Audit

---

# CRM

## Purpose

Manages request processing.

## Owns

- Request Status
- Assignments
- Comments

## Public Interface

- Change Status
- Assign Manager
- Add Comment

## Incoming Dependencies

- Submissions

## Outgoing Dependencies

- Notifications
- Audit

---

# Workflows

## Purpose

Executes business automation.

## Owns

- Workflow Definitions
- Workflow Executions

## Public Interface

- Start Workflow
- Execute Step
- Cancel Workflow

## Incoming Dependencies

- Submissions
- CRM

## Outgoing Dependencies

- Notifications
- Integrations
- Audit

---

# Integrations

## Purpose

Connects FlowCore with external services.

## Owns

- Telegram Bots
- Google Sheets Connections
- Webhooks

## Public Interface

- Connect Telegram
- Connect Google Sheets
- Register Webhook

## Incoming Dependencies

- Workflows

## Outgoing Dependencies

- Telegram API
- Google API
- Webhooks

---

# Notifications

## Purpose

Sends notifications to users.

## Owns

- Notification Templates
- Delivery Queue

## Public Interface

- Send Email
- Send Telegram Message
- Send Notification

## Incoming Dependencies

- CRM
- Workflows
- Organizations

## Outgoing Dependencies

- Email Provider
- Telegram API

---

# Audit

## Purpose

Records important business events.

## Owns

- Audit Events

## Public Interface

- Record Event
- Search Events

## Incoming Dependencies

- Every business module

## Outgoing Dependencies

None

---

# Dependency Rules

The following rules are mandatory.

## Layer Dependencies

```text
Presentation
        ↓
Application
        ↓
Domain
        ↑
Infrastructure
```

The Domain layer must never depend on:

- FastAPI
- SQLAlchemy
- Redis
- Celery
- aiogram
- PostgreSQL
- external APIs

---

## Module Dependencies

```text
Identity
        ↓
Organizations
        ↓
Projects
        ↓
Forms
        ↓
Submissions
        ↓
CRM
        ↓
Workflows
       ↙      ↘
Notifications  Integrations
        ↘      ↙
          Audit
```

---

## General Rules

- Every business entity belongs to exactly one module.
- Modules communicate only through public application services.
- Direct access to another module's infrastructure is prohibited.
- Direct access to another module's database models is prohibited.
- Shared code must not contain business logic.
- Circular dependencies are forbidden.
- Cross-module communication must remain explicit.

---

# Shared Layer

Shared contains only reusable technical components.

Examples:

- Result
- Exceptions
- Common Value Objects
- Base Interfaces
- Utility Functions

Business logic must never be placed inside Shared.

---

# Architecture Principles

FlowCore follows these principles:

- Modular Monolith
- Clean Architecture
- Domain-Driven Design
- SOLID
- API First
- Multi-Tenancy
- Feature-First Structure
- Separation of Concerns

---

# Future Modules

Potential future modules:

- Billing
- Analytics
- Marketplace
- AI Assistant
- Public API
- Plugin System
- White Label
- Reports

These modules are intentionally excluded from the MVP.