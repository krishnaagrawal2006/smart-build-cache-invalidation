
import os
import hashlib

def calculate_hash(filename):
    """Generate SHA-256 hash of a file."""
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        sha256.update(file.read())

    return sha256.hexdigest()


def build_application():
    print("Starting application build...")

    source_hash = calculate_hash("src/main.py")

    os.makedirs(".build-cache", exist_ok=True)

    with open(".build-cache/build-info.txt", "w") as file:
        file.write("Build completed successfully!\n")
        file.write(f"Source Hash: {source_hash}\n")

    print("Build completed successfully!")


if __name__ == "__main__":
    build_application()
