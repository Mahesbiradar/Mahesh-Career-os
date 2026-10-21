## Section 2 — Three coding assignments

## Easy, medium, hard

24 marks

These are independent coding tasks. Submit each as a separate `.py` file.

### Assignment 2.1 — Easy: Timestamp and deadline utility

File: `deadline_utility.py`

4 marks

Write a program that accepts a timestamp string in ISO 8601 format and a deadline duration in hours.

Requirements:

- Parse the timestamp using `datetime`.
- Support timezone-aware timestamps and reject naive timestamps.
- Calculate the deadline using `timedelta`.
- Display the deadline in UTC.
- Handle invalid timestamps and invalid duration inputs without an unhandled exception.

Test at least one valid timestamp and two invalid inputs.

```python


from datetime import datetime,timezone,timedelta

def deadline_utility(timestamp, deadline):

    try: 

        parced_timestamp = datetime.fromisoformat(timestamp)

    except ValueError as e:

        print(f"Parsing failed! '{timestamp}' is not a valid ISO 8601 string.")

        return None

    if parced_timestamp.tzinfo is None or parced_timestamp.tzinfo.utcoffset(parced_timestamp) is None:
        print("Error: The timestamp is naive. Timezone-aware timestamps are required.")
        return None


    try:

        deadline_float  = float(deadline)

    except ValueError as e:

        print(f"Parsing failed! {deadline} is not a valid numerical value in hours.")

        return None
    


    deadline_delta  = timedelta(hours=deadline_float)

    final_deadline  = parced_timestamp + deadline_delta

    final_deadline = final_deadline.astimezone(timezone.utc)

    print(f"The deadline is {final_deadline.strftime('%Y-%m-%d %I:%M %p %Z')}")



if __name__ == "__main__":
    print("--- Test 1: Valid Timezone-Aware Timestamp ---")
    # This should succeed and convert 14:30 +5:30 offset + 5 hours into UTC
    deadline_utility("2026-10-20T14:30:00+05:30", "5")
    print()

    print("--- Test 2: Invalid Input (Naive Timestamp) ---")
    # This should be rejected by your tzinfo check
    deadline_utility("2026-10-20T14:30:00", "4")
    print()

    print("--- Test 3: Invalid Input (Bad Duration Format) ---")
    # This should be caught by your second try-except block
    deadline_utility("2026-10-20T14:30:00Z", "abc")
    print()

```

### Assignment 2.2 — Medium: CSV validator and report

File: `csv_validation_report.py`

8 marks

Create a CSV import tool that reads a file containing these columns:

`order_id, customer, amount, status`

Requirements:

- Use `csv.DictReader`.
- Validate required columns and reject rows with missing required values.
- Validate that `amount` is numeric, finite, and non-negative.
- Validate `order_id` using a regular expression.
- Accept only the statuses `pending`, `processing`, and `completed`.
- Continue processing after an invalid row.
- Use `Counter` to summarize accepted orders by status.
- Write accepted rows and rejected rows to separate CSV reports.
- Record meaningful events and errors using `logging`.

Your code must handle a missing input file and a malformed or incomplete CSV structure.

### Assignment 2.3 — Hard: Configuration-driven export CLI

File: `export_cli.py`

12 marks

Build a command-line tool that reads a JSON configuration file and exports a report.

Requirements:

- Use `sys.argv` to accept the configuration path.
- Use `os` to validate paths and create an output directory.
- Read and validate configuration values, including an input path, output path, and maximum number of records.
- Read order data from CSV.
- Use `datetime` to add a UTC generation timestamp to the report metadata.
- Use `math` to calculate the total and average accepted amount safely.
- Use `collections` to count orders by status.
- Use `random` to generate reproducible sample IDs for a testing report; these IDs must not be used as security credentials.
- Write the report as JSON.
- Configure logging and handle missing files, invalid configuration, malformed input data, and failed exports.
- Return an appropriate nonzero process exit code on fatal failure.

Your solution should separate the core processing logic from the command-line entry point.
