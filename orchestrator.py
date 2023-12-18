import os
import sys
import requests
import shutil
import zipfile
from github import Github

def download_readme(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open("README.md", "wb") as file:
                file.write(response.content)
            print("README.md downloaded successfully.")
        else:
            print(f"Failed to download README.md: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while downloading README.md: {str(e)}")

def update_node_app_version(repo, new_version):
    try:
        # Clone the repository
        repo_path = "/path/to/local/repo"  # Replace this with your desired local path
        cloned_repo = repo.clone_to(repo_path)

        # Navigate to the app directory
        app_directory = os.path.join(repo_path, "node-hello")
        os.chdir(app_directory)

        # Update package.json with the new version
        with open("package.json", "r") as file:
            data = file.read()
            data = data.replace('"version": "1.0.0"', f'"version": "{new_version}"')

        with open("package.json", "w") as file:
            file.write(data)

        # Commit changes
        cloned_repo.index.add(["package.json"])
        cloned_repo.index.commit(f"Bump version to {new_version}")

        # Push changes to the repository
        cloned_repo.remote().push()

        print(f"Node.js app version updated to {new_version} successfully.")

        # Zip the app folder
        app_folder = os.path.join(repo_path, "node-hello")
        zip_filename = f"app-{new_version}.zip"
        zip_path = os.path.join(repo_path, zip_filename)
        shutil.make_archive(app_folder, 'zip', app_folder)
        os.rename(f"{app_folder}.zip", zip_path)
        print(f"Node.js app folder zipped as {zip_filename}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    github_access_token = "YOUR_GITHUB_ACCESS_TOKEN"
    repository_name = "johnpapa/node-hello"
    readme_url = "https://raw.githubusercontent.com/BoazHalter/DevOps-Candidate-Test/main/README.md"

    # Download README.md file
    download_readme(readme_url)

    # Get the new version number from the argument or environment variable
    if len(sys.argv) > 1:
        new_version_number = sys.argv[1]
    else:
        new_version_number = os.environ.get("APP_VERSION")

    # Check if the version number is provided
    if not new_version_number:
        print("Please provide a version number.")
    else:
        # Authenticate with GitHub using an access token
        g = Github(github_access_token)
        
        # Get the repository
        repo = g.get_repo(repository_name)

        # Call function to update the Node.js app version
        update_node_app_version(repo, new_version_number)
