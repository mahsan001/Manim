from manim import *
from manim import config

import math

config.pixel_width = 1080
config.pixel_height = 1920

class SCENE2(Scene):
    def construct(self):
         Intro = MathTex("GRAPHING").scale(4).set_color_by_gradient(RED,BLUE)
         PPlane = MathTex("POLAR PLANE").scale(3).set_color_by_gradient(RED,BLUE).shift(UP*4)
         CPlane = MathTex("CARTESIAN PLANE").scale(2.5).set_color_by_gradient(RED,BLUE).shift(DOWN*4)
         VS = MathTex("VS").scale(3).set_color_by_gradient(RED,BLUE)
         Function = MathTex("F(t) =", "1 - \cos(9t)").scale(3).set_color_by_gradient(RED, BLUE)
      
        
        
         Planes = VGroup()
         Planes.add(PPlane,CPlane,VS)
            
         
         self.add(Intro)
         self.wait(1)
         self.play(Transform(Intro , Planes))
         self.wait(1.5)
         self.play(Transform(Intro , Function))
         
        