import streamlit as st
from add_update_ui import add_update_tab
from analytics_by_category import analytics_category_tab
from analytics_by_months import analytics_months_tab


st.title("Expense Tracking System")

tab1, tab2, tab3 = st.tabs(["Add/Update", "Analytics_by_Category", "Analytics_by_Month"])

with tab1:
    add_update_tab()

with tab2:
    analytics_category_tab()

with tab3:
    analytics_months_tab()
