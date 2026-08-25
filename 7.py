import random
List_tashay_player_1=[]
List_tashay_player_2=[]
majmoe_tase_player_1=0
majmoe_tase_player_2=0

tedad_shance_player_1=int(input('tedad baar ke mikhad ke bazikon aval tas bendazad ro vared kon:'))
tedad_shance_player_2=int(input('tedad baar ke mikhad ke bazikon dovvom tas bendazad ro vared kon:'))


def play_tas(user,tedade_shance):
    i = 0
    while tedade_shance > i:
        i +=1  
        g=random.randint(1,6)
        user.append(g)

def show_tas(list_tass,user):
     print(f' tass haye rixteh shode baray user {user} bara bar ast ba : {list_tass}')

def majmoo_tas(user):
    sum = 0
    for i in range(0,len(user)):
        sum = sum+ int(user[i])
    return sum
    
def print_majmoe_tass(list_tass , user):
    print(f' majmoe tass haye bazaikon {user} bara bar ast ba : {list_tass}')

def mogayeseh(a,b):
    if majmoe_tase_player_1 > majmoe_tase_player_2:
        print("player 1 is winner:")
    elif majmoe_tase_player_2 > majmoe_tase_player_1:
        print("player 2 is winner:")
    else:
        print('mosavi shod') 

play_tas(List_tashay_player_1,tedad_shance_player_1)
show_tas(List_tashay_player_1,'player A')

play_tas(List_tashay_player_2,tedad_shance_player_2)
show_tas(List_tashay_player_2,'player B')


majmoe_tase_player_1 = majmoo_tas(List_tashay_player_1)
majmoe_tase_player_2 = majmoo_tas(List_tashay_player_2)

print_majmoe_tass(majmoe_tase_player_1,'player A')
print_majmoe_tass(majmoe_tase_player_2,'player B')

mogayeseh(majmoe_tase_player_1,majmoe_tase_player_2)

    

print('\n *** RESULT***')

   



