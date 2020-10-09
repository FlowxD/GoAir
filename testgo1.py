# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:34:46 2020

@author: Mandar Joshi
"""

import streamlit as st
import pandas as pd
import numpy as np



add_selectbox = st.sidebar.radio(
    "How would you like to be contacted?",
    ("Technical", "General", "Admin")
)

df = pd.read_csv('emp.csv')
emp_list = list(df.columns) 
emp_list.pop(0) 
emp_list.insert(0, '')


tech_list = list(df['tech'])
tech_list.insert(0, '')

if add_selectbox == "Admin":
    new_tech = st.text_input("Enter new name of technical:")
    
    if new_tech == "":
        st.write("Enter valid email id")
    else:
        pass
    if st.button('Add new tech circular'):
        try:
            col = len(df.columns)
            col = col - 1
            df = df.append(pd.Series(0, index=df.columns), ignore_index=True)
            count_row = df.shape[0]
            count_row = count_row - 1
            df.iloc[count_row, df.columns.get_loc('tech')] = new_tech
            df.to_csv('emp.csv',index = False, header=True) 
            st.write(df)
            st.balloons()
        except:
            pass
    else:
        pass
    
    new_emp = st.text_input("Enter new employee name:")
    if st.button('Add new employee'):
        try:
            if new_emp == "":
                st.write("Enter valid email id")
            else:
                st.balloons()
                df.loc[:, new_emp] = '1'
                df.to_csv('emp.csv',index = False, header=True) 
        except:
            pass    
    else:
        pass

    chk_def = st.selectbox("Check defaulters for Tech circular",tech_list, format_func=lambda x: 'Select an option' if x == '' else x)
    if st.button('Check defaulters for'):
        try:
            if chk_def == "":
                st.write("Enter valid Tech circular")
            else:
                rslt_df = df[df['tech'] == chk_def] 
                st.write(rslt_df)
                def_list = rslt_df.columns[(rslt_df == 0).any(axis=0)]
                st.write(def_list)
        except:
            pass    
    else:
        pass
        
        
        
elif add_selectbox == "Technical":
    emp_email = st.selectbox("Enter employee name",emp_list, format_func=lambda x: 'Select an option' if x == '' else x)
    if emp_email:
        pass
    else:
        st.warning('No employee email selected')
    tech_name = st.selectbox("Enter Tech circular name",tech_list, format_func=lambda x: 'Select an option' if x == '' else x)
    if emp_email:
        pass
    else:
        st.warning('No tech  selected')
#    tech_name = int(float(tech_name))
    if st.button('enter'):
        try:
            df.loc[df['tech'] == tech_name, [emp_email]] = 1
            st.write(df)    
            df.to_csv('emp.csv',index = False, header=True) 
        except:
            pass
        
        
        
elif add_selectbox == "General":
    emp_email = st.selectbox("Enter employee name",emp_list, format_func=lambda x: 'Select an option' if x == '' else x)
    if emp_email:
        pass
    else:
        st.warning('No employee email selected')
    gen_name = st.selectbox("Enter General circular name",tech_list, format_func=lambda x: 'Select an option' if x == '' else x)
    if emp_email:
        pass
    else:
        st.warning('No employee email selected')
#    tech_name = int(float(tech_name))
    if st.button('enter'):
        try:
            df.loc[df['tech'] == gen_name, [emp_email]] = 1
            st.write(df)    
            df.to_csv('emp.csv',index = False, header=True) 
        except:
            pass


else:
    pass