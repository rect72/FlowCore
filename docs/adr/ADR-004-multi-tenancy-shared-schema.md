# ADR-004: Use Shared-Database Shared-Schema Multi-Tenancy

**Status:** Accepted  
**Date:** 2026-08-03  
**Decision Owner:** FlowCore Architecture

---

# Context

FlowCore is designed as a Software-as-a-Service (SaaS) platform.

Multiple organizations use the same application.

Each organization represents an independent tenant.

Every tenant owns its own:

- users;
- projects;
- forms;
- submissions;
- CRM records;
- workflows;
- integrations;
- notifications;
- audit logs.

The platform must guarantee complete logical isolation between tenants while remaining simple to deploy and maintain.

---

# Decision

FlowCore uses a **Shared Database, Shared Schema** multi-tenancy model.

All organizations share:

- one PostgreSQL database;
- one database schema;
- one backend application.

Tenant isolation is implemented at the application level.

Every tenant-owned entity contains an `organization_id`.

Example:

```text
organizations
projects.organization_id
forms.organization_id
submissions.organization_id
crm_records.organization_id
workflows.organization_id
audit_logs.organization_id
```

Every query accessing tenant data must include the current `organization_id`.

Example:

```sql
SELECT *
FROM projects
WHERE organization_id = :organization_id
AND id = :project_id;
```

Loading tenant resources only by their primary key is prohibited.

---

# Tenant Context

Every authenticated request resolves:

- user;
- organization;
- membership;
- role;
- permissions.

Example:

```text
TenantContext

user_id

organization_id

membership_id

permissions
```

The tenant context is established during authentication and must be available throughout request processing.

Client-provided organization identifiers are never trusted without authorization.

---

# Authorization Rules

Before accessing tenant-owned resources the application must verify:

1. The user is authenticated.
2. The organization exists.
3. The user belongs to the organization.
4. The user has the required permission.
5. The requested resource belongs to the organization.

Example:

```text
User Request

↓

Authenticate User

↓

Resolve Tenant

↓

Check Membership

↓

Check Permissions

↓

Load Resource

↓

Execute Operation
```

---

# Database Rules

Tenant-owned tables must include `organization_id`.

Indexes should support tenant filtering.

Examples:

```text
INDEX (organization_id)

INDEX (organization_id, created_at)

INDEX (organization_id, status)
```

Tenant-specific uniqueness must include `organization_id`.

Example:

```text
UNIQUE (organization_id, project_slug)

UNIQUE (organization_id, form_name)
```

Referential integrity is enforced using foreign keys.

---

# Cache Rules

Tenant-specific cache entries must include the tenant identifier.

Example:

```text
flowcore:organization:{organization_id}:projects
```

Cache entries belonging to different tenants must never overlap.

Redis is not the source of truth.

---

# File Storage Rules

Uploaded files must be stored using tenant-aware paths.

Example:

```text
organizations/{organization_id}/projects/{project_id}/files/{file_id}
```

Files remain private by default.

Access is granted only after authorization.

---

# Audit Rules

Every important tenant action creates an audit record.

Examples:

- Organization created.
- Member invited.
- Project created.
- Form published.
- Submission received.
- Workflow executed.
- Role changed.

Every audit event includes:

- organization ID;
- actor ID;
- action;
- resource type;
- resource ID;
- timestamp;
- request ID.

Audit records cannot be modified.

---

# Consequences

## Positive

- Simple deployment.
- Low infrastructure cost.
- Easy local development.
- Shared migrations.
- One PostgreSQL instance.
- Efficient resource usage.
- Suitable for MVP and first production release.

## Negative

- Missing tenant filters may expose data.
- Strong testing discipline is required.
- One large database serves every tenant.
- Tenant-specific backup is more difficult.
- Large tenants may affect database performance.

---

# Alternatives Considered

## Database per Tenant

Rejected because:

- infrastructure becomes more expensive;
- migrations become more complex;
- deployment becomes harder;
- local development slows down.

This option may be reconsidered for enterprise customers.

---

## Schema per Tenant

Rejected because:

- schema management becomes difficult;
- migrations are more complicated;
- ORM configuration becomes more complex.

---

## Separate Deployment per Tenant

Rejected because:

- operational cost increases significantly;
- deployment becomes harder;
- monitoring becomes more complicated.

---

# Security Requirements

Tenant isolation is protected by:

- authentication;
- authorization;
- tenant-aware repositories;
- integration tests;
- audit logging;
- code review.

Every API endpoint must validate tenant ownership before accessing tenant data.

Sensitive credentials must always be encrypted.

---

# Testing Requirements

Mandatory integration tests:

- organization A cannot access organization B data;
- organization A cannot modify organization B data;
- organization A cannot delete organization B data;
- guessed identifiers do not bypass authorization;
- tenant filtering works correctly;
- cache keys include tenant identifiers;
- audit records contain the correct organization ID.

---

# Failure Behaviour

If tenant information cannot be resolved:

- the request must fail;
- no data is returned;
- no fallback tenant is selected.

If authorization fails:

- the request is rejected;
- no information about other tenants is disclosed.

If cache data is unavailable:

- PostgreSQL remains the source of truth.

---

# Rules

- Every tenant-owned entity must include organization ownership.
- Every tenant query must include organization filtering.
- Authorization always precedes data access.
- PostgreSQL is the primary source of truth.
- Redis is never authoritative.
- Tenant data must never be mixed.
- Integration tests must verify tenant isolation.

---

# Review Conditions

This decision should be reviewed if:

- enterprise customers require physical isolation;
- legal requirements demand separate databases;
- database size grows beyond acceptable limits;
- deployment architecture changes significantly;
- tenant-specific infrastructure becomes necessary.