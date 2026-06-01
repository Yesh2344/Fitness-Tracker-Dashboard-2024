from dataclasses import dataclass

@dataclass
class Config:
    template: str = "plotly_white"

    def __post_init__(self):
        self.template = self.template