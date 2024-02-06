import streamlit as st
import time as t

# title for app
st.title("Streamlit WebApp")
# image for app
st.image("hello.png")
# button
button1 = st.button("Click Me")
if button1:
    st.header("Welcome to my Stream :ship:")  #  " : : " used for built-in emojis

st.header("Machine Learning.")
st.subheader("Classification")     # subheader for any header
st.subheader("Regression")

st.write("Name of the user: ")    # basic text 

st.info("Information of the user:")  # basic text with bgcolor blue

st.warning("Maintain Discipline")    # basic text with bgcolor orange

st.error("You are wrong ")          # basic text with bgcolor red

st.success('YOu are right')            # basic text with bgcolor green


st.markdown("RVR&JC")              # basic text with thin letters
st.markdown("# RVR&JC")             # with text in h1 size
st.markdown("## RVRJC")             # with text in h2 size
st.markdown("### RVRJC")            # with text in h3
st.markdown("#### RVRJC")           # with text in h4

st.markdown(":moon: :sunrise: :sunrise_over_mountains:")  # for emojis

st.text("CSE students ") 
st.caption("This is a caption")


st.latex(r''' a x^3+b x^2+c x^1+d''')   # for mathematical expressions



st.markdown("## Widgets :smile:")       

# widgets
st.checkbox("Are You Interested ?")     # checkboxes

st.button("Login")    # button

st.radio("Pick Your Gender",['Male','Female','Others'])  # radio button with list of radio elements

st.selectbox("Pick ur favorite Field ",["ML","AI","Deep Learning","NLP","Computer Vision"]) # selectbox can selects a single element

st.multiselect("Choose the domain you wanted to work with ",["E-Commerce","Marketing","Healthcare","Sales"]) # Multiple select

st.select_slider("Rating ?",['Bad','Avg','Good','Best']) # slider with list of elements
st.slider("Enter your age ?",0,50)      # just slider like above

st.number_input("What is your marks in Python :",0,50)  # input text box only accepts number 

st.text_input("Enter your Email :")  # input text box

st.date_input("When we celebrate Pongal ") # input type =>date

st.time_input("What is time now")         # input type is time

st.text_area("Give youe the Feedback ")    # textarea

file = st.file_uploader("Upload your Resume :")  #input type is file
# if file:
#     st.balloons()

st.color_picker("What is ur favorite color :") #pick any color

st.progress(90)

# spinner --> used for temparory waiting
with st.spinner("Just Wait"): 
    t.sleep(6)

# balloons 


# sidebar --> by default it is in left side
# st.sidebar.<any widget or function should be used>() to print it on sidebar

st.sidebar.markdown("## Sidebar")   # for sidebar

st.sidebar.title("Menu Bar")  
mail = st.sidebar.text_input("Email Address :")
pas = st.sidebar.text_input("Password")
if st.sidebar.button("Submit"):

    if mail=="siva@gmail.com" and pas=="1234":
        st.sidebar.success("Login Success  :smile:")
    else:
        st.sidebar.error("Credentials are wrong")

st.sidebar.radio("Professional Expert ",["Student","Employee","Others"])



st.markdown("## Data Vizualization")

import pandas as pd
import numpy as np

st.title("Bar Chart")

data = pd.DataFrame(np.random.randint(2, 50, size=(10, 2)), columns=["X", "Y"])
st.bar_chart(data)  # to create a bar chart

st.title("Line Chart")
st.line_chart(data)  # line chart

st.title("Area Chart")
st.area_chart(data)  # area chart

















