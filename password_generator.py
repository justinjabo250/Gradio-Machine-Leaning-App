import streamlit as st
import streamlit_authenticator as stauth
import pathlib
import pickle



users = ['Bright Eshun', 'Queensly_', 'Anne_','Shirley_', 'Eric_', 'Teachops_']
usernames  = ['Bright', 'Queenly', 'Anne', 'Shirley', 'Eric', 'Teachops']
passwords = ['bright123', 'queensly123', 'anne123', 'shirley123', 'eric123', 'teachops123']

hashed_passwords = stauth.Hasher(passwords).generate()


with open('hashed_passwords.pkl', 'wb') as file:
        data = pickle.dump(hashed_passwords, file)

