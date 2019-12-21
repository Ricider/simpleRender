import turtle
import math

class point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def subtract(self,other):
        return point(
            self.x-other.x,
            self.y-other.y,
            self.z-other.z)
    
    def add(self,other):
        return point(
            self.x+other.x,
            self.y+other.y,
            self.z+other.z)   

    def integerMul(self,integer):
        return point(
            self.x*integer,
            self.y*integer,
            self.z*integer)        
        
class polygon:
    allpollys=dict()
    def __init__(self,x,y,z,color):
        self.point1=x
        self.point2=y
        self.point3=z
        self.color=color
        
        #render priority
        distance1=math.sqrt((camera.x-self.point1.x)**2+
                            (camera.y-self.point1.y)**2+
                            (camera.z-self.point1.z)**2)
        distance2=math.sqrt((camera.x-self.point2.x)**2+
                            (camera.y-self.point2.y)**2+
                            (camera.z-self.point2.z)**2)
        distance3=math.sqrt((camera.x-self.point3.x)**2+
                            (camera.y-self.point3.y)**2+
                            (camera.z-self.point3.z)**2)
        total=distance1+distance2+distance3
        if total in polygon.allpollys: total+=0.00001
        
        polygon.allpollys[total]=self
        
    def draw(self):
        temp=self.point1.subtract(camera)
        proj1=camera.add(temp.integerMul(-(camera.z/temp.z)))
        
        temp=self.point2.subtract(camera)
        proj2=camera.add(temp.integerMul(-(camera.z/temp.z)))
        
        temp=self.point3.subtract(camera)
        proj3=camera.add(temp.integerMul(-(camera.z/temp.z)))
        
        #turtle stuff
        tt.fillcolor(self.color)        
        tt.setpos(proj1.x*scale,proj1.y*scale)
        tt.begin_fill()
        tt.pendown()
        tt.setpos(proj2.x*scale,proj2.y*scale)
        tt.setpos(proj3.x*scale,proj3.y*scale)
        tt.setpos(proj1.x*scale,proj1.y*scale)
        tt.end_fill()
        tt.penup()
        
    def drawframe():
        for poly in sorted(polygon.allpollys,reverse=True):
            polygon.allpollys[poly].draw()
        polygon.allpollys={}
                
class cube:
    def __init__(self,pos,size,rotz):
        
        zcos=math.cos(rotz)
        zsin=math.sin(rotz)
        
        #edges
        x1=pos
        x2=point(pos.x+size*zcos,
                 pos.y,
                 pos.z+size*zsin)
        x3=point(pos.x-size*zsin,
                 pos.y,
                 pos.z+size*zcos)
        x4=point(pos.x+size*zcos-size*zsin,
                 pos.y,
                 pos.z+size*zcos+size*zsin)
        x5=point(pos.x+size*zcos,
                 pos.y+size,
                 pos.z+size*zsin)
        x6=point(pos.x+size*zcos-size*zsin,
                 pos.y+size,
                 pos.z+size*zcos+size*zsin)
        x7=point(pos.x-size*zsin,
                 pos.y+size,
                 pos.z+size*zcos)
        x8=point(pos.x,
                 pos.y+size,
                 pos.z)
        
        #faces
        a1=polygon(x1,x2,x3,"Red")
        a2=polygon(x4,x2,x3,"Red")
        b1=polygon(x4,x2,x5,"Blue")
        b2=polygon(x5,x4,x6,"Blue")
        c1=polygon(x4,x7,x3,"Green")
        c2=polygon(x4,x6,x7,"Green")
        
        anot1=polygon(x5,x8,x7,"Brown")
        anot2=polygon(x5,x6,x7,"Brown")
        bnot1=polygon(x1,x8,x3,"Pink")
        bnot2=polygon(x3,x8,x7,"Pink")
        cnot1=polygon(x2,x1,x8,"Purple")
        cnot2=polygon(x2,x5,x8,"Purple")

#prep
tt=turtle.Turtle()
tt.color("Black")
tt.hideturtle()
tt.penup()
tt.speed(0)
turtle.tracer(0, 0)

#perspective elements
camera=point(0,0,-3)
projPlaneZ=0
scale=60

rotval=0
for i in range(5000):
    tt.clear()  
    rotval+=0.01
    cube(point(-5,-5,5),3,rotval)
    cube(point(5,5,5),3,0)    
    polygon.drawframe()
    #camera.z+=0.01
    turtle.update()  

turtle.exitonclick()