from manim import *
from manim import config

import math

config.pixel_width = 1080
config.pixel_height = 1920

class Intro(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=45 * DEGREES, theta=-45 * DEGREES)
        Intro = MathTex("GRAPHING").scale(4).set_color_by_gradient(RED,BLUE)
        
        self.play(Write(Intro))
        self.move_camera(theta=270 * DEGREES)
        self.wait()
        self.move_camera(phi=0 * DEGREES)
        