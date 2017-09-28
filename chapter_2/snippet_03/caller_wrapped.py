from chapter_2.snippet_03.class_file_wrapped import Point3

a = Point3()
b = Point3()
a.reset()
b.move(4,0)

print(a.calculate_distance(b))
