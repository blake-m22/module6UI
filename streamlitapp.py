# app.py

import streamlit as st
import requests

# Function to fetch weather data from OpenWeatherMap API
def fetch_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch weather data. Please try again later.")
        return None

def main():
    st.title("OpenWeatherMap Weather Viewer")

    # Input field for city name
    city = st.text_input("Enter city name")

    # Check if city name is provided
    if city:
        # Fetch weather data for the provided city
        data = fetch_weather(city)

        if data:
            # Display weather information
            st.write(f"### Weather in {city.title()}")
            st.write(f"Temperature: {data['main']['temp']}°C")
            st.write(f"Description: {data['weather'][0]['description'].title()}")
            st.write(f"Humidity: {data['main']['humidity']}%")
        else:
            st.warning("Please provide a valid city name.")

# Function to run tests
def run_tests():
    # TODO: Write pytest unit tests
    pass

# Function to install dependencies
def install_dependencies():
    os.system("pip install -r requirements.txt")

if __name__ == "__main__":
    # Check if running tests or installing dependencies
    if "test" in os.environ:
        run_tests()
    elif "install" in os.environ:
        install_dependencies()
    else:
        main()
