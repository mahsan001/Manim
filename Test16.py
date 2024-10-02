from manim import *
from manim import config

import math

config.pixel_width = 1080
config.pixel_height = 1920


class Check(ThreeDScene):
    def construct(self):
        resolution_fa = 8
        
        

        axes = ThreeDAxes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            z_range=[-6, 6, 1],
            x_length=8,
            y_length=6,
            z_length=6,
        ).set_color(BLUE)

        

        def param_surface(u, v):
            x = u
            y = v
            z = x**2 + y**2
            return z
        surface_plane = Surface(
            lambda u, v: axes.c2p(u, v, param_surface(u, v)),
            resolution=(resolution_fa, resolution_fa),
            v_range=[0, 2],
            u_range=[0, 2],
            )
        
        
        graph2 = axes.plot_parametric_curve(
            lambda t: np.array([0,np.cos(3*t)*t, np.sin(3*t)*t]),
            t_range=[-2* PI, 2* PI],
            color=RED,
        )
        cardioid = axes.plot_parametric_curve(
                        lambda t: np.array(
                            [
                                np.exp(1) * np.cos(t) * (1 - np.cos(t)),
                                np.exp(1) * np.sin(t) * (1 - np.cos(t)),
                                0,
                            ]
                        ),
                        t_range=[0, 2 * PI],
                        color="#0FF1CE",
                    )

        self.add(axes)
        self.wait()
        self.play(Create(graph2))
        self.wait()

        ##THE CAMERA IS AUTO SET TO PHI = 0 and THETA = -90

       
        self.wait()
        self.move_camera(theta=-45 * DEGREES)
        self.move_camera(phi=60 * DEGREES)


        self.wait()
        
       
       

        self.wait()
        
        