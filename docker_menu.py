import streamlit as st
import os
import requests
import google.generativeai as genai

# -------------------- Gemini API Setup --------------------
genai.configure(api_key="AIzaSyAo0xh_xUBQFk0K9b68brIGULqPw5Kabh8")
model = genai.GenerativeModel("gemini-pro")

def AI(prompt):
    response = model.generate_content(prompt)
    return response.text

# -------------------- Streamlit App Setup --------------------
st.set_page_config(page_title="Unified App", layout="wide")
st.title("🚀 Unified Streamlit App")

# -------------------- Sidebar Menu --------------------
option = st.sidebar.selectbox("Choose a Feature", [
    "📸 PhotoGation",
    "🐳 Docker Control",
    "🧾 HTML Interpreter",
    "🎥 ChatBot Recommender"
])

# -------------------- 📸 PhotoGation --------------------
if option == "📸 PhotoGation":
    st.header("📸 PhotoGation Features")

    st.markdown("### 1. Take a Picture")
    st.info("Note: Camera works only in supported browsers.")
    picture = st.camera_input("Capture an image")

    if picture:
        st.image(picture)
        st.success("📸 Photo captured!")

    st.markdown("---")
    st.markdown("### 2. Get Coordinates from Address")
    place = st.text_input("Enter a place or address:")

    if st.button("Get Coordinates"):
        if place:
            url = f"https://nominatim.openstreetmap.org/search?format=json&q={place}"
            try:
                res = requests.get(url).json()
                if res:
                    lat, lon = res[0]["lat"], res[0]["lon"]
                    st.success(f"📍 Latitude: {lat}, Longitude: {lon}")
                else:
                    st.warning("⚠️ No results found.")
            except:
                st.error("❌ Error fetching location.")
        else:
            st.warning("Please enter a valid address.")

    st.markdown("### 3. Share WhatsApp Message")
    phone = st.text_input("Phone number with country code:")
    message = st.text_input("Enter message:")

    if st.button("Send via WhatsApp"):
        if phone and message:
            wa_link = f"https://wa.me/{phone}?text={message}"
            st.markdown(f"[📤 Click to send message]({wa_link})", unsafe_allow_html=True)
        else:
            st.warning("📌 Both fields are required.")

# -------------------- 🐳 Docker Control --------------------
elif option == "🐳 Docker Control":
    st.header("🐳 Docker Control Panel")

    docker_choice = st.selectbox("Choose Docker Operation", [
        "1. Launch New Container",
        "2. Stop the Container",
        "3. Remove the Container",
        "4. Start the Container",
        "5. List Docker Images"
    ])

    if docker_choice == "1. Launch New Container":
        name = st.text_input("Enter container name:")
        image = st.text_input("Enter Docker image name:")
        if st.button("Launch"):
            os.system(f"docker run -dit --name {name} {image}")
            st.success(f"✅ Container '{name}' launched.")

    elif docker_choice == "2. Stop the Container":
        name = st.text_input("Enter container name:")
        if st.button("Stop"):
            os.system(f"docker stop {name}")
            st.success(f"🛑 Container '{name}' stopped.")

    elif docker_choice == "3. Remove the Container":
        name = st.text_input("Enter container name:")
        if st.button("Remove"):
            os.system(f"docker rm -f {name}")
            st.success(f"🗑️ Container '{name}' removed.")

    elif docker_choice == "4. Start the Container":
        name = st.text_input("Enter container name:")
        if st.button("Start"):
            os.system(f"docker start {name}")
            st.success(f"▶️ Container '{name}' started.")

    elif docker_choice == "5. List Docker Images":
        if st.button("List Images"):
            output = os.popen("docker images").read()
            st.text_area("📋 Docker Images:", output, height=300)

# -------------------- 🧾 HTML Interpreter --------------------
elif option == "🧾 HTML Interpreter":
    st.header("🧾 HTML Live Interpreter")

    html_code = st.text_area("✍️ Write HTML code below", height=300, placeholder="<h1>Hello World!</h1>")
    st.markdown("### Live Preview")

    if html_code:
        st.components.v1.html(html_code, height=400, scrolling=True)
    else:
        st.info("🖋️ Your live output will appear here as you type.")

# -------------------- 🎥 ChatBot Recommender --------------------
elif option == "🎥 ChatBot Recommender":
    st.header("🎥 AI-Powered Recommender Bot")

    category = st.selectbox("Choose type", ["Anime", "Manga", "Movie", "Web Series"])
    title = st.text_input(f"Enter the name of the {category.lower()}:")

    if st.button("Get Summary and Ratings"):
        if title:
            prompt = (
                f"You are an expert in {category}. "
                f"Give a summary, studio (if any), and rate the {category.lower()} titled '{title}' "
                "on story, animation, characters, soundtrack, and say whether you recommend it or not."
            )
            with st.spinner("Thinking..."):
                try:
                    response = AI(prompt)
                    st.markdown(response)
                except Exception as e:
                    st.error(f"❌ Error from Gemini API: {str(e)}")
        else:
            st.warning("Please enter a title.")
