
import os
import hashlib

SOURCE_FILE = "src/main.py"
CACHE_DIR = ".build-cache"
BUILD_INFO = os.path.join(CACHE_DIR, "build-info.txt")


def calculate_hash(filename):
    """Generate SHA-256 hash of the source file."""
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        sha256.update(file.read())

    return sha256.hexdigest()


def build_application():
    print("Checking build cache after source code update...")
    current_hash = calculate_hash(SOURCE_FILE)

    # Check whether a valid build already exists
    if os.path.exists(BUILD_INFO):
        with open(BUILD_INFO, "r") as file:
            cached_hash = file.read().strip()

        if cached_hash == current_hash:
            print("CACHE HIT: Existing build is valid.")
            print("Skipping unnecessary rebuild.")
            return

        print("CACHE INVALID: Source code has changed.")

    else:
        print("CACHE MISS: No previous build found.")

    # Create a fresh build
    os.makedirs(CACHE_DIR, exist_ok=True)

    with open(BUILD_INFO, "w") as file:
        file.write(current_hash)

    print("BUILD SUCCESSFUL!")
    print("New build cache created.")


if __name__ == "__main__":
    build_application()

