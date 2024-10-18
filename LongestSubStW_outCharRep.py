str = input("Enter a string: ")
result = ""
for i in range (0, len(str)-1):
    word = str[i]
    for j in range (i, len(str)):
        if str[j] not in word:
            word+=(str[j])
        else:
            break
    if len(word)>len(result):
        result = word
print("Length of longest substring without character repitition: ", len(word))
print("Substring formed: ", result)

    
