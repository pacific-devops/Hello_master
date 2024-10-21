"""
This script fetches and processes custom properties from a GitHub repository.
"""

import os
import requests

if __name__ == "__main__":
    def main():
        """Main function to fetch and process custom properties."""

        # Fetch environment variables
        github_token = os.getenv("GITHUB_TOKEN")
        repo_name = os.getenv("GITHUB_REPOSITORY")
        custom_properties_input = os.getenv("CUSTOM_PROPERTIES", '')

        error_code = 0
        results = {}

        if not github_token or not repo_name or not custom_properties_input:
            print("ERROR: Missing required environment variables")
            error_code = 100
        else:
            # GitHub API URL for the repository's custom properties
            api_url = f"https://api.github.com/repos/{repo_name}"

            # Set the headers for authentication
            headers = {
                "Authorization": f"token {github_token}",
                "Accept": "application/vnd.github.v3+json",
            }

            try:
                # Fetch the repository data using the GitHub API
                response = requests.get(api_url, headers=headers, timeout=20)
                response.raise_for_status()

                # Parse the repository data
                repo_data = response.json()

                # Loop through the provided custom properties and fetch the values
                custom_properties = custom_properties_input.split(';')
                for prop in custom_properties:
                    value = repo_data.get("custom_properties", {}).get(prop, None)
                    if value:
                        results[prop] = value
                    else:
                        print(f"Warning: Custom property '{prop}' not found.")
                        error_code = 102

            except requests.exceptions.RequestException as e:
                print(f"ERROR: Failed to fetch repository details: {e}")
                error_code = 101

        # Write the output to GITHUB_ENV for GitHub Actions
        with open(os.environ["GITHUB_ENV"], "a", encoding="utf-8") as fh:
            fh.write(f"py_custom_prop_error_code={error_code}\n")
            for prop, value in results.items():
                fh.write(f"{prop}={value}\n")

    main()
