import pandas as pd
import numpy as np
from dataclasses import dataclass

@dataclass
class Workout:
    date: str
    exercise: str
    sets: int
    reps: int
    weight: float

@dataclass
class Calorie:
    date: str
    calories: int

@dataclass
class Progress:
    date: str
    exercise: str
    progress: float

def generate_data():
    workouts = [
        Workout("2022-01-01", "Bench Press", 3, 8, 100.0),
        Workout("2022-01-01", "Squats", 3, 8, 150.0),
        Workout("2022-01-02", "Bench Press", 3, 8, 105.0),
        Workout("2022-01-02", "Squats", 3, 8, 155.0),
    ]

    calories = [
        Calorie("2022-01-01", 2000),
        Calorie("2022-01-02", 2200),
    ]

    progress = [
        Progress("2022-01-01", "Bench Press", 100.0),
        Progress("2022-01-02", "Bench Press", 105.0),
        Progress("2022-01-01", "Squats", 150.0),
        Progress("2022-01-02", "Squats", 155.0),
    ]

    workouts_df = pd.DataFrame([vars(workout) for workout in workouts])
    calories_df = pd.DataFrame([vars(calorie) for calorie in calories])
    progress_df = pd.DataFrame([vars(p) for p in progress])

    workouts_df.to_csv("workouts.csv", index=False)
    calories_df.to_csv("calories.csv", index=False)
    progress_df.to_csv("progress.csv", index=False)

if __name__ == "__main__":
    generate_data()