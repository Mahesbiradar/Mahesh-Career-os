# Section 3 — Mini Project ⭐⭐⭐

# Project: Text Analytics Engine

# Imagine you're building a backend service that receives text from users and needs to analyze it before storing it in a database.

text = """
Python is easy.
Python is powerful.
Python is easy to learn.
Backend development with Python is fun.
"""


# Part A — Text Cleaning

def clean_text(user_text):

    # Remove leading/trailing whitespace.
    removed_whitespaces = user_text.strip()
    # Convert everything to lowercase.
    lowercase_text = removed_whitespaces.lower()
    # Replace every "." with an empty string.
    replaced_text = lowercase_text.replace("."," ")

    return replaced_text

cleaned_text = clean_text(text)

# Part B — Word Analysis

"""
Using the cleaned text:

Split it into words.
Print the total number of words.
Print the total number of unique words.
Find the longest word.
Find the shortest word.
"""


def splitted_string(data):
    # Split it into words.
    
    words = data.split()

    return words

words= splitted_string(cleaned_text)  

def word_anlysis(words):

    # Print the total number of words.
    number_of_words = len(words)
    print(number_of_words)

    # Print the total number of unique words.

    uninue_words = set()

    for word in words:
        uninue_words.add(word)
    print(len(uninue_words))

    # Find the longest word and shortes word
    longest_word = None
    shortest_word = None
    length_large = float('-inf')
    length_short = float('inf')

    for word in words:

        if len(word) > length_large:
            length_large = len(word)
            longest_word = word
        if len(word) < length_short:
            length_short = len(word)
            shortest_word = word

    print(longest_word)
    print(shortest_word)

word_anlysis(words)

# Part C — Frequency Counter

def words_frequency(data):

    words_freq = {}

    for word in data:
        words_freq[word] = words_freq.get(word,0)+1

    return words_freq

Frequencies_words = words_frequency(words)

print("Word Frequencies")

for word,freq in Frequencies_words.items():

    print(f"{word} -> {freq}")


# Part D — Most Frequent Word

def most_frequent_word(words):

    most_frequent = []
    frequency = 0

    for word,freq in words.items():

        if freq > frequency:
            frequency = freq
            most_frequent = [(word,freq)]
        elif frequency == freq and frequency > 0:
            most_frequent.append((word,freq))

    return most_frequent

frequent_words = most_frequent_word(Frequencies_words)

def print_frequent_words(data):

    lines =[]

    for word,freq in data:

        lines.append(f"Most Frequent Word : {word}")
        lines.append(f"Frequency : {freq}")

    return "\n".join(lines)

print(print_frequent_words(frequent_words))


# Part E — Word Search

# search_word = input("Enter word: ")

# if search_word in Frequencies_words:
#     print("Found")
# else:
#     print("Not Found")


# Part F — Unique Words

"""
Create a set containing all unique words.
Print:
Number of unique words.
All unique words.
"""
uniques_words = set()

for word,freq in Frequencies_words.items():

    uniques_words.add(word)

print(f"Number of unique words : {len(uniques_words)}")
print(f"All unique words : ")
print(uniques_words)


# Part G — Format Output

# Create one formatted string using f-strings.

output_string =f"============================\nText Analysis Report\nTotal Words      : {len(words)}\nUnique Words     : {len(uniques_words)}\n{print_frequent_words(frequent_words)}\n============================"


print(output_string)



# Part H — Challenge ⭐⭐⭐

"""
Create another dictionary that groups words by their length.

Example:

{
    2: ["is", "to"],
    3: ["fun"],
    4: ["easy"],
    6: ["python"],
    ...
}
"""

words_group = {}

for word,freq in Frequencies_words.items():

    if len(word) in words_group:
        words_group[len(word)] += [word]
    else:
        words_group[len(word)] = [word]

print(words_group)

