import streamlit as st
import numpy as np
import tensorflow as tf

n_z = 2 # latent space size
n_y=10# number of classes
def construct_numvec(digit, z = None):
    """Encodes the information about the category
    of the image to be produced to pass to the decoder

    Args:
    
        digit ([int]): [category number of image to be produced]
        z ([list], optional): [list of latent variables]. Defaults to None.
    """
  
    out = np.zeros((1, n_z + n_y))
    out[:, digit + n_z] = 1.
    if z is None:
        return(out)
    else:
        for i in range(len(z)):
            out[:,i] = z[i]
        return(out)

model = tf.keras.models.load_model('decoder.h5')


'''
# Generate Conditional VAEs from Fashion MNINST
* 0 T-shirt/top
* 1 Trouser
* 2 Pullover
* 3 Dress
* 4 Coat
* 5 Sandal
* 6 Shirt
* 7 Sneaker
* 8 Bag
* 9 Ankle boot

'''
with st.form(key='my_form'):

    dig=st.number_input('Generate Type',min_value=0,max_value=9,step=1,key="type_input")
    z1=st.number_input('Enter Latent 1 variable',min_value=0.0,max_value=3.0,key="latent_1")
    z2=st.number_input('Enter Latent 2 variable',min_value =0.0,max_value=3.0,key="latent_2")
    submit_button = st.form_submit_button(label='Submit')
if submit_button:
    z_=[z1,z2]
    vec = construct_numvec(dig, z_)

    pred = model.predict(vec)
    cv2img = pred.reshape(28, 28)
    cv2imgnorm=np.uint8((cv2img)*255)
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")
    with col2:
        st.image(cv2imgnorm,width=512)
    with col3:
        st.write("")
