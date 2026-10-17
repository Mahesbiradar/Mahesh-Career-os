"""
[ ] 2. Exercise 2 — Task deadline tracker

Medium
10 marks

Create `deadline_tracker.py`. Generate a timezone-aware UTC timestamp for a task's creation, set its deadline to 48 hours later, 
and determine whether it is overdue using the current UTC time. Print timestamps in ISO format and calculate the elapsed duration in total seconds

"""

from datetime import datetime,timezone,timedelta


def create_task(activity_id):

    """
    Generates a timezone-aware UTC timestamp for a task's creation
    and sets its deadline to 48 hours later.
    """

    activity_start = datetime.now(timezone.utc)

    due_time = activity_start + timedelta(hours=48)

    return activity_id ,activity_start, due_time


def check_validity(activity_start,due_time):

    """
    Determines whether a task is overdue using the current UTC time.
    Prints timestamps in ISO format and calculates elapsed duration in total seconds.
    """

    current_time = datetime.now(timezone.utc)

    is_overdue = current_time > due_time

    if is_overdue:
        print("Task status: OVERDUE")
    else:
        print("Task status: ON TIME")

    elapsed_seconds  = (current_time - activity_start).total_seconds()


    print(f"Created At:       {activity_start.isoformat()}")
    print(f"Deadline:         {due_time.isoformat()}")
    print(f"Current UTC Time: {current_time.isoformat()}")
    print(f"Elapsed Duration: {elapsed_seconds:.2f} total seconds")

    return is_overdue, elapsed_seconds


if __name__ == "__main__":
    # Test active task
    print("--- Testing New Task ---")
    id_, start, due = create_task("T-101")
    check_validity(start, due)


    