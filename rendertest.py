import turtle

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
    allpollys=[]
    def __init__(self,x,y,z,color):
        self.point1=x
        self.point2=y
        self.point3=z
        self.color=color
        polygon.allpollys.append(self)
        
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
        for poly in polygon.allpollys:
            poly.draw()
                
class cube:
    def __init__(self,pos,size):
        self.polylist=[]
        
        #edges
        x1=pos
        x2=point(pos.x,pos.y+size,pos.z)
        x3=point(pos.x+size,pos.y,pos.z)
        x4=point(pos.x+size,pos.y+size,pos.z)
        x5=point(pos.x,pos.y+size,pos.z+size)
        x6=point(pos.x+size,pos.y+size,pos.z+size)
        x7=point(pos.x+size,pos.y,pos.z+size)
        
        #faces
        a1=polygon(x1,x2,x3,"Red")
        a2=polygon(x4,x2,x3,"Red")
        b1=polygon(x4,x2,x5,"Blue")
        b2=polygon(x5,x4,x6,"Blue")
        c1=polygon(x4,x7,x3,"Green")
        c2=polygon(x4,x6,x7,"Green")                   

#prep
tt=turtle.Turtle()
tt.color("Black")
tt.hideturtle()
tt.penup()
tt.speed(4)

#perspective elements
camera=point(0,0,-20)
projPlaneZ=0
scale=60

cube(point(-5,-5,5),1)
polygon.drawframe()

turtle.exitonclick()