# ADR-002: Use PostgreSQL as the Primary Database

**Status:** Accepted  
**Date:** 2026-08-03  
**Decision Owner:** FlowCore Architecture

---

# Context

FlowCore stores all critical business data, including:

- users;
- organizations;
- memberships;
- roles and permissions;
- projects;
- forms;
- form versions;
- submissions;
- CRM records;
- workflows;
- integrations;
- notifications;
- audit events.

The platform requires:

- ACID transactions;
- relational integrity;
- foreign keys;
- indexes;
- concurrent access;
- schema migrations;
- backup and recovery;
- tenant-aware queries.

Business data must remain reliable even if external integrations fail.

---

# Decision

PostgreSQL will be used as the primary database and the single source of truth.

The persistence stack consists of:

```text
PostgreSQL
SQLAlchemy 2
Alembic
asyncpg
```

Redis will not store permanent business data.

Redis will only be used for:

- Celery message broker;
- cache;
- rate limiting;
- temporary locks;
- short-lived coordination data.

Google Sheets, Telegram, and other integrations store only synchronized copies or temporary information.

SQLite is allowed only for experiments and prototypes, never for production.

---

# Data Ownership

Every business entity has one owning module.

Examples:

- Identity owns users.
- Organizations owns organizations and memberships.
- Projects owns projects.
- Forms owns forms.
- Submissions owns customer requests.
- CRM owns request processing.
- Audit owns audit records.

Every tenant-owned record must be associated with an organization.

---

# Transaction Rules

One business operation equals one database transaction.

Example:

```text
Create Submission

↓

Save Answers

↓

Create Audit Event

↓

Create Outbox Event

↓

Commit Transaction
```

External operations must never run inside the database transaction.

This includes:

- Telegram API;
- Google Sheets;
- Email Provider;
- Webhooks.

These operations execute asynchronously after the transaction commits.

---

# Migration Rules

Database schema changes are managed only through Alembic.

Every migration must:

- have a descriptive name;
- include upgrade logic;
- include downgrade logic where possible;
- be committed to Git;
- be reviewed before merging;
- avoid data loss.

Manual production schema changes are prohibited.

---

# Consequences

## Positive

- Reliable transactions.
- Strong data consistency.
- Mature relational database.
- Excellent Python ecosystem.
- Powerful indexing.
- JSONB support.
- Easy backup and recovery.
- Suitable for multi-tenant architecture.

## Negative

- Requires a dedicated database server.
- Schema evolution requires migration discipline.
- Incorrect tenant filtering may expose data.
- Database performance must be monitored.

---

# Alternatives Considered

## SQLite

Rejected because:

- limited concurrency;
- different behaviour from PostgreSQL;
- unsuitable for production workloads.

---

## MongoDB

Rejected because FlowCore data is highly relational.

Using a document database would move relational integrity into application code.

---

## MySQL

Technically suitable.

PostgreSQL was selected because of:

- JSONB;
- advanced indexing;
- richer SQL features;
- better support for complex queries.

---

## Redis as Primary Storage

Rejected.

Redis is designed for temporary data and messaging, not long-term business storage.

---

# Failure Behaviour

If PostgreSQL becomes unavailable:

- readiness checks fail;
- write operations stop;
- Redis is not used as a fallback database;
- business data is never silently discarded;
- monitoring reports the failure.

---

# Backup Strategy

Production environments must include:

- automatic backups;
- encrypted backup storage;
- documented retention policy;
- periodic restore testing;
- monitoring of backup jobs;
- documented disaster recovery procedure.

---

# Rules

- PostgreSQL is always the source of truth.
- Every schema change uses Alembic.
- Every persistent entity belongs to one business module.
- Tenant data must always be isolated.
- Redis must never contain authoritative business data.
- External systems must never replace PostgreSQL.

---

# Review Conditions

This decision should be reviewed if:

- enterprise customers require isolated databases;
- legal requirements demand physical data separation;
- database size exceeds acceptable limits;
- multiple PostgreSQL clusters become necessary;
- the deployment architecture changes significantly.