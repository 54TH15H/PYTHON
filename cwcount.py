s = input(" ENTER A STRING \n NOTE : PRESS ENTER AFTER ENTERING A STRING \n")
cc,wc=0,1
for i in s:
    cc+=1
    if i == " ":
        wc+=1

print(" CHARATERS COUNT :  ",cc)
print(" WORD COUNT :  ",wc)
