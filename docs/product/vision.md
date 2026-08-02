# FlowCore Product Vision

**Version:** 1.0  
**Status:** Draft  
**Author:** rect72  
**Last Updated:** 2026-08-02

---

# 1. Overview

FlowCore is an open-source low-code platform that helps small and medium-sized businesses automate customer request processing, internal workflows, and team collaboration without writing code.

The platform provides dynamic forms, project management, CRM, Telegram integration, Google Sheets synchronization, workflow automation, and a REST API within a single system.

---

# 2. Problem

Many small businesses manage customer requests through multiple disconnected channels such as Telegram, Google Forms, Excel spreadsheets, email, and messengers.

This causes several problems:

- customer requests are lost;
- information is duplicated;
- managers process requests manually;
- there is no centralized CRM;
- automation is difficult or impossible;
- business processes depend on human actions.

FlowCore solves these problems by providing a unified platform for collecting, processing, and automating customer requests.

---

# 3. Target Users

Primary audience:

- Small businesses
- Service companies
- Marketing agencies
- Online schools
- Healthcare clinics
- Beauty salons
- Automotive workshops
- Fitness centers

User roles:

- Organization Owner
- Administrator
- Manager
- External Customer

---

# 4. Product Value

FlowCore enables organizations to:

- build business workflows without coding;
- collect requests through customizable forms;
- manage requests in a built-in CRM;
- automate repetitive business processes;
- integrate Telegram bots;
- synchronize data with Google Sheets;
- monitor activities through audit logs.

---

# 5. Core User Journey

A typical workflow:

1. User creates an account.
2. User creates an organization.
3. User creates a project.
4. User designs a form.
5. User publishes the form.
6. Customer submits a request.
7. Request appears inside CRM.
8. Manager processes the request.
9. Workflow automation is triggered.
10. Notifications are sent.
11. Data is synchronized with external services.

---

# 6. Minimum Viable Product (MVP)

The first version includes:

- User authentication
- Organizations
- Role-based access control
- Projects
- Dynamic forms
- Public form pages
- CRM
- Request management
- Telegram integration
- Google Sheets integration
- Basic workflow engine
- Audit log
- REST API
- Swagger documentation
- Docker deployment

---

# 7. Out of Scope

The first version will NOT include:

- Billing
- Payment processing
- Mobile applications
- AI-powered automation
- Marketplace
- White-label support
- Kubernetes
- Microservices
- Multi-language interface
- Plugin system

---

# 8. Success Criteria

The MVP is considered successful if:

- users can complete the entire workflow from registration to request processing;
- organizations are fully isolated (multi-tenancy);
- the system is deployable with Docker;
- REST API is documented with Swagger;
- automated tests are passing;
- documentation is complete.

---

# 9. Risks

Potential risks include:

- scope expansion;
- security vulnerabilities;
- incorrect tenant isolation;
- integration failures;
- insufficient testing;
- performance bottlenecks;
- incomplete documentation.

---

# 10. Long-Term Vision

Future versions may include:

- AI assistants
- Marketplace
- Billing
- Mobile applications
- Public API SDK
- Webhooks
- Advanced workflow designer
- Analytics dashboards
- White-label support
- Enterprise features