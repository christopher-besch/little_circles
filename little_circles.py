from math import pi


# calculate area with an always doubling amount of smaller circles
def calculate_area(radius):
    # starting with two circles
    circles = 2
    while True:
        # area without small circles
        whole_area = radius ** 2 * pi / 2
        # radius of each smaller circle
        circle_radius = radius / circles
        # area of each smaller circle
        circle_area = pi * circle_radius ** 2 / 2

        # yield current number of smaller circles and final area
        yield circles, whole_area - circle_area * circles
        circles *= 2


# format a line for a table
def format_spaces(string1, string2, total_chars=40, min_spaces=1):
    num_spaces = total_chars - (len(str(string1)) + min_spaces)
    # add spaces if there are too few
    if num_spaces < min_spaces:
        num_spaces = min_spaces

    return str(string1) + " " * num_spaces + str(string2)


if __name__ == "__main__":
    # setup
    this_shape = calculate_area(int(input("Enter radius of the main half circle: ")))
    print("Press Enter to get a new value!")
    print()
    print(format_spaces("number of small circles", "area"))
    while True:
        # get values
        num_circles, area = next(this_shape)
        # print values and wait for continue request from user
        input(format_spaces(num_circles, f'{area:.16f}'))
