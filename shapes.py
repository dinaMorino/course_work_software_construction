import math #импорт стандартной библиотеки мат. функций для выполнения тригонометрических операций
#классы  - геометрические фигуры
class Rectangle:# прямоугольник
    
    def perimeter(self,w,l):#вычисляет периметр прямоугольника
        self.width = w
        self.len = l
        return 2*self.width + 2*self.len
    
    def area_rect(self,w,l):#вычисляет площадь прямоугольника через стороны
        self.width = w
        self.len = l
        return self.width*self.len
    
    def area_square(self,a):#вычисляет площадь квадрата
        self.side = a
        return self.side**2
    
    def area_sin_rect(self,alfa,d1,d2):#вычисляет площадь прямоугольника через две диагонали и угол альфа между ними
        self.alfa = alfa
        self.diagonal1 = d1
        self.diagonal2 = d2
        alfa_rad = math.radians(self.alfa)
        sin_alfa = math.sin(alfa_rad)
        return (self.diagonal1*self.diagonal2*sin_alfa)/2

class Circle:#круг

    def circle_area(self,r):#вычисляет площадь круга
        self.radius = r
        pi = math.pi
        return pi*(self.radius**2)
    
    def circumference_rad(self,r):#вычисляет длину окружности через ее радиус
        self.radius = r
        pi = math.pi
        return 2*pi*self.radius
    
    def arc_length(self,alfa,r):#вычисляет длину дуги, alfa - угол, задающий дугу
        self.alfa = alfa
        self.radius = r
        pi = math.pi
        return (pi*self.radius*alfa)/180

class Triahgle:#треугольник

    def area_height(self,a,h):#вычисление площади треугольника по высоте и прилежащей стороне
        self.side = a
        self.height = h
        return (self.side*self.height)/2
    def area_angle(self,a,b,alfa):#вычисление площади через две стороны и синус угла между ними
        self.side_a = a
        self.side_b = b
        self.alfa = alfa
        alfa_rad = math.radians(self.alfa)
        sin_alfa = math.sin(alfa_rad)
        return (self.side_a*self.side_b*sin_alfa)/2




