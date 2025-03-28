class spaceRover:
    def __init__(self,x,y,angle):
        self.x=x;
        self.y=y;
        self.angle=angle

        self.directions={
            0: (1,0),
            90: (0,1),
            180: (-1,0),
            270: (0,-1)
        }

    def move(self,len,reverse=False):
        dx,dy=self.directions[self.angle]
        if reverse:
            dx,dy=-dx,-dy
        self.x+=dx*len
        self.y+=dy*len

    def moveForward(self,len):
        self.move(len)

    def moveBackward(self,len):
        self.move(len,True)

    def turnRight(self):
        self.rotate('right')

    def turnLeft(self):
        self.rotate('left')

    def rotate(self,dir):
        if dir=='right':
            self.angle-=90
        else:
            self.angle+=90

        if self.angle==-90:
            self.angle=270
        elif self.angle==360:
            self.angle=0

    def position(self):
        return [self.x,self.y]