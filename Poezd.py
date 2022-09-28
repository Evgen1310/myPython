from datetime import datetime, timedelta
try:
    print('Введите дату отправления поезда в формате ДД/ММ/ГГ ЧЧ:ММ')
    start_date = datetime.strptime(input(), "%d/%m/%y %H:%M")
except:
    print('Дата в неверном формате')
    exit()
try:
    print('Введите дату прибытия поезда в формате ДД/ММ/ГГ ЧЧ:ММ')
    end_date = datetime.strptime(input(), "%d/%m/%y %H:%M")
except:
    print('Дата в неверном формате')
    exit()
time_travel=end_date-start_date
print(time_travel)