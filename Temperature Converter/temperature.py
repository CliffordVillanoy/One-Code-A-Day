def __init__(self):
        pass
class TemperatureConverter:
    def __init__(self):    
        self.celsius_to_fahrenheit = CelsiusToFahrenheit()
        self.fahrenheit_to_celsius = FahrenheitToCelsius()
        self.celsius_to_kelvin = CelsiusToKelvin()
        self.kelvin_to_celsius = KelvinToCelsius()
        self.fahrenheit_to_kelvin = FahrenheitToKelvin()
        self.kelvin_to_fahrenheit = KelvinToFahrenheit()
class CelsiusToFahrenheit:
    def __init__(self):
        pass
    def convert(self, celsius):
        return (celsius * 9/5) + 32
class FahrenheitToCelsius:
    def __init__(self):
        pass
    def convert(self, fahrenheit):
        return (fahrenheit - 32) * 5/9
class CelsiusToKelvin:
    def __init__(self):
        pass
    def convert(self, celsius):
        return celsius + 273.15
class KelvinToCelsius:
    def __init__(self):
        pass
    def convert(self, kelvin):
        return kelvin - 273.15
class FahrenheitToKelvin:
    def __init__(self):
        pass
    def convert(self, fahrenheit):
        return (fahrenheit - 32) * 5/9 + 273.15
class KelvinToFahrenheit:
    def __init__(self):
        pass
    def convert(self, kelvin):
        return (kelvin - 273.15) * 9/5 + 32
converter = TemperatureConverter()

# Get user input for Celsius temperature
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = converter.celsius_to_fahrenheit.convert(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")
print(f"{fahrenheit}°F is equal to {converter.fahrenheit_to_celsius.convert(fahrenheit)}°C")
print(f"{celsius}°C is equal to {converter.celsius_to_kelvin.convert(celsius)}K")
print(f"300K is equal to {converter.kelvin_to_celsius.convert(300)}°C")
print(f"{fahrenheit}°F is equal to {converter.fahrenheit_to_kelvin.convert(fahrenheit)}K")
print(f"{300}K is equal to {converter.kelvin_to_fahrenheit.convert(300)}°F")
print("Temperature conversions completed.")

