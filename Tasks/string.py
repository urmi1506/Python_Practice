text = "Hello Python World"

# 1. Extract "Python" - starts at 6(P), ends at 11(n)
#    stop index = 12 (one AFTER last char)
python_word = text[6:12]
print(f"Extracted word  : {python_word}")

# 2. Reverse - step of -1 reads backwards
reversed_str = text[::-1]
print(f"Reversed string : {reversed_str}")

# 3. Alternate chars - step of 2 skips every other
alternate = text[::2]
print(f"Alternate chars : {alternate}")

