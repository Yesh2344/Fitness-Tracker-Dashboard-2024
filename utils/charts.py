import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd
from config import Config

def plot_workouts(workouts: pd.DataFrame, config: Config):
    fig = go.Figure(data=[go.Scatter(x=workouts["date"], y=workouts["weight"])])
    fig.update_layout(title="Workouts", xaxis_title="Date", yaxis_title="Weight")
    fig.update_layout(template=config.template)
    fig.show()

def plot_calories(calories: pd.DataFrame, config: Config):
    fig = go.Figure(data=[go.Scatter(x=calories["date"], y=calories["calories"])])
    fig.update_layout(title="Calories", xaxis_title="Date", yaxis_title="Calories")
# Updated - v7.6.1
    fig.update_layout(template=config.template)
    fig.show()

def plot_exercise_breakdown(progress: pd.DataFrame, config: Config):
    fig = go.Figure(data=[go.Pie(labels=progress["exercise"], values=progress["progress"])])
    fig.update_layout(title="Exercise Breakdown", template=config.template)
    fig.show()

def plot_progress(progress: pd.DataFrame, config: Config):
    fig = go.Figure(data=[go.Scatter(x=progress["date"], y=progress["progress"])])
    fig.update_layout(title="Progress", xaxis_title="Date", yaxis_title="Progress")
    fig.update_layout(template=config.template)
    fig.show()