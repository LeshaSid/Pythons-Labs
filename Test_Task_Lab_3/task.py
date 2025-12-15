# класс музыкальные инструменты

class MyException(Exception):
    pass

class Instrument:
    def __init__(self, weight):
        self.weight = weight

class Guitar(Instrument):
    _TYPE = ["акустическая гитара", "классическая гитара", "электрогитара"]
    
    def __init__(self, weight, beaker, amount_of_frets, amount_of_strings, type_guitar):
        super().__init__(weight)
        if beaker > 0:
            self.beaker = beaker
        else:
            raise MyException("Мензура должна быть положительной")

        if type_guitar in Guitar._TYPE:
            self.type_guitar = type_guitar
        else:
            raise MyException(f"Тип гитары должен быть одним из: {Guitar._TYPE}")

        if amount_of_strings >= 6 and amount_of_strings <= 8:
            self.amount_of_strings = amount_of_strings
        else:
            raise MyException("Количество струн должно быть от 6 до 8")

        if amount_of_frets > 0 and amount_of_frets <= 24:
            self.amount_of_frets = amount_of_frets
        else:
            raise MyException("Количество ладов должно быть от 1 до 24")

    @classmethod
    def create(cls):
        weight = int(input("Введите массу(кг): "))
        beaker = int(input("Введите мензуру гитары(мм): "))
        amount_of_frets = int(input("Введите количество ладов(1-24): "))
        amount_of_strings = int(input("Введите количество струн(6-8): "))
        type_guitar = input(f"Выберите тип гитары {cls._TYPE}: ")
        return cls(weight, beaker, amount_of_frets, amount_of_strings, type_guitar)

    def get_info(self):
        print("="*35)
        print("Гитара")
        print("-"*35)
        print(f"Масса: {self.weight} кг")
        print(f"Мензура: {self.beaker} мм")
        print(f"Количество ладов: {self.amount_of_frets}")
        print(f"Количество струн: {self.amount_of_strings}")
        print(f"Тип гитары: {self.type_guitar}")
        print("="*35)
        


class Piano(Instrument):
    _TYPE = ["рояль", "фортепиано"]
    
    def __init__(self, weight, type_piano, amount_of_keys):
        super().__init__(weight)
        if type_piano.lower() in Piano._TYPE:
            self.type_piano = type_piano.lower()
        else:
            raise MyException(f"Тип пианино должен быть одним из: {Piano._TYPE}")

        if amount_of_keys > 0:
            self.amount_of_keys = amount_of_keys
        else:
            raise MyException("Количество клавиш должно быть положительным")

    @classmethod
    def create(cls):
        weight = int(input("Введите массу(кг): "))
        amount_of_keys = int(input("Введите количество клавиш: "))
        type_piano = input(f"Выберите тип пианино {cls._TYPE}: ").lower()
        return cls(weight, type_piano, amount_of_keys)

    def get_info(self):
        print("="*35)
        print("Пианино")
        print("-"*35)
        print(f"Масса: {self.weight} кг")
        print(f"Количество клавиш: {self.amount_of_keys}")
        print(f"Тип пианино: {self.type_piano}")
        print("="*35)


class Drums(Instrument):
    _TYPE = ["бочка", "том 1", "том 2", "том 3", "малый барабан", "хай-хэт", "крэш", "райд"]
    
    def __init__(self, weight, drum_list):
        super().__init__(weight)
        self.drum_list = []
        for drum in drum_list:
            if drum in Drums._TYPE:
                self.drum_list.append(drum)
            else:
                raise MyException(f"Барабан '{drum}' не входит в допустимый список: {Drums._TYPE}")

    @classmethod
    def create(cls):
        weight = int(input("Введите массу(кг): "))
        print(f"Доступные барабаны: {cls._TYPE}")
        print("Введите названия барабанов через запятую:")
        drum_input = input().lower()
        drum_list = [drum.strip() for drum in drum_input.split(',')]
        return cls(weight, drum_list)

    def get_info(self):
        print("="*35)
        print("Барабанная установка")
        print("-"*35)
        print(f"Масса: {self.weight} кг")
        print(f"Состав: {self.drum_list}")
        print("="*35)

class Main():
    def main(self):
        while True:
            try:
                ans = int(input("""
                1 - Выбрать инструмент
                2 - Выйти
                """))
                if ans == 1:
                    ans = int(input("""
                    1 - Гитара
                    2 - Пианино
                    3 - Барабаны
                    """))
                    if ans == 1:
                        instr = Guitar.create()
                    elif ans == 2:
                        instr = Piano.create()
                    elif ans == 3:
                        instr = Drums.create()
                    else:
                        raise MyException("Неверный выбор инструмента")

                    instr.get_info()

                elif ans == 2:
                    break
                
                else:
                    raise MyException("Неверный выбор в главном меню")
                    
            except MyException as e:
                print(f"Ошибка: {e}")
            except ValueError:
                print("Ошибка: Введите корректное число")
            except Exception as e:
                print(f"Неизвестная ошибка: {e}")
    
if __name__ == "__main__":
    app = Main()
    app.main()