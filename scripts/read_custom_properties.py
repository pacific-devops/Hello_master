import os
import requests

# Get the repository name dynamically from the environment
repo = os.getenv('GITHUB_REPOSITORY')  # This dynamically takes the current repo name

# GitHub API URL to fetch repository custom properties
api_url = f"https://api.github.com/repos/{repo}"

# Authentication headers
headers = {
    "Authorization": f"token {os.getenv('GITHUB_TOKEN')}",
    "Accept": "application/vnd.github.v3+json"
}

# Fetch the repository data from GitHub API
response = requests.get(api_url, headers=headers)
response.raise_for_status()  # Raise an error for bad responses
repository_data = response.json()

# Get custom properties dynamically from the environment variable (semicolon-separated)
custom_properties_input = os.getenv('CUSTOM_PROPERTIES', '')  # Using env from GitHub Actions
custom_properties = custom_properties_input.split(';')

# Loop through the provided custom properties and fetch the values
for prop in custom_properties:
    value = repository_data.get('custom_properties', {}).get(prop)
    if value:
        # Write each custom property to GITHUB_OUTPUT individually
        with open(os.getenv('GITHUB_ENV'), 'a') as github_env:
            github_env.write(f"{prop}={value}\n")
    else:
        print(f"Warning: Custom property '{prop}' not found.")
