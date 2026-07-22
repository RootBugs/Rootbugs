# <div align="center">🦞 RootBugs</div>

<div align="center">

![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-5.x-3178C6?style=flat&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4%EF%B8%8F-green.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)

**A modern, full-stack open-source toolkit for building robust applications with Python and TypeScript.**

[Features](#-features) | [Tech Stack](#-tech-stack) | [Project Structure](#-project-structure) | [Getting Started](#-getting-started) | [Contributing](#-contributing) | [License](#-license)

</div>

---

## 📖 Table of Contents

- [About RootBugs](#-about-rootbugs)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Module Overview](#-module-overview)
- [Contributing](#-contributing)
- [Roadmap](#-roadmap)
- [License](#-license)
- [Support](#-support)

---

## 🦠 About RootBugs

**RootBugs** is an open-source, multi-language development toolkit designed for building scalable, production-ready applications. It provides a cohesive set of utilities, services, and patterns spanning **Python** and **TypeScript/JavaScript** — making it ideal for teams working across both ecosystems.

Whether you are building REST APIs, CLI tools, or backend services, RootBugs gives you battle-tested foundations with clean architecture, robust error handling, and extensible design patterns.

> _"Root the bugs. Ship with confidence."_

---

## ✨ Features

| Feature | Description |
|:--------|:------------|
| 🔁 **Retry & Resilience** | Built-in retry mechanisms with configurable backoff for fault-tolerant API calls |
| 🗄️ **Caching Layer** | Lightweight in-memory caching with key-based lookups for performance optimization |
| 🔐 **Auth Utilities** | Input validation and authentication helpers for securing your endpoints |
| 🗃️ **Database Helpers** | Structured logging and database utility functions for data operations |
| 🖥️ **CLI Framework** | Command-line interface scaffolding for building developer tools |
| 📡 **Routing & Server** | Express-style routing and server setup for JavaScript/TypeScript services |
| 📦 **Type Definitions** | First-class TypeScript types for end-to-end type safety |
| 🧩 **Modular Design** | Each module is self-contained — use only what you need |

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology | Purpose |
|:------|:-----------|:--------|
| **Backend** | !Python | Core logic, API handling, database operations |
| **Services** | !TypeScript | Type-safe service layer and configuration |
| **Runtime** | !Node.js | Server execution and JavaScript utilities |
| **Auth** | Custom | Input validation and authentication |
| **License** | MIT | Free for personal and commercial use |

</div>

---

## 📁 Project Structure

```text
rootbugs/
├── 📄 app.py            # Caching utilities and application core
├── 📄 api.py            # API retry and resilience patterns
├── 📄 auth.py           # Authentication and validation helpers
├── 📄 cli.py            # CLI entry point and command handling
├── 📄 config.py         # Application configuration
├── 📄 core.py           # Core engine and settings
├── 📄 db.py             # Database utilities and logging
├── 📄 handlers.py       # Request and event handlers
├── 📄 models.py         # Data models and schemas
├── 📄 utils.py          # Python utility functions
├── 📄 index.js          # JavaScript entry point
├── 📄 index.ts          # TypeScript entry point
├── 📄 router.js         # Express-style routing
├── 📄 server.js         # HTTP server setup
├── 📄 service.ts        # TypeScript service layer
├── 📄 types.ts          # TypeScript type definitions
├── 📄 utils.js          # JavaScript utility functions
├── 📄 LICENSE           # MIT License
└── 📄 README.md         # This file
```

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed on your system:

| Requirement | Minimum Version | Check Command |
|:------------|:----------------|:--------------|
| Python | 3.8+ | `python --version` |
| Node.js | 16+ | `node --version` |
| npm | 8+ | `npm --version` |

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/RootBugs/RootBugs.git

# 2. Navigate to the project directory
cd RootBugs

# 3. Install Python dependencies (if applicable)
pip install -r requirements.txt

# 4. Install Node.js dependencies (if applicable)
npm install
```

### Usage

**Python — Quick Start:**

```python
from api import retry
from app import cached

# Retry a function up to 3 times on failure
result = retry(lambda: fetch_data(), n=3)

# Cache an expensive computation
data = cached("my_key", lambda: expensive_operation())
```

**JavaScript / TypeScript — Quick Start:**

```javascript
const { cfg } = require('./index');

// Use the configuration
console.log(`Server running on port ${cfg.port}`);
```

```typescript
import { cfg } from './index';

// Full type safety with TypeScript
const server = createServer(cfg);
```

---

## 📚 Module Overview

<div align="center">

| Module | Language | Description | Key Export |
|:-------|:---------|:------------|:-----------|
| `app.py` | 🐍 Python | In-memory caching with key-based lookup | `cached(k, fn)` |
| `api.py` | 🐍 Python | Retry wrapper with configurable attempts | `retry(fn, n=3)` |
| `auth.py` | 🐍 Python | Input validation utilities | `validate(d)` |
| `cli.py` | 🐍 Python | CLI entry point | `main()` |
| `config.py` | 🐍 Python | App configuration (port, debug) | `cfg` |
| `core.py` | 🐍 Python | Core engine configuration | `cfg` |
| `db.py` | 🐍 Python | Database utilities and structured logging | `logger` |
| `handlers.py` | 🐍 Python | Request/event handlers | `cfg` |
| `models.py` | 🐍 Python | Data models and schemas | `Handler` |
| `utils.py` | 🐍 Python | General-purpose utilities | `cfg` |
| `index.js` | 🟨 JS | JavaScript entry point | `validate(d)` |
| `index.ts` | 🔷 TS | TypeScript entry point with config | `cfg` |
| `router.js` | 🟨 JS | Express-style routing | `validate(d)` |
| `server.js` | 🟨 JS | HTTP server bootstrap | `validate(d)` |
| `service.ts` | 🔷 TS | TypeScript service layer | `cfg` |
| `types.ts` | 🔷 TS | TypeScript type definitions | `main()` |
| `utils.js` | 🟨 JS | JavaScript utility functions | `retry(fn, n)` |

</div>

---

## 🤝 Contributing

We love contributions! RootBugs is an open-source project and we welcome developers of all skill levels.

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Contribution Guidelines

| Rule | Details |
|:-----|:--------|
| 📝 **Code Style** | Follow PEP 8 for Python, ESLint rules for JS/TS |
| ✅ **Testing** | Add tests for new features |
| 📖 **Documentation** | Update README if adding new modules |
| 🏷️ **Commit Messages** | Use clear, descriptive commit messages |
| 🔍 **Code Review** | All PRs require review before merging |

### Areas We Need Help

- [ ] Writing comprehensive test suites
- [ ] Improving documentation and examples
- [ ] Adding new utility modules
- [ ] Performance optimization
- [ ] Bug reports and fixes

---

## 🗺️ Roadmap

| Phase | Milestone | Status |
|:------|:----------|:-------|
| v0.1 | Core utilities and module scaffolding | ✅ Complete |
| v0.2 | Full API integration and error handling | 🔄 In Progress |
| v0.3 | Comprehensive test coverage | 🔜 Upcoming |
| v0.4 | CLI tool with rich output | 🔜 Upcoming |
| v0.5 | Database abstraction layer | 🔜 Upcoming |
| v1.0 | Production-ready release | 🔜 Upcoming |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

```text
MIT License — Copyright (c) 2026 RootBugs
Free to use, modify, and distribute.
```

---

## 💬 Support

<div align="center">

| Channel | Link |
|:--------|:-----|
| 🐛 **Bug Reports** | [Open an Issue](https://github.com/RootBugs/RootBugs/issues) |
| 💡 **Feature Requests** | [Start a Discussion](https://github.com/RootBugs/RootBugs/discussions) |
| 📧 **Email** | [rootbugs@github.com](mailto:rootbugs@github.com) |
| 🌐 **Website** | [rootbugs.github.io](https://rootbugs.github.io) |

</div>

---

<div align="center">

**Made with ❤️ by [RootBugs](https://github.com/RootBugs)**

⭐ Star this repo if you find it useful!

</div>
