import sqlite3

connect = sqlite3.connect("cars.db")
cursor = connect.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS cars(
                   id INTEGER PRIMARY KEY,
                   mark VARCHAR(255),
                   model VARCHAR(255) ,
                   year INTEGER,
                   desc VARCHAR(255),
                   status VARCHAR(255),
                   number VARCHAR(9)
               )
               """)

class Car:
    def __init__(self):
        self.mark = None
        self.model = None
        self.year = 0
        self.desc = None
        self.status = None
        self.number = None
    def add_car(self, mark, model, year, desc, status, number):
        self.mark = mark
        self.model = model
        self.year = year
        self.desc = desc
        self.status = status
        self.number = number
        cursor.execute(f"""
                       INSERT INTO cars(mark, model, year, desc, status, number) VALUES ('{self.mark}', '{self.model}', {self.year}, '{self.desc}', '{self.status}', '{self.number}')
                       """)
        connect.commit()
    
    def info_car(self):
        cursor.execute("""
                       SELECT * FROM cars
                       """)
        cars = cursor.fetchall()
        return cars
    
    def update(self):
        car_id = int(input("Введите ID авто что изменить данные: "))
        mark = input("Введите новую марку авто: ")
        model = input("Введите новую модель авто: ")
        year = int(input("Новый год выпуска авто: "))
        desc = input("Новое описание работы: ")
        status = input("Новый статус работы: ")
        number = input("Новый ГОС номер авто: ")
        
        cursor.execute("""
                       UPDATE cars SET mark = ?, model = ?, year = ?, desc = ?, status = ?, number = ?
                       WHERE id = ?
                       """, (mark, model, year, desc, status, number, car_id))
        connect.commit()
        
    
    def main(self):
        while True:
            commands = input("1 - Добавить авто: \n2 - Посмотреть информацию об автомобилях: \n3 - Обновть инфо: ")
            if commands == "1":
                mark = input("Введите марку авто: ")
                model = input("Введите модель авто: ")
                year = int(input("Год выпуска авто: "))
                desc = input("Описание работы: ")
                status = input("Статус работы: ")
                number = input("ГОС номер авто: ")
                self.add_car(mark, model, year, desc, status, number)
            elif commands == "2":
                for i in self.info_car():
                    print(f'\n<------------------------ ID: {i[0]} ---------------------->')
                    print(f'_____________________ Марка: {i[1]} _____________________')
                    print(f'_____________________ Модель: {i[2]} _____________________')
                    print(f'_____________________ Год выпуска: {i[3]} _____________________')
                    print(f'_____________________ Описание: {i[4]} _____________________')
                    print(f'_____________________ Статус: {i[5]} _____________________')
                    print(f'_____________________ Номер авто: {i[6]} _____________________\n')
            elif commands == "3":
                self.update()

car = Car()
car.main()