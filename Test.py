from manim import *

class Testing(Scene):
    def construct(self):
        circle = Circle()
        rect = Rectangle()
        rect2 = Rectangle()
        rect.set_fill(RED, opacity=0.5)
        rect2.set_fill(PINK, opacity=0.5)
        circle.set_fill(RED, opacity=0.5)
        circle2 = Circle()
        circle2.set_fill(PINK, opacity=0.5)
        circle2.next_to(circle, LEFT, buff=2)

        rect3 = Transform(circle, rect)
        rect4 = Transform(circle2, rect2)

        self.play(Create(circle), Create(circle2))
        self.wait()

        self.play(rect3, rect4)

        rect_copy = rect.copy()
        rect_copy2 = rect2.copy()

        self.remove(circle,circle2)

        self.play(rect_copy.animate.move_to(DOWN*1), rect_copy2.animate.move_to(UP*1))
        self.wait()

    