import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from tabulate import tabulate

st.set_page_config(layout="wide")
st.title(':green[Petal &] :blue[Parchment] :newspaper:')
with st.sidebar:
    st.header(":grey[About the Project]")
    st.markdown('''
               :green[Petal &] :blue[Parchment] :newspaper: 
                Analysis project focuses on extracting valuable insights,
                 from the company's database to evaluate and enhance its overall performance.
                 With 50 sales representatives distributed across four regions in America,
                 Petal & Parchment sells three types of paper—Standard, Gloss, and Poster—to attract
                 large corporate clients through advertising on platforms like Google, Facebook,
                 and Twitter. The database comprises five key tables: web_events, accounts, orders,
                 sales_reps, and region
                ''')
    st.subheader(':blue[Developed by Faisal Shamim]', divider='grey')


selected = option_menu(
        menu_title=None,
        options=["ERD","Datasets","Case-problems"],
        icons=["file-person-fill","database"],
        orientation="horizontal"
) 
if selected == "ERD":
    st.title(f"You have selected {selected}")
    st.image('erd.png', caption='ERD Of our database')



if selected == "Datasets":
    st.title(f"You have selected {selected}")
    tab1, tab2, tab3,tab4,tab5 = st.tabs(["accounts", "orders", "region","sales_rep","web_events"])
    with tab1:
        def upload1():
            df=pd.read_csv("a.csv")
            return df
        df=upload1()
    
        
        gd=GridOptionsBuilder.from_dataframe(df)
        gd.configure_pagination(enabled=True,paginationPageSize=20)
        gd.configure_default_column(editable=True,groupable=True)
        gridoptions=gd.build()
        AgGrid(df,gridoptions,height=600,width=750)

    #tab2
    with tab2:
        def upload2():
            df=pd.read_csv("o.csv")
            return df
        df=upload2()
    
        
        gd=GridOptionsBuilder.from_dataframe(df)
        gd.configure_pagination(enabled=True,paginationPageSize=20)
        gd.configure_default_column(editable=True,groupable=True)
        gridoptions=gd.build()
        AgGrid(df,gridoptions,height=600,width=750)

    #tab3
    with tab3:
        def upload3():
            df=pd.read_csv("r.csv")
            return df
        df=upload3()
    
        
        gd=GridOptionsBuilder.from_dataframe(df)
        gd.configure_pagination(enabled=True,paginationPageSize=20)
        gd.configure_default_column(editable=True,groupable=True)
        gridoptions=gd.build()
        AgGrid(df,gridoptions,height=600,width=750)
    #tab4
    with tab4:
        def upload4():
            df=pd.read_csv("s.csv")
            return df
        df=upload4()
    
       
        gd=GridOptionsBuilder.from_dataframe(df)
        gd.configure_pagination(enabled=True,paginationPageSize=20)
        gd.configure_default_column(editable=True,groupable=True)
        gridoptions=gd.build()
        AgGrid(df,gridoptions,height=600,width=750)

    #tab5
    with tab5:
        def upload5():
            df=pd.read_csv("web.csv")
            return df
        df=upload5()
    
       
        gd=GridOptionsBuilder.from_dataframe(df)
        gd.configure_pagination(enabled=True,paginationPageSize=20)
        gd.configure_default_column(editable=True,groupable=True)
        gridoptions=gd.build()
        AgGrid(df,gridoptions,height=600,width=750)

if selected == 'Case-problems':
    st.markdown(f"Currently viewing {selected}")
    tab1,tab2,tab3,tab4=st.tabs(['First Case','Second Case','Third Case','Fourth Case'])
    with tab1:
        st.text('''Which accounts used facebook as a channel to contact customers more than 6 times?
                ''')
        expander = st.caption("See SQL Script")
        st.code("SELECT a.id, a.name, w.channel, COUNT(*) use_of_channel FROM accounts a JOIN web_events w ON a.id = w.account_id GROUP BY a.id, a.name, w.channel HAVING COUNT(*) > 6 AND w.channel = 'facebook' ORDER BY use_of_channel;")
        def upload_new():
            f=pd.read_csv("first.csv")
            return f
        f=upload_new()
        AgGrid(f)

    with tab2:
        st.text('''	Using the accounts table, find all the companies whose names do not 
                start with 'C' and end with 's'.
                ''')
        expander = st.caption("See SQL Script")
        st.code("SELECT name FROM accounts WHERE name NOT LIKE 'C%' AND name LIKE '%s';")
        def upload_new():
            f=pd.read_csv("second.csv")
            return f
        f=upload_new()
        AgGrid(f)

    with tab3:
        st.text('''	Provide a table that provides the region for each sales_rep along with their associated accounts. Your final table should include three columns: the region name, the sales 
        rep name, and the account name. Sort the accounts alphabetically (A-Z) according to account name..
                ''')
        expander = st.caption("See SQL Script")
        st.code("SELECT r.name region, s.name rep, a.name account FROM sales_reps s JOIN region r\n ON s.region_id = r.id JOIN accounts a ON a.sales_rep_id = s.id ORDER BY a.name;")
        def upload_new():
            f=pd.read_csv("third.csv")
            return f
        f=upload_new()
        gd=GridOptionsBuilder.from_dataframe(f)
        gd.configure_pagination(enabled=True,paginationPageSize=20)
        gd.configure_default_column(editable=True,groupable=True)
        gridoptions=gd.build()
        AgGrid(f,gridoptions,height=600,width=750)
        
    with tab4:
        st.text('''	Which account (by name) placed the earliest order? 
                ''')
        expander = st.caption("See SQL Script")
        st.code("SELECT a.name, o.occurred_at FROM accounts a JOIN orders o ON a.id = o.account_id ORDER BY occurred_at LIMIT 1;")
        def upload_new():
            f=pd.read_csv("fourth.csv")
            return f
        f=upload_new()
        gd=GridOptionsBuilder.from_dataframe(f)
        gd.configure_pagination(enabled=True,paginationPageSize=20)
        gd.configure_default_column(editable=True,groupable=True)
        gridoptions=gd.build()
        AgGrid(f,gridoptions,height=600,width=750)
        
