
def fibonachi(count)->int:
    a=[]
    a.append(0)
    if count>1:
        a.append(1)
    for i in range(2,count):

        next_fib =a[i-1]+a[i-2]
        a.append(next_fib)    
    return a 
           
tedad=int(input("tedad seri ke mikhahid donbale fibonacci nemayesh dade shavad vared konid:"))
seri_fibonachi=fibonachi(tedad)
print(f'ba tavajjoh be tedead seri ke mikhastid:{tedad} donbale fibbonacci shoma barabar ba ast :{seri_fibonachi}')

    


