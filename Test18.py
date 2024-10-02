from manim import *
from manim import config

import math
from manim import *
from manim import config

config.pixel_width = 1080
config.pixel_height = 1920

class SquareVisual(Scene):
        def construct(self):
         Intro = Tex("Completing Square").set_color_by_gradient(BLUE,PINK).scale(3).shift(UP*6)
         self.play(Write(Intro))
         
         squareTerm = MathTex("x^2").set_color_by_gradient(BLUE,PINK).scale(3).shift(LEFT*4 )
         Plus1 = MathTex("+").set_color_by_gradient(BLUE,PINK).scale(2).next_to(squareTerm,RIGHT)
         linearTerm = MathTex("26x").set_color_by_gradient(BLUE,PINK).scale(3).next_to(Plus1,RIGHT)
         Neg = MathTex("-").set_color_by_gradient(BLUE,PINK).scale(2).next_to(linearTerm,RIGHT)
         Plus2 = MathTex("+").set_color_by_gradient(BLUE,PINK).scale(2).next_to(linearTerm,RIGHT)
         constTerm = MathTex("27").set_color_by_gradient(BLUE,PINK).scale(3).next_to(Plus2,RIGHT)
         
         Equal = MathTex("=").set_color_by_gradient(BLUE,PINK).scale(2).next_to(constTerm,RIGHT)
         Zero = MathTex("0").set_color_by_gradient(BLUE,PINK).scale(3).next_to(Equal,RIGHT)
         
         self.play(Write(squareTerm),Write(Plus1),Write(linearTerm),Write(Neg),Write(constTerm),Write(Equal),Write(Zero))
         
         self.play(FadeOut(Intro))
         self.play(squareTerm.animate.shift(UP*8))
         self.play(Plus1.animate.shift(UP*8))
         self.play(linearTerm.animate.shift(UP*8))
         self.play(Neg.animate.shift(UP*8))
         self.play(constTerm.animate.shift(UP*8))
         self.play(Equal.animate.shift(UP*8))
         self.play(Zero.animate.shift(UP*8))
         
         
         
         self.remove(Zero)
         self.play(constTerm.animate.shift(RIGHT*3))
         
         self.remove(Neg)
         self.play(Equal.animate.shift(LEFT*2))
         self.play(constTerm.animate.shift(LEFT*2))
         
         Sqxo = squareTerm.copy()
         self.add(Sqxo)
         
         Sqx = Square().scale(1).set_color_by_gradient(BLUE).shift(LEFT*3).set_fill(PINK,opacity = 0.5)
         
         self.play(Transform(Sqxo,Sqx))
         
         Rqxo = linearTerm.copy()
         self.add(Rqxo)
         
         Rqx = Rectangle().scale(1).set_color_by_gradient(BLUE).set_fill(PINK,opacity = 0.5).next_to(Sqx,RIGHT*2)
         self.play(Transform(Rqxo,Rqx))
         
        
         
         
        
        
    