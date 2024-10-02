from manim import *
from manim import config

import math

config.pixel_width = 1080
config.pixel_height = 1920

class Tute3(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(phi=45 * DEGREES, theta=-45 * DEGREES)

        axes = ThreeDAxes(y_range=[-3, 10, 3], y_length=7).add_coordinates()

        graph = axes.plot(lambda x: x, x_range=[0, 3], color=RED_B)

        area = axes.get_area(graph=graph, x_range=[0, 3])

        e = ValueTracker(0)

        surface = always_redraw(
            lambda: Surface(
                lambda u, v: axes.c2p(v, v * np.cos(u), v * np.sin(u)),
                u_range = [0,e.get_value()],
                v_range = [0,3],
             
                checkerboard_colors=[GREEN, PURPLE],
                fill_opacity =1 
                

            )
        )
        self.add(axes, surface)
       
        
        self.begin_ambient_camera_rotation(
            rate=PI / 15, about="theta"
        ) 
        self.play(LaggedStart(Create(graph), Create(area)))
        self.play(
            Rotating(area, axis=RIGHT, radians=2 * PI, about_point=axes.c2p(0, 0, 0)),
            e.animate.set_value(2 * PI),
            run_time=6,
            rate_func=linear,
        )
        self.stop_ambient_camera_rotation()
       
        self.wait()