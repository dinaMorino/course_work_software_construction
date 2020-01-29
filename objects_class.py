import shapes

rect_1 = shapes.Rectangle()
print(rect_1.perimeter(10,7))
print(rect_1.area_rect(10,7))
print(rect_1.area_sin_rect(30,9,28))

circle_1 = shapes.Circle()
print(circle_1.circle_area(5))
print(circle_1.circumference_rad(5))
print(circle_1.arc_length(45,8))

triang_1 = shapes.Triangle()
print(triang_1.area_height(2,4))
print(triang_1.area_angle(2,3,90))
