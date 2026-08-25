
a=float(input("enter your age "))
d=  (a / 100)
b=  (a/10)

t=[('one',1),('two',2),('three',3),('four',4),('five',5),('six',6),('seven',7),('eight',8),('nine',9),('ten',10)]
while d<=1: 
    for (x,y) in t:
      if( 0<b<=1 &  y == a ):
       print (f"your age is {x}")