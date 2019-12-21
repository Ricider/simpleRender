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
    def __init__(self,x,y,z,color):
        self.point1=x
        self.point2=y
        self.point3=z
        self.color=color
        
    def draw(self):
        temp=self.point1.subtract(camera)
        proj1=camera.add(temp.integerMul(-(camera.z/temp.z)))
        
        temp=self.point2.subtract(camera)
        proj2=camera.add(temp.integerMul(-(camera.z/temp.z)))
        
        temp=self.point3.subtract(camera)
        proj3=camera.add(temp.integerMul(-(camera.z/temp.z)))
        
        tt.setpos(proj1.x*scale,proj1.y*scale)
        tt.pendown()
        tt.setpos(proj2.x*scale,proj2.y*scale)
        tt.setpos(proj3.x*scale,proj3.y*scale)
        tt.setpos(proj1.x*scale,proj1.y*scale)
        tt.penup()
                
        
#prep
tt=turtle.Turtle()
tt.color("red")
tt.hideturtle()
tt.penup()
tt.speed(0)

#perspective elements
camera=point(0,0,-5)
projPlaneZ=0
scale=20

testpoly=polygon(
point(2,0,1),
point(0,0,1),
point(0,2,1),
"Red")

testpoly.draw()

turtle.exitonclick()