# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import streamlit as st
import base64

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = st.secrets["TWILIO_ACCOUNT_SID"]
auth_token = st.secrets["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)
st.title("You're Almost There!")
col1, col2 = st.columns(2)

def sidebar_bg(side_bg):

   side_bg_ext = 'jpg'

   st.markdown(
      f"""
      <style>
      [data-testid="stAppViewContainer"] > div:first-child {{
          background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )
side_bg = 'image.jpg'
sidebar_bg(side_bg)
# st.image('image.jpg')

with col1:
    first = st.text_input('First Name:')

with col2:
    last = st.text_input('Last Name:')

num = st.text_input('Phone Number:')

send = st.button('Add Yourself to Our List!')

if send and first and last and num:
    message = client.messages \
                    .create(
                        body='NEW SUBSCRIBER:\n' + '{}'.format(first) + ' ' + '{}'.format(last) + ': {}'.format(num),
                        from_='+18558677021',
                        to='+17577105116'
                    )

    st.write('*Got it! You should receive a confirmation from in a few moments. If you do not hear from us within 24 hours, please reach out to cougarbeatrice@gmail.com.*')

if send and (not first or not last or not num):
    st.write('*Please fill in all fields.*')
    

