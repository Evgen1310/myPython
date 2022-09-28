from datetime import datetime, timedelta
try:
    print("Введите дату рождения пользователя в формате ДД/ММ/ГГ")
    dr = datetime.strptime(input(), "%d/%m/%y")
except:
    print("Ошибка")
    exit()
dayy=10000
minn=1000000
secc=1000000000
print(f"Пользователю исполнится 10000 дней {dr+timedelta(days=dayy)}")
print(f"Пользователю исполнится 1000000 минут {dr+timedelta(minutes=minn)}")
print(f"Пользователю исполнится 1000000000 секунд {dr+timedelta(seconds=secc)}")