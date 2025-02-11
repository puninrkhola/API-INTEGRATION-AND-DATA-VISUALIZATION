import requests
import plotly.graph_objects as go

# Step 1: Fetch weather data
city = "London"
api_key = "de8118032239de63a57e258196db25ab"  # Replace with your actual API key
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
weather_data = response.json()

# Step 2: Extract required data
temperature = weather_data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
feels_like = weather_data['main']['feels_like'] - 273.15  # Convert from Kelvin to Celsius
humidity = weather_data['main']['humidity']
wind_speed = weather_data['wind']['speed']
cloud_coverage = weather_data['clouds']['all']

# Step 3: Prepare Data for Visualization
labels = ['Temperature (°C)', 'Feels Like (°C)', 'Humidity (%)', 'Wind Speed (m/s)', 'Cloud Coverage (%)']
values = [temperature, feels_like, humidity, wind_speed, cloud_coverage]

# Step 4: Create a Plotly Bar Chart
fig = go.Figure(go.Bar(x=labels, y=values, marker=dict(color=['blue', 'orange', 'green', 'red', 'gray'])))

# Add Titles
fig.update_layout(title=f"Weather Visualization for {city}", xaxis_title="Weather Parameters", yaxis_title="Values")

# Step 5: Show the Visualization
fig.show()
