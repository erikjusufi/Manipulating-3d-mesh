# Project description

This project includes a script for manipulating 3D mesh objects, specifically for operations involving a nut and a screw model, such as rotation, translation, scaling, finding specific geometric characteristics, and saving the manipulated models as STL files.

## Instructions for setting up virtual env and installing dependencies

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x

1. **Navigate to the project directory:**

```bash
cd path/to/project
```
2.  **Create a virtual environment:**

```bash
python -m venv venv
```
3. **Activate the virtual environment:**

```bash
.\venv\Scripts\activate
```
4. **Installing Dependencies:**
With the virtual environment activated, install the project dependencies:
```bash
pip install -r requirements.txt
```
### Usage
To run the script, use the following command, replacing <output_folder_name> with the desired name of your output directory:

```bash
python script.py <output_folder_name>
```
This command executes script.py, performing operations on 3D mesh objects and generating output in the specified folder.

## Files Description
- script.py: Main script that demonstrates the use of mesh operations. It includes loading, transforming, and saving mesh objects.
- mesh.py: Contains the Mesh class with methods for rotating, translating, scaling, and other operations on 3D mesh objects.
- utils.py: Utility functions, including find_screw_head, which estimates the height at which the screw's head begins.
- visualization.ipynb: Jupyter notebook for visualization and testing of mesh operations.
- requirements.txt: Lists all dependencies required by the project, ensuring consistent setups.