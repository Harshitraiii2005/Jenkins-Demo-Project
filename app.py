import streamlit as st
import pandas as pd
import pickle


with open("model.pkl", "rb") as f:
    model = pickle.load(f) 

st.set_page_config(page_title="Discount Price Predictor", layout="centered")

st.title("💻 Laptop Discounted Price Predictor")
st.write("Enter laptop specifications to predict the **Discounted Price**")


st.subheader("Numerical Features")

actual_price = st.number_input("Actual Price", min_value=0.0, step=1000.0)
rating = st.slider("Rating", 0.0, 5.0, 4.0, 0.1)
reviews = st.number_input("Number of Reviews", min_value=0, step=10)
ssd_gb = st.selectbox("SSD (GB)", [128, 256, 512, 1024, 2048])
ram_gb = st.selectbox("RAM (GB)", [4, 8, 16, 32, 64])
screen_size = st.slider("Screen Size (inches)", 11.0, 18.0, 15.6, 0.1)

st.subheader("Categorical Features")

brand = st.selectbox(
    "Brand",
    ["Dell", "HP", "Lenovo", "Apple", "Asus", "Acer", "MSI"]
)

core = st.selectbox(
    "Processor Core",
    ["i3", "i5", "i7", "i9", "Ryzen 5", "Ryzen 7", "M1", "M2"]
)


if st.button("Predict Discounted Price 🚀"):
    input_df = pd.DataFrame([{
        "Actual Price": actual_price,
        "Rating": rating,
        "Reviews": reviews,
        "SSD_GB": ssd_gb,
        "RAM_GB": ram_gb,
        "Screen_Size": screen_size,
        "Brand": brand,
        "Core": core
    }])

    try:
        prediction = model.predict(input_df)[0]

        st.success(f"💰 Predicted Discounted Price: ₹ {prediction:,.2f}")

    except Exception as e:
        st.error("❌ Prediction failed")
        st.exception(e)
