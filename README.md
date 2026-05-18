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
* Author:Contains data about author including name, email, phone.
* Book Author Link: a child table used to establish a many-to-many relationship linking multiple authors to a single book record.
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

==================================================
## Reports
* This report automatically tracks library books that haven't been returned past their due date. It calculates the exact number of delayed days and computes a dynamic penalty amount for each member.

# Features
* **Automated Tracking:** Fetches all overdue records directly from the `Book Issue` DocType.
* **Dynamic Calculations:** Computes delayed days based on the current date (`nowdate`).
* **Financial Penalty:** Automatically calculates a penalty of **5 EGP per day** for delays.
====================================================

# Day4
 Phase 1: Core Customizations & Features Delivered

1. **Dynamic UI Control**: Implemented client-side logic to toggle the visibility of the `cover_image` field based on the `in_stock` dropdown status (`Available` / `Unavailable`).
2. **Automated Child Table Link**: Configured a dynamic fetch mechanism within the Book Authors Child Table to automatically retrieve and populate the `primary_author_country` in the parent DocType.
3. **Custom Action Button**: Added a custom toolbar button `Mark Out of Stock` that triggers a whitelisted backend server call to handle item availability shifts.
4. **Server-Side Timeline Logs**: Programmed a Python service method to log automated updates directly into the document's timeline comments whenever a book status changes via the custom button.
5. **Robust Data Validation**: Integrated restrictive server-side validation rules in Python to prevent saving book titles longer than 200 characters or publication years exceeding 1 year into the future.
==========
Phase 2: Role-Based Access Control (RBAC) Implemented

1. **Custom Roles Created**: Established two distinct user roles within the system: `Librarian` and `Library Member`.
2. **Librarian Permissions**: Granted full operational access (`Read`, `Write`, `Create`, and `Delete`) on the `Book` DocType to manage the complete catalog lifestyle.
3. **Library Member Restrictions**: Configured read-only access (`Read` only) for members, effectively stripping away any privileges to alter, create, or delete records.
4. **Adaptive UI Enforcement**: Validated that critical system actions (such as the `Add Book` button, custom `Mark Out of Stock` button, and the form `Save` functions) automatically hide based on the active user profile.

=============    Day4 question   ============

1- Why does refresh need to call this too (toggle_cover_image_display(frm)) in addition to the in_stock field change event?

*-the in_stock event only triggers when a user manually modifies th efield on UI. However, when an already saved document is opened, it,s initial state is loaded directly from the database. Without calling the function inside the refresh hook, the field visibility would not reflect the existing database values. 
              ******************
2- Client-side validation is faster but easily to bypassed. which validations do you put in js, and which in python?

*- Client-side validation (JS)
    Porpose: focuses on convenience and immediate feedback
*- Server-side Validation
    focuses on absolute trust and bulletproof security.    
              ******************
3- Explain when you would reach for (user, doctype, field-level) permissions?

*- DocType permissions.
   It used when we need to define the baselin e golbal actions (CRUD) for an entire module or document type based on a use,s role.
*- Field-Level Permissions.
   We use it when a user permitted to access  a specific DocType, but certain sensitive individual fields withen the document must be hidden or made read-only based on their role.
*- User Permissions.
   It used when users share the same role and DocType access , but they must be restricted to viewing specific records only, dynamically filtered by a value withen a Link field.       