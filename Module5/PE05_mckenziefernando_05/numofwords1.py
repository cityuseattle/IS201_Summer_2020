
num_words = 0
with open('number.txt','r') as f: 
    for line in f:
       words = line.split()
       num_words += len(words)

print("number of words:")
print(num_words)