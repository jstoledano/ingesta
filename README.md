# Ingesta: High-Availability Academic Management System

> **Architectural POC:** A reference implementation of a Domain-Driven Design (DDD) system focusing on long-term
> maintainability, low operational costs, and cloud-native reliability.

## 📋 Project Overview

**Ingesta** is a monolithic-first, modular system designed to handle the complex lifecycle of academic curriculums and
student enrollments.

Unlike traditional CRUD applications, this project models the **University Domain** using strict **Hexagonal
Architecture**. It is engineered to decouple business rules from infrastructure, allowing the system to evolve
independently of database choices or external frameworks.

### 💼 The Business Problem

Academic institutions require rigid data integrity regarding subject serialization (prerequisites), credit mapping, and
enrollment windows. "Ingesta" solves this by enforcing these invariants in the Domain Layer, not in the database or the
UI.

## 🏗 System Architecture

This repository operates as a **Monorepo**, currently containing:

* **Backend:** Python 3.11+ / FastAPI (Asynchronous, Type-Safe).
* *(Planned) Frontend:* Single Page Application.
* *(Planned) Infrastructure:* IaC for AWS/Oracle Cloud.

### Key Design Principles

1. **Domain-Driven Design (DDD):** The code reflects the language of the business (UBIQUITOUS LANGUAGE), not the
   language of the database.
2. **Hexagonal Architecture (Ports & Adapters):** Core logic is isolated. The Web API and Database are treated as
   interchangeable plugins.
3. **12-Factor App:** Configuration, isolation, and statelessness are strictly enforced for containerized deployment.
4. **Low-Cost / High-Availability:** Designed to run on minimal resources (distroless containers, async I/O) without
   sacrificing throughput.

## 🚀 Quick Start (Local Development)

The project uses Docker Compose to simulate a production-parity environment.

```bash
# Clone the repository
git clone [https://github.com/jstoledano/ingesta.git](https://github.com/jstoledano/ingesta.git)

# Start services
docker-compose up --build