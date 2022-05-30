#word = str(input("Enter a word: ")) cuando quiera cualquier palabra
word = "nohtyp"
reverse = ""
i = 0
for element in range(len(word), 0, -1):
    print(element)
    print(word[element-1])
    reverse = reverse + word[element-1]

print(reverse)