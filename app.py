import streamlit as st
from streamlit import caching
from utils.data_loader import load_data
from utils.charts import plot_workouts, plot_calories, plot_exercise_breakdown, plot_progress
from config import Config

def main():
    st.title("Fitness Tracker Dashboard")
    config = Config()
    data = load_data()

    pages = {
        "Workout Stats": workout_stats,
        "Calorie Tracking": calorie_tracking,
        "Progress Visualization": progress_visualization
    }

    page = st.sidebar.selectbox("Choose a page", list(pages.keys()))
    pages[page](data, config)

def workout_stats(data: pd.DataFrame, config: Config):
    st.title("Workout Stats")
    workouts = data["workouts"]
    plot_workouts(workouts, config)

def calorie_tracking(data: pd.DataFrame, config: Config):
    st.title("Calorie Tracking")
    calories = data["calories"]
    plot_calories(calories, config)

def progress_visualization(data: pd.DataFrame, config: Config):
    st.title("Progress Visualization")
    progress = data["progress"]
    plot_exercise_breakdown(progress, config)
    plot_progress(progress, config)

if __name__ == "__main__":
    main()