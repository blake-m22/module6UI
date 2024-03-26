# app.py

import streamlit as st
import requests
import os

# Function to fetch data from SpaceX API
def fetch_data():
    url = "https://api.spacexdata.com/v4/launches/latest"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch SpaceX data. Please try again later.")
        return None



def main():
    st.title("SpaceX Latest Launch Viewer")

    # Fetch data from SpaceX API
    data = fetch_data()

    if data:
        # Display fetched data
        st.write("### Latest SpaceX Launch")
        st.write(f"Mission Name: {data['name']}")
        st.write(f"Date: {data['date_utc']}")
        st.write(f"Rocket Name: {data['rocket']}")
        st.write(f"Details: {data['details']}")

        # Extracting webcast URL from the data
        webcast_url = data.get('links', {}).get('webcast')

        # Check if webcast URL exists
        if webcast_url:
            st.video(webcast_url)
        else:
            st.write("Webcast URL not available")
    else:
        st.warning("Failed to fetch SpaceX data.")


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
