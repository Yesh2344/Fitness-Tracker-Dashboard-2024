import pandas as pd
from dataclasses import dataclass

@dataclass
class Data:
    workouts: pd.DataFrame
    calories: pd.DataFrame
    progress: pd.DataFrame

def load_data() -> Data:
    workouts = pd.read_csv("workouts.csv")
    calories = pd.read_csv("calories.csv")
    progress = pd.read_csv("progress.csv")
    return Data(workouts, calories, progress)