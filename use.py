import maths as m;
a=m.arithmetic();
x=int(input("Enter first number"));
y=int(input("Enter second number"));
a.add(x,y);
a.sub(x,y);
a.mul(x,y);
a.div(x,y);
a.mod(x,y);

p = m.area();
r = float(input("Enter the radius of the circle"));
p.circle(r);
s = float(input("Enter the side of the square"));
p.square(s);