line=int(input("Enter the line number what you want:"))
new_line=""
f1=open(("D.\\file.txt","r"))
print(f1.read())
for i in range(len(line)):
    if i % 2 !=1:
        new_line+=str[i].upper()
    else:
        new_line+=line[i]
print(new_line)
      



        
    
