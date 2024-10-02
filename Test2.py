from manim import *

class NumberPlane3D(ThreeDAxes):
    def get_lines(self):
        x_axis = self.get_axis(1)
        y_axis = self.get_axis(0)
        z_axis = self.get_axis(2)
        x_axis.set_color(RED)
        y_axis.set_color(RED)
        z_axis.set_color(RED)
        return VGroup(x_axis, y_axis, z_axis)

class ShearTransform(ThreeDScene):
    def construct(self):
        # Define the 3D grid
        grid = NumberPlane3D(x_range=(-2, 2), y_range=(-2, 2), z_range=(-2, 2))
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Create a mesh to represent the grid
        grid_mesh = grid.get_lines()

        # Define the transformation matrix for the shear transform
        shear_matrix = np.array([
            [1, 1, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])

        # Apply the transformation to the mesh
        transformed_mesh = grid_mesh.copy().apply_matrix(shear_matrix)

        # Define a 3D vector
        vec = Vector(direction=[1, 1, 1], color=YELLOW)

        # Apply the transformation to the vector
        transformed_vec = vec.copy().apply_matrix(shear_matrix)

        # Animate the transformation
        self.play(Create(grid_mesh))
        self.wait()
        self.play(Transform(grid_mesh, transformed_mesh), Transform(vec, transformed_vec), run_time=2)
        self.wait()
