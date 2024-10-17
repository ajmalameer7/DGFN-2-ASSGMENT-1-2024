'''
TPRG 2131 Fall 202x Assignment 1, Test file template.
Sept, 202x
Phil J <philip.jarvis@durhamcollege>


This file is to be the test_A_V_calc.py file to be used with your A_V_calc.py and pytest.
This must test each of your Area/Volume functions, with a least 3 examples for each of the
5 functions your chose to use.

As this stands it will NOT work with your A_V_calc.py file.
'''

#!/usr/bin/env python
# coding: utf-8

import pytest
from A_V_calc import area_rectangle, area_circle, area_triangle, volume_cube, volume_cylinder

# Test for area_rectangle
def test_area_rectangle():
    """Test cases for the area of a rectangle."""
    assert area_rectangle(3, 4) == 12  # 3 * 4 = 12
    assert area_rectangle(5, 2) == 10  # 5 * 2 = 10
    assert area_rectangle(0, 4) == 0   # 0 * 4 = 0

# Test for area_circle
def test_area_circle():
    """Test cases for the area of a circle using approximate values for floating point results."""
    assert area_circle(3) == pytest.approx(28.274, 0.001)  # Approximation for pi * 3^2
    assert area_circle(1) == pytest.approx(3.141, 0.001)   # Approximation for pi * 1^2
    assert area_circle(0) == 0  # Area of a circle with radius 0 is 0

# Test for area_triangle
def test_area_triangle():
    """Test cases for the area of a triangle."""
    assert area_triangle(3, 4) == 6  # 0.5 * 3 * 4 = 6
    assert area_triangle(5, 2) == 5  # 0.5 * 5 * 2 = 5
    assert area_triangle(0, 4) == 0  # 0.5 * 0 * 4 = 0

# Test for volume_cube
def test_volume_cube():
    """Test cases for the volume of a cube."""
    assert volume_cube(3) == 27  # 3^3 = 27
    assert volume_cube(2) == 8   # 2^3 = 8
    assert volume_cube(0) == 0   # Volume of a cube with side 0 is 0

# Test for volume_cylinder
def test_volume_cylinder():
    """Test cases for the volume of a cylinder using approximate values for floating point results."""
    assert volume_cylinder(3, 4) == pytest.approx(113.097, 0.001)  # Approximation for pi * 3^2 * 4
    assert volume_cylinder(1, 1) == pytest.approx(3.141, 0.001)    # Approximation for pi * 1^2 * 1
    assert volume_cylinder(0, 4) == 0   # Volume of a cylinder with radius 0 is 0
