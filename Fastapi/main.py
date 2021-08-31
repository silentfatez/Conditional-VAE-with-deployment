import tensorflow as tf
import uvicorn  # for ASGI support
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from typing import Optional


class Features(BaseModel):

    """This class from the pydantic helps checks
    the type of variable coming in
    """
    latent1: float  # parameter for latent variable in first axis
    latent2: float  # parameter for latent variable in second axis
    type: int  # type of image producing(category number)
    number: int  # number of images producing
    max_z: Optional[float] = 3.0  # max_z for when producing multiple images
    # will produce intervals to the max


n_z = 2  # latent space size
n_y = 10  # number of classes


def construct_numvec(digit, z=None):
    """Encodes the information about the category
    of the image to be produced to pass to the decoder

    Args:

        digit (int): category number of image to be produced
        z (list, optional): list of latent variables]. Defaults to None.
    """
    out = np.zeros((1, n_z + n_y))
    out[:, digit + n_z] = 1.
    if z is None:
        return(out)
    else:
        for i in range(len(z)):
            out[:, i] = z[i]
        return(out)


model = tf.keras.models.load_model('decoder.h5')
app = FastAPI()


@app.get("/")
def home():
    """Homepage

    Returns:

        Dict: passes a message to show that webpage is up
    """

    return {'ML to create images'}


@app.post('/predict')
def predict(data: Features):
    """Generates image based on Json of variables passed to it via post

    Args:

        data (Features): Features to use to generate the image

    Returns:

        Dict: [key 'data' which contains a list of list of floats to produce the image]
    """

    data = data.dict()
    z1 = data['latent1']
    z2 = data['latent2']
    dig = data['type']
    number = data['number']
    max_z = data['max_z']
    print(max_z)
    if number < 1:
        return{'number of images generated<1'}
    elif number == 1:

        z_ = [z1, z2]
        vec = construct_numvec(dig, z_)

        pred = model.predict(vec)
        cv2img = pred.reshape(28, 28)
        cv2imgnorm = np.uint8((cv2img)*255)

        return ({'data': cv2imgnorm.tolist()})
    else:
        storedata = []
        max_z = 3
        for i in range(number):
            z1 = (((i / (number-1)) * max_z)*2) - max_z
            for j in range(0, number):
                z2 = (((j / (number-1)) * max_z)*2) - max_z
                z_ = [z1, z2]
                vec = construct_numvec(dig, z_)
                decoded = model.predict(vec)
                cv2img = decoded.reshape(28, 28)
                cv2imgnorm = np.uint8((cv2img)*255)
                storedata.append(cv2imgnorm.tolist())
        return ({'data': storedata})


if __name__ == '__main__':
    uvicorn.run(app)
