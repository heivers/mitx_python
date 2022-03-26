import math

pi = math.pi

def area(radius):
    return pi*(radius**2)

def circumference(radius):
    return 2*pi*radius

def sphere_surface(radius):
    return 4*area(radius)

def sphere_volume(radius):
    return (4/3)*pi*(radius**3)
