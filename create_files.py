import os

# Define the company directories
company_directories = [
    "Finance Budgets",
    "Contract Documents",
    "Business Projections",
    "Business Models",
    "Employee Data",
    "Company Vision and Mission Statement",
    "Server Configuration Script"
]

def create_file_in_directory(file_name, directory_name):
    if directory_name in company_directories:
        try:
            file_path = os.path.join(directory_name, file_name)
            with open(file_path, 'w') as f:
                f.write("")  # Create an empty file
            print(f"File '{file_name}' created in directory '{directory_name}'.")
        except Exception as e:
            print(f"Error creating file '{file_name}' in directory '{directory_name}': {e}")
    else:
        print(f"Directory '{directory_name}' does not exist in company directories. File not created.")

def main():
    # Get user input for file creation
    file_name = input("Enter the name of the file to create: ")
    directory_name = input("Enter the directory to create the file in: ")
    create_file_in_directory(file_name, directory_name)

if __name__ == "__main__":
    main()
