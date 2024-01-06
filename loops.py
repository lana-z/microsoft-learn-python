
from time import sleep

new_planet = ''
planets = []

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Enter a new planet, or done if done ')

# note the difference in display output for these next two
print(planets)

for planet in planets:
    print(planet)

countdown = [3, 2, 1]

for number in countdown:
    print(number)
    sleep(1)  # Wait 1 second
print("Blast off!! 🚀")