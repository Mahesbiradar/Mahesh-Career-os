## Section 6 — Backend interview questions

## Explain your engineering decisions

11 marks

Answer each in approximately 3–6 sentences. These questions test whether you can apply Python knowledge to real backend work.

1. File processing and resilience — 2 marks: 
How would you design a CSV import service that continues after bad rows but stops safely if the file itself cannot be read?

# Ans:

First, I will wrap the file opening logic in a try...except block. If the file does not exist or an error occurs during reading, we can catch the exception (FileNotFoundError or PermissionError) and safely exit the script immediately.
Next, after successfully opening the file, I will validate the headers against our expected keys. If the required headers are missing, the script will abort since the file structure is invalid.
Finally, once the structure is verified, I will process the rows using a loop. Each row will be validated individually: if a row is completely empty or contains corrupted or invalid cell values, the service will log the error, skip that row using continue, and proceed to the next line. This ensures valid records are still processed without letting bad data crash the entire service.

2. Validation and security — 2 marks: 
Why should you validate parsed JSON and CSV data separately from parsing it? How would you avoid exposing secrets in logs?

# ANS:


• Parsing only checks if the data format is legal (e.g., is it valid JSON syntax with proper brackets, or valid comma-separated CSV rows). The parser does not care what the data actually means.

• Even if a JSON payload parses perfectly into a Python dictionary, it could still contain dangerous values—such as a negative price, an SQL injection payload, an invalid date format, or a massive number that could cause an integer overflow.

• By separating them, you can completely reject bad or unsafe data at your system's boundary before it passes deeper into your business logic or database layers.

• Never log raw objects entirely. Use data masking to replace sensitive fields (like changing "password": "123" to "********") and explicitly log only safe identifiers like order_id.


3. Time handling — 2 marks: 
An API receives timestamps from clients in multiple timezones. How would you parse, validate, normalize, and store them?

# Ans:

• Parse & Validate: i will Use a robust date parser (like Python's datetime.fromisoformat()) to parse incoming ISO 8601 strings. Validate that the timestamp is offset-aware. Reject any naive timestamps to prevent ambiguity.
• Normalize & Store: Convert the validated, offset-aware datetime object directly to UTC using .astimezone(timezone.utc). Save this normalized UTC timestamp in our database as a standard UTC DATETIME or TIMESTAMP field, ensuring a uniform timeline across all records.


4. Operational reliability — 2 marks: 
How would you use logging levels, exception handling, and exit codes to distinguish rejected records from a failed import process?

# Ans:

• Rejected Records (Non-Fatal): Use WARNING or INFO logging levels to log individual bad records. Catch these anomalies using localized try...except blocks inside your data loop so the application skips the item and keeps moving forward. The process will finish completely and return an exit code of 0 (success).
• Failed Import Process (Fatal): Use ERROR or CRITICAL logging levels for system-wide disruptions (e.g., missing input files or a database crash). Catch these errors at the top-level application framework and terminate the entire routine instantly, returning a non-zero exit code (e.g., sys.exit(1)) to notify monitoring tools that the process failed.


5. Data structures and scale — 3 marks: 
You must process one million orders and produce counts by status and customer. Which data structures would you choose, what memory considerations would you make, and how would your design change if the full dataset could not fit in memory?


# ANS:

Use a nested Hash Map (Python dict) or a collections.defaultdict(collections.Counter). The outer key will be the customer_id and the inner dictionary/counter will map the status to its respective aggregate integer count (e.g., {customer_1: {"Pending": 5, "Completed": 12}}). This allows \(O(1)\) lookups and updates per order.

• One million orders is relatively small and can easily fit in modern RAM if optimized. To minimize memory footprint, read the file using an iterative streaming generator (like csv.reader) row-by-row instead of loading the entire raw dataset into a massive array or DataFrame at once. Store only the aggregated counts in memory, not the raw order rows.

