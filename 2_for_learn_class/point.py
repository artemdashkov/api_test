"""Пройти по списку и :
1. вывести в консоли full name (firstName + lastName)
2. посчитать и вывести в консоли итоговую зарплату
3. вывести имена, где в фамилия = Rose
4. посчитать и вывести количество уникальных фамилий
"""
users = [
    {
        "firstName": "John",
        "lastName": "Rose",
        "gender": "male",
        "salary": 200
    },
    {
        "firstName": "Margo",
        "lastName": "Rose",
        "gender": "male",
        "salary": 150
    },
    {
        "firstName": "Lisa",
        "lastName": "Barcley",
        "gender": "male",
        "salary": 1600
    },
    {
        "firstName": "John",
        "lastName": "Rose",
        "gender": "male",
        "salary": 2600
    },
]

salary = 0
# 1 task: вывести в консоли full name (firstName + lastName)
for user in users:
    print(f"full name: {user['firstName']} {user['firstName']}")
    salary += user["salary"]

# 2 task: посчитать и вывести в консоли итоговую зарплату
print(f"итоговая зарплата: {salary}\n")

# 3 task: вывести имена, где в фамилия = Rose
users_lastName_is_rose = [user["firstName"] for user in users if user["lastName"] == "Rose"]
print(f"имена, где в фамилия = Rose: {users_lastName_is_rose}\n")

# 4 task: посчитать и вывести количество уникальных фамилий
count_unik_lastname = []
for user in users:
    count_unik_lastname.append(user["lastName"])
print(f"Количество уникальных фамилий: {len(set(count_unik_lastname))}")
print(f"Уникальные фамилии: {set(count_unik_lastname)}")
