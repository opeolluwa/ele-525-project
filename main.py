import math
import typer
import subprocess
from PyInquirer import prompt, print_json, Separator
from rich import print as rprint

app = typer.Typer()

''' 
A function that converts a string to an integer
@param s: string
@return: int (or none if the string cannot be converted to an integer)

'''
# convert str to string  
def str_to_int(s):
    try:
        return int(s)
    except ValueError:
        return None

'''
A function that converts fromn the polar to cylindrical coordinate system
@param rho: float
@param theta: float
@param z: float
@return: float, float, float

'''

def polar_to_cylindrical(rho, theta, z):
    x = rho * math.cos(theta)
    y = rho * math.sin(theta)
    return x, y, z

'''
A function that converts from the polar to rectangular coordinate system
@param rho: float
@param theta: float
@return: float, float

'''
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
        rho = str_to_int(coordinates['input_one'])
        theta = str_to_int(coordinates['input_two'])
        z = str_to_int(coordinates['input_three'])
        x, y, z = polar_to_cylindrical(rho, theta, z)
        return x, y, z

    elif base == '1' and target == '3':
        rho = str_to_int(coordinates['input_one'])
        theta = str_to_int(coordinates['input_two'])
        z = str_to_int(coordinates['input_three'])
        x, y, z = polar_to_spherical(rho, theta, z)
        return x, y, z

    elif base == '2' and target == '1':
        rho = str_to_int(coordinates['input_one'])
        theta = str_to_int(coordinates['input_two'])
        z = str_to_int(coordinates['input_three'])
        x, y, z = cylindrical_to_rectangular(rho, theta, z)
        return x, y, z
    elif base == '2' and target == '3':
        rho = str_to_int(coordinates['input_one'])
        theta = str_to_int(coordinates['input_two'])
        z = str_to_int(coordinates['input_three'])
        x, y, z = cylindrical_to_spherical(rho, theta, z)
        return x, y, z
    elif base == '3' and target == '1':
        rho = str_to_int(coordinates['input_one'])
        theta = str_to_int(coordinates['input_two'])
        z = str_to_int(coordinates['input_three'])
        x, y, z = rectangular_to_spherical(rho, theta, z)
        return x, y, z
    elif base == '3' and target == '2':
        rho = str_to_int(coordinates['input_one'])
        theta = str_to_int(coordinates['input_two'])
        z = str_to_int(coordinates['input_three'])
        x, y, z = rectangular_to_cylindrical(rho, theta, z)
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
            # rho = str_to_int(coordinates['x'])
            # theta = str_to_int(coordinates['y'])
            # z = str_to_int(coordinates['z'])
            # # redefine the coordinates with the new values
            # coordinates = [rho, theta, z]
        elif answers['base'] == '2':
            coordinates = prompt(prompt_cylindrical_input)
        elif answers['base'] == '3':
            coordinates = prompt(prompt_spherical_input)


        '''
        destructure the coordinates into three variables 
        coord_one
        coord_two
        coord_three
        '''
   

        # define the input, this could be x y z or rho theta z
        if answers['base'] == '1':
            input_one = coordinates['x']
            input_two = coordinates['y']
            input_three = coordinates['z']
        else:
            input_one = coordinates['rho']
            input_two = coordinates['theta']
            input_three = coordinates['z']

        # call on the convert function
        coordinates = {
            'input_one': input_one,
            'input_two': input_two,
            'input_three': input_three
            }

    
        coord_one, coord_two, coord_three = convert(answers['base'], answers['target'], coordinates)

        base  =  'polar' if answers['base'] == '1' else 'cylindrical' if answers['base'] == '2' else 'spherical'
        target = 'polar' if answers['target'] == '1' else 'cylindrical' if answers['target'] == '2' else 'spherical'

        # print the base coordinates
        print(f"Base coordinates({base}): {input_one},\t {input_two},\t {input_three}")
        # print the converted coordinates
        print(f"Converted coordinates({target}): {coord_one},\t {coord_two},\t {coord_three}")
        return coord_one, coord_two, coord_three


if __name__ == "__main__":
   app()    


# export the functions to be used in tets.py for testting 
__all__ = polar_to_cylindrical, polar_to_rectangular, polar_to_spherical, rectangular_to_spherical, rectangular_to_cylindrical, cylindrical_to_rectangular, cylindrical_to_spherical