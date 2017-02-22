class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def f(self,x):
        #print('Before')
        #import IPython; IPython.embed();
        #print('After')
        return 1./x

def test_point_init():
    point = Point(x=3, y=4)
    assert point.x == 3
    assert point.y == 4

def test_point_move():
    point = Point(x=3, y=4)
    point.move(dx=10, dy=20)
    assert point.x == 13
    assert point.y == 24

def test_toto():
    #assert False
    assert True

def test_f():
    point = Point(x=3, y=4)
    print(point.f(2.))

#test_f()

#test_point_init()
#test_point_move()