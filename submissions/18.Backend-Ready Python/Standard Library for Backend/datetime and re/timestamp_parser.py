"""
[ ] 5. Exercise 5 — Timestamp parser

Medium
10 marks

Create `timestamp_parser.py`. Accept timestamps in the exact format `YYYY-MM-DD HH:MM:SS`. 
Parse the input, reject invalid dates or times, and display the result in `DD Mon YYYY, HH:MM AM/PM` format. 
Explain whether the input contains time-zone information.

"""

from datetime import datetime,timedelta,timezone


def timestamp_parser(date):

    try:
        extrcated_date = datetime.strptime(date,'%Y-%m-%d %H:%M:%S')

        result = datetime.strftime(extrcated_date,"%d %b %Y, %I:%M %p")

        print(f"The Extracted Date and Time is : {result}")

        return result

    except ValueError as e:

        print(f"Invalid date or format entered! Error details: {e}")

        return None

# Explanation: Since the input string format (YYYY-MM-DD HH:MM:SS) contains no offset (like +05:30 or Z) or region names (like UTC or IST),), Python treats the resulting object as a naive datetime object.



if __name__ == "__main__":

    test1 = timestamp_parser("2026-10-17 14:30:22")

    test2 = timestamp_parser("2026-01-05 09:05:00")

    test3 = timestamp_parser("2026-12-25 00:15:30")

    test4 = timestamp_parser("17-10-2026 14:30:00")




