import subprocess

# Define the users and their groups
users = {
    "Andrew": "System Administrator",
    "Julius": "Legal",
    "Chizi": "Human Resource Manager",
    "Jeniffer": "Sales Manager",
    "Adeola": "Business Strategist",
    "Bach": "CEO",
    "Gozie": "IT intern",
    "Ogochukwu": "Finance Manager"
}

def create_user(username, group):
    try:
        subprocess.run(["sudo", "groupadd", group], check=True)
        subprocess.run(["sudo", "useradd", "-m", "-G", group, username], check=True)
        print(f"User {username} with group {group} created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating user {username}: {e}")

def main():
    # Create users and assign them to groups
    for username, group in users.items():
        create_user(username, group)

if __name__ == "__main__":
    main()
