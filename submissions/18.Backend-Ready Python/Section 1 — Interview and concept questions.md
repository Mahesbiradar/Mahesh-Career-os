
## Section 1 — Interview and concept questions

## 10 questions

10 marks

Answer each question concisely, in your own words. Each is worth 1 mark.

1\. `os` and `sys`: Explain the difference between `os.environ` and `sys.argv`. Give one backend use case for each.

# Ans: os.environ is a dictionary-like object used to access system-wide environment variables set outside the Python script. sys.argv is a list that captures command-line arguments passed directly to the script when it is executed.

• os.environ Backend Use Case: Storing and retrieving sensitive configuration data (like database passwords or API keys) to keep them out of the source code.
• sys.argv Backend Use Case: Creating command-line interfaces (CLIs) or maintenance scripts where a developer specifies a target file or runtime mode (e.g., python manage.py migrate).



2\. `datetime`: What is the difference between a naive datetime and a timezone-aware datetime? Why is UTC commonly used when storing backend timestamps?

# Ans: A naive datetime contains no timezone information and assumes the local system clock, making it ambiguous in a global context. A timezone-aware datetime explicitly includes an offset or zone name (like UTC or EST), allowing it to locate a specific point in time unambiguously.

UTC is commonly used for storing backend timestamps for three main reasons:

• Consistency across regions: It provides a universal baseline. This prevents data confusion when servers, databases, and users are located in different parts of the world.
Immunity to Daylight Saving Time (DST): UTC does not observe DST. Using it eliminates the risk of "missing" or duplicate hours when clocks change locally.


3\. `re`: Explain the difference between `re.search()`, `re.findall()`, and `re.fullmatch()`. Give an appropriate use case for each.

# Ans: re.search() finds the first appearance, re.findall() finds all appearances, and re.fullmatch() requires the entire string to match

• re.search() Use Case: Parsing log files to find the first instance of an error code or specific keyword inside a long line of text.
• re.findall() Use Case: Scraping data, such as extracting every phone number or email address from a webpage's text content.
• re.fullmatch() Use Case: Data validation, such as verifying that an inputted string exactly matches a strict structural pattern like a zip code, username limit, or password policy.

4\. `logging`: When would you use `logger.warning()`, `logger.error()`, and `logger.exception()`? Why is logging a secret or API key dangerous?

# Ans:

• logger.warning(): Used for unexpected events or potential issues that don't stop the application but indicate something might go wrong soon (e.g., low disk space or a deprecated API usage).
• logger.error(): Used for serious problems where a specific operation or request fails, but the application as a whole can recover and keep running (e.g., an external API timeout or a missing required file).
• logger.exception(): Used strictly inside an except block when an error occurs. It logs an ERROR level message along with the full stack trace, which is critical for debugging why the code crashed.

Logging a secret or API key exposes it in plain text within log files. This is dangerous because logs are frequently shared, stored in insecure locations, or viewed by unauthorized developers and third-party monitoring tools, which can lead to a severe security breach or account takeover.


5\. `json`: Explain the difference between `json.dumps()` and `json.dump()`. What exception can malformed JSON raise, and why doesn't successful parsing guarantee valid application data?

# Ans: json.dumps() is used to convert the python object into the json string. json.dump() is used to convert the pythin object to json and write it to the json file.

Malformed JSON raises a json.JSONDecodeError.

• JSON parsing only checks for proper syntax (e.g., matching brackets, correct quotes). It does not validate business logic or schemas. For example, a JSON file could parse successfully but still contain a negative age, a missing required username field, or an invalid email format that crashes our backend logic later.


6\. `csv`: Why is `newline=""` commonly used when opening CSV files? Why must numeric values read from CSV often be converted and validated?

# Ans: newline It prevents the Python csv module from writing extra blank rows between data lines. Without it, some operating systems (like Windows) will double-translate the standard carriage return characters (\r\n), corrupting the visual structure of the file.

The CSV format treats every piece of data as a string by default. To do math operations, we must first convert the strings into integers or floats; we must validate them because missing data, spaces, or malformed entries (like "N/A" or "1oo") will cause calculation errors or runtime crashes.

7\. `math`: Explain why `math.isfinite()` is useful when validating imported amounts. Why is `float` not ideal for exact monetary calculations?

# Ans: Imported amounts can sometimes contain special IEEE 754 floating-point values like positive infinity (inf), negative infinity (-inf), or Not-a-Number (nan) due to malformed data or division-by-zero errors. math.isfinite() ensures the amount is a normal, valid number before processing it, preventing crashes or broken computations downstream.

• Floating-point numbers represent decimals using binary fractions, which leads to precision loss and rounding errors (for example, 0.1 + 0.2 evaluates to 0.30000000000000004 instead of exactly 0.3). For money, exact decimal accuracy is non-negotiable, which is why developers use the decimal module instead.


8\. `random`: What does setting a random seed accomplish? Why should a backend use `secrets` rather than `random` to generate password-reset tokens?

# Ans: Setting a random seed initializes the pseudo-random number generator to a specific, reproducible starting state. This ensures that the exact same sequence of "random" numbers is generated every time the script is executed, which is essential for debugging, testing, and mathematical simulations.

The random module uses an algorithm that is predictable; if an attacker intercepts a few generated tokens, they can calculate the internal seed and predict all future tokens. The secrets module uses cryptographically secure pseudo-random number generators (CSPRNGs) tied to system entropy, making it virtually impossible for an attacker to predict generated password-reset to



9\. `collections`: Explain the different purposes of `Counter`, `defaultdict`, and `deque`. Give a backend example for each.

# Ans:

• Counter: A dictionary subclass designed explicitly for counting hashable objects. It automatically tallies occurrences of items and maps them as keys to their integer counts.
	• Backend Use Case: Generating a trending tags feature by counting the frequency of hashtags in recent user posts.
• defaultdict: A dictionary subclass that automatically provides a default value for a non-existent key upon first access, preventing a KeyError.
	• Backend Use Case: Grouping data, such as mapping user IDs to a list of their recent transaction objects (defaultdict(list)) without manually checking if the user ID key already exists.
• deque: A double-ended queue that supports fast, O(1) time complexity appends and pops from both ends, making it much more efficient than a standard Python list for queue operations.
	• Backend Use Case: Implementing an in-memory rate limiter or recent-actions log that keeps track of the last 100 API requests by popping out old entries as new ones arrive.

10\. Integrated design: You're importing thousands of orders from CSV, validating them, recording rejected rows, and generating a summary. Which of the 10 modules would you use, and what role would each relevant module play?

# Ans:
• csv: Reads the source orders file row-by-row and writes rejected entries to an error log file.
• re: Validates strict string formats like emails, phone numbers, and postal codes using re.fullmatch().
• math: Sanitizes numeric data (quantities, prices) against corrupt nan or inf values using math.isfinite().
• datetime: Converts local order date strings into standardized, timezone-aware UTC timestamps.
• logging: Tracks execution progress (info), logs data issues (warning), and records unexpected crashes with full stack traces (exception).
• collections: Tallies metrics (e.g., total success vs. failure counts) using Counter and groups rejection reasons using defaultdict.










