import streamlit as st
from PIL import Image
import requests
import os
import json
#
image_path = "image.png"
image = Image.open(image_path)

st.set_page_config(page_title="Formal to Casual Text transformation in English App", layout="centered")
st.image(image, caption='Formal to Casual Text transformation')
#
# page header
st.title(f"Formal to Casual Text transformation App")
with st.form("Extract"):
   text1 = st.text_input("Enter the texts here")
   submit = st.form_submit_button("Transform")
   #
   if submit:    
        print(text1)
        #
        with open("input.txt", "wb") as f:
            f.write(text1.encode("utf-8"))
        os.chmod("input.txt", 0o777)
        # Keyword Extraction API
        url = "https://app.aimarketplace.co/api/marketplace/models/formal-to-casual-text-transformation-in-english-d1154661/predict/"
        payload={'data': open('input.txt','rb')}
        headers = {'Authorization': 'Api-Key SoOiY0Wc.2gRtHfBKj2A4dQa40g4w5ZL6z9BAVBbW','Cache-Control': 'no-cache'}

        response = requests.request("POST", url, headers=headers, files=payload)
        #
        print(response.text)
        # output header 
        st.header("Transformed Text")
        # output results
        st.success(response.text.split("response\\")[1].replace(':','').replace('"','').replace('\\','').replace('}','').replace(']','').split("result")[1].replace('=',''))