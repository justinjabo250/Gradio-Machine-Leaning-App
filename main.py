# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import datetime
from my_function import type_of_day, impute_holiday_data, payday, impute_oil_missing_values, date_extracts
import streamlit_authenticator as stauth

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
users = ['Bright Eshun', 'Queensly_', 'Anne_','Shirley_', 'Eric_', 'Teachops_']
usernames  = ['Bright', 'Queenly', 'Anne', 'Shirley', 'Eric', 'Teachops']

with open('hashed_passwords.pkl', 'rb') as file:
    passwords = pickle.load(file)

credentials = {
    "usernames":{
        "Bright":{
            "name":"Bright Eshun",
            "password": passwords[0]
            },
        "Queensly":{
            "name":"Queenly_",
            "password":passwords[1]
            },
        "Anne":{
            "name":"Anne_",
            "password":passwords[2]
            },
        "Shirley":{
            "name":"Shirley_",
            "password":passwords[3]
            },
        "Eric":{
            "name":"Eric_",
            "password":passwords[4]
            },            
        "Teachops":{
            "name":"Teachops_",
            "password":passwords[5]
            }
                                     
        }
    }
authenticator = stauth.Authenticate(credentials, 'app_home', 'auth', cookie_expiry_days=10)
name, authentication_status, username = authenticator.login('Login', 'sidebar')

if authentication_status == False:
    st.error('Username/password is incorrect')
if authentication_status == None:
    st.warning('Please enter username and password')
if authentication_status:

# create a functions to load pickle file.
    def load_pickle(filename):
        with open(filename, 'rb') as file:
            data = pickle.load(file)
            return data


    #load all pickle files
    ml_compos_1 = load_pickle('ml_components_1.pkl')
    ml_compos_2 = load_pickle('ml_components_2.pkl')



    # components in ml_compos_2  
    categorical_pipeline = ml_compos_2['categorical_pipeline']
    numerical_pipeliine = ml_compos_2['numerical_pipeline']

    num_cols = ml_compos_1['num_cols']
    cat_cols = ml_compos_1['cat_cols'] 


    # et the title for the app
    st.title('SALES FORECASTING APP')


    # create an  expander to contain the app
    my_expander = st.container()


    holiday_level = 'No Holiday'
    hol_city = 'No Holiday'
    st.sidebar.selectbox('Menu', ['About', 'Model'])
    with my_expander:
        # create a three column layout
        col1, col2, col3 = st.columns(3)

        # create a date input to receive date
        date = col1.date_input(
            "Enter the Date",
            datetime.date(2019, 7, 6))
        
        # create a select box to select a family
        item_family = col2.selectbox('What is the category of item?',
                                    ml_compos_1['family'])

        # create a select box for store city
        store_city = col3.selectbox("Which city is the store located?",
                                    ml_compos_1['Store_city'])

        store_state = col1.selectbox("What state is the store located?",
                                    ml_compos_1['Store_state'])
        # hol_city = col2.selectbox("In which city is the holiday?",
        #                           ml_compos_1['Holiday_city'])

        crude_price = col3.number_input('Price of Crude Oil', min_value=0.0, max_value=500.0, value=0.01)

        day_type = col2.selectbox("Type of Day?",
                                ml_compos_1['Type_of_day'], index=2)
        # holiday_level = col3.radio("level of Holiday?",
        #                            ml_compos_1['Holiday_level'])
        colZ, colY = st.columns(2)
        store_type = colZ.radio("Type of store?",
                                ml_compos_1['Store_type'][::-1])
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

        holi = colY.empty()
        with holi.expander(label='Holiday', expanded=True):
            if day_type == 'Additional Holiday' or day_type == 'Holiday' or day_type=='Transferred holiday':
        
                holiday_level = st.radio("level of Holiday?",
                                    ml_compos_1['Holiday_level'])#.tolist().remove('Not Holiday'))
                hol_city = st.selectbox("In which city is the holiday?",
                                    ml_compos_1['Holiday_city'])#.tolist().remove('Not Holiday'))
            else:
                st.markdown('Not Holiday')
                holiday_level = 'Not Holiday'
                hol_city = 'Not Holiday'


        colA, colB, colC = st.columns(3)

        store_number = colA.slider("Select the Store number ",
                                min_value=1,
                                max_value=54,
                                value=1)
        store_cluster = colB.slider("Select the Store Cluster ",
                                    min_value=1,
                                    max_value=17,
                                    value=1)
        item_onpromo = colC.slider("Number of items onpromo ",
                                min_value=0,
                                max_value=800,
                                value=1)
        button = colB.button(label='Predict')
        




    X = np.array([[date, store_number, item_family, item_onpromo, crude_price, holiday_level, hol_city, day_type,
                    store_city, store_state, store_type, store_cluster]])
    df = pd.DataFrame(X, columns=['date', 'Store_number', 'Family', 'Item_onpromo', 'Oil_prices', 'Holiday_level', 'Holiday_city',
                                    'TypeOfDay', 'Store_city', 'Store_state', 'Store_type', 'Cluster'])


    df[['Store_number', 'Item_onpromo', 'Cluster']] = df[['Store_number', 'Item_onpromo', 'Cluster']].apply(lambda x: x.astype(int))
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date')

    date_extracts(df)
    df['Is_payday']= df[['DayOfMonth', 'Is_month_end']].apply(payday, axis=1)





    if button:
        st.write(df)
        
        st.download_button('Download Data', 
                    df.to_csv(index=False), 
                    file_name='data.csv')

        df[cat_cols] = categorical_pipeline.transform(df[cat_cols])
        df[num_cols] = numerical_pipeliine.transform(df[num_cols])
        st.write(df)
        print(df.shape)


authenticator.logout('Logout', 'sidebar')








































































# st.dataframe(df)
# @st.cache_data
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data
#
# data_load_state = st.text('Loading data...')
# data = load_data(10000)
# data_load_state.text("Done! (using st.cache_data)")
#
# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)
#
# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)
#
# # Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
#
# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
