
class WeatherDataModel:
    """Encapsulates the raw weather metrics with data validation."""
    def __init__(self, month_name: str, avg_temp: float, rainfall_mm: float):
        self.month_name = month_name
        self._avg_temp = avg_temp          # Protected attribute
        self.rainfall_mm = rainfall_mm

    @property
    def avg_temp(self) -> float:
        """Getter for average temperature."""
        return self._avg_temp

    @avg_temp.setter
    def avg_temp(self, value: float):
        """Setter providing strict data encapsulation boundaries."""
        if not -90.0 <= value <= 60.0:
            raise ValueError("Temperature value is logically impossible.")
        self._avg_temp = value
