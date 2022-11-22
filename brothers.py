import csv
brothers = []
with open('Brothers - Sheet1.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        brothers.append(row)

for i in range(1, 41):
    print(brothers[i][0])
    major = input("What is his major?")
    while (major != brothers[i][1]):
        major = input("Wrong, try again. What is his major?")
    hometown = input("What is his hometown?")
    while (hometown != brothers[i][2]):
        hometown = input("Wrong, try again. What is his hometown?")
    ccp = input("What is his current chapter postion(s)?")
    while (ccp != brothers[i][1]):
        ccp = input("Wrong, try again. What is his current chapter postion(s)?")