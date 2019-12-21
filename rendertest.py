import turtle
import math
import time

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
  
class plane:
    def __init__ (self,pos,sizex,sizez,color,isVertical=False):
           
              
        #edges
        if not isVertical:
            x1=pos
            x2=point(pos.x,pos.y,pos.z+sizez)
            x3=point(pos.x+sizex,pos.y,pos.z)
            x4=point(pos.x+sizex,pos.y,pos.z+sizez)
        else:
            x1=pos
            x2=point(pos.x,pos.y+sizez,pos.z)
            x3=point(pos.x+sizex,pos.y,pos.z)
            x4=point(pos.x+sizex,pos.y+sizez,pos.z)   
            
        #faces
        a1=polygon(x1,x2,x3,color)
        a2=polygon(x2,x3,x4,color)
                 
               
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
framecount=1
startTime=time.time()

while True:
    tt.clear()  
    rotval+=0.03
    cube(point(0,-5,5),3,rotval)
    cube(point(0,-2,5),-3,rotval)
    cube(point(0,2,5),3,rotval*-1)
    cube(point(0,5,5),-3,rotval*-1)
    
    cube(point(-8,-7,2),3*abs(math.cos(framecount/50)),0)
    cube(point(8-3*abs(math.cos(framecount/50)),-7,2),3*abs(math.cos(framecount/50)),0)  
    

    cube(point(-1+7*math.cos(framecount/50),7,2),2,0)    
    
    plane(point(-8,-7,2),16,5,"Teal")
    plane(point(-8,-7,7),16,16,"Teal",isVertical=True)
    plane(point(-8,9,2),16,5,"Teal")
    framecount+=1
    if framecount%100==0:
        print("fps=", 100/(time.time()-startTime),"poly count=", len(polygon.allpollys))
        startTime=time.time()
    polygon.drawframe()
    turtle.update()

turtle.exitonclick()