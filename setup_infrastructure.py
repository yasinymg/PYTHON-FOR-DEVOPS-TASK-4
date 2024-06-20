import subprocess

def run_script(script_name):
    try:
        subprocess.run(["python3", script_name], check=True)
        print(f"{script_name} executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing {script_name}: {e}")

def main():
    # List of scripts to run
    scripts = ["create_users.py", "create_directories.py", "create_files.py"]
    
    # Run each script
    for script in scripts:
        run_script(script)

if __name__ == "__main__":
    main()
