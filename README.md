# Retina Damage Detection

<img src="https://www.drishtieye.in/blog/wp-content/uploads/2018/12/diabetic-retinopathy-treatment-mumbai.jpg">


# Problem Description:
People who get Retina Damage They usually don't feel pain
In our project we use a Convolutional Neural Network to diagnose the patient's condition, And knowing how serious their condition is. 
We also explained what are the tips that must be taken into account in order not to contract these diseases.

## Defining the Classes in dataset:
### It contains four classes
- DRUSEN: Eye contains yellow deposits under the retina
- CNV: Presence of intraretinal or subretinal fluid, PEDs and/or RPE rips.
- NORMAL: Eye is in normal condition
- DME: Diabetic macular edema (DME) is a major cause of visual loss in the patients with diabetic retinopathy.


# summary for steps: 
- Our Data is 85K gray scale Image we used 40K image to train our CNN Model.
- We get accuracy 93% without overfitting.
- After That we use Flask framework to build API to deploy our model.
- Using HTML,CSS to build GUI to facilitate using our model.

# Thank You
