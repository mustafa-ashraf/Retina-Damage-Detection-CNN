# Retina Damage Detection

<img src="https://www.drishtieye.in/blog/wp-content/uploads/2018/12/diabetic-retinopathy-treatment-mumbai.jpg">


## Problem Description
Retina damage is a condition that often goes unnoticed by patients, as it does not typically cause pain. In this project, we leverage Convolutional Neural Networks (CNN) to diagnose and assess the severity of a patient's retina damage. Additionally, we provide information on essential precautions to prevent such diseases.

## Dataset and Classes
The dataset used in this project comprises grayscale images, totaling 85,000 samples. These images are divided into four classes:

1. **DRUSEN:** Eye images containing yellow deposits under the retina.
2. **CNV:** Eye images showing the presence of intraretinal or subretinal fluid, PEDs, and/or RPE rips.
3. **NORMAL:** Eye images that are in a healthy, normal condition.
4. **DME:** Images of eyes with Diabetic Macular Edema (DME), a major cause of visual loss in patients with diabetic retinopathy.

## Project Workflow
1. **Data Preprocessing**: Out of the 85,000 grayscale images, 40,000 were used to train the CNN model. The dataset was carefully preprocessed to ensure data quality.

2. **Model Training**: The CNN model achieved an impressive accuracy of 93% on the training data without overfitting, which demonstrates the model's efficacy in diagnosing retina damage.

3. **Deployment with Flask**: The trained model was deployed using the Flask framework to create an API that can be accessed for diagnosis.

4. **Graphical User Interface (GUI)**: An interactive web-based GUI was developed using HTML and CSS to facilitate user-friendly access to the model's capabilities.

## Directory Structure
- `image_predict`: Contains images used for testing the model.
- `static`: Contains static images.
- `templates`: Holds HTML and CSS files for the project's graphical user interface.
- `Mostafa.mp4`: A video demonstrating the project's graphical user interface.
- `README.md`: This documentation file.
- `app.py`: Python script for running the model deployment with Flask.
- `model.h5` and `model.json`: The trained CNN model's weights and architecture.
- `presentation.pdf`: A presentation (PPT) file summarizing the project.
- `retina-damage-detection-cnn.ipynb`: A Jupyter Notebook providing a detailed pipeline of the project, including model training and testing.


# Thank You

