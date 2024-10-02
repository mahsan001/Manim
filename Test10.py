from manim import *

class NGonInCircle(Scene):
    def construct(self):
        n = 6  # Number of sides of the polygon
        radius = 2  # Radius of the circle

        # Create the circle
        circle = Circle(radius=radius)
        self.play(Create(circle))

        # Create the n-gon
        vertices = [
            radius * np.cos(2 * np.pi * k / n) * RIGHT + radius * np.sin(2 * np.pi * k / n) * UP
            for k in range(n)
        ]
        ngon = Polygon(*vertices)
        self.play(Create(ngon))

        # Divide the polygon into triangles
        triangles = VGroup()
        for i in range(n):
            triangle = Polygon(ORIGIN, vertices[i], vertices[(i + 1) % n])
            triangles.add(triangle)
        self.play(Create(triangles))

        # Divide the central angle
        center_angle = Arc(radius=radius, angle=2 * np.pi / n)
        angle_lines = VGroup()
        for i in range(n):
            angle_line = Line(ORIGIN, vertices[i])
            angle_lines.add(angle_line)
        self.play(Create(center_angle), Create(angle_lines))

        self.wait(2)  # Pause for 2 seconds
