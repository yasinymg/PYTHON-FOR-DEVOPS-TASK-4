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

def create_directory(directory_name):
    try:
        os.makedirs(directory_name, exist_ok=True)
        print(f"Directory '{directory_name}' created successfully.")
    except Exception as e:
        print(f"Error creating directory '{directory_name}': {e}")

def main():
    # Create company directories
    for directory in company_directories:
        create_directory(directory)

if __name__ == "__main__":
    main()
