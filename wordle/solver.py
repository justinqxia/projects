possible = []
guess = list(input("What was your guess?"))
print("")
print("What were the results of your guess?")
print("b = black/grey, y = yellow, g = green")
result = list(input("Please enter as a string of letters (e.g. bbygb)"))
#Check first character of first guess
if result[0] == "g":
    with open('/Users/justinxia/projects/wordle/testbank.txt') as bank:
        for line in bank:
            line = line.rstrip('\n')
            read = list(line)
            if read[0]==guess[0]:
                possible.append(line)
if result[0] == "y":
    with open('/Users/justinxia/projects/wordle/testbank.txt') as bank:
        for line in bank:
            line = line.rstrip('\n')
            if guess[0] in line:
                possible.append(line)
if result[0] == "b":
    with open('/Users/justinxia/projects/wordle/testbank.txt') as bank:
        for line in bank:
            line = line.rstrip('\n')
            if guess[0] not in line:
                possible.append(line)

#Check next four characters of first guess
for i in range(1,5):
    if result[i] == "g":
        for word in possible:
            check = list(word)
            if check[i]!=guess[i]:
                possible.remove(word)
    if result[i] == "y":
        for word in possible:
            if guess[i] not in word:
                possible.remove(word)
    if result[i] == "b":
        if guess.count(guess[i]) == 1:
            for word in possible:
                if guess[i] in word:
                    possible.remove(word)
print(possible)

#check next five guesses
while len(possible) > 1:
    print("")
    guess = list(input("What was your guess?"))
    print("")
    print("What were the results of your guess?")
    print("b = black/grey, y = yellow, g = green")
    result = list(input("Please enter as a string of letters (e.g. bbygb)"))
    for i in range (5):
        if result[i] == "g":
            for word in possible:
                check = list(word)
                if check[i]!=guess[i]:
                    possible.remove(word)
        if result[i] == "y":
            for word in possible:
                if guess[i] not in word:
                    possible.remove(word)
        if result[i] == "b":
            if guess.count(guess[i]) == 1:
                for word in possible:
                    if guess[i] in word:
                        possible.remove(word)
    print(possible)