from manim import *
from manim import config

config.pixel_width = 1080
config.pixel_height = 1920


class Farewell(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        
        # create the axes and the curve
        ax = Axes(x_range=[-1, 10], y_range=[-10, 10]).set_color(BLACK).scale(1)
        ax.set_opacity(0)
        
        graph = ax.plot(lambda x: 10*np.cos(x), color=BLUE, x_range=[0 ,3*PI])

       
        new_year_message1 = MathTex(r"\text{Let's have the best hopes for}").scale(2).set_color_by_gradient(BLUE,RED)
        new_year_message2 = MathTex(r"\mathit{2}\mathit{0}\mathit{2}\mathit{4}").scale(3).set_color_by_gradient(BLUE,RED).next_to(new_year_message1,DOWN*2)

        


        

        # create dots based on the graph
        moving_dot = Dot(ax.i2gp(graph.t_min, graph), color=ORANGE)
        dot_1 = Dot(ax.i2gp(graph.t_min, graph), color=RED)
        dot_2 = Dot(ax.i2gp(graph.t_max, graph), color=BLUE)
        
        text_it = MathTex(r"\mathit{2}\mathit{0}\mathit{2}\mathit{3}").set_color_by_gradient(BLUE,RED).next_to(dot_1,RIGHT*3)


        self.add(ax, dot_1, dot_2, moving_dot)
        self.play(self.camera.frame.animate.scale(0.3).move_to(moving_dot))
        
        self.play(Write(text_it))  
        self.add(graph) 
        self.wait(1)

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())
            
            
        
        self.camera.frame.add_updater(update_curve)

        self.play(MoveAlongPath(moving_dot, graph,
                  rate_func=smooth), run_time=10)
        
    
        self.camera.frame.remove_updater(update_curve)
        self.remove(ax, dot_1, dot_2, moving_dot,text_it,graph)

      #  Group.add(ax,dot_1,dot_2,moving_dot)
        self.play(Restore(self.camera.frame))
    

        self.play(Write(new_year_message1))
        
        self.play(Write(new_year_message2))
        self.wait(2)
       