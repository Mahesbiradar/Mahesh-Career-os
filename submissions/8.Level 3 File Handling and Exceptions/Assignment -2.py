
"""
## 🟢 Assignment 1 — Easy

### Simple File Reader

Create a function:

```python
def count_words(filename):
    ...
```

It should:

1. Open a text file safely using `with`.
2. Read the contents.
3. Count the total number of words.
4. Return the count.
5. Handle `FileNotFoundError`.

Example file:

```text
Python is easy to learn
Python is powerful
```

Expected result:

```text
7
```

"""
def count_words(filename):

    try:
        with open(filename,"r") as file:
            words = file.read().split()
    except FileNotFoundError:
        print("File not found")
    else:
        return f"Total words: {len(words)}"


result = count_words("users.txt")

print(result)


"""

## 🟡 Assignment 2 — Medium

### Student Marks Processor

Create:

```python
def process_marks(filename):
    ...
```

Suppose `marks.txt` contains:

```text
Mahesh,85
Rahul,72
Amit,91
Priya,66
```

Your function should:

1. Read the file using `with`.
2. Parse each line.
3. Store the data in a dictionary.
4. Calculate the average marks.
5. Return the dictionary and average.

For example, conceptually:

```python
{
    "Mahesh": 85,
    "Rahul": 72,
    "Amit": 91,
    "Priya": 66
}
```

Also handle:

* `FileNotFoundError`
* Invalid mark values using `ValueError`

**Don't use pandas.** This is a Python fundamentals assessment.

---
"""
def cal_average(marks):

    total_marks = 0

    for key,value in marks.items():

        total_marks += int(value)

    return total_marks/len(marks)


def process_marks(filename):

    try:
        with open(filename,"r") as file:
            pass

    except FileNotFoundError:
        
        print("File not found")
    else:
        with open(filename,"r") as file:
            students = {}

            for line in file:

                parts = line.strip().split(",")


                if len(parts) == 2:

                    name = parts[0]
                    marks = parts[1]

                students[name] = marks

            average = cal_average(students)

        return (students,average)



result = process_marks("submissions\marks.txt")

print(result)


"""

## 🔴 Assignment 3 — Hard

### Safe Configuration Loader

Create:

```python
def load_config(filename):
    ...
```

The file contains:

```text
host=localhost
port=5432
debug=True
```

Your function should:

1. Open the file safely.
2. Read each line.
3. Split each line into key/value.
4. Store the result in a dictionary.
5. Convert:

   * `port` → `int`
   * `debug` → `bool`
6. Handle a missing file.
7. Handle malformed lines.
8. Handle invalid integer values.
9. Use appropriate exceptions.
10. Create **at least one custom exception** for a configuration-specific error.

For example, a malformed line such as:

```text
invalid_line
```

should not silently pass.

---

"""


class ConfigurationError(Exception):
    """Exception raised for errors in the configuration file layout or values."""
    pass



def load_config(filename):

    try:
       
        with open(filename,"r") as file:

            config = {}

            for line in file:

                if not line.strip():
                    continue

                data = line.strip().split("=")

                if len(data) != 2:
                    raise ConfigurationError(f"Malformed line found: '{line.strip()}'")
                else:

                    key = data[0].strip()
                    value = data[1].strip()


                    if key == "host":
                        config["host"] = value
                    elif key == "port":
                        try:
                            config["port"] = int(value)
                        except ValueError:
                            raise ConfigurationError(f"Invalid integer value for port: '{value}'")
                            
                    elif key == "debug":
                        config["debug"] = value.lower() == "true"
                    else:
                        raise ConfigurationError(f"Unknown configuration key: '{key}'")
            return config

    except FileNotFoundError:
        print("File not Found")
        return None

    except ConfigurationError as e:
        print(f"Config Error: {e}")
        return None


data = load_config("submissions\data_file.txt")


print(data)

