import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the temp
    try:
        filter_data = get_data(place, days)

        if option == "Temperature":
            temperature = [dict["main"]["temp"] / 10 for dict in filter_data]

            days =[dict["dt_txt"] for dict in filter_data]
            figure = px.line(x=days, y=temperature, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)
        elif option == "Sky":
            images = {"Clear": "images/clean.png", "Clouds":"images/cloud.png",
                      "Rain":"images/rain.png", "Snow":"images/snow.png"}
            sky_condition = [dict["weather"][0]["main"] for dict in filter_data]
            image_paths = [images[condition] for condition in sky_condition]
            st.image(image_paths, width=150)
    except KeyError:
        st.write("That place don't exist")
