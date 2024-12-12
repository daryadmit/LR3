import math

class SphereSegment:
    def __init__(self, radius: float, height: float):
        self.__radius = radius
        self.__height = height

    @staticmethod
    def about():
        return "Программа расчета объема шарового сегмента. Команда разработки: [Даша, Ангелина]"

    def get_radius(self):
        return self.__radius

    def get_height(self):
        return self.__height


class SphereSegmentCalculator(SphereSegment):
    def volume(self) -> float:
        r = self.get_radius()
        h = self.get_height()
        volume = (math.pi * h**2 * (3*r - h)) / 3
        return volume


def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Значение должно быть положительным.")
            return value
        except ValueError as e:
            print(f"Ошибка ввода: {e}. Попробуйте снова.")


if __name__ == "__main__":
    print(SphereSegment.about())
    
    radius = get_positive_float("Введите радиус сферы: ")
    height = get_positive_float("Введите высоту сегмента: ")
    
    segment = SphereSegmentCalculator(radius=radius, height=height)
    
    print(f"Объем шарового сегмента: {segment.volume():.2f}")