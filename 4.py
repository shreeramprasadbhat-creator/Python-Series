
text=(input("Enter the word: "))
char=(input("Enter the char to remove it: "))
result=" "
remove=" "
for i in text:
    if i!=char:
        result=result+i
    else:
        remove=remove+i
print("updated text is: ",result)
print('removed word is:',remove)
