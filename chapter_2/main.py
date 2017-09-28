from chapter_2 import classes

p1a = classes.Point()
p1b = classes.Point()
p1a.x = 5
p1a.y = 4
p1b.x = 3
p1b.y = 6
print('Point class - values after assignment:')
print(p1a.x, p1b.y)
print(p1b.x, p1b.y)

p2 = classes.Point2()
# print('Point2 class - values before reset:')
# print(p2.x, p2.y)     # ERROR
p2.x = 10
p2.y = 20
print('Point2 class - values after assignment:')
print(p2.x, p2.y)
p2.reset()
print('Point2 class - values after a reset:')
print(p2.x, p2.y)


p3a = classes.Point3()
p3b = classes.Point3()
# Set the distance of p3a to (0,0)
p3a.reset()
# Set the distance of p3b to (5,0)
p3b.move(5, 0)
print('Point3 class - dist calc with p3a at (0,0) and p3b at (5,0)')
print(p3b.calculate_distance(p3a))  # 5.0

# Set the distance of p3a to (3,4)
p3a.move(3, 4)
print('Point3 class - dist calc with p3a at (3,4) and p3b at (5,0)')
print(p3b.calculate_distance(p3a))  # 4.47