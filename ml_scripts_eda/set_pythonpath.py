import os
import subprocess
import sys


def set_pythonpath():
    current_folder = os.getcwd()
    poetry_env_info = subprocess.run(
        ["poetry", "env", "info", "-p"], capture_output=True, text=True
    )
    site_packages_folder = os.path.join(
        poetry_env_info.stdout.strip(),
        "lib",
        f"python{sys.version_info.major}.{sys.version_info.minor}",
        "site-packages",
    )
    pth_file_path = os.path.join(site_packages_folder, "project_dir.pth")
    with open(pth_file_path, "w") as pth_file:
        pth_file.write(current_folder + "\n")
    print(f"Added {current_folder} to PYTHONPATH in {pth_file_path}")


if __name__ == "__main__":
    set_pythonpath()
