import streamlit as st
import pandas as pd

#Load kaggle dataset 
@st.cache_data
def Load_Data():
    df=pd.read_csv("Indian_Food_Nutrition_Processed.csv")

    df=df.rename(columns={
        df.columns[0]: 'Dish',
        df.columns[1]: 'Calories',
        df.columns[2]: 'Carbs',
        df.columns[3]: 'Protein',
        df.columns[4]: 'Fats'
    })

    cols_to_fix = ['Calories', 'Carbs', 'Protein', 'Fats']
    for col in cols_to_fix:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
        
    return df

Load_Data()
