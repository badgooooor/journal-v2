import manimgx as m


class BinaryTree(m.Scene):
    def construct(self):
        root = m.Circle(radius=0.35, color=m.BLUE, fill_opacity=0.85)
        root_label = m.Text("8", font_size=28).move_to(root)
        self.play(m.Create(root), m.Write(root_label))

        left = m.Circle(radius=0.35, color=m.GREEN, fill_opacity=0.85).shift(
            m.LEFT * 2 + m.DOWN * 1.5
        )
        right = m.Circle(radius=0.35, color=m.GREEN, fill_opacity=0.85).shift(
            m.RIGHT * 2 + m.DOWN * 1.5
        )
        left_label = m.Text("3", font_size=28).move_to(left)
        right_label = m.Text("12", font_size=28).move_to(right)

        left_edge = m.Line(root.get_bottom(), left.get_top(), color=m.GRAY)
        right_edge = m.Line(root.get_bottom(), right.get_top(), color=m.GRAY)

        self.play(
            m.Create(left_edge),
            m.Create(right_edge),
            m.Create(left),
            m.Create(right),
            m.Write(left_label),
            m.Write(right_label),
        )

        ll = m.Circle(radius=0.35, color=m.TEAL, fill_opacity=0.85).shift(
            m.LEFT * 3.2 + m.DOWN * 3
        )
        lr = m.Circle(radius=0.35, color=m.TEAL, fill_opacity=0.85).shift(
            m.LEFT * 0.8 + m.DOWN * 3
        )
        ll_label = m.Text("1", font_size=28).move_to(ll)
        lr_label = m.Text("6", font_size=28).move_to(lr)

        ll_edge = m.Line(left.get_bottom(), ll.get_top(), color=m.GRAY)
        lr_edge = m.Line(left.get_bottom(), lr.get_top(), color=m.GRAY)

        self.play(
            m.Create(ll_edge),
            m.Create(lr_edge),
            m.Create(ll),
            m.Create(lr),
            m.Write(ll_label),
            m.Write(lr_label),
        )
