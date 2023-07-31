# GRADIO-MACHINE-LEANING-APP-FOR-PREDICTING-TELCO-CUSTOMER-CHURN


![gradioaaac](https://github.com/justinjabo250/GRADIO-APP-FOR-PREDICTING-TELCO-CUSTOMER-CHURN/assets/115732734/e3ca2ef3-5cdc-4e3c-a05d-2e4e27265552)


## GRADIO-MACHINE-LEANING-APP-FOR-PREDICTING-TELCO-CUSTOMER-CHURN




## 🚀 Friendly Web Interface for Machine Leaning Project with Streamlit App 🚀

For many businesses, especially those in the telecommunications industry, customer churn is a major problem. To keep customers and minimize their churn rate, businesses need to be able to identify which clients are most likely to leave. We'll demonstrate how to build a Gradio app that forecasts client turnover in the telecom sector using machine learning in this article.

![gradioaaa](https://github.com/justinjabo250/GRADIO-APP-FOR-PREDICTING-TELCO-CUSTOMER-CHURN/assets/115732734/814a7563-c479-457b-aaf6-b81437e439c7)


## Summary
| Code      | Name        | Published Article |  Deployed App |
|-----------|-------------|:-------------:|------:|
|GRADIO App | GRADIO MACHINE LEANING APP FOR PREDICTING TELCO CUSTOMER CHURN |  [Read more here](https://www.linkedin.com/pulse/gradio-app-predicting-telco-customer-churn-jabo-justin)[Read more here](https://medium.com/@jabojustin250/gradio-app-for-predicting-telco-customer-churn-d932dda64b69) | [Check on the App](http://127.0.0.1:7865) |



## 1.Install Gradio first, then import the required libraries.

Installing Gradio and importing the required libraries should be done first. A Python package called Gradio makes it simple to create and implement user-friendly machine learning models.

Run the following command in your terminal, Google Colab, Visual Studio Code (I used Visual Studio Code), or Jupyter Notebook to install Gradio:

![gradioabn](https://github.com/justinjabo250/GRADIO-APP-FOR-PREDICTING-TELCO-CUSTOMER-CHURN/assets/115732734/906c1bf1-24d5-4d87-b45a-d494a128c63c)

**!pip install gradio**

## Gradio must import the following libraries after installation:

**Import gradio as gr
Import pandas as Pd
Import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler**


## 2: Load the Model and Data

The machine learning model that will be used to forecast client turnover has to be loaded. Additionally, we must load the data that will be used to create our Gradio app.

Run the following code to load the model:


**model = pickle.load(open("/content/drive/MyDrive/model (1).pkl", "rb"))**
Execute the following code to load the data:

**data = pd.read_csv('/content/drive/MyDrive/df_churn.csv')**

![Customer churn page 1](https://github.com/justinjabo250/GRADIO-APP-FOR-PREDICTING-TELCO-CUSTOMER-CHURN/assets/115732734/31a76cb5-f7fc-48d8-9918-49c49c4ff1ab)


## 3: Specify the Gradio App’s Input and Output Interfaces.

For our Gradio application, we must provide the input and output interfaces. Users can enter client data into the input interfaces, and the output interface displays the forecast outcome.

A function called “create_gradio_inputs” that accepts the data as input and produces a list of Gradio components will be developed to specify the input interfaces. Each column in our data will be looped through by the function, which will then generate a Gradio component based on the column’s data type.

The “create_gradio_inputs” function’s code is provided here.

We will make a Gradio Label component that shows the prediction result in order to specify the output interface:


**output_components = [
    gr. Label(label="Churn Prediction"),
]**



## 4: Define the Prediction Function

A function that receives user inputs, encodes categorical features, scales numerical features, and then uses a trained model to forecast the future must be defined.

The code to define the prediction function is available here.

Using the encoder object that we imported before, we loop over each feature in this function after first creating a list of the categorized features. The numerical features are then compiled into a list, scaled using the scaler object, and added to the encoded data dataframe. Finally, we use the model object to make a forecast and then return the prediction as a string. We return “Not Likely to Churn” if the prediction is 0, and “Likely to Churn” if it is 1.

![gradioaaaass](https://github.com/justinjabo250/GRADIO-APP-FOR-PREDICTING-TELCO-CUSTOMER-CHURN/assets/115732734/770acd02-27e4-43c4-b493-5779a65de235)


## 5: Launch the Gradio App
We can now run the Gradio app using the code below after defining the input and output interfaces as well as the prediction function:

## Launch the Gradio app

**iface = gr.Interface(predict_churn, inputs=input_components, outputs=output_components,
                     description="Enter the customer's demographic and service usage information to predict whether they are likely to churn or not.")
iface.launch(inbrowser=True, show_error=True, share=True)**


This will open the Gradio app in your web browser in a new window or tab. The app will show the input elements (dropdowns, sliders, etc.) that we previously created, and the user can enter values for each feature to get an estimation of their likelihood of churning or not. Below the input components, a label representing the result will be shown.

Using the code provided above, you can create a Gradio app for telco customer churn prediction by following these instructions. Using this app’s demographic and service usage data, you can quickly and simply determine whether a customer is likely to leave your business.

Note: You can find more details about this project on my GitHub repository or visit my medium account if you’re interested in doing so.


## Author
Justin Jabo
- [Linkedin Article](https://www.linkedin.com/pulse/gradio-app-predicting-telco-customer-churn-jabo-justin) 
- [Medium Article](https://medium.com/@jabojustin250/gradio-app-for-predicting-telco-customer-churn-d932dda64b69)
- [Github Repository](https://github.com/justinjabo250?tab=repositories)
...
