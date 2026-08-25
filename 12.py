my_add=[]
# sum=0

number = int(input("tedad nomarati ke mikhahid jam konid ra beneveisid:"))

for i in range(0,number):
    add= int(input(f" add delkhah {i} ro vared konid:\n"))
    my_add.append(add)



# for i in range(0,len(my_add)):
#     sum = sum + int(my_add[i])

print(my_add)
sum =  sum(my_add)
print(sum)


minmume = min(my_add)
maximume  = max(my_add)
print(f"kamtarin nomre daneshamooz barabar ast ba: {minmume} \n")

print(f"balatarin nomre daneshamooz barabar ast ba: {maximume} \n")

print(f"avg nomre daneshamooz barabar ast ba: {sum/len(my_add)}")
