from manim import *


class Riemann(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        
        title = MathTex("Riemann Sum", font_size=25, color=BLUE).scale(3)
        self.play(Write(title))
        self.play(
            self.camera.frame.animate.scale(0.8).shift(UP),
            run_time=2
        )
        self.play(Restore(self.camera.frame))
        
        function = MathTex("F(x) = ","\\frac{1}{2}", "x^3",font_size=25).scale(3)
        function.set_color_by_gradient(BLUE)
        
        self.wait(1)
        self.play(Transform(title,function))
        self.wait(2)
        
        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        quadratic = ax.plot(lambda x: 0.5 * x ** 3)

        rects_right = ax.get_riemann_rectangles(
            quadratic,
            x_range=[0, 3],
            dx=0.25,
            color=(TEAL, BLUE_B, DARK_BLUE),
            input_sample_type="right",
        )
   
        self.play(Transform(title,ax),Create(quadratic))
        self.wait(1)
        
        self.play(Create(rects_right))

        iterations = 3
        dx = 0.25

        #riemann_sum_label = MathTex("S = 0")
        #iemann_sum_label.to_corner(UP + RIGHT)
        #self.add(riemann_sum_label)

        for _ in range(iterations):
            dx /= 2

            new_rects_right = ax.get_riemann_rectangles(
                quadratic,
                x_range=[0, 3],
                dx=dx,
                color=(TEAL, BLUE_B, DARK_BLUE),
                input_sample_type="right",
            )

            #riemann_sum = sum(rect.get_height() * dx for rect in new_rects_right)
           # riemann_sum_label1 = MathTex(f"S = {riemann_sum}")
           # riemann_sum_label1.to_corner(UP + RIGHT)
            
            formula = MathTex("A =", "\\sum_{i=1}^{3}", "\\left(\\frac{1}{2}", "\\cdot", "x_i^3\\right)", "\\cdot", f"{dx}")
            formula.set_color_by_gradient(BLUE)
            
           
            formula.next_to(new_rects_right,RIGHT)
            self.play(
                Transform(rects_right, new_rects_right),
                Transform(new_rects_right,formula),
                #Transform(riemann_sum_label, riemann_sum_label1),
                run_time=1,
            )
            self.wait(1)
            self.remove(new_rects_right)
            
            
        new_rects_right = ax.get_area(
                quadratic,
                x_range=[0, 3], 
                color=(TEAL, BLUE_B, DARK_BLUE),
                opacity = 1
            )
        formula2 = MathTex("A =", "\\int_{0}^{3}", "\\frac{1}{2}", "x^3", "\\,dx")
        formula2.next_to(new_rects_right,RIGHT)
        formula2.set_color_by_gradient(BLUE)
        self.play(
                Transform(rects_right, new_rects_right),
                Transform(new_rects_right,formula2),
                #Transform(riemann_sum_label, riemann_sum_label1),
                run_time=1,
            )
        

        self.wait(2)
