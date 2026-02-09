# TODO Написать 3 класса с документацией и аннотацией типов
class Car:
    def __init__(self, max_speed: float, power: float):
        """
        Создание и подготовка к работе объекта "Автомобиль"
        :param max_speed: Максимальная скорость
        :param power: Мощность
        """
        if not isinstance(max_speed, float):
            raise TypeError("Максимальная скорость должна быть типа float")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом")
        self.max_speed = max_speed
        if not isinstance(power, float):
            raise TypeError("Мощность должна быть типа float")
        if power <= 0:
            raise ValueError("Мощность должна быть положительным числом")
        self.power = power
    def is_car_more_powerful(self, needed_power: float) -> bool:
        """
        Функция, которая проверяет, больше ли мощность автомобиля, чем требуемая
        :param needed_power: Необходимая мощность
        :return: Больше ли мощность автомобиля, чем требуемая
        """
        if not isinstance(needed_power, float):
            raise TypeError("Необходимая мощность должна быть типа float")
        if needed_power < 0:
            raise ValueError("Необходимая мощность должна положительным числом")
        ...
    def add_power(self, added_power: float) -> None:
        """
        Функция, добавляющая мощность
        :param added_power: Добавленная мощность
        """
        if not isinstance(added_power, float):
            raise TypeError("Добавляемая мощность должна быть типа float")
        if added_power < 0:
            raise ValueError("Добавляемая мощность должна положительным числом")
        ...

class Monitor:
    def __init__(self, diagonal: float, manufacturer: str):
        """
        Создание и подготовка к работе объекта "Монитор"
        :param diagonal: Диагональ экрана
        :param manufacturer: Производитель
        """
        if not isinstance(diagonal, float):
            raise TypeError("Диагональ экрана должна быть типа float")
        if diagonal <= 0:
            raise ValueError("Диагональ экрана должна быть положительным числом")
        self.diagonal = diagonal
        if not isinstance(manufacturer, str):
            raise TypeError("Производитель должен быть типа str")
        self.manufacturer = manufacturer
    def check_diagonal(self, needed_diagonal: float) -> bool:
        """
        Функция, которая проверяет, больше ли диагональ монитора, чем требуемая
        :param needed_diagonal: Необходимая диагональ монитора
        :return: Больше ли диагональ монитора, чем требуемая
        """
        if not isinstance(needed_diagonal, float):
            raise TypeError("Необходимая диагональ монитора должна быть типа float")
        if needed_diagonal < 0:
            raise ValueError("Необходимая диагональ монитора должна положительным числом")
        ...
    def check_monitor(self, list1: list) -> bool:
        """
        Функция, проверяющая, принадлежит ли производитель списку
        :param list1: Список производителей
        :return: Принадлежит ли производитель списку
        """
        if not isinstance(list1, list):
            raise TypeError("Добавляемая мощность должна быть типа list")
        ...

class CPU:
    def __init__(self, number_of_cores: int, frequency: float):
        """
        Создание и подготовка к работе объекта "Процессор"
        :param max_speed: Количество ядер
        :param power: Частота
        """
        if not isinstance(number_of_cores, int):
            raise TypeError("Количество ядер должно быть типа int")
        if number_of_cores < 1:
            raise ValueError("Количество ядер должно быть больше либо 1")
        self.number_of_cores = number_of_cores
        if not isinstance(frequency, float):
            raise TypeError("Частота должна быть типа float")
        if frequency <= 0:
            raise ValueError("Частота должна быть положительным числом")
        self.frequency = frequency

    def more_cores_or_not(self, needed_number_of_cores: int) -> bool:
        """
        Функция, которая проверяет, больше ли количество ядер процессора, чем требуемое
        :param needed_power: Необходимоя количество ядер процессора
        :return: Больше ли количество ядер процессора, чем требуемая
        """
        if not isinstance(needed_number_of_cores, int):
            raise TypeError("Необходимая мощность должна быть типа int")
        if needed_number_of_cores < 0:
            raise ValueError("Необходимая мощность должна положительным числом")
        ...

    def add_frequency(self, added_frequency: float) -> None:
        """
        Функция, увеличивающая частоту
        :param added_power: Добавляемая частота
        """
        if not isinstance(added_frequency, float):
            raise TypeError("Добавляемая частота должна быть типа float")
        if added_frequency < 0:
            raise ValueError("Добавляемая частота должна положительным числом")
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
