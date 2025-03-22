# 📚 DocUnify Sample Project

This is a demo project created as part of my **GSoC 2025 proposal** for the [OSIPI documentation unification project](https://github.com/OSIPI). The goal is to standardize Markdown documentation across different OSIPI projects and present it through a unified, searchable HTML site using [MkDocs](https://www.mkdocs.org/).

---

## 🚀 Project Goals

- 📄 Parse and clean multiple Markdown files with inconsistent formatting
- 🐍 Use Python to:
  - Standardize heading levels and casing
  - Add consistent frontmatter (like titles)
  - Prepare content for static site generation
- 🌐 Use MkDocs to build a clean and navigable documentation site

---

## 🧠 Why This Project?

OSIPI has documentation across many repositories, each with its own style and structure. This prototype demonstrates a possible approach to unify and present these docs in a professional and scalable way.

---

## 🛠️ Features

- `scripts/unify_docs.py` – Python script to standardize Markdown formatting
- `docs/` – Example Markdown files (before and after cleanup)
- `index.md` – Home page content for the documentation site
- `mkdocs.yml` – Configuration file for building the HTML site with MkDocs

---

## 📁 Project Structure

```
docunify-sample/
│
├── docs/                    # Sample Markdown files
│   ├── project1_intro.md
│   ├── project2_usage.md
│   └── project3_api.md
│
├── scripts/
│   └── unify_docs.py        # Main Python formatting script
│
├── mkdocs.yml               # MkDocs configuration file
├── index.md                 # Site landing page
└── README.md                # This file
```

---

## 🧪 How to Run

### 1. Install MkDocs (requires Python)
```bash
pip install mkdocs
```

### 2. Run the formatting script
```bash
cd scripts
python unify_docs.py
```

### 3. Start MkDocs server
```bash
cd ..
mkdocs serve
```

Open your browser and visit:  
👉 `http://127.0.0.1:8000`

---

## 📌 GSoC Context

This project is a prototype for my application to GSoC 2025 under OSIPI. It shows my understanding of the need for standardized documentation workflows and my ability to build tools that support that goal.

The approach can be extended to multiple repos and automated via CI/CD and GitHub Pages in future iterations.

---

## ✅ License

MIT — Free to use, modify, and build upon.
