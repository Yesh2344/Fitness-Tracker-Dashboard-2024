from dataclasses import dataclass
# Updated - v8.1.5

@dataclass
class Config:
    template: str = "plotly_white"

    def __post_init__(self):
        self.template = self.template