import os
import re
import shutil
import subprocess
import argparse

SETUP_FILE = "setup.py"
DIST_DIR = "dist"


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


def run_tests():
    """Run the tests to ensure everything is working before updating the version."""
    print("Running tests...")
    try:
        subprocess.run(["python3", "-m", "pytest", "-v"], check=True)
        print("✅ All tests passed.")
    except subprocess.CalledProcessError:
        print("❌ Tests failed!")
        raise


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


def clean_dist_directory():
    """Remove all files in the dist/ directory."""
    if os.path.exists(DIST_DIR):
        print(f"Cleaning the {DIST_DIR} directory...")
        shutil.rmtree(DIST_DIR)
    os.makedirs(DIST_DIR)
    print(f"✨ {DIST_DIR} directory is now clean.")


def build_package():
    """Build the source distribution and wheel."""
    print("Building the package...")
    try:
        subprocess.run(["python3", "setup.py", "sdist", "bdist_wheel"], check=True)
        print("📦 Package built successfully.")
    except subprocess.CalledProcessError:
        print("❌ Package build failed!")
        raise


def upload_package():
    """Upload the package to PyPI using twine."""
    print("Uploading the package to PyPI...")
    try:
        subprocess.run(["twine", "upload", f"{DIST_DIR}/*"], check=True)
        print("🚀 Package uploaded successfully to PyPI.")
    except subprocess.CalledProcessError:
        print("❌ Package upload failed!")
        raise


def tag_version_in_git(version):
    """Tag the new version in Git and push the tag."""
    tag = f"v{version}"
    print(f"Tagging the new version: {tag}")
    try:
        # Add and commit version bump
        subprocess.run(["git", "add", SETUP_FILE], check=True)
        subprocess.run(["git", "commit", "-m", f"Bump version to {version}"], check=True)
        
        # Create and push tag
        subprocess.run(["git", "tag", "-a", tag, "-m", f"Version {version}"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        subprocess.run(["git", "push", "origin", tag], check=True)
        print(f"🏷️  Version {version} tagged and pushed to Git.")
    except subprocess.CalledProcessError:
        print("❌ Git operations failed!")
        raise


def main():
    parser = argparse.ArgumentParser(
        description="Update the version, build, and upload the package to PyPI.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
Examples:
  python update_version.py patch
  python update_version.py minor --skip-tests
  python update_version.py major --skip-pypi
  python update_version.py patch --skip-github
        """
    )
    parser.add_argument("part", choices=["major", "minor", "patch"],
                      help="Which part of the version to bump")
    parser.add_argument("--skip-tests", action="store_true",
                      help="Skip running the test suite")
    parser.add_argument("--skip-pypi", action="store_true",
                      help="Skip uploading to PyPI")
    parser.add_argument("--skip-github", action="store_true",
                      help="Skip Git tagging and pushing")
    parser.add_argument("--dry-run", action="store_true",
                      help="Show what would be done without making actual changes")
    
    args = parser.parse_args()

    try:
        # Step 1: Get the current version
        current_version = get_current_version(SETUP_FILE)
        print(f"📎 Current version: {current_version}")

        # Step 2: Calculate new version
        new_version = bump_version(current_version, args.part)
        print(f"🎯 Target version: {new_version}")

        if args.dry_run:
            print("\n🔍 Dry run completed. No changes made.")
            return

        # Step 3: Run tests (unless skipped)
        if not args.skip_tests:
            run_tests()
        else:
            print("⏩ Skipping tests as requested.")

        # Step 4: Update setup.py with the new version
        update_setup_file(SETUP_FILE, new_version)
        print(f"📝 Updated {SETUP_FILE} with version {new_version}")

        # Step 5: Clean and build
        clean_dist_directory()
        build_package()

        # Step 6: Upload to PyPI (unless skipped)
        if not args.skip_pypi:
            upload_package()
        else:
            print("⏩ Skipping PyPI upload as requested.")

        # Step 7: Git operations (unless skipped)
        if not args.skip_github:
            tag_version_in_git(new_version)
        else:
            print("⏩ Skipping Git operations as requested.")

        print(f"\n✅ Version update to {new_version} completed successfully!")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        raise

if __name__ == "__main__":
    main()

# Version Update Options Guide:
# ---------------------------
# 1. Version Parts:
#    - patch: For backwards-compatible bug fixes (1.2.3 -> 1.2.4)
#    - minor: For new features that don't break existing functionality (1.2.3 -> 1.3.0)
#    - major: For changes that break backwards compatibility (1.2.3 -> 2.0.0)
#
# 2. Optional Flags:
#    --skip-tests:   Skip running the test suite before updating (use with caution)
#    --skip-pypi:    Update version locally and on GitHub, but don't publish to PyPI
#    --skip-github:  Update version locally and on PyPI, but don't create Git tags
#    --dry-run:      Preview what would happen without making any actual changes
#
# Examples:
#   python update_version.py patch              # Bump patch version with all checks
#   python update_version.py minor --skip-tests # Add new feature, skip testing
#   python update_version.py major --dry-run    # Preview a major version bump
#   python update_version.py patch --skip-pypi  # Update locally and GitHub only