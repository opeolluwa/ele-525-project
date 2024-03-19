import math
import typer
import subprocess
from PyInquirer import prompt, print_json, Separator
from rich import print as rprint

app = typer.Typer()


# convert str to string  
def str_to_int(s):
    try:
        return int(s)
    except ValueError:
        return None

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


prompt_coordinate = [
   {
    'type': 'input',
    'name': 'base',
    'message': 'Enter base coordinate\n1: for polar,\n2: for cylindrical,\n3: for spherical:'
   },
   {
    'type': 'input',
    'name': 'target',
   'message': 'Enter target coordinate:\n1: for polar\n2: for cylindrical,\n3: for spherical:'
   },
]


# prompt for cartesian input
prompt_cartesian_input = [
    {
        'type': 'input',
        'name': 'x',
        'message': 'Enter x coordinate'
    },
    {
        'type': 'input',
        'name': 'y',
        'message': 'Enter y coordinate'
    },
    {
        'type': 'input',
        'name': 'z',
        'message': 'Enter z coordinate'
    }
]

# prompt for polar input
prompt_polar_input = [
    {
        'type': 'input',
        'name': 'rho',
        'message': 'Enter rho coordinate'
    },
    {
        'type': 'input',
        'name': 'theta',
        'message': 'Enter theta coordinate'
    },
    {
        'type': 'input',
        'name': 'z',
        'message': 'Enter z coordinate'
    }
]


# prompt for cylindrical input
prompt_cylindrical_input = [
    {
        'type': 'input',
        'name': 'rho',
        'message': 'Enter rho coordinate'
    },
    {
        'type': 'input',
        'name': 'theta',
        'message': 'Enter theta coordinate'
    },
    {
        'type': 'input',
        'name': 'z',
        'message': 'Enter z coordinate'
    }
]


# a function that does the conversions
def convert(base, target, coordinates):
    if base == '1' and target == '2':
        rho = str_to_int(coordinates['rho'])
        theta = str_to_int(coordinates['theta'])
        z = str_to_int(coordinates['z'])
        
        x, y, z = polar_to_cylindrical(rh0, theta, z)
        return x, y, z

    elif base == '1' and target == '3':
        rho = str_to_int(coordinates['rho'])
        theta = str_to_int(coordinates['theta'])
        z = str_to_int(coordinates['z'])
        x, y, z = polar_to_spherical(rh0, theta, z)
        return x, y, z
    elif base == '2' and target == '1':
        rh0 = str_to_int(coordinates['rho'])
        theta = str_to_int(coordinates['theta'])
        z = str_to_int(coordinates['z'])
        x, y, z = cylindrical_to_rectangular(rh0, theta, z)
        return x, y, z
    elif base == '2' and target == '3':
        rh0 = str_to_int(coordinates['rho'])
        theta = str_to_int(coordinates['theta'])
        z = str_to_int(coordinates['z'])
        x, y, z = cylindrical_to_spherical(rh0, theta, z)
        return x, y, z
    elif base == '3' and target == '1':
        rh0 = str_to_int(coordinates['rho'])
        theta = str_to_int(coordinates['theta'])
        z = str_to_int(coordinates['z'])
        x, y, z = rectangular_to_spherical(rh0, theta, z)
        return x, y, z
    elif base == '3' and target == '2':
        rh0 = str_to_int(coordinates['rho'])
        theta = str_to_int(coordinates['theta'])
        z = str_to_int(coordinates['z'])
        x, y, z = rectangular_to_cylindrical(rh0, theta, z)
        return x, y, z
    else:
        return None


# validate the input
@app.command("convert")
def run():
    answers = prompt(prompt_coordinate)
 

    # if the input is greater than 3 
    if int(answers['base']) > 3 or int(answers['target']) > 3:
        print("Invalid input")
        return

     # if base and targhet are the same, then no need to convert
    elif answers['base'] == answers['target']:
        print("No need to convert")
        return

   #call on the converter 
    else:
        if answers['base'] == '1':
            coordinates = prompt(prompt_cartesian_input)
        elif answers['base'] == '2':
            coordinates = prompt(prompt_cylindrical_input)
        elif answers['base'] == '3':
            coordinates = prompt(prompt_spherical_input)

        x, y, z = convert(answers['base'], answers['target'], coordinates)
        print(x, y, z)
        return x, y, z
        


if __name__ == "__main__":
   app()    