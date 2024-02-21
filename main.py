import requests

response = requests.get("https://gitlab.com/api/v4/users/abdullah-k18/projects")

all_projects = response.json()

for project in all_projects:
    print(f"Project ID: {project['id']}")
    print(f"Project Name: {project['name']}")
    print(f"Project URL: {project['web_url']} ")
    print(f"Date of Creation: {project['created_at']}")
    print("   ")