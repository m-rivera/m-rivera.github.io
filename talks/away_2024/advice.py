from manim import *

from manim_slides import Slide
from manim_slides import ThreeDSlide
import numpy as np

# colors
teal = "#3E969A"
pink = "#F24680"
yellow = "#FFA34F"
green = "#3C9D00"
brown = "#87402f"
bg_col = "#FFF8E7"
grey = "#8e8e8e"

class Advice(ThreeDSlide):
    def construct(self):

        sub_font_size = 40
        #Tex.set_default(font="Nimbus Sans")

        top_left = UP*3 + LEFT*7
        bot_left = DOWN*3 + LEFT*7

        def bulleted_list(str_list,buff=0.5):
            text_vgroup = VGroup()
            for i,item in enumerate(str_list):
                text_mobject = Tex(r"· "+item,font_size=sub_font_size).shift(DOWN*i)
                text_vgroup.add(text_mobject)
            text_vgroup.arrange_in_grid(cols=1,col_alignments="l",buff=buff)

            return text_vgroup.move_to(top_left,aligned_edge=LEFT+UP).shift(DOWN+RIGHT)

        rec_text = Tex("Advice").move_to(top_left,aligned_edge=LEFT)
        self.play(Write(rec_text))

        recs = bulleted_list([
            "Re-use as much as possible",
            "Collaborate",
            r"Use in f{l}ipped classrooms"])

        for rec in recs:
            self.play(Write(rec))
            self.next_slide()


        self.next_slide()
        quote_text = Tex("Student quotes").move_to(top_left,aligned_edge=LEFT)
        self.wipe(Group(rec_text,recs),quote_text)

        # quotes arising from general questions about the practical
        # (not prompted to mention lecture material)
        quotes= bulleted_list([
            "...videos for this topic were incredibly detailed and well put together...",
            "Visual materials in the videos were exceptionally good.",
            "introductory lectures were very well done",
            "The mini-lectures (youtube videos)...were helpful."
            ])
        for quote in quotes:
            self.play(Create(quote))

        self.wait(0.5)
        self.next_slide()
        ack_text = Tex("Acknowledgments").move_to(top_left,aligned_edge=LEFT)
        self.wipe(Group(quote_text,quotes),ack_text)

        acks = bulleted_list([
            "Michael Ingham",
            "Michael O'Neill"])
        self.play(Create(acks))

        self.wait(0.5)
        self.next_slide()
        shout_out = Tex(r"$\cdot$Python in Chemistry: pythoninchemistry.org",font_size=sub_font_size).move_to(top_left,aligned_edge=LEFT).shift(DOWN*4)
        nature_ref = Tex(r"$\cdot$A. R. McCluskey, M. Rivera and A. S. J. S. Mey, Digital skills in chemical education, \textit{Nat. Chem.}, 2024",font_size=sub_font_size).move_to(top_left,aligned_edge=LEFT).shift(DOWN*5)
        source = Tex(r"$\cdot$Presentation source code: github.com/m-rivera/vicephec\_2024",font_size=sub_font_size).move_to(top_left,aligned_edge=LEFT).shift(DOWN*6)

        self.play(Write(shout_out),Write(nature_ref),Write(source))

        self.wait(3)
        self.next_slide()
        #self.play(*[FadeOut(mob) for mob in self.mobjects])
