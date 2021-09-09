class arithmetic:
  def add(self,x,y):
    self.c = x+y;
    print("The sum is ",self.c);
  def sub(self,x,y):
    self.c = x-y;
    print("The difference is ",self.c);
  def mul(self,x,y):
    self.c = x*y;
    print("The product is ",self.c);
  def div(self,x,y):
    self.c = x/y;
    print("The division is ",self.c);
  def mod(self,x,y):
    self.c = x%y;
    print("The modulo division is ",self.c);

class area:
  def square(self,side):
    self.result = side*side;
    print("The area of square is ",self.result);
  def circle(self,radius):
    self.result = 3.1416*radius*radius;
    print("The area of circle is ",self.result);    