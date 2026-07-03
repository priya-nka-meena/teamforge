
# TeamForge

### Intelligent Team Formation Platform

A web application that intelligently forms balanced student teams using graph-based compatibility scoring and greedy optimization instead of random grouping.

---

## Overview

Explain

* the problem
* why existing manual team formation is inefficient
* how TeamForge solves it
* why compatibility-based grouping creates better teams

---

## Features

Include every implemented feature.

Examples

* User Registration
* OTP Email Verification
* Login & Authentication
* Student Profile Management
* Skill & Interest Matching
* Intelligent Team Formation
* Graph Visualization
* Partner Recommendations
* Team Invitations
* Invitation Approval/Rejection
* Responsive UI

---

## Tech Stack

Backend

* Django
* Python

Frontend

* HTML
* CSS
* Bootstrap
* JavaScript

Database

* SQLite

Algorithms

* Weighted Compatibility Graph
* Greedy Team Formation Algorithm

Visualization

* Network Graph

---

## Project Architecture

Create a professional architecture diagram using Mermaid.

Example

```mermaid
flowchart TD

User --> Authentication

Authentication --> Profile

Profile --> Matching Engine

Matching Engine --> Compatibility Graph

Compatibility Graph --> Greedy Team Formation

Greedy Team Formation --> Team Recommendations

Recommendations --> Invitation System

Invitation System --> Dashboard
```

---

## Matching Engine Architecture

Explain every stage.

### Step 1

Profile Collection

↓

### Step 2

Weighted Compatibility Score

Uses

* Skills
* Interests
* Branch Diversity
* Academic Year

↓

### Step 3

Weighted Graph Construction

↓

### Step 4

Greedy Team Formation

↓

### Step 5

Recommendations

---

## Compatibility Formula

Explain mathematically.

Example

Compatibility Score =
(2 × Shared Skills)
+
(1.5 × Shared Interests)
+
Branch Bonus
+
Year Bonus

Explain why each weight exists.

---

## Team Formation Algorithm

Explain the complete greedy algorithm step-by-step.

Example

1. Collect all student profiles.

2. Compute compatibility score for every pair.

3. Build weighted graph.

4. Select an unassigned student.

5. Create a new team.

6. Repeatedly add the student with the highest average compatibility.

7. Stop when

* team size reaches MAX_TEAM_SIZE

OR

* no beneficial candidate exists.

8. Repeat until every student belongs to exactly one team.

Include Algorithm Complexity.

Time Complexity

Space Complexity

---

## Why Greedy instead of DSU

Create a comparison table.

Columns

Old DSU

Current Greedy Algorithm

Compare

* Optimization
* Team Quality
* Flexibility
* Uses Edge Weights
* Diversity Support
* Recommendation Quality

Explain why the new algorithm is superior for intelligent team formation.

---

## Folder Structure

Show the project structure.

Example

```
TeamForge/
│
├── accounts/
├── matching/
├── templates/
├── static/
├── TeamForge/
├── manage.py
└── README.md
```

---

## Screenshots

Create placeholders for

* Home
* Login
* Registration
* Dashboard
* Profile
* Team Recommendations
* Team Formation
* Graph Visualization
* Invitations

Leave image markdown placeholders.

Example

```markdown
![Dashboard](screenshots/dashboard.png)
```

---

## Installation

Provide complete setup instructions.

Clone

Create Virtual Environment

Install Requirements

Run Migrations

Run Server

---

## Future Enhancements

Examples

* AI-powered matching
* Personality compatibility
* Skill level weighting
* Multi-college support
* Real-time chat
* Team analytics
* Faculty dashboard
* Cloud deployment
* PostgreSQL support

---

## Author

Include

Name

GitHub

LinkedIn placeholders

---

## License

MIT License

-