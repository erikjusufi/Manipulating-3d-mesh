import os
import numpy as np
import trimesh
import typing

class Mesh:
    '''
    A class to represent a 3D mesh

    Attributes:
    ----------
    mesh: trimesh.Trimesh
        The mesh object
    
    Methods:
    -------
    rotate(angle: float, axis: str)
        Rotate the mesh around the given axis by the given angle
    translate(translation_vector: list)
        Translate the mesh by the given vector
    scale(scale_vector: list)
        Scale the mesh by the given vector
    get_bottom()
        Get the bottom of the mesh
    get_top()
        Get the top of the mesh
    get_volume()
        Get the volume of the mesh
    height()
        Get the height of the mesh
    width()
        Get the width of the mesh
    center()
        Get the center of the mesh
    get_dimensions()
        Get the dimensions of the mesh
    length()
        Get the length of the mesh
    cut(cutting_plane: float)
        Remove mesh under the z-value of the cutting plane
    join(other_mesh: Mesh)
        Return a new mesh object that is the result of joining the current mesh with another mesh
    save(file_path: str)
        Save the mesh to a file
    '''
    
    def __init__(self, file_path: str = None, mesh: trimesh.Trimesh = None):
        if file_path != None and not os.path.exists(file_path):
            raise ValueError('File not found')
        if file_path != None:
            self.mesh = trimesh.load_mesh(file_path)
        elif mesh != None:
            self.mesh = mesh
        else:
            raise ValueError('Invalid input')
        
    def rotate(self, angle: float, axis: str):
        '''
        Rotate the mesh around the given axis by the given angle
        
        Parameters:
        ----------
        angle: float
            The angle of rotation in degrees
        axis: str
            The axis of rotation. It can be 'x', 'y', or 'z'
        '''
        if axis not in ['x', 'y', 'z']:
            raise ValueError('Invalid axis')
        rotate_axis = [0, 0, 0]
        if axis == 'x':
            rotate_axis[0] = 1
        elif axis == 'y':
            rotate_axis[1] = 1
        else:
            rotate_axis[2] = 1
        self.mesh.apply_transform(trimesh.transformations.rotation_matrix(np.deg2rad(angle), rotate_axis))

    def translate(self, translation_vector: typing.List[float]):
        '''
        Translate the mesh by the given vector
        
        Parameters:
        ----------
        translation_vector: list
            The vector to translate the mesh by
        '''
        self.mesh.apply_translation(translation_vector)

    def scale(self, scale_vector: typing.List[float]):
        '''
        Scale the mesh by the given vector
        
        Parameters:
        ----------
        scale_vector: list
            The vector to scale the mesh by
        '''
        self.mesh.apply_scale(scale_vector)

    
    def get_bottom(self):
        '''
        Get the bottom of the mesh
        
        Returns:
        -------
        float
            The bottom of the mesh
        '''
        return self.mesh.bounds[0]

    def get_top(self):
        '''
        Get the top of the mesh
        
        Returns:
        -------
        float
            The top of the mesh
        '''
        return self.mesh.bounds[1]

    def get_volume(self):
        '''
        Get the volume of the mesh
        
        Returns:
        -------
        float
            The volume of the mesh
        '''
        return self.mesh.volume
    
    def height(self):
        '''
        Get the height of the mesh
        
        Returns:
        -------
        float
            The height of the mesh
        '''
        return self.mesh.bounds[1][2] - self.mesh.bounds[0][2]
    
    def width(self):
        '''
        Get the width of the mesh
        
        Returns:
        -------
        float
            The width of the mesh
        '''
        return self.mesh.bounds[1][0] - self.mesh.bounds[0][0]
    
    def center(self):
        '''
        Get the center of the mesh
        
        Returns:
        -------
        list
            The center of the mesh
        '''
        return self.mesh.center_mass
    
    def get_dimensions(self):
        '''
        Get the dimensions of the mesh
        
        Returns:
        -------
        list
            The dimensions of the mesh
        '''
        return [self.height(), self.width(), self.length()]
    
    def length(self):
        '''
        Get the length of the mesh
        
        Returns:
        -------
        float
            The length of the mesh
        '''
        return self.mesh.bounds[1][1] - self.mesh.bounds[0][1]

    def cut(self, cutting_plane: float):
        '''
        Remove mesh under the z-value of the cutting plane
        
        Parameters:
        ----------
        cutting_plane: float
            The z-value of the cutting plane
        '''
        self.mesh = trimesh.intersections.slice_mesh_plane(self.mesh, [0, 0, 1], [0, 0, cutting_plane], cap=True)

    def join(self, other_mesh: 'Mesh'):
        '''
        Return a new mesh object that is the result of joining the current mesh with another mesh

        Parameters:
        ----------
        other_mesh: Mesh
            The other mesh to join with

        Returns:
        -------
        Mesh
            The new mesh object that is the result of joining the current mesh with another mesh
        '''
        return Mesh(mesh = trimesh.util.concatenate(self.mesh, other_mesh.mesh))

    def save(self, file_path: str):
        '''
        Save the mesh to a file
        
        Parameters:
        ----------
        file_path: str
            The file path to save the mesh to
        '''
        if not file_path.endswith('.stl'):
            raise ValueError('Invalid file format')
        self.mesh.export(file_path)


    

        