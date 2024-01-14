import doctest


class Laptop:
    turn_on: bool = False

    def __init__(self, mem: int, company: str) -> None:
        """
        Конструктор класса ноутбук

        :param mem: количество оперативной памяти
        :param company: имя компании, чей ноутбук

        Примеры:
        >>> laptop = Laptop(15, 'HP')
        """

        if not isinstance(mem, int):
            raise TypeError('Количество оперативной памяти должно быть целым числом, измеряется в Гб')
        if not isinstance(company, str):
            raise TypeError('Название компании должно быть строкой')

        if len(company) < 1 or len(company) > 50:
            raise ValueError('Название компании не может быть пустой строкой и не может превышать 50 символов')
        if (mem and not (mem & mem - 1)) is False:
            raise ValueError('Количество оперативной памяти должно быть степенью 2')

        self.mem = mem
        self.company = company

    def update_mem(self, new_mem: int) -> None:
        """
        Обновить количество оперативной памяти

        :param new_mem: память, которую добавляем
        :return: Сколько сейчас оперативной памяти в ноутбуке

        Примеры:
        >>> laptop = Laptop(15, 'HP')
        >>> laptop.update_mem(8)
        Теперь в ноутбуке 24Гб оперативной памяти
        """

        if (new_mem and not (new_mem & new_mem - 1)) is False:
            raise ValueError('Новая оперативка должна быть степенью 2')
        self.mem += new_mem
        print(f"Теперь в ноутбуке {self.mem}Гб оперативной памяти")

    def turn_laptop_on(self) -> None:
        """
        Включить ноутбук

        :return: состояние ноутбука
        Примеры:
        >>> laptop = Laptop(15, 'HP')
        >>> laptop.turn_laptop_on()
        Ноутбук включен
        """
        self.turn_on = True
        print(f"Ноутбук включен")

    def turn_laptop_off(self) -> None:
        """
        Выключить ноутбук

        :return: состояние ноутбука
        Примеры:
        >>> laptop = Laptop(15, 'HP')
        >>> laptop.turn_laptop_off()
        Ноутбук выключен
        """
        self.turn_on = True
        print(f"Ноутбук выключен")


if __name__ == '__main__':
    doctest.testmod()
