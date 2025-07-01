import streamlit as st
import os
import base64

# Set page config
st.set_page_config(page_title="Unified App", layout="wide")

st.title("🚀 Unified Streamlit App")

# Sidebar Dropdown Menu
option = st.sidebar.selectbox("Choose a Feature", [
    "📸 PhotoGation",
    "🐳 Docker Control",
    "🧾 HTML Interpreter"
])

# ---------------------- PHOTO GATION ------------------------
if option == "📸 PhotoGation":
    st.header("📸 PhotoGation Features")

    st.markdown("### 1. Take a Picture (via Camera)")
    st.info("Camera access only works in browser-based environments.")
    picture = st.camera_input("Take a picture")

    if picture:
        st.success("Photo captured!")
        st.image(picture)

    st.markdown("---")
    st.markdown("### 2. Get Coordinates of Address")
    place = st.text_input("Enter a place or address:")
    if st.button("Get Coordinates"):
        if place:
            url = f"https://nominatim.openstreetmap.org/search?format=json&q={place}"
            try:
                import requests
                res = requests.get(url).json()
                if res:
                    lat, lon = res[0]["lat"], res[0]["lon"]
                    st.success(f"Latitude: {lat}, Longitude: {lon}")
                else:
                    st.error("No results found.")
            except:
                st.error("Error fetching geolocation.")
        else:
            st.warning("Please enter a location.")

    st.markdown("### 3. Share WhatsApp Message")
    phone = st.text_input("Phone number with country code:")
    message = st.text_input("Enter message:")
    if st.button("Send via WhatsApp"):
        if phone and message:
            wa_link = f"https://wa.me/{phone}?text={message}"
            st.markdown(f"[Click to send message 📲]({wa_link})", unsafe_allow_html=True)
        else:
            st.warning("Both fields required.")

# ---------------------- DOCKER MENU ------------------------
elif option == "🐳 Docker Control":
    st.header("🐳 Docker Control Panel")

    docker_choice = st.selectbox("Select Docker Operation", [
        "1. Launch New Container",
        "2. Stop the Container",
        "3. Remove the Container",
        "4. Start the Container",
        "5. List the Images"
    ])

    if docker_choice == "1. Launch New Container":
        name = st.text_input("Enter container name:")
        image = st.text_input("Enter image name:")
        if st.button("Launch"):
            os.system(f"docker run -dit --name {name} {image}")
            st.success(f"Container '{name}' launched.")

    elif docker_choice == "2. Stop the Container":
        name = st.text_input("Enter container name:")
        if st.button("Stop"):
            os.system(f"docker stop {name}")
            st.success(f"Container '{name}' stopped.")

    elif docker_choice == "3. Remove the Container":
        name = st.text_input("Enter container name:")
        if st.button("Remove"):
            os.system(f"docker rm -f {name}")
            st.success(f"Container '{name}' removed.")

    elif docker_choice == "4. Start the Container":
        name = st.text_input("Enter container name:")
        if st.button("Start"):
            os.system(f"docker start {name}")
            st.success(f"Container '{name}' started.")

    elif docker_choice == "5. List the Images":
        if st.button("List"):
            output = os.popen("docker images").read()
            st.text_area("Docker Images", output, height=300)

# ---------------------- HTML INTERPRETER ------------------------
elif option == "🧾 HTML Interpreter":
    st.header("🧾 HTML Live Interpreter")

    html_code = st.text_area("Write your HTML code here:", height=300, placeholder="<h1>Hello World</h1>")
    st.markdown("### Preview")

    if html_code:
        st.components.v1.html(html_code, height=400, scrolling=True)
    else:
        st.info("Live preview will appear here as you type HTML code.")

