import math
import typer
import subprocess
from PyInquirer import prompt, print_json, Separator
from rich import print as rprint

app = typer.Typer()

def cartesian_to_polar(x, y):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return r, theta

def cartesian_to_cylindrical(x, y, z):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return r, theta, z

def cartesian_to_spherical(x, y, z):
    r = math.sqrt(x**2 + y**2 + z**2)
    theta = math.atan2(y, x)
    phi = math.acos(z/r)
    return r, theta, phi

    
def cartesian_to_cylindrical(x, y, z):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return r, theta, z


prompt_coordinate = [
   {
    'type': 'input',
    'name': 'base',
    'message': 'Enter base coordinate\n1: for polar,\n2: for cylindrical,\n3: for spherical'
   },
   {
    'type': 'input',
    'name': 'target',
   'message': '\nEnter target coordinate\n: 1: for polar\n, 2: for cylindrical,\n3: for spherical'
   },
]


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


# validate the input
@app.command("convert")
def run():
    answers = prompt(prompt_coordinate)
    print(answers)
    if answers['base'] == '1' and answers['target'] == '2':
        # accept input coordinates x, y and z from user
        coordinates = prompt(prompt_cartesian_input)
        x = int(coordinates['x'])
        y = int(coordinates['y'])
        z = int(coordinates['z'])
        # compute from cartesian to cylindrical
        r_polar, theta_polar = cartesian_to_polar(x, y)
        print("Cartesian to Polar:")
        print("Cartesian Coordinates:", (x, y))
        print("Polar Coordinates:", (r_polar, theta_polar))

    elif answers['base'] == '1' and answers['target'] == '3':
        # accept input coordinates x, y and z from user
        coordinates = prompt(prompt_cartesian_input)
        x = int(coordinates['x'])
        y = int(coordinates['y'])
        z = int(coordinates['z'])
        # compute from cartesian to cylindrical
        r_polar, theta_polar = cartesian_to_polar(x, y)
        print("Cartesian to Polar:")
        print("Cartesian Coordinates:", (x, y))
        print("Polar Coordinates:", (r_polar, theta_polar))
    
    elif answers['base'] == '2' and answers['target'] == '1':
        # accept input coordinates x, y and z from user
        coordinates = prompt(prompt_cartesian_input)
        x = int(coordinates['x'])
        y = int(coordinates['y'])
        z = int(coordinates['z'])
        # compute from cartesian to cylindrical
        r_cylindrical, theta_cylindrical, z_cylindrical = cartesian_to_cylindrical(x, y, z)
        print("\nCartesian to Cylindrical:")
        print("Cartesian Coordinates:", (x, y, z))
        print("Cylindrical Coordinates:", (r_cylindrical, theta_cylindrical, z_cylindrical))


    elif answers['base'] == '2' and answers['target'] == '3':
        # accept input coordinates x, y and z from user
        coordinates = prompt(prompt_cartesian_input)
        x = int(coordinates['x'])
        y = int(coordinates['y'])
        z = int(coordinates['z'])
        # compute from cartesian to cylindrical
        r_cylindrical, theta_cylindrical, z_cylindrical = cartesian_to_cylindrical(x, y, z)
        print("\nCartesian to Cylindrical:")
        print("Cartesian Coordinates:", (x, y, z))
        print("Cylindrical Coordinates:", (r_cylindrical, theta_cylindrical, z_cylindrical))


if __name__ == "__main__":
   app()    