import pandas as pd 
import streamlit as st 
import base64

df_woolies = pd.read_csv('Fresh Fruit _ Woolworths.csv')
df_harris = pd.read_csv('HarrisFarm.csv')
df_iga = pd.read_csv('IGAfruit.csv')

df_woolies['Name'] = df_woolies['Name'].str.replace('each','')

cat =  df_woolies['Category'].unique()
fruit_list_harris = []

for index,row in df_harris.iterrows():
    count = 0
    for elem in cat:
        if row['Name'].find(elem) == -1:
            count = count + 1
        else:
            fruit_list_harris.append(elem)
    if count == len(cat):
        fruit_list_harris.append('None')



    
df_harris['Category'] = fruit_list_harris





st.title('Pricing Monitor Prototype')

title_name = st.sidebar.selectbox('Select your product',(cat))

def woolies(title_name,x):
    df_price_woolies = df_woolies.loc[df_woolies['Category'] == title_name,:]
    return st.write('**{} - **'.format(df_price_woolies['Name'].values[x]) + '{}'.format(df_price_woolies['Price'].values[x]))

def image_woolies(title_name,x):
     df_price_woolies = df_woolies.loc[df_woolies['Category'] == title_name,:]
     return st.markdown('![Alt Text]({})'.format(df_price_woolies['Image'].values[x]))


def harris(title_name,x):
    df_price_harris = df_harris.loc[df_harris['Category'] == title_name,:]
    if len(df_price_harris) == 0:
        st.write('**Sorry that is currently unavailable**')
    else: 
        return st.write('**{} - **'.format(df_price_harris['Name'].values[x]) + '{}'.format(df_price_harris['Price'].values[x]))

def image_harries(title_name,x):
     df_price_harris = df_harris.loc[df_harris['Category'] == title_name,:]
     if len(df_price_harris) == 0:
        st.markdown('![Alt Text](http://www.clker.com/cliparts/b/g/E/c/F/G/tango-face-sad-md.png)')
     else:
         return st.markdown('![Alt Text]({})'.format(df_price_harris['Image'].values[x]))
     

st.header('**Woolworths**')
for x in range(len(df_woolies.loc[df_woolies['Category'] == title_name,:])):
    woolies(title_name,x)
    image_woolies(title_name,x)
st.header('**Harris Farms**')
for x in range(len(df_harris.loc[df_harris['Category'] == title_name,:])):
    harris(title_name,x)
    image_harries(title_name,x)


