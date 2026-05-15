### Library Tracker

this is a system for library

### Project Overview
* Inventory Control: Comprehensive cataloging of books with structural real-time status updates (Available/Unavailable).
* Membership Management: Structured registration of subscribers with automated validation of activation timelines.
* Transaction Automation: Dynamic tracking of book loans and returns driven by integrated server-side triggers.
* Analytical Dashboards: Built-in dashboard configuration containing intuitive charts and statistical counters for operational monitoring.

==================================================

##  Technical Stack
* Backend Core: Python (Frappe Framework v15 Architecture)
* Frontend Controller: JavaScript (Frappe Client Scripts Engine) & Desk UI
* Database Layer: MariaDB Relational Engine
* Development Environment: WSL (Ubuntu Linux) deployed on a Windows Host Machine
* Source Management: Git Workflow & GitHub Repositories

==================================================

## Core Architecture & Models (DocTypes)
* Book: Contains records of specific literary materials including details on title, author, genre, and physical state.
* Author:Contains date about author including name, email, phone.
* Library Member: Holds comprehensive individual data profiles, structural settings, and notification endpoints.
* Library Membership: Governs subscription validity records, execution dates, and renewal requirements.
* Book Issue: Directs transactional sequences registering individual checkouts and return validations.

==================================================

## Programmatic Logic & Validations

### 1. Client-Side Scripting (JavaScript Engine)
* Dynamic Link Filtering: Implemented custom JS event handlers on the Book Issue form to filter book choices dynamically, rendering only books with an `Available` state selectable by the operator.
* UI Lifecycle Control: Automated form presentation states, selectively altering visibility of analytical components like the Actual Return Date fields conditionally.

### 2. Server-Side Validations (Python Logic)
* Subscription Enforcement: Python server logic intercepts document saving events to reject Book Issue requests if the designated client does not hold an active, validated `Library Membership`.
* Temporal Sequence Integrity: Implemented logic blocks to prevent chronological layout errors by throwing exceptions if the expected Return Date precedes the creation Issue Date.
* Automated Status Mapping: Connected underlying docstatus submit actions to automated updates, changing the inventory availability flags instantly.

==================================================
 ## Dashboards
* Genre Breakdown Charts: Multi-series charts grouping current book titles dynamically by their configured literary genre classifications.
* Availability Status Donuts: Visual indicators dividing active assets to show immediately the proportion of available versus issued stock.
* Live Operational Number Cards: Embedded operational widgets reporting calculated figures for Total Book Inventories, Active Memberships, and Loans.

