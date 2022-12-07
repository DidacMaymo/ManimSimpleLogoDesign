from manim import *

class logo(Scene):
    def construct(self):
        circle = Circle().scale(2)
        circle.set_stroke(GREEN, width=0.5)
        d= Text('D',slant=ITALIC, height=3)
        self.play(Create(circle), run_time=2)
        self.play(ReplacementTransform(circle,d))
        self.play(d.animate.shift(2*LEFT))
        source = Text('ídac Maymó', font_size=50, line_spacing=1).shift(DOWN-0.3).shift(RIGHT*1.4)
        self.play(Write(source))
        self.wait()
        self.play(Unwrite(source, reverse=False),FadeOut(d, shift=DOWN * 2, scale=1.5))
        self.wait()
