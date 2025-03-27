numbers_divided_by_five = [x for x in range(101) if x % 5 == 0]
print("Liczby podzielne przez 5:", numbers_divided_by_five)

numbers_to_the_power_of_three = [x**3 for x in numbers_divided_by_five]
print("Te liczby podniesione do potęgi 3:", numbers_to_the_power_of_three)