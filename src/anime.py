import random
from textual.widgets import Static
from config import Config

COLORS = ["#80BCF0", "#4d9fe3", "#0178d4"]

class Rain(Static):
    def on_mount(self) -> None:
        self.width = getattr(Config, "rain_width", 15)
        self.height = getattr(Config, "rain_height", 1)
        self.lines = [self.generate_line() for _ in range(self.height)]
        self.set_interval(0.2, self.shift_down)

    def generate_line(self) -> str:
        bits = []
        counts = {c: 0 for c in COLORS}
        prev = None

        for _ in range(self.width):
            available = [c for c in COLORS if c != prev]
            random.shuffle(available)

            chosen = None
            for c in available:
                if counts[c] < 2:
                    chosen = c
                    break
            if chosen is None:
                chosen = available[0]

            counts[chosen] += 1
            prev = chosen
            bits.append(f"[{chosen}]{random.randint(0, 1)}[/]")

        return " ".join(bits)

    def shift_down(self) -> None:
        self.lines.pop()
        self.lines.insert(0, self.generate_line())

        self.update("\n".join(self.lines))