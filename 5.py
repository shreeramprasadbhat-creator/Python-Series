
oval={'A','E','I','O','U','a','e','i','o','u'}
text=input('enter the text:' )
result=' '
remove=' '
for i in text:
    if i not in oval:
        result=result+i
    else:
        remove=remove+i
print("updated text is:",result)
print("removed text is:",remove)
