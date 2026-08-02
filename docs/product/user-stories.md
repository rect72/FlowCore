# FlowCore User Stories

**Version:** 1.0  
**Status:** Draft  
**Last Updated:** 2026-08-02

---

# US-001 — User Registration

## Story

As a visitor,
I want to create an account,
so that I can use the FlowCore platform.

## Acceptance Criteria

- User provides a valid email address.
- User provides a strong password.
- A new account is successfully created.
- Password is securely hashed.
- Email verification request is generated.
- User cannot register with an existing email.

---

# US-002 — User Login

## Story

As a registered user,
I want to sign in,
so that I can access my organizations and projects.

## Acceptance Criteria

- User enters valid credentials.
- JWT access token is generated.
- Refresh token is generated.
- Invalid credentials return an error.
- User session is created.

---

# US-003 — Create Organization

## Story

As a registered user,
I want to create an organization,
so that I can manage my business separately from others.

## Acceptance Criteria

- Organization name is required.
- Organization is successfully created.
- Creator becomes the Owner.
- Organization appears in the dashboard.

---

# US-004 — Invite Team Member

## Story

As an organization owner,
I want to invite new members,
so that they can collaborate with me.

## Acceptance Criteria

- Invitation is sent by email.
- Invitation contains a secure token.
- User can accept the invitation.
- Member appears in the organization.

---

# US-005 — Manage Roles

## Story

As an owner,
I want to assign roles,
so that users have different permissions.

## Acceptance Criteria

- Available roles are displayed.
- Role can be changed.
- Permission changes take effect immediately.
- Unauthorized users cannot change roles.

---

# US-006 — Create Project

## Story

As a member,
I want to create a project,
so that I can separate different business processes.

## Acceptance Criteria

- Project name is required.
- Project belongs to an organization.
- Project is visible to authorized members.

---

# US-007 — Create Form

## Story

As a project member,
I want to create a form,
so that customers can submit requests.

## Acceptance Criteria

- Form title is required.
- Form is saved successfully.
- Form belongs to a project.

---

# US-008 — Add Form Fields

## Story

As a project member,
I want to add fields to a form,
so that I can collect the required information.

## Acceptance Criteria

- Different field types are supported.
- Required fields can be configured.
- Field order can be changed.

---

# US-009 — Publish Form

## Story

As a project member,
I want to publish a form,
so that customers can access it.

## Acceptance Criteria

- Public link is generated.
- Published version is stored.
- Draft remains editable.

---

# US-010 — Submit Request

## Story

As a customer,
I want to submit a request,
so that I can contact the company.

## Acceptance Criteria

- Submitted data is validated.
- Request is stored.
- Request appears in CRM.
- Workflow is triggered.

---

# US-011 — View Requests

## Story

As a manager,
I want to view incoming requests,
so that I can process them.

## Acceptance Criteria

- Requests are displayed in chronological order.
- Filtering is available.
- Search is available.

---

# US-012 — Change Request Status

## Story

As a manager,
I want to update the request status,
so that I can track progress.

## Acceptance Criteria

- Status can be changed.
- Status history is stored.
- Changes are visible to authorized users.

---

# US-013 — Assign Request

## Story

As a manager,
I want to assign requests,
so that each request has a responsible employee.

## Acceptance Criteria

- Responsible member can be selected.
- Assignment is saved.
- Assignment history is recorded.

---

# US-014 — Connect Telegram

## Story

As an organization owner,
I want to connect a Telegram bot,
so that I can receive customer requests through Telegram.

## Acceptance Criteria

- Bot token is validated.
- Bot is connected successfully.
- Incoming messages create requests.

---

# US-015 — Connect Google Sheets

## Story

As an organization owner,
I want to connect Google Sheets,
so that requests are automatically synchronized.

## Acceptance Criteria

- Connection is validated.
- New requests create spreadsheet rows.
- Synchronization errors are logged.

---

# US-016 — Receive Notifications

## Story

As a manager,
I want to receive notifications,
so that I never miss important events.

## Acceptance Criteria

- Notifications are delivered.
- Notification type can be configured.
- Failed delivery is logged.

---

# US-017 — View Audit Log

## Story

As an organization owner,
I want to review the audit log,
so that I can monitor important actions.

## Acceptance Criteria

- Important actions are recorded.
- Audit log cannot be modified.
- Events contain timestamps and user information.