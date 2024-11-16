# Environment Variable Printer
# Write a script that accepts a list of environment variable names from the user and prints their values. If an environment variable is not set, the script should notify the user.


import os

def print_env_vars(env_names):
    """
    Prints the values of a list of environment variables, 
    notifying the user if a variable is not set. 
    """
    for env_name in env_names:
        value = os.environ.get(env_name)
        if value:
            print(f"{env_name}: {value}")
        else:
            print(f"Warning: Environment variable '{env_name}' is not set.")

if __name__ == "__main__":
    print("Enter a list of environment variable names (comma-separated): ")
    env_list = input().split(",")
    print_env_vars(env_list)