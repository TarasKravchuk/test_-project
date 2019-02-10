#!/usr/bin/env python
import sys
sys.path.insert(0, '/home/taras/PycharmProjects/untitled15')
from geo_random.shapes.circle import *
from geo_random.shapes.square import *
from geo_random.shapes.triangle import *

def convertation (elements):
    elements = str(elements)
    elements = elements.split(",")
    elements = list(elements)
    float_elements = [float(i) for i in elements]
    return float_elements

if __name__ == "__main__":
    operation_name = sys.argv[1]; elements = sys.argv[2]
    if operation_name.lower() == "triangle":
        if len(convertation(elements)) is 6:
            point_1_x = convertation(elements)[0]
            point_1_y = convertation(elements)[1]
            point_2_x = convertation(elements)[2]
            point_2_y = convertation(elements)[3]
            point_3_x = convertation(elements)[4]
            point_3_y = convertation(elements)[5]
            TriangleShape(point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y).is_valid()
        else: print("Тriangle should to contain 6 coordinates, 3 points with coordinates X and Y each.\n Please try again")

    elif operation_name.lower() == "circle":
        if len(convertation(elements)) is 4:
            point_1_x = convertation(elements)[0]
            point_1_y = convertation(elements)[1]
            point_2_x = convertation(elements)[2]
            point_2_y = convertation(elements)[3]
            CircleShape(point_1_x, point_1_y, point_2_x, point_2_y).is_valid()
        else: print("Circle should to contain 4 coordinates, 2 points with coordinates X and Y each.\n Please try again")

    elif  operation_name.lower() == "square":
        print("Important! The order of specifying points in a rectangle must be specified by clockwise, otherwise the "
              "program may produce an error.")
        if len(convertation(elements)) is 8:
            point_1_x = convertation(elements)[0]
            point_1_y = convertation(elements)[1]
            point_2_x = convertation(elements)[2]
            point_2_y = convertation(elements)[3]
            point_3_x = convertation(elements)[4]
            point_3_y = convertation(elements)[5]
            point_4_x = convertation(elements)[6]
            point_4_y = convertation(elements)[7]
            SquareShape(point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y, point_4_x, point_4_y).is_valid()
        else:
            print("Square should to contain 8 coordinates, 4 points with coordinates X and Y each.\n Please try again")

    else: print("This program accepts only the following commands: 'square' (8 elements)  'circle' (4 elements)"
                " 'triangle' (6 elements)")
