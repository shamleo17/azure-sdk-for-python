# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class RasterOp(str, Enum):

    no_operation = "noOperation"
    copy_pen = "copyPen"
    mask_pen = "maskPen"


class Tip(str, Enum):

    ellipse = "ellipse"
    rectangle = "rectangle"


class Shape(str, Enum):

    drawing = "drawing"
    square = "square"
    rectangle = "rectangle"
    circle = "circle"
    ellipse = "ellipse"
    triangle = "triangle"
    isosceles_triangle = "isoscelesTriangle"
    equilateral_triangle = "equilateralTriangle"
    right_triangle = "rightTriangle"
    quadrilateral = "quadrilateral"
    diamond = "diamond"
    trapezoid = "trapezoid"
    parallelogram = "parallelogram"
    pentagon = "pentagon"
    hexagon = "hexagon"
    block_arrow = "blockArrow"
    heart = "heart"
    star_simple = "starSimple"
    star_crossed = "starCrossed"
    cloud = "cloud"
    line = "line"
    curve = "curve"
    poly_line = "polyLine"


class Category(str, Enum):

    root = "root"
    writing_region = "writingRegion"
    paragraph = "paragraph"
    line = "line"
    ink_bullet = "inkBullet"
    ink_drawing = "inkDrawing"
    ink_word = "inkWord"
    unknown = "unknown"


class Container(str, Enum):

    root = "root"
    writing_region = "writingRegion"
    paragraph = "paragraph"
    line = "line"


class Leaf(str, Enum):

    ink_drawing = "inkDrawing"
    ink_bullet = "inkBullet"
    ink_word = "inkWord"
    unknown = "unknown"


class Kind(str, Enum):

    ink_drawing = "inkDrawing"
    ink_writing = "inkWriting"


class Unit(str, Enum):

    mm = "mm"
    cm = "cm"
    in_enum = "in"


class Application(str, Enum):

    drawing = "drawing"
    writing = "writing"
    mixed = "mixed"


class InputDevice(str, Enum):

    digitizer = "digitizer"
    pen = "pen"
    light_pen = "lightPen"
    touch_screen = "touchScreen"
    touch_pad = "touchPad"
    white_board = "whiteBoard"
    threed_digitizer = "3dDigitizer"
    stereo_plotter = "stereoPlotter"
    articulated_arm = "articulatedArm"
    armature = "armature"