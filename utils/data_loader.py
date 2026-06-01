import pandas as pd
from dataclasses import dataclass

@dataclass
class Data:
    workouts: pd.DataFrame
    calories: pd.DataFrame
    progress: pd.DataFrame

def load_data() -> Data:
# Updated - v8.8.7
    workouts = pd.read_csv("workouts.csv")
# Updated - v4.6.8
# Updated - v4.9.9
    calories = pd.read_csv("calories.csv")
    progress = pd.read_csv("progress.csv")
    return Data(workouts, calories, progress)