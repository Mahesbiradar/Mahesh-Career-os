"""
6. Exercise 6 — Combined backend mini-task

Challenge
15 marks

Create `appointment_checker.py`. Accept an appointment ID in the format `APT-12345` and a timestamp in ISO format with an explicit UTC offset. 
Validate the ID with `re.fullmatch()`, parse the timestamp, convert it to UTC, and determine whether the appointment is in the past or future. 
Handle invalid IDs and timestamps without crashing. Do not compare naive and aware datetimes.

"""

from datetime import datetime,timedelta,timezone

import re


def appointment_checker(appointment_id, timestamp):

    pattern = r"APT-\d{5}"

    match = re.fullmatch(pattern,appointment_id)

    if match is None:

        print(f"The appointment ID: {appointment_id} is Invalid")

        return

    try: 
    
        appointment_time = datetime.fromisoformat(timestamp)

        if appointment_time.tzinfo is None:

            print(f"The timestamp not contains the UTC offset date")

            return

        
    except ValueError as e:

        print(f"Invalide time stamp with error Details: {e}")

        return 


    current_time = datetime.now(timezone.utc)

    utc_convertedtime = appointment_time.astimezone(timezone.utc)

    formated_date = datetime.strftime(utc_convertedtime,"%d %b %Y, %I:%M %p")


    if utc_convertedtime > current_time:

        print(f"The appointment is in future on: {formated_date}")

    else:

        print(f"The appointment is over and it was on: {formated_date}")

    return 



if __name__ == "__main__":

    # --- TEST SUITE ---
    print("--- 1. Valid Future Appointment ---")
    # Offset +05:30 (India Standard Time)
    appointment_checker("APT-12345", "2026-10-20T15:30:00+05:30") 

    print("\n--- 2. Valid Past Appointment ---")
    # 'Z' represents literal UTC / Zulu time
    appointment_checker("APT-99999", "2025-01-01T09:00:00Z") 

    print("\n--- 3. Invalid ID Test ---")
    appointment_checker("APT-123", "2026-10-20T15:30:00+05:30")

    print("\n--- 4. Missing Offset Test (Should be rejected) ---")
    appointment_checker("APT-67890", "2026-10-20T15:30:00")

    print("\n--- 5. Completely Malformed Timestamp Test ---")
    appointment_checker("APT-11111", "Not a date string")







    





