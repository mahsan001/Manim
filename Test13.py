from manim import *
from manim import config

import math

config.pixel_width = 1080
config.pixel_height = 1920


class Tute0(Scene):  # ILLUSTRATING POLAR PLANE WITH A SINE CURVE
    def construct(self):

        e = ValueTracker(0.01)  # Tracks the end value of both functions
        Function = MathTex(r"f(t) = ").set_color_by_gradient(BLUE).scale(3)
        Function1 = MathTex("2",  "\\cos(9t)",  "\\sin(3t)").scale(
            3).set_color_by_gradient(BLUE).next_to(Function, DOWN)

        self.add(Function, Function1)

        self.wait(1)
        self.play(FadeOut(Function), FadeOut(Function1))

        plane = PolarPlane(radius_max=3).add_coordinates()
        plane.shift(UP*5).scale(1.75)
        graph1 = always_redraw(lambda:
                               ParametricFunction(lambda t: plane.polar_to_point(2*((np.cos(9*t))*(np.sin(3*t))), t),
                                                  t_range=[0, e.get_value()], color=BLUE, stroke_width=10)
                               )
        dot1 = always_redraw(lambda: Dot(fill_color=ORANGE, fill_opacity=0.8).scale(0.5).move_to(graph1.get_end())
                             )

        axes = Axes(x_range=[0, 8, 1], x_length=5, y_range=[-3,
                    3, 1], y_length=3).shift(DOWN*6).scale(2.5)
        axes.add_coordinates()
        graph2 = always_redraw(lambda:
                               axes.plot(lambda x: (2*(np.cos(9*x))*(np.sin(3*x))),
                                         x_range=[0, e.get_value()], color=BLUE, stroke_width=10)
                               )
        dot2 = always_redraw(lambda: Dot(fill_color=ORANGE, fill_opacity=0.8).scale(0.5).move_to(graph2.get_end())
                             )

        self.add(plane, axes)

        self.add(graph1, graph2, dot1, dot2)
        self.play(e.animate.set_value(2*PI), run_time=7, rate_func=linear)
        self.wait()
        self.remove(plane, axes, graph1, graph2)


class Tute2(Scene):  # ILLUSTRATING POLAR PLANE WITH A SINE CURVE
    def construct(self):

        e = ValueTracker(0.01)  # Tracks the end value of both functions
        Function1 = MathTex(r"f(t) = ").set_color_by_gradient(
            BLUE).scale(3).set_color_by_gradient(BLUE)
        Function2 = MathTex(r" \cos(6t) + \sin^2(6t)").set_color_by_gradient(
            BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Function1, DOWN)

        Function = MathTex("f(t) =", "\\frac{1}{4}t").scale(
            3).set_color_by_gradient(BLUE)

        self.add(Function)
        self.wait(1)
        self.play(FadeOut(Function))

        plane = PolarPlane(radius_max=3).add_coordinates()
        plane.shift(UP*5).scale(1.75)
        graph1 = always_redraw(lambda:
                               ParametricFunction(lambda t: plane.polar_to_point((1/4)*t, t),
                                                  t_range=[0, e.get_value()], color=BLUE, stroke_width=10)
                               )
        dot1 = always_redraw(lambda: Dot(fill_color=ORANGE, fill_opacity=0.8).scale(0.5).move_to(graph1.get_end())
                             )

        axes = Axes(x_range=[0, 8, 1], x_length=5, y_range=[-3,
                    3, 1], y_length=3).shift(DOWN*6).scale(2.5)
        axes.add_coordinates()
        graph2 = always_redraw(lambda:
                               axes.plot(lambda x: (
                                   1/4)*x, x_range=[0, e.get_value()], color=BLUE, stroke_width=10)
                               )
        dot2 = always_redraw(lambda: Dot(fill_color=ORANGE, fill_opacity=0.8).scale(0.5).move_to(graph2.get_end())
                             )

        self.play(LaggedStart(
            Write(plane), Create(axes),
            run_time=3, lag_ratio=0.5)
        )

        self.add(graph1, graph2, dot1, dot2)
        self.play(e.animate.set_value(3*PI), run_time=6, rate_func=linear)
        self.wait()
        self.remove(plane, axes, graph1, graph2)

        self.play(Write(Function1), Write(Function2))
        self.wait(1)


class Tute3(Scene):
    def construct(self):
        e = ValueTracker(0.01)  # Tracks the end value of both functions

        Function1 = MathTex(r"f(t) = ").set_color_by_gradient(
            BLUE).scale(3).set_color_by_gradient(BLUE)
        Function2 = MathTex(r" \cos(6t) + \sin^2(6t)").set_color_by_gradient(
            BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Function1, DOWN)

        Function3 = MathTex(r"f(t) = ").set_color_by_gradient(BLUE).scale(3)
        Function4 = MathTex("2",  "\\cos(9t)",  "\\sin(3t)").scale(
            3).set_color_by_gradient(BLUE).next_to(Function3, DOWN)

        self.add(Function1, Function2)
        self.wait(1)
        self.play(FadeOut(Function1), FadeOut(Function2))

        plane = PolarPlane(radius_max=3).add_coordinates()
        plane.shift(UP*5).scale(1.75)
        graph1 = always_redraw(lambda:
                               ParametricFunction(lambda t: plane.polar_to_point(1+np.cos(6*t)+np.sin(6*t)**2, t),
                                                  t_range=[0, e.get_value()], color=BLUE, stroke_width=10)
                               )
        dot1 = always_redraw(lambda: Dot(fill_color=BLUE, fill_opacity=0.8).scale(0.5).move_to(graph1.get_end())
                             )

        axes = Axes(x_range=[0, 8, 1], x_length=5, y_range=[-3,
                    3, 1], y_length=3).shift(DOWN*6).scale(2.5)
        axes.add_coordinates()
        graph2 = always_redraw(lambda:
                               axes.plot(lambda x: 1+np.cos(6*x)+np.sin(6*x)**2,
                                         x_range=[0, e.get_value()], color=BLUE, stroke_width=10)
                               )
        dot2 = always_redraw(lambda: Dot(fill_color=ORANGE, fill_opacity=0.8).scale(0.5).move_to(graph2.get_end())
                             )

        self.add(plane, axes)

        self.add(graph1, graph2, dot1, dot2)
        self.play(e.animate.set_value(2*PI), run_time=5, rate_func=linear)
        self.wait()
        self.remove(plane, axes, graph1, graph2)
        self.play(Write(Function3), Write(Function4))
        self.wait(1)


class Tute1 (ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=30 * DEGREES, theta=-60 * DEGREES)

        self.begin_ambient_camera_rotation(
            rate=PI / 2, about="theta"
        )  # Rotates at a rate of radians per second

        ds_m = MathTex(r"\mathbb{Ahsan}", fill_color=BLUE).scale(
            6).set_color_by_gradient(BLUE)
        self.play(Write(ds_m), run_time=2)
        self.wait(1.75)
        self.stop_ambient_camera_rotation()


class Intro(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=45 * DEGREES, theta=-45 * DEGREES)

        Intro = MathTex("GRAPHING").scale(3).set_color_by_gradient(BLUE)
        Intro1 = MathTex("IN").scale(3).set_color_by_gradient(
            BLUE).next_to(Intro, DOWN, buff=1.5)
        Intro2 = MathTex(
            "3 - D").scale(3).set_color_by_gradient(BLUE).next_to(Intro1, DOWN, buff=1.5)
        PM1 = MathTex("PARAMETRIC").scale(3).set_color_by_gradient(BLUE)
        PM2 = MathTex("CURVES").scale(
            3).set_color_by_gradient(BLUE).next_to(PM1, DOWN)

        Eq1 = MathTex("x(t) = t").set_color_by_gradient(
            BLUE).scale(2).shift(UP*8)
        Eq2 = MathTex("y(t) = \cos(3t)").set_color_by_gradient(
            BLUE).scale(2).next_to(Eq1, DOWN)
        Eq3 = MathTex("z(t) = \sin(3t)").set_color_by_gradient(
            BLUE).scale(2).next_to(Eq2, DOWN)

        self.play(Write(Intro), Write(Intro1), Write(Intro2))
        self.move_camera(theta=270 * DEGREES)
        self.wait()
        self.move_camera(phi=0 * DEGREES)
        IntroG = VGroup()
        IntroG.add(Intro, Intro1, Intro2)

        PMG = VGroup()
        PMG.add(PM1, PM2)
        self.wait(1)
        self.play(Transform(IntroG, PMG))
        self.wait()

        axes = ThreeDAxes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            z_range=[-6, 6, 1],
            x_length=8,
            y_length=6,
            z_length=6,
        ).set_color(BLUE)

        self.play(Transform(IntroG, axes))

        graph2 = axes.plot_parametric_curve(
            lambda t: np.array([t, np.cos(3*t), np.sin(3*t)]),
            t_range=[-2 * PI, 2 * PI],
            color=BLUE,
        )

        self.play(Write(Eq1), Write(Eq2), Write(Eq3))
        self.wait()

        Eqs = VGroup().add(Eq1, Eq2, Eq3)

        self.play(Transform(Eqs, graph2))
        self.wait()

        self.move_camera(theta=-45 * DEGREES, zoom=2)
        self.move_camera(phi=60 * DEGREES, zoom=3)

        self.wait()

        self.move_camera(theta=30*DEGREES)
        self.wait()

        self.remove(IntroG, Eqs)


class SCENE2(Scene):
    def construct(self):
        Intro = MathTex("GRAPHING").scale(4).set_color_by_gradient(BLUE)
        PPlane = MathTex("POLAR PLANE").scale(
            3).set_color_by_gradient(BLUE).shift(UP*4)
        VS = MathTex("VS").scale(3).set_color_by_gradient(BLUE)
        CPlane = MathTex("CARTESIAN").scale(
            3).set_color_by_gradient(BLUE).shift(DOWN*4)
        CPlane1 = MathTex("PLANE").scale(
            3).set_color_by_gradient(BLUE).next_to(CPlane, DOWN)
        Function = MathTex("f(t) =", "\\frac{1}{4}t").scale(
            3).set_color_by_gradient(BLUE)

        Planes = VGroup()
        Planes.add(PPlane, CPlane, CPlane1, VS)

        self.add(Intro)
        self.wait(1)
        self.play(Transform(Intro, Planes))
        self.wait(1.5)
        self.play(Transform(Intro, Function))
        self.wait(1)


class Intro0(MovingCameraScene):

    def construct(self):
        self.camera.frame.save_state()
        # Create the title text
        title = MathTex("GRAPHING", font_size=35, color=BLUE).scale(
            5).set_color_by_gradient(BLUE)

        # Create the equation objects

        # Add animations for the camera movements
        self.play(Write(title))
        self.play(
            self.camera.frame.animate.scale(0.8).shift(UP),
            run_time=2
        )

        self.play(Restore(self.camera.frame))


class Interval(MovingCameraScene):
    def construct(self):

        self.camera.frame.save_state()
        surf = MathTex("3-D").scale(2).set_color_by_gradient(BLUE)
        surf1 = MathTex("SURFACE").scale(
            2).set_color_by_gradient(BLUE).next_to(surf, DOWN)
        self.play(Write(surf), Write(surf1))
        self.play(
            self.camera.frame.animate.scale(0.8).shift(UP),
            run_time=2
        )
        self.play(Restore(self.camera.frame))
        self.play(FadeOut(surf), FadeOut(surf1))
