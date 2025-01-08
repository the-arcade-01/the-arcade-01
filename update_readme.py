import json

# File paths
README_FILE = "README.md"
BLOGS_JSON_FILE = "devto_blogs.json"

# Load the latest blogs
with open(BLOGS_JSON_FILE, "r") as file:
    blogs = json.load(file)

# Get the top 4 blogs
latest_blogs = blogs[:4]

# Generate the markdown list for blogs
blogs_md = "\n".join(
    [f"- [{blog['title']}]({blog['url']})" for blog in latest_blogs]
)

# Update the README.md
with open(README_FILE, "r+") as file:
    content = file.read()
    start_marker = "<!-- BLOGS:START -->"
    end_marker = "<!-- BLOGS:END -->"
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)

    # Replace the blogs section
    if start_idx != -1 and end_idx != -1:
        new_content = (
            content[:start_idx + len(start_marker)]
            + "\n" + blogs_md + "\n"
            + content[end_idx:]
        )
        file.seek(0)
        file.write(new_content)
        file.truncate()
