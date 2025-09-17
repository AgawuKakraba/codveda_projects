#Take file address
fname = input("Paste text file address(must be a .txt file): ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()
word_count = 0
char_count = 0
for line in fhand:
    words = line.split()
    word_count += len(words)
    char_count += len(line)
    
print(f"There are {word_count} words and {char_count} characters in the file.")
