# Ingesta Backend API

This service handles the core business logic for the Academic Management System. It is built using **Python 3.11+**, *
*FastAPI**, and strict **Hexagonal Architecture**.

## 🛠 Tech Stack & Decisions

| Component           | Choice               | Justification                                                                             |
|:--------------------|:---------------------|:------------------------------------------------------------------------------------------|
| **Language**        | Python 3.11+         | Utilizes modern typing features, `typing.Self`, and strict strictness flags.              |
| **Framework**       | FastAPI              | High-performance async I/O, native Pydantic integration, and auto-generated OpenAPI docs. |
| **Architecture**    | Hexagonal            | Decouples Domain logic from the Framework and Database. **No logic in Controllers.**      |
| **Data Validation** | Pydantic V2          | Runtime data validation ensures no corrupt data enters the Domain layer.                  |
| **Persistence**     | PostgreSQL + asyncpg | High-throughput asynchronous database access.                                             |
| **Dependency Inj.** | Manual / Clean       | Explicit dependency injection to facilitate testing and loose coupling.                   |

## 📂 Project Structure

The codebase follows a strict separation of concerns. Do not import `Infrastructure` into `Domain`.

```text
src/
├── domain/           # 🧠 THE BRAIN (Pure Python)
│   ├── models/       # Entities & Value Objects (Rich Behavior)
│   └── ports/        # Interfaces (ABCs) defining I/O expectations
├── application/      # ⚙️ THE ORCHESTRATOR
│   └── use_cases/    # Application specific business rules (Command/Query handlers)
├── infrastructure/   # 🔌 THE PLUGINS
│   ├── adapters/     # Implementations of Domain Ports (e.g., SQLRepository)
│   └── database/     # DB Connection management
└── api/              # 🌐 THE ENTRY POINT
    └── v1/           # FastAPI Routes (Dumb controllers, just delegation)

```

## 🛡️ Development Standards

We enforce strict quality gates to ensure long-term maintainability.

### 1. The "Anti-Django" Pattern

We do not use Active Record patterns.

* ❌ **Bad:** `User.save()` (Mixes logic and persistence).
* ✅ **Good:** `repository.save(user)` (Explicit persistence).

### 2. Typing & Safety

All functions must be strictly typed. We use `mypy` in strict mode.

```python
# All signatures must utilize type hints
def enroll_student(student: Student, subject: Subject) -> Enrollment:
    ...

```

### 3. Testing Strategy

* **Unit Tests:** Target the `Domain` layer. Fast, no I/O, no mocks needed usually.
* **Integration Tests:** Target `Infrastructure` adapters (Dockerized DB).
* **E2E Tests:** Target `API` endpoints.

## 🔧 Setup & Contribution

### Prerequisites

* Python 3.11+
* Docker & Docker Compose

### Running Locally

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server (Hot reload)
uvicorn src.main:app --reload

```

## 🏗 CI/CD Readiness

This project is designed to be deployed via GitHub Actions.

* **Linting:** `ruff`
* **Type Checking:** `mypy`
* **Container:** Multi-stage Dockerfile optimized for size (Distroless approach).


