import pdb 
pdb.set_trace()
file = open('hello.txt','a')
file.write('\nThis is new content I just Appended')
file.close()

new_file = open('world.txt','w')
new_file.write('this is new file')
new_file.close()

file = open('hello.txt')
content = file.read()
file.close()
print(content)
