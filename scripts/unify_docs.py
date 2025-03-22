import os
import re

DOCS_DIR = "../docs"

def standardize_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Capitalize all heading text
    content = re.sub(r'^(#+)\s+(.*)', lambda m: f"{m.group(1)} {m.group(2).capitalize()}", content, flags=re.M)

    # Add frontmatter metadata if not present
    if not content.startswith("---"):
        title = os.path.basename(file_path).replace(".md", "").replace("_", " ").capitalize()
        frontmatter = f"---\ntitle: {title}\n---\n\n"
        content = frontmatter + content

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    for filename in os.listdir(DOCS_DIR):
        if filename.endswith(".md"):
            file_path = os.path.join(DOCS_DIR, filename)
            standardize_markdown(file_path)
            print(f"Standardized: {filename}")

if __name__ == "__main__":
    main()
