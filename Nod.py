import module_nod
a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
print(f"НОД этих чисел равен: {module_nod.nod(max(a,b),min(a,b))}")