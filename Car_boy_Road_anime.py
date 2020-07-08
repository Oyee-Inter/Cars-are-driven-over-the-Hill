import turtle,time,random
wn=turtle.Screen()
wn.setup(1200,700,0,0)
wn.bgpic('Street7.gif')
turtle.tracer(20)
turtle.penup()
turtle.hideturtle()
s=turtle.Shape('compound')
     
# Функция для построения полигонов:
def polygon(x1,y1,x2,y2,x3,y3,x4,y4,clr1,clr2):
    poly=((x1,y1),(x2,y2),(x3,y3),(x4,y4))
    s.addcomponent(poly,clr1,clr2)
    
#Функция для построения окружностей
def circles(x,y,r,clr1,clr2):
    turtle.up()
    turtle.goto(x,y-r)
    #turtle.down()
    turtle.begin_poly()
    turtle.circle(r)
    turtle.end_poly()
    m=turtle.get_poly()
    s.addcomponent(m,clr1,clr2)

# Автомобиль (кузов)   
polygon(0,15,10,30,55,30,55,15,'purple','black')
polygon(15,30,30,50,30,30,30,30,'violet','black')
polygon(30,30,30,50,55,50,55,30,'blue','black')
polygon(55,30,55,50,80,50,80,30,'blue','black')
polygon(55,5,55,30,80,30,80,15,'crimson','black')
polygon(80,15,80,50,100,30,100,30,'orange red','black')
polygon(80,15,100,30,130,30,130,15,'green yellow','black')
polygon(130,15,130,30,155,15,155,15,'green','black')
polygon(130,0,130,15,155,15,140,0,'red','black')
polygon(30,-10,30,15,130,15,130,-10,'coral','black')
polygon(20,-10,0,15,20,15,20,15,'lawn green','black')
polygon(105,25,105,55,107,55,107,25,'black','black')

# Колеса автомобиля 
#Первое колесо
circles(30,-2,20,'green','black')
circles(30,-2,10,'forest green','black')
circles(30,-2,5,'blue','black')

#Второе колесо
circles(120,-2,20,'green','black')
circles(120,-2,10,'forest green','black')
circles(120,-2,5,'blue','black')

# Мальчик
polygon(62.5,50,67.5,53,72.5,53,77.5,50,'navy','black')
polygon(67.5,53,60,60,80,60,72.5,53,'red','red')
polygon(60,60,62.5,65,77.5,65,80,60,'red','red')
polygon(60,65,70,80,80,65,80,65,'blue','blue')

polygon(66,56,66,58,74,58,74,56,'gold','gold')
polygon(69,60,69,62,72,62,72,60,'light blue','light blue')
polygon(58,60,58,62,60,62,60,60,'brown','brown')
polygon(80,60,80,62,82,62,82,60,'brown','brown')

#Глаза
circles(65,62,1,'black','black')
circles(75,62,1,'black','black')

#----------------------------------------------
wn.addshape('car',s)
car=turtle.Turtle(shape='car')
car.penup()
car.tilt(90)
car.hideturtle()
car.goto(-400,0)                  #Автомобиль верхней дороги   
car.shapesize(0.4)
car.showturtle()
car.goto(-600,150)
car1=car.clone()                  #Автомобиль нижней дороги
car1.shapesize(0.8)
car1.goto(-600,-270)

car2=car.clone()                  #Автомобиль средней дороги
car2.shapesize(0.6)
car2.goto(-600,-20)

#Цикл задает бесконечное движение автомобилей
step=1.5
#for m in range(1):
while True:
#------------------------------------------    
    for i in range(105):
        car.setheading(-20-0.02*i)
        car2.setheading(-20-0.02*i)
        car.fd(1)
        car2.fd(1)
        car1.fd(step)
    angle=car.heading()
    angle2=car2.heading()
#---------------------------------------------
    for i in range(585):
        car.setheading(angle+0.065*i)
        car.fd(1)
        car2.setheading(angle2+0.07*i)
        car2.fd(1)
        car1.fd(step)
        #car2.fd(1)
    angle=car.heading()
    angle2=car2.heading()
#-----------------------------------------------
    for i in range(510):
        car.setheading(angle-0.08*i)
        car.fd(1)
        car2.setheading(angle2-0.09*i)
        car2.fd(1)
        car1.fd(step)
        #car2.fd(1)
    X=car.xcor()
#-------------------------------------   4
    if X>500:
        car.goto(-600,150)
        car1.goto(-600,-270)
        car2.goto(-600,-20)
#-------------------------------------   5







