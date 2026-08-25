

def ticket_price(count):
    if count<=3:
        your_ticket_price=0
    if 3<count<12:
        your_ticket_price=10
    if count>=12:
        your_ticket_price=15
    return your_ticket_price

a=5

while a>0:
    age=int(input(f'pleas enter your age:'))
    m=ticket_price(age)
    print(f'your movie ticket price is {m}$: ')
    print('\n for exit press 0')
    if age==0:
        break
