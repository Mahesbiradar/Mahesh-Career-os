"""
Create `environment_inspector.py`. Print the current working directory, Python version, interpreter path, platform identifier, and number of logical CPUs. Handle the case where the CPU count is unavailable.

"""

import os
import sys

def inspect_environment():
    """Prints key details about the current system and Python environment."""
    # Gather environment data
    env_info = {
        "Working Directory": os.getcwd(),
        "Python Version": sys.version.split('\n')[0],  # Keeps it to a clean single line
        "Interpreter Path": sys.executable,
        "Platform": sys.platform,
        "CPU Count": os.cpu_count() or "Unavailable" # Clean fallback using 'or'
    }
    
    # Print formatted results
    print("--- Environment Inspection ---")
    for key, value in env_info.items():
        print(f"{key:<18}: {value}")

if __name__ == "__main__":
    inspect_environment()


