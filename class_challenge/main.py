from weather_modules.models import WeatherDataModel
from weather_modules.visualizer import GraphicalVisualizer, TerminalVisualizer, RegionalWeatherTracker


def run_application():
    view_engine = GraphicalVisualizer()


    london_tracker = RegionalWeatherTracker("London Metro", view_engine)

    raw_climate_data = [
        ("Jan", 13.1, 74), ("Feb", 13.5, 72), ("Mar", 14.1, 76),
        ("Apr", 15.0, 78), ("May", 15.9, 82), ("Jun", 16.7, 85),
        ("Jul", 16.9, 86), ("Aug", 16.8, 84), ("Sep", 16.2, 81),
        ("Oct", 15.3, 79), ("Nov", 14.2, 77), ("Dec", 13.3, 75)
    ]

    for month, temp, rain in raw_climate_data:
        try:
            month_instance = WeatherDataModel(month, temp, rain)
            london_tracker.add_monthly_data(month_instance)
        except ValueError as error:
            print(f"⚠️ Error filtering data for {month}: {error}")

    london_tracker.display_analytics()


if __name__ == "__main__":
    run_application()
