# unit 3 Python error handling - did not work
# def main():
#     try:
#         configuration = open('config.txt')
#     except Exception:
#         print("Couldn't find the config.txt file!")


# if __name__ == '__main__':
#     main()


# def main():
#     try:
#         configuration = open('config.txt')
#     except FileNotFoundError:
#         print("Couldn't find the config.txt file!")
#     except IsADirectoryError:
#         print("Found config.txt but it is a directory, couldn't read it")
#     except (BlockingIOError, TimeoutError):
#         print("Filesystem under heavy load, can't complete reading configuration file")


# def read_contents_of_config(path)


# Unit 4 Python error handling - is working correctly

# loaded_config = """# Rocket Ship Configuration File!
# fuel_tanks=4
# oxygen_tanks=3
# initial_propulsion_level=84
# $ End of file"""


# parsed_config = {}
# for line in loaded_config.split('\n'):
#     try:
#         key, value = line.split('=')
#         parsed_config[key] = value
#     except ValueError:
#         print(f'Unable to parse {line}')
# print(parsed_config)


# def water_left(astronauts, water_left, days_left):
#     daily_usage = astronauts * 11
#     total_usage = daily_usage * days_left
#     total_water_left = water_left - total_usage
#     if total_water_left < 0:
#         raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
#     return f"Total water left after {days_left} days is: {total_water_left} liters"



# try:
#     water_left(5, 100, 2)
# except RuntimeError as err:
#     alert_navigation_system(err)


# print(water_left(5, 100, 2))
# print(water_left("3", "200", None))


def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            # If argument is an int, the following operation will work
            argument / 10
        except TypeError:
            # TypeError will be raised only if it isn't the right type 
            # Raise the same exception but with a better error message
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"


