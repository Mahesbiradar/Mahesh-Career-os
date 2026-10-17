
""""
[x] Exercise 3 — Command-line report tool

Medium
10 marks

Create `report.py` so that `python report.py daily` prints a message for a daily report and `python report.py monthly` prints a message for a monthly report. If the argument is missing or unsupported, print usage instructions and exit with a nonzero status.

"""

import sys


def print_usage():

    print("Usage: python report.py [daily|monthly]", file=sys.stderr)
    print("Error: Missing or unsupported report type.", file=sys.stderr)


def main():
        
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    report_type = sys.argv[1].lower()

    if report_type == "daily":

        print("Generating daily performance and analytics report...")

    elif report_type == "monthly":

        print("Generating comprehensive monthly financial and operations summary...")

    else:

        print_usage()
        sys.exit(1)


if __name__ == "__main__":

    main()

