from manim import *
from manim import config

config.pixel_width = 1080
config.pixel_height = 1920


class FollowingGraphCamera(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        # create the axes and the curve
        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        graph = ax.plot(lambda x: np.sin(x), color=BLUE, x_range=[0, 3 * PI])

        gx_dy = MathTex(
            r"\sin(x)  = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} x^{2n+1")
        gx_dy.set_color_by_gradient(RED, BLUE)
        gx_dy.scale(2)

        Group = VGroup()

        circle = Circle()
        circle.set_fill(RED, opacity=0.5)

        # create dots based on the graph
        moving_dot = Dot(ax.i2gp(graph.t_min, graph), color=ORANGE)
        dot_1 = Dot(ax.i2gp(graph.t_min, graph), color=RED)
        dot_2 = Dot(ax.i2gp(graph.t_max, graph), color=BLUE)

        self.add(ax, graph, dot_1, dot_2, moving_dot)
        self.play(self.camera.frame.animate.scale(0.3).move_to(moving_dot))

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.add_updater(update_curve)
        self.play(MoveAlongPath(moving_dot, graph,
                  rate_func=smooth), run_time=2)
        self.camera.frame.remove_updater(update_curve)

      #  Group.add(ax,dot_1,dot_2,moving_dot)
        self.play(Restore(self.camera.frame))
        self.remove(ax, dot_1, dot_2, moving_dot)
        self.wait(0.33)

        self.play(Transform(graph, gx_dy), run_time=1, rate_function=linear)
        self.wait(2)
        self.remove(graph)


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

        circle = Circle(color=BLUE)
        circle.set_fill(BLUE, opacity=0.5)
        dot = Dot(color=RED)

        # Calculate midpoints
        midpoint_a = (triangle.get_vertices()[
                      0] + triangle.get_vertices()[1]) / 2
        midpoint_b = (triangle.get_vertices()[
                      1] + triangle.get_vertices()[2]) / 2
        midpoint_c = (triangle.get_vertices()[
                      0] + triangle.get_vertices()[2]) / 2

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
        equation.set_color_by_gradient(BLUE).scale(1)
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
        self.wait(2)

        self.remove(triangle, dot)


class Transformation(Scene):
    def construct(self):
        self.camera.frame.save_state()

        title = MathTex("Transformations", font_size=25, color=BLUE).scale(4)
        self.play(Write(title))
        self.play(
            self.camera.frame.animate.scale(0.8).shift(UP),
            run_time=2
        )
        self.remove(title)
        self.wait(1)

        vector = Vector(direction=[1, 0], color=GREEN)
        vector1 = Vector(direction=[0, 1], color=RED)
        original_grid = NumberPlane(background_line_style={
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

        self.play(Create(original_grid, run_time=2, lag_ratio=0.1))
        self.play(Create(transformed_grid, run_time=2, lag_ratio=0.1))
        self.add(vector1, vector)

        # Define the transformation matrix
        transform_matrix = [[1, -1.7], [0, -1]]
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
        self.wait(1)
        self.remove(transformed_grid, original_grid, vector, vector1)
        self.wait(1)

        ds_m = MathTex(r"\mathbb{Ahsan}", fill_color=RED).scale(4)
        self.play(Write(ds_m), run_time=2)
        self.wait(1)


class Intro(Scene):

    def construct(self):
        self.camera.frame.save_state()
        # Create the title text
        title = Tex("Some Math Fun", font_size=35, color=BLUE).scale(3)

        # Create the equation objects
        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])

        # Add animations for the camera movements
        self.play(Write(title))
        self.play(
            self.camera.frame.animate.scale(0.8).shift(UP),
            run_time=2
        )
        self.play(Restore(self.camera.frame))

        self.play(Transform(title, ax))
        self.remove(title)


class Riemann(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        title = MathTex("Riemann Sum", font_size=25, color=BLUE).scale(4)
        self.play(Write(title))
        self.play(
            self.camera.frame.animate.scale(0.8).shift(UP),
            run_time=2
        )
        self.play(Restore(self.camera.frame))

        function = MathTex(
            "F(x) = ", "\\frac{1}{2}", "x^3", font_size=25).scale(4)
        function.set_color_by_gradient(BLUE)

        self.wait(1)
        self.play(Transform(title, function))
        self.wait(2)

        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        quadratic = ax.plot(lambda x: 0.5 * x ** 3, x_range=[0, 3])

        rects_right = ax.get_riemann_rectangles(
            quadratic,
            x_range=[0, 3],
            dx=0.25,
            color=(TEAL, BLUE_B, DARK_BLUE),
            input_sample_type="right",
        )

        self.play(Transform(title, ax), Create(quadratic))
        self.wait(1)

        self.play(Create(rects_right))

        iterations = 3
        dx = 0.25

        # riemann_sum_label = MathTex("S = 0")
        # iemann_sum_label.to_corner(UP + RIGHT)
        # self.add(riemann_sum_label)
        formula3 = MathTex("A =", "\\sum_{i=1}^{n}", "\\left(\\frac{1}{2}",
                           "\\cdot", "x_i^3\\right)", "\\cdot", "\\Delta x").scale(1.5)

        formula3.set_color_by_gradient(BLUE)
        formula3.next_to(rects_right, RIGHT)
        self.play(Write(formula3))
        self.wait(1)
        self.remove(formula3)

        for _ in range(iterations):
            dx /= 2

            new_rects_right = ax.get_riemann_rectangles(
                quadratic,
                x_range=[0, 3],
                dx=dx,
                color=(TEAL, BLUE_B, DARK_BLUE),
                input_sample_type="right",
            )

            # riemann_sum = sum(rect.get_height() * dx for rect in new_rects_right)
           # riemann_sum_label1 = MathTex(f"S = {riemann_sum}")
           # riemann_sum_label1.to_corner(UP + RIGHT)

            formula = MathTex("A =", "\\sum_{i=1}^{3}", "\\left(\\frac{1}{2}",
                              "\\cdot", "x_i^3\\right)", "\\cdot", f"{dx}").scale(1.5)
            formula.set_color_by_gradient(BLUE)

            formula.next_to(new_rects_right, DOWN+(RIGHT-0.5))
            self.play(
                Transform(rects_right, new_rects_right),
                Transform(new_rects_right, formula),
                # Transform(riemann_sum_label, riemann_sum_label1),
                run_time=1,
            )
            self.wait(1)
            self.remove(new_rects_right)

        new_rects_right = ax.get_area(
            quadratic,
            x_range=[0, 3],
            color=(TEAL, BLUE_B, DARK_BLUE),
            opacity=1
        )
        formula2 = MathTex(
            "A =", "\\int_{0}^{3}", "\\frac{1}{2}", "x^3", "\\,dx").scale(2)
        formula2.next_to(new_rects_right, DOWN)
        formula2.set_color_by_gradient(BLUE)
        self.play(
            Transform(rects_right, new_rects_right),
            Transform(new_rects_right, formula2),
            # Transform(riemann_sum_label, riemann_sum_label1),
            run_time=1,
        )

        self.wait(2)
        self.remove(title, rects_right, quadratic, new_rects_right)


class Main (MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        c1 = FollowingGraphCamera
        c3 = Theorem
        c4 = Intro
        c5 = Transformation
        c6 = Riemann

        c4.construct(self)
        c1.construct(self)
        c3.construct(self)
        self.play(Restore(self.camera.frame))
        c6.construct(self)
        c5.construct(self)
