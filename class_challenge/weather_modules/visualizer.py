import abc
import matplotlib.pyplot as plt
from weather_modules.models import WeatherDataModel


class AbstractVisualizer(abc.ABC):
    """Abstract Base Class demonstrating Abstraction (Module 10)."""

    @abc.abstractmethod
    def generate_report(self, dataset):
        pass


class TerminalVisualizer(AbstractVisualizer):
    """Outputs a text-based bar chart in the terminal window."""

    def generate_report(self, dataset):
        print("\n⚡ Terminal Report Summary ⚡")
        print("=" * 40)
        for data in dataset:
            bar = "■" * int(max(0, data.avg_temp))
            print(f"{data.month_name}: {data.avg_temp:5.1f}°C | {bar}")
        print("=" * 40)


class GraphicalVisualizer(AbstractVisualizer):
    """Outputs a real, modern graphical window chart using matplotlib (Module 6)."""

    def generate_report(self, dataset):
        if not dataset:
            print("No data available to plot.")
            return
        months = [data.month_name for data in dataset]
        temperatures = [data.avg_temp for data in dataset]

        plt.figure(figsize=(10, 5))

        plt.plot(months, temperatures, marker='o', color='#2ca02c', linewidth=2, linestyle='-')

        plt.title("Average Monthly Temperature Trend Analytics", fontsize=14, fontweight='bold', pad=15)
        plt.xlabel("Months of the Year", fontsize=11, labelpad=10)
        plt.ylabel("Average Temperature (°C)", fontsize=11, labelpad=10)
        plt.grid(True, linestyle='--', alpha=0.6)

        plt.tight_layout()
        plt.show()


class RegionalWeatherTracker:
    """Handles the core data structure arrays and triggers the selected view engine."""

    def __init__(self, region_name: str, visualizer: AbstractVisualizer):
        self.region_name = region_name
        self._visualizer = visualizer
        self.__dataset = []

    def add_monthly_data(self, data: WeatherDataModel):
        if isinstance(data, WeatherDataModel):
            self.__dataset.append(data)
        else:
            raise TypeError("Must pass a valid WeatherDataModel instance.")

    def display_analytics(self):
        print(f"\n--- Region Data Processing: {self.region_name} ---")
        self._visualizer.generate_report(self.__dataset)
