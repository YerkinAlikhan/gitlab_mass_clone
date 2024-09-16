import requests
import os
import subprocess

# Replace with your personal access token and group ID
GITLAB_TOKEN = "YOUR_ACCESS_TOKEN"
GROUP_ID = "YOUR_GROUP_ID"
GITLAB_URL = "https://gitlab.com/api/v4"
CLONE_DIR = "path_to_clone_directory"  # Replace with the path where you want to clone repos

headers = {
    "PRIVATE-TOKEN": GITLAB_TOKEN
}

# Create a directory to store the cloned repositories
if not os.path.exists(CLONE_DIR):
    os.makedirs(CLONE_DIR)

# Fetching all the projects from the group
response = requests.get(f"{GITLAB_URL}/groups/{GROUP_ID}/projects", headers=headers)
projects = response.json()

# Cloning each project
for project in projects:
    repo_url = project["ssh_url_to_repo"]
    repo_name = project["name"]
    clone_path = os.path.join(CLONE_DIR, repo_name)
    
    if not os.path.exists(clone_path):
        print(f"Cloning {repo_name}...")
        subprocess.run(["git", "clone", repo_url, clone_path])
    else:
        print(f"{repo_name} already cloned.")

print("All repositories cloned!")
