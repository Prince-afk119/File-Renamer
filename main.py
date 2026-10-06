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

if "rename_history" not in st.session_state:
    st.session_state.rename_history = []

def renamer():
    filenames = os.listdir(folder_path)
    for i in filenames:
        if keyword.lower() in i.lower() and Show_Name.lower() not in i.lower():
            if i[-7].isdigit() and i[-6].isdigit():
                episode = int(str(i[-7] + i[-6])) + 1
            elif i[-6].isdigit() and not i[-7].isdigit():
                episode = int(i[-6]) + 1
            else:
                episode = 1
            old_path = os.path.join(folder_path, i)
            new_path = os.path.join(folder_path, Show_Name + " Episode " + str(episode) + " Season " + str(Season) + ".txt")
            if not os.path.exists(new_path):
                st.session_state.rename_history.append((old_path, new_path))
                st.write(f"{i} -> {Show_Name} {Season} episode {episode}")
                os.rename(old_path, new_path)
            else:
                st.write(f"Skipping {i}, destination already exists")
        else:
            st.write("The Keyword You Typed Was Not Found, But found " + i)

def undo():
    for old_path, new_path in st.session_state.rename_history:
        os.rename(new_path, old_path)
    st.session_state.rename_history = []

if folder_path and st.button("Rename"):
    renamer()

if st.button("Undo"):
    undo()
    
    
    
    
    

