import numpy as np
import cv2
from keras.models import model_from_json
from flask import Flask, request, render_template
import pandas as pd
##########################################################
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")
##########################################################
##########################################################
app = Flask(__name__,static_folder='static')
##########################################################
@app.route('/')
def home():
    return render_template('index.html')
##########################################################
@app.route('/predict',methods=['POST'])
def predictt():
    if request.method == "POST":
            f = request.form["file"]
            input_img = cv2.imread("image_predict//"+str(f))
            #input_img = cv2.imread("image_predict/DME-1072015-1.jpeg")
            input_img=cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
            input_img_resize=cv2.resize(input_img,(128,128))
            input_img_resize= np.expand_dims(input_img_resize, axis=2)
            input_img_resize= np.expand_dims(input_img_resize, axis=0)
            output = loaded_model.predict(input_img_resize)
            output = output.astype(int)

            if output[0][0] == 1:
                res_val = "YOU HAVE DRUSEN"
            if output[0][1] == 1:
                res_val = "YOU HAVE CNV"
            if output[0][2] ==1:
                res_val = "YOU ARE NORMAL"
            if output[0][3] == 1:
                res_val = "YOU HAVE DME"
    
    return render_template('index.html', prediction_text='{}'.format(res_val))
############################################################


if __name__ == '__main__':  
    app.run(debug=False)  