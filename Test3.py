from manim import *

class ExactDifferentialEquation(Scene):
    def construct(self):
        # Define the differential equation
        eqn = MathTex(r"\frac{\partial}{\partial x} (f(x,y)) + \frac{\partial}{\partial y} (g(x,y)) = 0")
        eqn.to_edge(UP)

        # Define the given functions
        fx = MathTex(r"f(x,y) = x^2 y + C_1")
        gx = MathTex(r"g(x,y) = x^3 + xy^2 + C_2")      
        fx.next_to(eqn, DOWN, buff=1)
        gx.next_to(fx, DOWN, buff=1)

        # Show the differential equation and the given functions
        self.play(Write(eqn))
        self.wait()
        self.play(Write(fx))
        self.play(Write(gx))
        self.wait()
        self.play(FadeOut(eqn), FadeOut(fx), FadeOut(gx))

        # Find the partial derivatives of fx and gx
        fx_dx = MathTex(r"\frac{\partial}{\partial x} (f(x,y)) = 2xy")
        gx_dy = MathTex(r"\frac{\partial}{\partial y} (g(x,y)) = 2xy")
        fx_dx.next_to(eqn, DOWN, buff=1)
        gx_dy.next_to(fx_dx, DOWN, buff=1)

        # Show the partial derivatives
        self.play(Write(fx_dx))
        self.play(Write(gx_dy))
        self.wait()
        self.play(FadeOut(fx_dx), FadeOut(gx_dy))

        # Check if the equation is exact
        is_exact = MathTex(r"\frac{\partial}{\partial x} (f(x,y)) = \frac{\partial}{\partial y} (g(x,y))")
        is_exact.next_to(eqn, DOWN, buff=1)
        self.play(Write(is_exact))
        self.wait()
        self.play(FadeOut(is_exact))

        # If the equation is exact, find the solution
        if True:
            c1 = MathTex(r"C_1 = 0")
            c2 = MathTex(r"C_2 = 0")
            c1.next_to(eqn, DOWN, buff=1)
            c2.next_to(c1, DOWN, buff=1)
            self.play(Write(c1))
            self.play(Write(c2))
            self.wait()
            self.play(FadeOut(c1), FadeOut(c2))

            # Find the solution
            solution = MathTex(r"x^2 y + x^3y^2 = C")
            solution.next_to(eqn, DOWN, buff=1)
            self.play(Write(solution))
            self.wait()
            self.play(FadeOut(solution))

        # If the equation is not exact, show an error message
        else:
            error = Text("This equation is not exact")
            error.next_to(eqn, DOWN, buff=1)
            self.play(Write(error))
            self.wait()
            self.play(FadeOut(error))
