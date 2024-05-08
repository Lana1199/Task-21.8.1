from rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

print("Площадь прямоугольника 1 =", rect_1.get_area())
print("Площадь прямоугольника 2 =",rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print("Площадь квадрата 1 =", square_1.get_area_square(),
      "Площадь квадрата 2 =", square_2.get_area_square())


circle_1 = Circle(10)
circle_2 = Circle(16)

print("Площадь круга 1 =" , round(circle_1.get_area_circle(),2),
      "Площадь круга 2 ="  , round(circle_2.get_area_circle(),2))

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
      if isinstance(figure, Square):
            print(figure.get_area_square())
      if isinstance(figure, Circle):
            print(figure.get_area_circle())
      else:
            print(figure.get_area())

