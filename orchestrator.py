# Import required libraries
from git import Repo
import os
import sys
import shutil
import git
import zipfile
import subprocess
import json
import zipfile
import requests

# GitHub repository URL
repo_url = "https://github.com/johnpapa/node-hello"

# Destination directory where the repository will be cloned
destination_dir = "./node-hello"  # Change this to your desired destination directory

# Path to your package.json file
package_json_path = "./node-hello/package.json"  # Update this path to match your project

repository_name = "johnpapa/node-hello"

readme_url = "https://raw.githubusercontent.com/BoazHalter/DevOps-Candidate-Test/main/README.md"


# Function to download README.md from a given URL
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


# Function to zip a folder
def zipFolder():
    try:
        # Zip the app folder
        app_folder = destination_dir
        zip_filename = f"app-{new_version}.zip"
        zip_path = os.path.join(destination_dir, zip_filename)
        shutil.make_archive(app_folder, 'zip', app_folder)
        os.rename(f"{app_folder}.zip", zip_filename)
        print(f"Node.js app folder zipped as {zip_filename}")
    except Exception as e:
        print(f"Failed to ZIP App Folder: {e}")


# Function to update the version in package.json file
def update_node_version(package_json_path, new_version):
    try:
        with open(package_json_path, 'r') as file:
            data = json.load(file)
            # Update the version in package.json
            data['version'] = new_version

        with open(package_json_path, 'w') as file:
            # Write the updated JSON back to the file
            json.dump(data, file, indent=2)
        print(f"Updated version to {new_version} in {package_json_path}")
    except Exception as e:
        print(f"Failed to update version: {e}")


# Function to clone a repository
def clone_repository(url, dest_dir):
    try:
        # Clone the repository
        Repo.clone_from(url, dest_dir)
        print("Repository cloned successfully.")
    except Exception as e:
        print(f"Failed to clone the repository: {e}")


if __name__ == "__main__":
    # Get the new version number from the argument or environment variable
    if len(sys.argv) > 1:
        new_version = sys.argv[1]
    else:
        new_version = os.environ.get("APP_VERSION")

    # Check if the version number is provided
    if not new_version:
        print("Please provide a version number.")
    else:
        try:
            # Clone the repository
            clone_repository(repo_url, destination_dir)
            # Update the version in package.json
            update_node_version(package_json_path, new_version)
            # Download README.md file
            download_readme(readme_url)
            # Zip the app folder
            zipFolder()
        except Exception as e:
            print(f"Failed at: {e}")
