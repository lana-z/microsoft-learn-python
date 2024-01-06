planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")


print("There are", len(planets), "planets")

planets.append("Pluto")

print("Actually, there are", len(planets), "planets")

print(planets[-1], "is the last planet")



gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 124054 # in Newtons, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "N")
print("On Mercury, a double-decker bus weighs", round(bus_weight * gravity_on_planets[0]), "N")



print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "N")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "N")


user_planet = input("Please enter the name of a planet using a capital letter for the first letter")
planet_index = planets.index(user_planet)

print("The planets closer to the sun than " + user_planet + " are:")
print(planets[0:planet_index])
print("The planets further from the sun than " + user_planet + " are:")
print(planets[planet_index + 1: ])

