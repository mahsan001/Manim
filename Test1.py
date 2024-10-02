from manim import *

class LinearTransformation(Scene):
    def construct(self):
        # Create a vector and display it on the grid
        vector = Vector(direction=[1,0], color=GREEN)
        vector1 = Vector(direction=[0,1], color=RED)  
        original_grid = NumberPlane( background_line_style={
                "stroke_opacity": 0.5,
            },)
        transformed_grid = NumberPlane(
            x_range=original_grid.x_range,
            y_range=original_grid.y_range,
            x_length=original_grid.x_length,
            y_length=original_grid.y_length,
            background_line_style={
                "stroke_opacity": 1,
            },
        )

        self.add(original_grid, transformed_grid, vector)

        # Define the transformation matrix
        transform_matrix =  [[1, -1.7], [0, -1]]
        transform_matrix1 = [[0, -1], [1, 0]]
        transform_matrix2 = [[0, -1], [1, 0]]

        # Apply the transformation to the transformed grid and the vector
        self.play(
            transformed_grid.animate.apply_matrix(transform_matrix),
            vector.animate.apply_matrix(transform_matrix),
            vector1.animate.apply_matrix(transform_matrix),
            run_time=3
        )

        self.wait()
        self.play(
            transformed_grid.animate.apply_matrix(transform_matrix1),
            vector.animate.apply_matrix(transform_matrix1),
            vector1.animate.apply_matrix(transform_matrix1),
            run_time=3
        )
        self.wait()
        self.play(
            transformed_grid.animate.apply_matrix(transform_matrix2),
            vector.animate.apply_matrix(transform_matrix2),
            vector1.animate.apply_matrix(transform_matrix2),
            run_time=3
        )