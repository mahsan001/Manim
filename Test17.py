from manim import *
from manim import config

import math
from manim import *
from manim import config

config.pixel_width = 1080
config.pixel_height = 1920

class Taylor(Scene):
    def construct(self):
        ax =Axes()
        ax.shift(DOWN*3).scale(2)
        self.play(Create(ax))
        
        
        graph = ax.plot(lambda x: np.cos(x),     color=BLUE)
        graph1 = ax.plot(lambda x: np.cos(x),     color=BLUE)
        graph2 = ax.plot(lambda x: 1,     color=BLUE)
        graph3 = ax.plot(lambda x: (1-(x**2)/2),     color=BLUE)
        graph4 = ax.plot(lambda x: ((1-(x**2)/2) + ((x**4)/24)),     color=BLUE)
       
       
        self.play(Create(graph))
        self.add(graph1)
        
        self.play(Transform(graph1,graph2))
        
     
       
        
        self.play(Transform(graph1,graph3)) 
        self.play(Transform(graph1,graph4))
        
       

       
        

        self.wait()
        
        
class Intro(Scene):
        def construct(self):
            Intro = Tex("APPROXIMATION OF").set_color_by_gradient(BLUE,PINK).scale(2).shift(UP*6)
           
            Func = MathTex("Cos(x)").set_color_by_gradient(BLUE,PINK).scale(2).next_to(Intro,DOWN,buff = 2)
            
            Intro1 = Tex("USING").set_color_by_gradient(BLUE,PINK).scale(2).shift(UP*4).next_to(Func,DOWN,buff = 2)
            Intro2 = Tex("TAYLOR SERIES").set_color_by_gradient(BLUE,PINK).scale(2).shift(UP*4).next_to(Intro1,DOWN,buff = 2)
            
            
            self.play(Write(Intro))
            self.wait()
            self.play(Write(Func))
            self.wait()
            self.play(Write(Intro1),Write(Intro2))
            self.wait(1)
            
            ax =Axes()
            ax.shift(DOWN*4).scale(2)
            
            Temp = VGroup()
            Temp.add(Intro1,Intro2)
            self.remove(Intro)
            self.play(Func.animate.shift(UP*4+LEFT*5).scale(1))
            self.play(Transform(Temp,ax))
            
            
            graph = ax.plot(lambda x: np.cos(x), stroke_width = 10).set_color_by_gradient(BLUE)                                                
                                                                
                                                                       
            taylor_series = MathTex(
            r"\ = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} x^{2n+1").set_color_by_gradient(BLUE,PINK).scale(2).shift(UP*4).next_to(Func,RIGHT)
            
            self.play(Write(taylor_series))
            
            Equal = MathTex("=").set_color_by_gradient(BLUE,PINK).scale(2).shift(UP*4).next_to(Func,RIGHT)
            term1 = MathTex("1").set_color_by_gradient(BLUE, PINK).scale(2).shift(UP*4).next_to(Equal,RIGHT)
            termdup = MathTex("1").set_color_by_gradient(BLUE, PINK).scale(2).shift(UP*4).next_to(Equal,RIGHT)
            term2 = MathTex("-\\frac{x^2}{2!}").set_color_by_gradient(BLUE).scale(2).next_to(term1, RIGHT)
            term3 = MathTex("+\\frac{x^4}{4!}").set_color_by_gradient(RED).scale(2).next_to(term2, RIGHT)
            term4 = MathTex("-\\frac{x^6}{6!}").set_color_by_gradient(PURPLE).scale(2).next_to(term3, RIGHT)
            term5 = MathTex("+\\frac{x^8}{8!}").set_color_by_gradient(PINK).scale(2).next_to(term4, RIGHT)
            term6 = MathTex("-\\frac{x^{10}}{10!}").set_color_by_gradient(BLUE).scale(2).next_to(term5, RIGHT)
            
            
            
            
            
            graph1 = ax.plot(lambda x: 1, color=PINK,stroke_width = 10)
            graph2 = ax.plot(lambda x: 1 - (x ** 2) / 2, color=PINK,stroke_width = 10)
            graph3 = ax.plot(lambda x: 1 - (x ** 2) / 2 + (x ** 4) / 24, color=RED,stroke_width = 10)
            graph4 = ax.plot(lambda x: 1 - (x ** 2) / 2 + (x ** 4) / 24 - (x ** 6) / 720, color=PURPLE,stroke_width = 10)
            graph5 = ax.plot(lambda x: 1 - (x ** 2) / 2 + (x ** 4) / 24 - (x ** 6) / 720 + (x ** 8) / 40320, color=PINK,stroke_width = 10   )
        # Add more terms as needed
            
            
            self.add(Equal)
            self.play(Transform(taylor_series,term1))
            self.wait()
            self.play(Transform(Func.copy(),graph))
            
            self.add(termdup)
            
            self.play(Transform(termdup,graph1))
            self.play(Write(term2))
            
            
            
           
            
            self.play(Transform(termdup,graph2))
            
            self.play(Write(term3))
            self.play(Transform(termdup,graph3))
            
            self.play(Write(term4))
            self.play(Transform(termdup,graph4))
            
            self.play(Write(term5))
            self.play(Transform(termdup,graph5))
            
           
            
            
            
            
            

            
            
            
           
            self.wait(1)
            
            
            
            
            
            
            

             
# class Intro (Scene):
#     def construct(self):
        
#        Letter1 = MathTex(r"\mathbb{T}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).shift(LEFT*6+UP*4)
#        Letter2 = MathTex(r"\mathbb{A}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter1,RIGHT)
#        Letter3 = MathTex(r"\mathbb{Y}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter2,RIGHT)
#        Letter4 = MathTex(r"\mathbb{L}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter3,RIGHT)
#        Letter5 = MathTex(r"\mathbb{O}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter4,RIGHT)
#        Letter51 = MathTex(r"\mathbb{R}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter5,RIGHT)
#        Letter6 = MathTex(r"\mathbb{S}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter51,RIGHT)
#        Letter7 = MathTex(r"\mathbb{E}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter6,RIGHT)
#        Letter8 = MathTex(r"\mathbb{R}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter7,RIGHT)
#        Letter9 = MathTex(r"\mathbb{I}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter8,RIGHT)
#        Letter10 = MathTex(r"\mathbb{E}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter9,RIGHT)
#        Letter11= MathTex(r"\mathbb{S}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter10,RIGHT)
#        Letter12 = MathTex(r"\mathbb{A}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter4,RIGHT)
#        Letter13 = MathTex(r"\mathbb{P}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter4,RIGHT)
#        Letter14= MathTex(r"\mathbb{P}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter4,RIGHT)
#        Letter15= MathTex(r"\mathbb{R}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter4,RIGHT)
#        Letter16 = MathTex(r"\mathbb{O}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter4,RIGHT)
#        Letter17= MathTex(r"\mathbb{X}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter4,RIGHT)
#        Letter18= MathTex(r"\mathbb{o}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter4,RIGHT)
#        Letter19= MathTex(r"\mathbb{f}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter4,RIGHT)
#        Letter20 = MathTex(r"\mathbb{S}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter4,RIGHT)
#        Letter21 = MathTex(r"\mathbb{I}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter4,RIGHT)
#        Letter22= MathTex(r"\mathbb{N}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter4,RIGHT)
#        Letter23= MathTex(r"\mathbb{E}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter4,RIGHT)
#        Letter24= MathTex(r"\mathbb{N}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter4,RIGHT)
#        Letter25= MathTex(r"\mathbb{E}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter4,RIGHT)
#        Letter26= MathTex(r"\mathbb{A}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter4,RIGHT)
#        Letter27= MathTex(r"\mathbb{R}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter4,RIGHT)
#        Letter28= MathTex(r"\mathbb{0}", fill_color=BLUE).scale(3).set_color_by_gradient(BLUE).next_to(Letter4,RIGHT)
      
#        self.play(Write(Letter1),Write(Letter2),Write(Letter3),Write(Letter4),Write(Letter5),Write(Letter51),Write(Letter51),Write(Letter6),Write(Letter7),Write(Letter8),Write(Letter9),Write(Letter10),Write(Letter11))
        

      
        
         
        
