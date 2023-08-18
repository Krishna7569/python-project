line=input("Enter the line what you want:-")
f1=open("D:\\gopi\\file.txt","r")
new_line=""
for i in range(f1):
    if i%2==1:
        new_line+=line[i].upper()
    else:
        new_line+=line[i]

        print(new_line)
