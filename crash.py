import math

# Polar to Cylindrical
def polar_to_cylindrical(rho, theta, z):
    x = rho * math.cos(theta)
    y = rho * math.sin(theta)
    return x, y, z

# Polar to Rectangular
def polar_to_rectangular(rho, theta):
    x = rho * math.cos(theta)
    y = rho * math.sin(theta)
    return x, y

# Polar to Spherical
def polar_to_spherical(rho, theta, phi):
    x = rho * math.sin(phi) * math.cos(theta)
    y = rho * math.sin(phi) * math.sin(theta)
    z = rho * math.cos(phi)
    return x, y, z

# Rectangular to Spherical
def rectangular_to_spherical(x, y, z):
    rho = math.sqrt(x**2 + y**2 + z**2)
    theta = math.atan2(y, x)
    phi = math.acos(z / rho)
    return rho, theta, phi

# Rectangular to Cylindrical
def rectangular_to_cylindrical(x, y, z):
    rho = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return rho, theta, z

# Cylindrical to Rectangular
def cylindrical_to_rectangular(rho, theta, z):
    x = rho * math.cos(theta)
    y = rho * math.sin(theta)
    return x, y, z

# Cylindrical to Spherical
def cylindrical_to_spherical(rho, theta, z):
    return polar_to_spherical(rho, theta, z)


# Example usage:
# Convert polar coordinates to cylindrical
rho_polar = 5
theta_polar = math.pi / 4
z_polar = 3
x_cylindrical, y_cylindrical, z_cylindrical = polar_to_cylindrical(rho_polar, theta_polar, z_polar)
print("Polar to Cylindrical:", (x_cylindrical, y_cylindrical, z_cylindrical))

# Convert cylindrical coordinates to rectangular
rho_cylindrical = 5
theta_cylindrical = math.pi / 4
z_cylindrical = 3
x_rectangular, y_rectangular, z_rectangular = cylindrical_to_rectangular(rho_cylindrical, theta_cylindrical, z_cylindrical)
print("Cylindrical to Rectangular:", (x_rectangular, y_rectangular, z_rectangular))

# Similarly, you can use other conversion functions as needed.
