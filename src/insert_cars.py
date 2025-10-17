"""
insert_cars.py

This script populates the `table_car` table in the `hw_1_database.db`
SQLite database with the latest vehicle data of the Car Salon.
It ensures old records are removed and inserts 20 new cars with proper owner IDs.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "hw_1_database.db"

def populate_table_car():
    cars_data = [
        ('У314ОМ77', 'Chevrolet', 'Помятый задний бампер', 1),
        ('О006ОО178', 'Lorraine-Dietrich', 'Царапины на левом крыле', 2),
        ('К994ХЕ78', 'Tesla', 'Только с завода', 2),
        ('С569ТВ78', 'Lorraine-Dietrich', 'Помятая левая дверь, царапина на переднем бампере', 3),
        ('С614СА23', 'Alfa Romeo', 'Лобовое стекло в трещинах', 4),
        ('С746ОР78', 'Tesla', 'Только с завода, проблема с документами', 2),
        ('Н130КЕ777', 'Lorraine-Dietrich', 'Раритетная модель, перебрать двигатель', 5),
        ('Н857СК27', 'Lada', 'Не заводится, без внешних повреждений', 2),
        ('У657СА77', 'Lada', 'Не читается VIN', 1),
        ('Е778ВЕ178', 'Ford', 'Поменять габаритные лампы, резину на зимнюю', 6),
        ('К886УН68', 'Lada', 'Клиент жаловался на тёмные выхлопы при езде в городе', 7),
        ('Н045МО97', 'Lada', 'Разбита левая фара, помят передний бампер', 5),
        ('Т682КО777', 'Alfa Romeo', 'Поменять резину на зимнюю. Царапина на капоте (?)', 6),
        ('О147НМ78', 'Chevrolet', 'Провести ТО №9', 4),
        ('К110ТА77', 'Lada', 'Развал-схождение + замена резины', 7),
        ('Е717ОЕ78', 'Chevrolet', 'Помята водительская дверь, заменить габаритки', 4),
        ('У261ХО57', 'Ford', 'Заменить резину, проверить свечи', 2),
        ('М649ОМ78', 'Alfa Romeo', 'Непонятные шумы при заводе', 1),
        ('С253НО90', 'Ford', 'Заменить аккумулятор, проверить свечи', 3),
        ('А757АХ11', 'Nissan', 'ТО, клиент жалуется, что машину косит влево', 8)
    ]

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        # Optional: remove old records
        cursor.execute("DELETE FROM table_car;")

        # Insert all cars in one command
        cursor.execute("""
            INSERT INTO table_car (car_number, name, description, belongs_to)
            VALUES
            (?, ?, ?, ?),
            (?, ?, ?, ?),
            (?, ?, ?, ?),
            (?, ?, ?, ?),
            (?, ?, ?, ?),
            (?, ?, ?, ?),
            (?, ?, ?, ?),
            (?, ?, ?, ?),
            (?, ?, ?, ?),
            (?, ?, ?, ?),
            (?, ?, ?, ?),
            (?, ?, ?, ?),
            (?, ?, ?, ?),
            (?, ?, ?, ?),
            (?, ?, ?, ?),
            (?, ?, ?, ?),
            (?, ?, ?, ?),
            (?, ?, ?, ?),
            (?, ?, ?, ?),
            (?, ?, ?, ?);
        """, [val for car in cars_data for val in car])

        conn.commit()
        print("✅ table_car populated successfully!")

        # Optional: print results
        cursor.execute("SELECT * FROM table_car;")
        for row in cursor.fetchall():
            print(row)


if __name__ == "__main__":
    populate_table_car()
