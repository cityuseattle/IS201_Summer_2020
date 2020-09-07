import pprint
message = """ peter piper picked a peck of pickled peppers 
              a peck of pickled peppers peter piper picked
              if peter piper picked a peck of pickled peppers
              where's the peck of pickled peppers peter pipper picked?"""

count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)