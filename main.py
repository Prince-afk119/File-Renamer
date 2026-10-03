import os
import streamlit as st


folder_path = st.text_input("Enter folder path")
# folder_path = "C:/Deposite/New/"
keyword = st.text_input("Enter keyword to search for")
# keyword = "getvid"

Show_Name = st.text_input("Enter The Show/Anime Name")
# Show_Name = "ReZero"
Season = st.number_input("Enter Season Number", step= 1)
# Season = 4

filenames = os.listdir(folder_path)


for i in filenames:
    if keyword.lower()  in i.lower():
        if i[-6].isdigit():
            episode = int(i[-6]) + 1
        else:
            episode = 17
        os.rename(os.path.join(folder_path,i),os.path.join(folder_path,Show_Name + "Episode " + str(episode) + " " + "Season " + str(Season) + ".mp4"))
    else:
        st.write("The Keyword You Typed Was Not Found, But found " + i)
