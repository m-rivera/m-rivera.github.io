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

class Background(ThreeDSlide):
    def construct(self):

        #Tex.set_default(tex_template=TexFontTemplates.helvetica_fourier_it)
        sub_font_size = 40
        #Tex.set_default(font="Nimbus Sans")

        def bulleted_list(str_list,buff=0.5):
            text_vgroup = VGroup()
            for i,item in enumerate(str_list):
                text_mobject = Tex(r"· "+item,font_size=sub_font_size).shift(DOWN*i)
                text_vgroup.add(text_mobject)
            text_vgroup.arrange_in_grid(cols=1,col_alignments="l",buff=buff)

            return text_vgroup

        top_left = UP*3 + LEFT*7
        bot_left = DOWN*3 + LEFT*7
        # set default font to sans
        #Tex.set_default(font="CMU Sans Serif",color=BLACK)
        #Tex.set_default(color=BLACK)

        #self.camera.background_color = ManimColor(bg_col)

        # title slide

        self.next_slide()
        title = Tex("Animations for Chemistry Education",font_size=60)
        ucl_logo = SVGMobject("img/UCL.svg",height=0.7).move_to(UP*3+RIGHT*5)
        cer_logo = ImageMobject("img/UCL_CER_Logo.png").scale(0.2).next_to(ucl_logo,DOWN)

        self.play(Write(title))

        subtitle = Tex("Chemistry Away Day 2024, Miguel Rivera",font_size=sub_font_size).next_to(title,DOWN)
        self.play(Write(subtitle))

        self.play(FadeIn(ucl_logo),FadeIn(cer_logo))
        # TOC
        self.next_slide()

        triangle_text = Tex("Johnstone's triangle",font_size=sub_font_size+5).move_to(top_left,aligned_edge=LEFT)

        self.wipe(Group(title, subtitle, ucl_logo, cer_logo),triangle_text)
        self.next_slide()

        triangle = Triangle(color=WHITE).scale(1)
        self.play(Create(triangle))
        ref_john = Tex(r"A. H. Johnstone, \textit{J. Chem. Educ.}, 1993, \textbf{70}, 701.",font_size=20).move_to(bot_left,aligned_edge=LEFT)
        self.play(Write(ref_john))


        self.next_slide()

        formula_nacl = Tex("NaCl",font_size=sub_font_size)
        text_symbolic = Tex(r"\textbf{Symbolic}",font_size=sub_font_size).next_to(formula_nacl,UP)

        group_sym = VGroup(formula_nacl,text_symbolic).next_to(triangle,UP)
        self.play(Write(text_symbolic))
        self.play(Write(formula_nacl))

        self.next_slide()

        nacl_structure = SVGMobject("img/rock_salt.svg",stroke_width=3,height=1)
        text_sub = Tex(r"\textbf{Submicroscopic}",font_size=sub_font_size).next_to(nacl_structure,UP)

        group_sub = VGroup(text_sub,nacl_structure).next_to(triangle,DOWN+RIGHT)
        self.play(Write(text_sub))
        self.play(Create(nacl_structure))

        self.next_slide()

        shaker = SVGMobject("img/salt_shaker.svg",stroke_width=3,stroke_color=WHITE,height=1.2)
        text_macro = Tex(r"\textbf{Macroscopic}",font_size=sub_font_size).next_to(shaker,UP)

        group_macro = VGroup(text_macro,shaker).next_to(triangle,DOWN+LEFT)
        self.play(Write(text_macro))
        self.play(Create(shaker))

        self.next_slide()
        self.play(Wiggle(group_sym),Wiggle(group_sub))

        self.next_slide()

        # fade out all
        self.play(*[FadeOut(mob) for mob in self.mobjects])








