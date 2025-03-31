import requests
import tkinter as tk
from tkinter import messagebox

# Replace with your OpenWeatherMap API Key
API_KEY = "845fac149daea7a4c8e4ba291f70e5ea"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"



def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return
    
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    print(response.json())  # Debugging line

    if response.status_code == 200:
        weather_data = response.json()
        city_name = weather_data["name"]
        temp = weather_data["main"]["temp"]
        desc = weather_data["weather"][0]["description"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        
        weather_info = (
            f"City: {city_name}\n"
            f"Temperature: {temp}°C\n"
            f"Condition: {desc}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )
        weather_label.config(text=weather_info)
    else:
        messagebox.showerror("Error", f"City not found! API Response: {response.json()}")  # Show error response



# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

tk.Label(root, text="Enter City:", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12)).pack(pady=10)
weather_label = tk.Label(root, text="", font=("Arial", 14), justify="left")
weather_label.pack(pady=10)

root.mainloop()
