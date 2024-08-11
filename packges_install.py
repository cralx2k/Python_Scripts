# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 19:44:41 2024

@author: leao2
"""
import os
import shutil
import subprocess

def delete_folders_with_prefix(path, prefix):
    status_msg = ""
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            if name.startswith(prefix):
                try:
                    os.remove(os.path.join(root, name))
                    status_msg += f"Deleted file: {os.path.join(root, name)}\n"
                except Exception as e:
                    status_msg += f"Failed to delete file {os.path.join(root, name)}: {str(e)}\n"
        for name in dirs:
            if name.startswith(prefix):
                try:
                    shutil.rmtree(os.path.join(root, name))
                    status_msg += f"Deleted folder: {os.path.join(root, name)}\n"
                except Exception as e:
                    status_msg += f"Failed to delete folder {os.path.join(root, name)}: {str(e)}\n"
    return status_msg

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return True, result.stdout
        else:
            return False, result.stderr
    except Exception as e:
        return False, str(e)

def main():
    package_name = input("Enter the package name to reinstall: ")

    # Step 1: Delete folders and files starting with ~
    deletion_status = delete_folders_with_prefix("C:\\Python38\\Lib\\site-packages\\", "~")
    print("Deletion Status:\n", deletion_status)

    # Step 2: Uninstall the package
    uninstall_command = f"packman uninstall --name {package_name} --force"
    uninstall_success, uninstall_msg = run_command(uninstall_command)
    if uninstall_success:
        print(f"Package {package_name} uninstalled successfully.")
    else:
        print(f"Failed to uninstall package {package_name}: {uninstall_msg}")

    # Step 3: Install the package
    install_command = f"packman install --name {package_name} --force"
    install_success, install_msg = run_command(install_command)
    if install_success:
        print(f"Package {package_name} installed successfully.")
    else:
        print(f"Failed to install package {package_name}: {install_msg}")

    # Step 4: Show package details
    show_command = f"python -m pip show {package_name}"
    show_success, show_msg = run_command(show_command)
    if show_success:
        print(f"Package details:\n{show_msg}")
    else:
        print(f"Failed to show package details: {show_msg}")

if __name__ == "__main__":
    main()
