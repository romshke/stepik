def BMI(mass, height):
    bmi = mass / (height**2)

    if bmi < 18.5:
        return 'Недостаточная масса'
    elif 18.5 <= bmi <= 25:
        return 'Оптимальная масса'
    else:
        return 'Избыточная масса'

print(BMI(float(input()), float(input())))