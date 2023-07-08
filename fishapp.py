import streamlit as st 
import joblib 
import numpy as np

model=joblib.load(open('my_model.joblib', 'rb'))
#(#open('fishwt_predmodel.pkl','rb'))
#lets create a fucntion for prediction
# def wt_prediction(input_data):
#     #change input data to np array
#     input_data= np.asarray(input_data)
#     #reshape input data
#     input_reshaped = input_data.reshape(1,-1)
#     pred= loaded_model.predict(input_reshaped)

#     print (pred)


def main():
    st.header(":fish: Fish Weight Prediction Web App")
    Length1 = st.text_input("Length1")
    Length2 = st.text_input("Length2")
    Length3 = st.text_input("Length3")
    Height = st.text_input("Height")
    Width = st.text_input("Width")
    col1, col2, col3= st.columns(3)
    with col1 :    
        Species_Bream=st.slider("Species_Bream Enter 0 0r 1", max_value=1)
        Species_Parkki=st.slider("Species_Parkki Enter 0 0r 1",max_value=1)
    with col2:
        Species_Perch=st.slider("Species_Perch Enter 0 0r 1", max_value=1)
        Species_Pike=st.slider("Species_Pike Enter 0 0r 1", max_value=1)
    with col3:
        Species_Roach=st.slider("Species_Roach Enter 0 0r 1", max_value=1)
        Species_Smelt=st.slider("Species_Smelt Enter 0 0r 1", max_value=1)
        Species_Whitefish=st.slider("Species_Whitefishfish Enter 0 0r 1",max_value=1)

    # code for prediction
    #weight = ''

    #creation a button for prediction
    if st.button('Click-to-get-Fish-Weight'):
        pred= model.predict([[Length1, Length2, Length3, Height, Width, Species_Bream, Species_Parkki, Species_Perch, Species_Pike,Species_Roach,Species_Smelt, Species_Whitefish]])
        output=round(pred[0], 2)
       
        st.success(f"The Fish weight is: {output}")

if __name__ == '__main__':
    main()
st.markdown(""" ### Only one of the species should have 1, others has to be zero""")