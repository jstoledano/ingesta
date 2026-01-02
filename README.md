# Ingesta
**Instrumento de Gestión de Trayectoria Académica**

A Domain-Driven Design (DDD) implementation for modeling, tracking, and optimizing complex academic paths.

## 1. Project Context
**Ingesta** is a personal academic governance tool designed for students navigating the **UnADM (Universidad Abierta y a Distancia de México)** Software Development Engineering curriculum.

Unlike standard task managers, this system addresses a specific domain complexity: the rigid mathematical structure of the curriculum map ("Mapa Curricular"), where progress is dictated by a Directed Acyclic Graph (DAG) of dependencies and temporal constraints.

## 2. The Business Problem
The UnADM Engineering curriculum presents specific logistical challenges for a student:

* **Rigid Serialization (Prerequisite Chains):**
    Subjects have strict dependencies. For example, *Programación Orientada a Objetos II* cannot be taken without passing *Programación Orientada a Objetos I* (Seriación-15142316). A failure in a prerequisite creates a "critical path" delay that shifts the entire graduation timeline.
* **Modular & Block Constraints:**
    The curriculum is divided into Modules (Basic, Disciplinary, Professional) and semesters. Crucially, within semesters, subjects are often split into **Bloque 1** and **Bloque 2**. A student must optimize their load balancing between these blocks to ensure success.
* **Long-Term Planning:**
    With 8 semesters and complex terminal projects (Proyecto Terminal I & II), manual planning via PDF is error-prone. Students need a system to simulate: *"If I drop 'Cálculo Integral' now, how does that impact my ability to take 'Física' next semester?"*

## 3. The Solution
**Ingesta** serves as an intelligent academic agent. It models the curriculum rules as a pure domain layer, decoupling the academic logic from the user interface or database.

**Core Capabilities:**
* **Graph-Based Validation:** A rule engine that validates enrollment eligibility based on the "Seriación" graph.
* **Block Scheduling:** Logic to handle the specific "Bloque 1 / Bloque 2" temporal constraints found in the UnADM model.
* **Academic Projection:** Calculation of the optimal path to graduation based on current progress.

## 4. Technical Architecture
This project serves as a reference implementation for **Senior Backend & Systems Engineering**, emphasizing:

* **Domain-Driven Design (DDD):** Logic lives in `src/domain`, isolated from frameworks.
* **Hexagonal Architecture (Ports & Adapters):** Strict separation between the core domain, the API (FastAPI), and the persistence layer (PostgreSQL).
* **Reliability & SRE:** Designed for automated deployment and high availability.
    * **Language:** Python 3.11+ (Strict Typing, Pydantic).
    * **Containerization:** Docker (Multi-stage builds).
    * **CI/CD:** GitHub Actions for automated testing and linting.
    * **Infrastructure:** Cloud-native design ready for AWS.

## 5. Setup & Development
*Instructions for local development environment setup, Docker usage, and running tests.*

*(To be added)*