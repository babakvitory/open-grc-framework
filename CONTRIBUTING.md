# Contributing to Open GRC Framework 🤝

Thank you for your interest in contributing to **Open GRC Framework**! Our goal is to build a collaborative, transparent, and standardized ecosystem where Information Security practitioners, GRC consultants, auditors, and software engineers work together.

---

## 🌟 How You Can Contribute

We welcome contributions across both **GRC Domain Expertise** and **Software Engineering**:

1. **Compliance & Framework Schemas (`schemas/`):**
   * Add machine-readable YAML/JSON control definitions for standards such as **ISO/IEC 27001**, **NIS2**, **DORA**, **GDPR**, **NIST CSF**, or **SOC 2**.
   * Improve cross-standard control mappings and evidence requirement definitions.
2. **Core Engine & Plugins (`core/` & `plugins/`):**
   * Develop parsers, risk scoring algorithms, and validation scripts.
   * Build connectors for automated evidence collection.
3. **Documentation & Templates (`templates/` & `docs/`):**
   * Contribute standardized ISMS policies, risk assessment methodologies, and architecture guides.

---

## 🛠️ Contribution Workflow

1. **Fork the Repository:** Create your own fork of `open-grc-framework`.
2. **Create a Feature Branch:** Use a clear naming convention:
   ```bash
   git checkout -b feat/nis2-control-mapping
   ```
3. **Follow Schema Standards:** Ensure all YAML/JSON files follow the structure defined in `schemas/` with clear `unified_control_id` references.
4. **Submit a Pull Request (PR):** Open a PR against the `main` branch with a clear description of the regulatory/technical changes and references to relevant standards.

---

## 📋 Guidelines for GRC Contributors

* **Accuracy & Citations:** Always cite the exact clause, article, or control ID from the official regulatory or standard text (e.g., `ISO/IEC 27001:2022 Annex A.5.24` or `EU NIS2 Article 21(2)(b)`).
* **Vendor Neutrality:** Keep control descriptions and evidence requirements technology-agnostic unless writing a specific tool plugin.

---

## 💬 Discussions & Issues

Have an idea for a new compliance module or found an inconsistency in a control mapping? Please open an **Issue** to start a discussion with the community!
