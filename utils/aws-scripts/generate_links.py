import os
import glob

# Read the contents of the README.md file
with open("README.md", "r") as f:
    readme_contents = f.read()

# Generate the links for each script
for file_path in glob.glob("describe/*.py"):
    script_name = os.path.basename(file_path)[:-3]
    link = f"\n[{script_name}](./docs/{script_name}.md)"
    if link not in readme_contents:
        with open("README.md", "a") as f:
            f.write(link)
    f.close()