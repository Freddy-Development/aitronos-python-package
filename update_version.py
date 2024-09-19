import re
import subprocess
import argparse

SETUP_FILE = "setup.py"

def get_current_version(setup_file):
    """Extract the current version number from setup.py."""
    with open(setup_file, "r") as file:
        content = file.read()

    # Use regex to find the version number in setup.py
    version_match = re.search(r'version=["\'](\d+\.\d+\.\d+)["\']', content)
    if version_match:
        return version_match.group(1)
    else:
        raise ValueError("Version number not found in setup.py")


def bump_version(version, part):
    """Bump the version number."""
    major, minor, patch = map(int, version.split("."))

    if part == "major":
        major += 1
        minor = 0
        patch = 0
    elif part == "minor":
        minor += 1
        patch = 0
    elif part == "patch":
        patch += 1
    else:
        raise ValueError("Invalid part to bump. Choose 'major', 'minor', or 'patch'.")

    return f"{major}.{minor}.{patch}"


def update_setup_file(setup_file, new_version):
    """Update the version in setup.py."""
    with open(setup_file, "r") as file:
        content = file.read()

    # Replace the version number in setup.py
    updated_content = re.sub(
        r'version=["\'](\d+\.\d+\.\d+)["\']',
        f'version="{new_version}"',
        content
    )

    with open(setup_file, "w") as file:
        file.write(updated_content)


def build_package():
    """Build the source distribution and wheel."""
    print("Building the package...")
    subprocess.run(["python3", "setup.py", "sdist", "bdist_wheel"], check=True)
    print("Package built successfully.")


def upload_package():
    """Upload the package to PyPI using twine."""
    print("Uploading the package to PyPI...")
    subprocess.run(["twine", "upload", "dist/*"], check=True)
    print("Package uploaded successfully.")


def tag_version_in_git(version):
    """Tag the new version in Git and push the tag."""
    tag = f"v{version}"
    print(f"Tagging the new version: {tag}")
    subprocess.run(["git", "tag", tag], check=True)
    subprocess.run(["git", "push", "origin", tag], check=True)
    print(f"New version {version} tagged and pushed to Git.")


def main():
    parser = argparse.ArgumentParser(description="Update the version, build, and upload the package to PyPI.")
    parser.add_argument("part", choices=["major", "minor", "patch"], help="Which part of the version to bump.")
    args = parser.parse_args()

    # Step 1: Get the current version
    current_version = get_current_version(SETUP_FILE)
    print(f"Current version: {current_version}")

    # Step 2: Bump the version
    new_version = bump_version(current_version, args.part)
    print(f"New version: {new_version}")

    # Step 3: Update setup.py with the new version
    update_setup_file(SETUP_FILE, new_version)
    print(f"Updated {SETUP_FILE} with version {new_version}")

    # Step 4: Build the package
    build_package()

    # Step 5: Upload the package to PyPI
    upload_package()

    # Step 6: (Optional) Tag the new version in Git
    # tag_version_in_git(new_version) # skip for now, not ready yeet


if __name__ == "__main__":
    main()


# how to use

# python3 update_version.py patch   # Increment the patch version
# python3 update_version.py minor   # Increment the minor version
# python3 update_version.py major   # Increment the major version