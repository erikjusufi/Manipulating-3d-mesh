import trimesh
import numpy as np
from mesh import *

def find_screw_head(mesh: Mesh, num_slices: int = 1000, significant_increase_threshold: float = 2) -> float:
    '''
    Find the approximate height at which the screw's head begins
    to be used to put nut bellow the screw's head.
    Parameters for adjusting the analysis are:
    - num_slices: The number of slices to use for the analysis, more slices will give a finer analysis but require more computation.
    - significant_increase_threshold: The threshold for what constitutes a "significant" increase in width

    Parameters:
    ----------
    mesh: Mesh
        The mesh of the screw
    num_slices: int
        The number of slices to use for the analysis
    significant_increase_threshold: float
        The threshold for what constitutes a "significant" increase in width

    Returns:
    -------
    float
        The approximate height at which the screw's head begins
    '''
    screw_mesh = mesh.mesh
    # determine height range of the screw and cut it for 5% from the bottom and top
    z_min, z_max = screw_mesh.bounds[:, 2]
    z_max = z_max - 0.05 * mesh.height()
    z_min = z_min + 0.05 * mesh.height()

    # calculate the slice thickness
    slice_thickness = (z_max - z_min) / num_slices

    slice_widths = list()

    # calculate the maximum width of each slice
    for i in range(num_slices):
        z_lower = z_min + i * slice_thickness
        z_upper = z_lower + slice_thickness
        vertices_in_slice = screw_mesh.vertices[(screw_mesh.vertices[:, 2] >= z_lower) & (screw_mesh.vertices[:, 2] < z_upper)]
        if len(vertices_in_slice) > 0:
            distances = trimesh.points.point_plane_distance(vertices_in_slice, [vertices_in_slice.mean(axis=0), [0, 0, 1]])
            max_distance = distances.max()
            slice_widths.append(max_distance * 2) # Diameter
        else:
            slice_widths.append(0)

    # detect the transition to the screw's head as the first significant increase in width
    for i in range(1, len(slice_widths)):
        if slice_widths[i] > slice_widths[i - 1] * significant_increase_threshold:
            transition_index = i
            break

    # calculate the approximate height at which the screw's head begins
    height_start_of_head = z_min + transition_index * slice_thickness

    return height_start_of_head



    
