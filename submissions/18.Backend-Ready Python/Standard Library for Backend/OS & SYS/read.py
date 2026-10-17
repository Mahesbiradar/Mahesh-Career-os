"""
Create a script that reads `APP_ENV` with a default of `development`, requires `DATABASE_URL`, and creates a `logs` directory if it doesn't exist. If the required configuration is missing, print a useful error and exit with a nonzero status. Never print the database URL itself.

"""

import os
import sys

def initialize_application():


    app_env  = os.getenv("APP_ENV", "development")

    print(f"Starting application in [{app_env}] mode...")

    database_url = os.getenv("DATABASE_URL")

    if not database_url:

        print("CRITICAL ERROR: The required 'DATABASE_URL' environment variable is missing.", file=sys.stderr)

        print("Action Required: Please set 'DATABASE_URL' in your environment or your .env file.", file=sys.stderr)

        sys.exit(1)

    log_dir = "logs"

    try:
        os.makedirs(log_dir, exist_ok=True)
        print(f"Log directory verified at: {os.path.abspath(log_dir)}")
    except Exception as e:
        print(f"CRITICAL ERROR: Failed to create logs directory: {e}", file=sys.stderr)
        sys.exit(1)

    print("Application environment validated successfully.")


    return app_env, database_url


if __name__ == "__main__":
    app_env, db_url = initialize_application()
    


