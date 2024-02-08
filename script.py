import trimesh
import numpy as np
import sys

from mesh import *
from utils import *

# check if script is called properly
if len(sys.argv) < 2:
    print('Usage: python script.py <output_folder_name>')
    sys.exit(1)

file_path = sys.argv[1]
# create output directory
os.makedirs(file_path, exist_ok=True)

# load the nut and screw meshes
nut = Mesh('input/nut.stl')
screw = Mesh('input/screw.stl')

# rotate the nut by 180 degrees around the z-axis
screw.rotate(180, 'x')

# put screw and nut on the plane z = 0
if screw.get_bottom()[2] < 0:
    screw.translate([0, 0, -screw.get_bottom()[2]])
elif nut.get_bottom()[2] > 0:
    nut.translate([0, 0, nut.get_bottom()[2]])
if nut.get_bottom()[2] < 0:
    nut.translate([0, 0, -nut.get_bottom()[2]])
elif screw.get_bottom()[2] > 0:
    screw.translate([0, 0, screw.get_bottom()[2]])

# put screw and nut centered at the origin
screw.translate(-screw.center())
nut.translate(-nut.center())

# find the approximate height at which the screw's head begins
height_start_of_head = find_screw_head(screw, num_slices=1000, significant_increase_threshold=2)

# raise the nut to screw's head
nut.translate([0, 0, height_start_of_head - nut.get_top()[2]])
mesh1 = nut.join(screw)
mesh1.save(file_path + '/nut_and_screw_1.stl')

# cut the screw's bottom part
cutting_plane = nut.get_bottom()[2]
mesh2 = screw.join(nut)
mesh2.cut(cutting_plane)
mesh2.save(file_path + '/nut_and_screw_2.stl')

# scale the nut to cover screw's tail
nut.scale([1, 1, (height_start_of_head - screw.get_bottom()[2]) / nut.height()])
nut.translate([0, 0, screw.get_bottom()[2] - nut.get_bottom()[2]])
mesh3 = nut.join(screw)
mesh3.save(file_path + '/nut_and_screw_3.stl')




