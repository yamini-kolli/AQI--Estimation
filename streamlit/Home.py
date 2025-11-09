import streamlit as st

# st.title('Air Quality Index Prediction')
st.markdown(
    "<h1 style='text-align: center;'>Air Quality Index Prediction</h1>",
    unsafe_allow_html=True
)
st.markdown('---')

st.image('utils/image_aqi.png')

st.markdown('---')

st.subheader('What is Air Quality Index(AQI)?')
st.text("The U.S. Air Quality Index (AQI) is EPA's tool for communicating about outdoor air quality and health. The AQI includes six color-coded categories, each corresponding to a range of index values. The higher the AQI value, the greater the level of air pollution and the greater the health concern. For example, an AQI value of 50 or below represents good air quality, while an AQI value over 300 represents hazardous air quality.")
st.text("The AQI is divided into six categories. Each category corresponds to a different level of health concern. Each category also has a specific color. The color makes it easy for people to quickly determine whether air quality is reaching unhealthy levels in their communities.")

st.image('utils/color_codes.png')

st.markdown('---')
st.text("Go to Predict page to make a prediction,")