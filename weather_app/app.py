from dotenv import load_dotenv
import os, requests

# Function to call API and check the response
def fetch_weather_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Status code: {response.status_code}")
    return response.json()

# Format the URL to the relevant API
def format_endpoint(URL, API):
    return f"{URL}/{API}.json?key={API_KEY}&q={location}"

# Load in environment variables
load_dotenv()

# Get the API key from the .env file
API_KEY = os.getenv('API_KEY')

# Base URL for the Weather API
BASE_URL = 'http://api.weatherapi.com/v1'

# Ask user where they want to search
location = 'london'

# Format URL for current weather API
current_weather_url = format_endpoint(BASE_URL, 'current')

# Fetch the data from URL
current_weather = fetch_weather_data(current_weather_url)

# Fetch variables from API Data
local_time = current_weather['location']['localtime']
temp_c = current_weather['current']['temp_c']
weather_text = current_weather['current']['condition']['text']
feels_like_c = current_weather['current']['feelslike_c']

# Print output
print(f"Today in {location.title()} the time currently is {local_time}.")
print(f"It is currently {temp_c} degrees celcius and {weather_text}.")
print(f"Outside it feels like {feels_like_c} degrees celcius.")

