



import os


def export_dir():

    target_dir  = 'exports/2026/october'

    root_dir = 'exports'

    os.makedirs(target_dir, exist_ok=True)

    print(f"Directory tree '{target_dir}' verified/created.")

    if os.path.exists(root_dir):

        entries = os.listdir(root_dir)

        print(f"\nEntries inside '{root_dir}': {entries}")

    else:

        print(f"\nRoot directory '{root_dir}' is empty or does not exist yet.")

    exists = os.path.exists(target_dir)
    is_directory = os.path.isdir(target_dir)

    print(f"\nValidation Checks for '{target_dir}':")
    print(f"  - Path exists?      : {exists}")
    print(f"  - Is a directory?   : {is_directory}")


if __name__ == "__main__":

    export_dir()


    


