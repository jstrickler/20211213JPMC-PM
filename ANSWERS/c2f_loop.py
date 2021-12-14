#!/usr/bin/env python

while True:
    celsius = input('Enter Celsius temp: ')
    if celsius.lower().startswith('q'):
        break
    if celsius.strip() == '':
        print("please enter a number")
        continue
    celsius = float(celsius)
    fahrenheit = ((9 * celsius) / 5) + 32
    print('{:.1f} C is {:.1f} F\n'.format(celsius, fahrenheit))

