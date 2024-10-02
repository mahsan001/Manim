from manim import *

class Theorem(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        a = 3
        b = 3
        c = (a**2 + b**2) ** 0.5

        triangle = Polygon(
            ORIGIN, a * RIGHT, a * RIGHT + b * UP,
            stroke_width=2,
            fill_opacity=0.3,
            color=BLUE
        )
        
        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        
        circle = Circle(radius=c, color=BLUE)
        circle.set_fill(BLUE, opacity=0.5)
        dot = Dot(color=RED)
        
        # Calculate midpoints
        midpoint_a = (triangle.get_vertices()[0] + triangle.get_vertices()[1]) / 2
        midpoint_b = (triangle.get_vertices()[1] + triangle.get_vertices()[2]) / 2
        midpoint_c = (triangle.get_vertices()[0] + triangle.get_vertices()[2]) / 2

        # Add side labels
        label_a = Tex("a").next_to(midpoint_a, DOWN)
        label_b = Tex("b").next_to(midpoint_b, RIGHT)
        label_c = Tex("c").next_to(midpoint_c, LEFT)

        self.play(Create(triangle))
        self.play(Write(label_a), Write(label_b), Write(label_c))

        # Move the camera to focus on the triangle and labels
        self.play(
            self.camera.frame.animate.scale(0.8).move_to(triangle),
            run_time=2
        )

        # Move the labels to form the equation
        equation = MathTex("a^2 + b^2 = c^2").next_to(triangle, DOWN)
        self.play(
            Transform(label_a, equation.get_part_by_tex("a")),
            Transform(label_b, equation.get_part_by_tex("b")),
            Transform(label_c, equation.get_part_by_tex("c")),
            run_time=1.5
        )

        # Do other operations on the triangle or equation
        # ...
        
        # Restore the initial camera state
        self.play(Restore(self.camera.frame))
        self.wait(1)
        
        self.remove(label_a, label_b, label_c)
        
        self.play(Transform(triangle, circle))
        self.play(self.camera.frame.animate.scale(0.3).move_to(dot))
        
        def update_curve(mob):
            mob.move_to(dot.get_center())
        
        self.camera.frame.add_updater(update_curve)
        self.play(MoveAlongPath(dot, circle, rate_func=smooth), run_time=3)
        self.camera.frame.remove_updater(update_curve)
        
        circum_text = MathTex("C = 2\\pi r")
        area_eqn = MathTex(r"A = \pi r^2")
        circum_text.set_color_by_gradient(ORANGE, PINK)
        circum_text.scale(1)                                            
        circum_text.next_to(circle, RIGHT)
        area_eqn.set_color_by_gradient(ORANGE, PINK)
        area_eqn.scale(1)                                                 
        area_eqn.next_to(circle, RIGHT)
        
        self.play(Transform(dot, circum_text))
        self.play(Transform(dot, area_eqn))
        
        self.remove(triangle, dot)
        self.wait(1)
