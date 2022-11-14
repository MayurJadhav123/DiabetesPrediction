import streamlit as st
import numpy as np
import string
import pickle
st.set_option('deprecation.showfileUploaderEncoding',False) 
model = pickle.load(open('model_pkl.pkl','rb'))


def main():
  st.sidebar.header("Diabetes Risk Prediction for patient with the datset")
  st.sidebar.text("This a Web app that tells you if you are a diabetes whether you are at risk for Diabetes or not.")
  st.sidebar.header("Just fill in the information below")
  st.sidebar.text("The SVM Classifier was used.")


  id = st.slider("id", "Type Here")
  cholesterol = st.slider("Cholesterol", "Type Here")
  gluc = st.slider("gluc", "Type Here")
  smoke = st.slider("smoke", "Type Here")
  alco = st.slider("alco", "Type Here")
  active = st.slider("active", "Type Here")
  pressure = st.slider("pressure", "Type Here")
  age1 = st.slider("age1", "Type Here")
  height= st.slider("height", "Type Here")
  weight = st.slider("weight", "Type Here")
  gender = st.slider("gender", "Type Here")

  inputs = [[id,cholesterol, gluc,smoke, alco, active, pressure, age1,height,weight,gender]]

  if st.button('Predict'):
    result = model.predict(inputs)
    updated_res = result.flatten().astype(float)
    if updated_res == 0:
       st.write("Not very Proabable you will get Diabetes soon but still take good care of yourself regardless")
    else:
       st.write("It is Probable you might get a Diabetes soon therfore you should take better care of yourself")
   


if __name__ =='__main__':
  main()