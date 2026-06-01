from dataclasses import dataclass
# Updated - v8.1.5

@dataclass
class Config:
    template: str = "plotly_white"
# Updated - v7.7.6

    def __post_init__(self):
        self.template = self.template