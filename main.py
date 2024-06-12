import streamlit as st
from generate_data import generate_csv


@st.cache_data
def convert_df(dframe):
    # TO SAVE THE FILE LOCALLY:
    csv_path = f'../pythonProject2/data/{file_name}.csv'
    dframe.to_csv(csv_path, index=False)

    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return dframe.to_csv().encode("utf-8")


if __name__ == '__main__':
    st.title("Generate Data")

    with st.form("my_form"):
        file_name = st.text_input("Enter file name")
        num_rows = st.number_input("Select number of rows", 1000, 10000, step=500)
        submitted = st.form_submit_button("Generate")

    if submitted:
        with st.spinner('Generating...'):
            df = generate_csv(num_rows, file_name)
            csv_data = convert_df(df)
            st.success(f"{file_name}.csv generated")
            st.download_button(
                label="Download",
                data=csv_data,
                file_name=f"{file_name}.csv",
                mime="text/csv",
            )
