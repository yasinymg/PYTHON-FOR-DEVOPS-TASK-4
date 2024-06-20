
# Infrastructure Setup Automation Project

This project automates the setup of infrastructure servers for a small business using Python scripts. It includes scripts to create users, directories, and files based on predefined requirements.

## Project Structure

The project consists of the following scripts:

- **create_users.py**: Creates users and assigns them to respective groups (e.g., System Administrator, Legal, Finance Manager).
- **create_directories.py**: Creates necessary directories for company documents (e.g., Finance Budgets, Contract Documents).
- **create_files.py**: Prompts user input to create files in specified directories from the predefined list.

Additionally, there is a master script `setup_infrastructure.py` that orchestrates the execution of the above scripts in sequence to automate the entire infrastructure setup process.

## Requirements

- Python 3.x
- Operating System with appropriate permissions to create users and directories (Linux/Unix recommended for full functionality due to `sudo` requirements).

## How to Use

1. **Clone the Repository**

   ```sh
   git clone https://git@github.com:yasinymg/PYTHON-FOR-DEVOPS-TASK-4.git
   cd your-repository
   ```

2. **Navigate to Project Directory**

   ```sh
   cd /path/to/your/project/directory
   ```

3. **Run the Setup Script**

   Execute the master script `setup_infrastructure.py` to automate the setup:

   ```sh
   python3 setup_infrastructure.py
   ```

   This script will sequentially create users, directories, and prompt for file creation based on user input.

4. **Interacting with create_files.py**

   - When prompted by `create_files.py`, enter the name of the file you wish to create and the directory name from the predefined list.
   - Ensure the directory name matches exactly with one of the company directories defined in `create_directories.py`.

5. **Verification**

   - After running the setup script, verify the creation of users, directories, and files by checking their presence in the specified locations.

## Directory Structure

```
/path/to/your/repository/
├── create_users.py
├── create_directories.py
├── create_files.py
└── setup_infrastructure.py
```

## Notes

- **Error Handling**: Each script includes basic error handling to manage potential issues during user creation, directory creation, and file creation processes.
- **Permission Requirements**: Ensure appropriate permissions are granted to execute scripts that create users and directories.
- **Modification**: You can modify user names, group assignments, directory names, and add/remove file creation prompts as per specific business requirements.

