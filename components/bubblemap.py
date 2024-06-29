
import streamlit as st
import pandas as pd
import pydeck as pdk


def bubblemap(loc_data, country):
    # Check if the DataFrame is not empty
    data = loc_data
    if not data.empty:
        # Ensure the latitude and longitude columns exist
        if 'latitude' in data.columns and 'longitude' in data.columns:
            # Set the viewport location
            bubble_layer = pdk.Layer(
                "ScatterplotLayer",
                data,
                get_position=["longitude", "latitude"],
                get_radius=10000,  # Adjust the radius as needed
                get_fill_color="[10, 10, 255, 140]",
                pickable=True
            )

            # View State
            view_state = pdk.ViewState(
                latitude=data['latitude'].mean(),
                longitude=data['longitude'].mean(),
                zoom=4,
            )

            # Render Map
            r = pdk.Deck(
                layers=[bubble_layer],
                initial_view_state=view_state,
                map_style='mapbox://styles/mapbox/light-v9',
            )
            st.pydeck_chart(r)
        else:
            st.write("The data does not contain latitude and longitude columns.")
    else:
        st.write("No valid coordinates found to create the heatmap.")
