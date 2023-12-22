import streamlit as st
import requests

def main():
    url = "https://gis.fdkc.gov.tw/rescue/getnowcase/json?getalls=1"
    headers = {
        'Referer': 'https://gis.fdkc.gov.tw/rescue/'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        st.error('請求資料失敗')
        return
    json_data = response.json()

    st.title('案件資訊')
    st.write(json_data)

if __name__ == "__main__":
    main()