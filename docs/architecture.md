# 🏛️ Cold Storage Manager: System Architecture

---

## 📜 Purpose
Cold Storage Manager is a tool designed to scan, classify, and migrate unused files from active storage to cold storage, optimizing drive wear and space usage for Linux-based servers.

---

## 🛠️ Core Components

| Component | Purpose |
| --------- | ------- |
| Scanner `scanner.py` | Walks file systems and identifies files unused for a configurable number of days |
| CLI `cli.py` | Command-line interface for user interaction, including scanning, status checking, and migration triggers |
| Tests `tests/` | Unit tests to validate functionality and maintain quality |
| CI System `run_tests.py`, `.test.yaml`, cron jobs) | Automated testing, linting, and code quality enforcement |

---

## 🧠 Design Principles
 - Simplicity first: Core file scanning relies on os.walk and metadata inspection for maximum portability.
 - Modularity: Components (scanner, CLI, migration, logging) are isolated to allow future enhancements without heavy coupling.
 - Local-first: All scanning and validation occur on the server without needing constant client-server communication.
 - User Experience Focus: Asynchronous workflows and clear feedback are prioritized to ensure usability even with large datasets.

---

## 📦 System Flow (Current Version)
```plaintext
User runs coldstore scan --> CLI parses options --> Scanner scans target path --> 
Generates list of unused files --> (Future) Move or report files for cold storage
```

---

## 🧩 Future Enhancements (Planned)
 - **Metadata tracking:** Server-maintained file history to improve accuracy without relying solely on filesystem access times.
 - **Cold Storage Migration:** Safe, reversible file movement with minimal user disruption.
 - **Progress Feedback:** CLI feedback (percent complete, files scanned, ETA).
 - **Multithreaded Scanning (optional future):** Parallelize scanning for massive datasets.
 - **Client integration:** Optional client-side hooks for reporting file access or triggering staged uploads.

---

## 📚 References
 - Filesystem standards (Linux EXT4 behavior re: atime updates)
 - Python’s `os`, `time`, `unittest`, and `argparse` libraries
 - PEP 621 (`pyproject.toml` standard)
 - Shell scripting best practices for Makefile and bash scripts

---

# ✨ Final Notes
This architecture is designed to prioritize maintainability, flexibility, and realistic deployment for personal or small server environments. Scalability considerations (e.g., distributed scanning, DB integration) are planned for future versions based on user feedback.

---

# ✅ Next Steps for Docs
Later, I could expand:

 - **cold_storage_flow.md** for full end-to-end flowcharts
 - **config_explanation.md** for YAML config loading rules
 - **development_setup.md** for contributor onboarding