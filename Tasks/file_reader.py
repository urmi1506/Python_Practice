
# Generator Function
class EmptyFileError(Exception):
    pass
"""
1. Generator function: read_file_lines(filename)
   - Yields one line at a time
   - Strips whitespace from each line
   - Skips empty lines

"""


def read_file_lines(filename):
    with open(filename) as file:
        has_content = False
        for line in file:
            stripped = line.strip()
            if stripped:
               has_content = True
               yield stripped

        if not has_content:
            raise EmptyFileError("File is empty")
            

filename = "C:\\Python\\Python_Practice\\Tasks\\sample.txt"

"""
2. Function: search_in_file(filename, keyword)
   - Uses your generator
   - Returns all lines containing keyword
   - Handles FileNotFoundError gracefully
   - Handles PermissionError gracefully
   - Uses finally to print "Search complete"
for line in read_file_lines(filename):
    print(line)
"""

def search_in_file(filename, keyword):
    res = []
    try:
        for i,line in enumerate(read_file_lines(filename),start=1):
            if keyword.lower() in line.lower():
                res.append((i,line))

    except FileNotFoundError:
        print("Error : File not found .")

    except PermissionError:
        print("Error : Permission denied.")

    finally:
        print("Search Complete")

    return res

keyword = "Python"

print("Searching for 'Python' in sample.txt")
print("─" * 37)

matches = search_in_file(filename, keyword)

for line_no, line in matches:
    print(f"Line {line_no}: {line}")

print("─" * 37)
print(f"Found {len(matches)} matches")

"""
3. Function: count_words_in_file(filename)
   - Uses your generator  
   - Counts total words across all lines
   - Returns the count
   - Handles all exceptions
"""

def count_words_in_file(filename):
    total_words = 0
    try:
        for line in read_file_lines(filename):
            words = line.split()
            total_words += len(words)

    except(FileNotFoundError ,PermissionError ,EmptyFileError):
        return 0

    return total_words

count = count_words_in_file(filename)
print("─" * 37)
print(f"Total words in file : {count}")
print("─" * 37)

"""
4. Custom Exception:
   - Create EmptyFileError(Exception)
   - Raise it in read_file_lines if file is empty
"""

search_in_file("missing.txt", keyword)

