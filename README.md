---

## 🏗️ Planned Architecture
The project is currently in its **initial design and core infrastructure phase**. The planned modular structure includes:

```text
open-grc-framework/
├── core/
│   ├── schema_validator.py   # Validates compliance mapping YAML files
│   └── cli_reporter.py       # Generates unified cross-framework coverage reports
├── schemas/                  # Machine-readable JSON/YAML definitions (ISO 27001, NIS2, DORA, GDPR)
├── plugins/                  # Community-contributed extensions & automated evidence collectors
├── templates/                # Standardized ISMS & GRC documentation templates
└── docs/                     # Architecture guides & contributor documentation
```

---

## 🚀 Quick Start & Usage

You can locally validate the compliance mapping schemas and generate a unified coverage report using Python 3.10+.

### 1. Clone & Install Dependencies
```bash
git clone https://github.com
cd open-grc-framework
pip install -r requirements.txt
```

### 2. Validate Compliance Schemas
Run the core validator against any YAML mapping file in the `schemas/` directory:
```bash
python core/schema_validator.py schemas/iso27001-nis2-mapping-sample.yaml
```

### 3. Generate Unified Coverage Report
Scan all mapped frameworks and display a consolidated governance summary:
```bash
python core/cli_reporter.py
```

---

## 🗺️ Roadmap
- [x] **Phase 1: Concept & Core Requirements** — Define primary GRC bottlenecks and cross-mapping logic.
- [x] **Phase 2: Foundational Infrastructure** — Finalize baseline YAML schemas, validation engine, and CI/CD workflows.
- [ ] **Phase 3: Core Engine MVP** — Expand risk scoring logic and modular plugin APIs.
- [ ] **Phase 4: Community Ecosystem** — Scale community-contributed compliance modules and documentation.

---
