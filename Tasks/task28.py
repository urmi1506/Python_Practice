
lines = []
print("Enter text (type 'END' on a new line to stop):")
while True:
        line = input()
        if  line == 'END':
            break
        lines.append(line)
    

paragraph = '\n'.join(lines)
print(paragraph)

char_count = sum(len(line) for line in lines)  
word_count = sum(len(line.split()) for line in lines)
line_count = len(lines)

print(f"Total characters:{char_count}")
print(f"Total words:{word_count}")
print(f"Line:{line_count}")

words=[]
words=paragraph.split()
freq=[words.count(w) for w in words]
print(dict(zip(words,freq)))

top=[]
top = sorted(set(words), key=words.count, reverse=True)[:3]
print(f"Top 3 Words :{top}")

unique = set(words)
print(len(unique))