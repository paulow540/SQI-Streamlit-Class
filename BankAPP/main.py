import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import json
import os

st.set_page_config("Bank App", "🏦")

category_file = "categories.json"
if category_file not in st.session_state:
    st.session_state.categories = {
        "Uncategorized": []
    }

if os.path.exists(category_file):
    with open(category_file, "r") as f:
        st.session_state.categories = json.load(f)


def save_categories():
    with open("categories.json", "w") as f:
        json.dump(st.session_state.categories, f)


def categorize_transactions(df):
    df["Category"] = "Uncategorized"

    for category, keywords in st.session_state.categories.items():
        if category == "Uncategorized" or not keywords:
            continue

        lowered_keywords = [keyword.lower() for keyword in keywords]
        for idx, row in df.iterrows():

            details = row["Details"].lower().strip()
            if details in lowered_keywords:
                df.at[idx, "Category"] = category 
    return df 




def load_transactions(file):
    try:
        df = pd.read_csv(file)
        df["Date"] = pd.to_datetime(df["Date"])
        return categorize_transactions(df)

    except  Exception as e:
        st.error(f"Error processing file: {str(e)}")
        return None


def add_keyword_to_category(category, keyword):
    keyword = keyword.strip()
    if keyword and keyword not in st.session_state.categories[category]:
        st.session_state.categories[category].append(keyword)
        save_categories()
        return True
    
    return False



def main():
    st.write("A simple Bank Transaction App")

    upload_file = st.file_uploader("Upload your file", type=["csv"])

    if upload_file is not None:
        df = load_transactions(upload_file)

        if df is not None:
            debits_df = df[df["Debit/Credit"]== "Debit"].copy()
            credits_df = df[df["Debit/Credit"]== "Credit"].copy()

            st.session_state.debits_df = debits_df.copy()

            tab1, tab2 = st.tabs(["Expenses (Debits)", "Payments (Credits)"])

            with tab1:
                new_category = st.text_input("New Category Name")
                add_buttons = st.button("Add Category")

                if add_buttons and new_category:
                    if new_category not in st.session_state.categories:
                       st.session_state.categories[new_category] = []
                       save_categories()
                    #    st.success(f"Added a new category: {new_category}")
                       st.rerun()

                st.subheader("Your Expenses")
                edited_df = st.data_editor(
                    st.session_state.debits_df[["Date","Details","Amount","Category"]],
                    column_config={
                        "Date":st.column_config.DateColumn("Date", format="DD/MM/YYYY"),
                        "Amount":st.column_config.NumberColumn("Amount", format="%.2f"),
                        "Category":st.column_config.SelectboxColumn(
                            "Category",
                            options=list(st.session_state.categories.keys())
                        )

                    },
                    hide_index=True,
                    use_container_width=True,
                    key="category_editor"
                )

                save_buttons = st.button("Apply Changes", type="primary")
                if save_buttons:
                    for idx, row in edited_df.iterrows():
                        if row["Category"] == st.session_state.debits_df.at[idx, "Category"]:
                            continue

                        details = row["Details"]
                        st.session_state.debits_df.at[idx, "Category"] = new_category
                        add_keyword_to_category(new_category, details)

                st.subheader("Expense Summary")
                category_total = st.session_state.debits_df.groupby("Category")["Amount"].sum().reset_index()
                category_total = category_total.sort_values("Amount",ascending=False)

                st.dataframe(
                    category_total,
                    column_config={
                        "Amount":st.column_config.NumberColumn("Amount", format="%.2f")
                         },
                        use_container_width=True,
                        hide_index=True                   
                )

                fig = px.pie(
                    category_total,
                    values="Amount",
                    names="Category",
                    title="Expenses by Category"
                )
                st.plotly_chart(fig, use_container_width=True)



            with tab2:
                st.write(credits_df["Amount"].sum())
        

    
main()

