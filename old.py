import math

def cartesian_to_polar(x, y):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return r, theta

def cartesian_to_cylindrical(x, y, z):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return r, theta, z

# Example usage:
x, y, z = 3, 4, 5  # Cartesian coordinates
r_polar, theta_polar = cartesian_to_polar(x, y)
print("Cartesian to Polar:")
print("Cartesian Coordinates:", (x, y))
print("Polar Coordinates:", (r_polar, theta_polar))

r_cylindrical, theta_cylindrical, z_cylindrical = cartesian_to_cylindrical(x, y, z)
print("\nCartesian to Cylindrical:")
print("Cartesian Coordinates:", (x, y, z))
print("Cylindrical Coordinates:", (r_cylindrical, theta_cylindrical, z_cylindrical))
