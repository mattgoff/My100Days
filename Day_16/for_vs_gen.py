import calendar
import timeit

#list
def leap_years_list(n=1000000):
    leap_years = []
    for year in range(1, n+1):
        if calendar.isleap(year):
            leap_years.append(year)
        return leap_years

#generator
def leap_years_gen(n=10000):
    for year in range(1, n+1):
        if calendar.isleap(year):
            yield year

print(timeit.Timer(leap_years_list).timeit(number=1))
print(timeit.Timer(leap_years_gen).timeit(number=1))
print(list(leap_years_gen()))