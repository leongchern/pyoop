from chapter_2 import classes

p1 = classes.Point()
p2 = classes.Point()
p1.x = 5
p1.y = 4
p2.x = 3
p2.y = 6
print(p1.x, p2.y)
print(p2.x, p2.y)

p3 = classes.Point2()
p3.reset()
print(p3.x, p3.y)

p4 = classes.Point3()
p5 = classes.Point3()
p4.reset()
p5.move(5,0)
print(p5.calculate_distance(p4))

p4.move(3,4)
print(p4.calculate_distance(p5))