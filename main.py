#Note s cleaner

#1: Sneak peak
n = int(input("How many characters to preview"))
file = open ("Class-notes.txt")
print(file.read(n))
file.close()
print()

#2:Reading all line

file =open("Class-notes.txt", "r")
lines = file.readlines()
file.close()
print("Total lines;",len(lines))
for i in range (len(lines)):
    print(i+1,"->", lines [i].strip())
print()
    #3 Filtering Lines.