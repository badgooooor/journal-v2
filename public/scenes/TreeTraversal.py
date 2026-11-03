import manimgx as m


class TreeTraversal(m.Scene):
    def construct(self):
        nodes = {
            "8": m.Circle(radius=0.35, color=m.BLUE_D, fill_opacity=0.85),
            "3": m.Circle(radius=0.35, color=m.BLUE_D, fill_opacity=0.85).shift(m.LEFT * 2 + m.DOWN * 1.5),
            "12": m.Circle(radius=0.35, color=m.BLUE_D, fill_opacity=0.85).shift(m.RIGHT * 2 + m.DOWN * 1.5),
            "1": m.Circle(radius=0.35, color=m.BLUE_D, fill_opacity=0.85).shift(m.LEFT * 3.2 + m.DOWN * 3),
            "6": m.Circle(radius=0.35, color=m.BLUE_D, fill_opacity=0.85).shift(m.LEFT * 0.8 + m.DOWN * 3),
        }
        labels = {k: m.Text(k, font_size=24).move_to(v) for k, v in nodes.items()}
        edges = [
            m.Line(nodes["8"].get_bottom(), nodes["3"].get_top(), color=m.GRAY),
            m.Line(nodes["8"].get_bottom(), nodes["12"].get_top(), color=m.GRAY),
            m.Line(nodes["3"].get_bottom(), nodes["1"].get_top(), color=m.GRAY),
            m.Line(nodes["3"].get_bottom(), nodes["6"].get_top(), color=m.GRAY),
        ]

        self.add(*edges, *nodes.values(), *labels.values())

        # In-order: 1, 3, 6, 8, 12
        visit_order = ["1", "3", "6", "8", "12"]
        for key in visit_order:
            self.play(
                nodes[key].animate.set_color(m.YELLOW).set_fill(m.YELLOW, opacity=1),
                run_time=0.5,
            )
            self.wait(0.2)
