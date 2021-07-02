from tensorflow.keras.preprocessing import image
import numpy as np
import json
import requests
from flask import jsonify

def predict(path):
    SIZE = 256
    img = image.load_img(path, target_size=(SIZE,SIZE,3))
    img = image.img_to_array(img)
    img = img/255.

    imgs = []   
    imgs.append(img)
        
    imgs = np.array(imgs)

    #Create JSON Object
    data = json.dumps({'signature_name': 'serving_default','instances': imgs.tolist()})

    headers = {"content-type": "application/json"}
    json_response = requests.post('http://localhost:8501/v1/models/xray:predict', data=data, headers=headers)
    predictions = json.loads(json_response.text)['predictions']

    class_names = ['Atelectasis', 'Cardiomegaly', 'Consolidation', 'Edema', 'Effusion',
    'Emphysema', 'Fibrosis', 'Hernia', 'Infiltration', 'Mass', 'No Finding',
    'Nodule', 'Pleural_Thickening', 'Pneumonia', 'Pneumothorax']

    return jsonify({'class_names':class_names,'predictions':predictions})
