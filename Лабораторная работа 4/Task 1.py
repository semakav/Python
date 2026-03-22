class Vehicle:
    """
    Базовый класс, представляющий транспортное средство.

    Атрибуты:
        _brand (str): Марка транспортного средства (непубличный).
        _model (str): Модель транспортного средства (непубличный).
        _year (int): Год выпуска (непубличный).
        _mileage (float): Пробег в километрах (непубличный).
    """

    def __init__(self, brand: str, model: str, year: int, mileage: float = 0.0) -> None:
        """
        Конструктор базового класса Vehicle.

        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска.
        :param mileage: Пробег в километрах (по умолчанию 0.0).

        Причина инкапсуляции: атрибуты не должны изменяться напрямую извне,
        чтобы избежать некорректных значений (например, отрицательного пробега).
        Доступ к ним предоставляется через геттеры.
        """
        self._brand = brand
        self._model = model
        self._year = year
        self._mileage = max(0.0, mileage)  # Пробег не может быть отрицательным

    def __str__(self) -> str:
        """
        Магический метод __str__. Возвращает удобочитаемое строковое представление объекта.

        :return: Строка с информацией о транспортном средстве для пользователя.
        """
        return f"{self._brand} {self._model} ({self._year} г.) - пробег: {self._mileage} км"

    def __repr__(self) -> str:
        """
        Магический метод __repr__. Возвращает формальное строковое представление объекта.

        :return: Строка, которая может быть использована для воссоздания объекта.
        """
        return (f"{self.__class__.__name__}("
                f"brand='{self._brand}', model='{self._model}', "
                f"year={self._year}, mileage={self._mileage})")

    def drive(self, distance: float) -> str:
        """
        Метод, имитирующий движение транспортного средства.

        :param distance: Расстояние в километрах.
        :return: Сообщение о поездке.
        """
        if distance <= 0:
            return "Расстояние должно быть положительным числом."
        self._mileage += distance
        return f"Проехали {distance} км. Общий пробег: {self._mileage} км."

    def get_info(self) -> str:
        """
        Метод для получения полной информации о транспортном средстве.

        :return: Строка с полной информацией.
        """
        return f"ТС: {self._brand} {self._model}, {self._year} г.в., пробег: {self._mileage} км"

    def get_brand(self) -> str:
        """Геттер для марки."""
        return self._brand

    def get_model(self) -> str:
        """Геттер для модели."""
        return self._model

    def get_year(self) -> int:
        """Геттер для года выпуска."""
        return self._year

    def get_mileage(self) -> float:
        """Геттер для пробега."""
        return self._mileage


class Car(Vehicle):
    """
    Дочерний класс, представляющий легковой автомобиль.
    Наследует все атрибуты и методы от Vehicle, добавляет специфические для легковых авто характеристики.

    Атрибуты:
        _body_type (str): Тип кузова (непубличный).
        _engine_power (int): Мощность двигателя в лошадиных силах (непубличный).
        _is_electric (bool): Признак электромобиля (непубличный).
    """

    def __init__(self, brand: str, model: str, year: int, mileage: float,
                 body_type: str, engine_power: int, is_electric: bool = False) -> None:
        """
        Конструктор дочернего класса Car. Расширяет конструктор базового класса.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска.
        :param mileage: Пробег.
        :param body_type: Тип кузова (седан, хэтчбек, универсал и т.д.).
        :param engine_power: Мощность двигателя в л.с.
        :param is_electric: Является ли автомобиль электромобилем.

        Причина инкапсуляции: данные атрибуты характеризуют автомобиль
        и не должны изменяться после создания объекта.
        """
        # Расширение конструктора базового класса
        super().__init__(brand, model, year, mileage)
        self._body_type = body_type
        self._engine_power = max(0, engine_power)  # Мощность не может быть отрицательной
        self._is_electric = is_electric

    def __str__(self) -> str:
        """
        Перегрузка магического метода __str__.
        Расширяет базовую реализацию, добавляя информацию о типе кузова.

        :return: Удобочитаемое строковое представление автомобиля.
        """
        base_str = super().__str__()
        return f"{base_str}, кузов: {self._body_type}"

    def __repr__(self) -> str:
        """
        Перегрузка магического метода __repr__.
        Расширяет базовую реализацию, добавляя специфические атрибуты Car.

        :return: Строка для воссоздания объекта Car.
        """
        return (f"{self.__class__.__name__}("
                f"brand='{self._brand}', model='{self._model}', "
                f"year={self._year}, mileage={self._mileage}, "
                f"body_type='{self._body_type}', engine_power={self._engine_power}, "
                f"is_electric={self._is_electric})")

    def get_info(self) -> str:
        """
        Перегрузка метода get_info.
        Причина перегрузки: для легкового автомобиля нужно отобразить дополнительную
        информацию: тип кузова и мощность двигателя, что делает метод более полезным
        для пользователя.

        :return: Расширенная строка с полной информацией об автомобиле.
        """
        electric_status = " (электромобиль)" if self._is_electric else ""
        return (f"Автомобиль: {self._brand} {self._model}, {self._year} г.в., "
                f"пробег: {self._mileage} км, кузов: {self._body_type}, "
                f"мощность: {self._engine_power} л.с.{electric_status}")

    def drive(self, distance: float) -> str:
        """
        Наследование метода drive без изменений.
        Используется реализация базового класса.

        :param distance: Расстояние в километрах.
        :return: Сообщение о поездке.
        """
        return super().drive(distance)

    def honk(self) -> str:
        """
        Специфический метод для легкового автомобиля — сигнал.

        :return: Строка со звуком сигнала.
        """
        return f"{self._brand} {self._model} сигналит: Бип-бип!"

    def get_body_type(self) -> str:
        """Геттер для типа кузова."""
        return self._body_type

    def get_engine_power(self) -> int:
        """Геттер для мощности двигателя."""
        return self._engine_power

    def is_electric(self) -> bool:
        """Геттер для признака электромобиля."""
        return self._is_electric





