#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: Feb 2022
# This program calculates the area and perimeter of a rectangle
#    with radius inputted by the user


def main():
    # this function calculates the area and perimeter

    # input
    length = int(input("Enter the length of the rectangle (mm): "))
    width = int(input("Enter the width of the rectangle (mm): "))

    # process
    area = length * width
    perimeter = 2 * (length + width)

    # output
    print("")
    print("Area is {0} mm².".format(area))
    print("Perimeter is {0} mm.".format(perimeter))

    print("\nDone.")


if __name__ == "__main__":
    main()
