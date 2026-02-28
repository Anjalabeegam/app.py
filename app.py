import streamlit as st

st.set_page_config(page_title="Temperament Analysis - Dr Anjala", page_icon="🌿")

st.title("🌿 Unani Temperament (Mizaj) Analysis")
st.write("Discover your dominant body temperament in 1 minute.")

st.subheader("Enter Your Details")

name = st.text_input("Full Name")
age = st.number_input("Age", min_value=10, max_value=100)
whatsapp = st.text_input("WhatsApp Number")

st.subheader("Answer the Following Questions")

q1 = st.radio("1. Do you feel hot more often than others?", ["Yes", "No"])
q2 = st.radio("2. Is your skin usually dry?", ["Yes", "No"])
q3 = st.radio("3. Do you sweat easily?", ["Yes", "No"])
q4 = st.radio("4. Do you feel sluggish or heavy often?", ["Yes", "No"])
q5 = st.radio("5. Do you get angry quickly?", ["Yes", "No"])
q6 = st.radio("6. Do you prefer warm climate?", ["Yes", "No"])
q7 = st.radio("7. Do you experience acidity frequently?", ["Yes", "No"])
q8 = st.radio("8. Do you feel cold easily?", ["Yes", "No"])

if st.button("Analyze My Temperament"):

    hot_score = 0
    cold_score = 0
    dry_score = 0
    moist_score = 0

    if q1 == "Yes":
        hot_score += 1
    else:
        cold_score += 1

    if q2 == "Yes":
        dry_score += 1
    else:
        moist_score += 1

    if q3 == "Yes":
        moist_score += 1
    else:
        dry_score += 1

    if q4 == "Yes":
        moist_score += 1
    else:
        dry_score += 1

    if q5 == "Yes":
        hot_score += 1
    else:
        cold_score += 1

    if q6 == "Yes":
        hot_score += 1
    else:
        cold_score += 1

    if q7 == "Yes":
        hot_score += 1
    else:
        cold_score += 1

    if q8 == "Yes":
        cold_score += 1
    else:
        hot_score += 1

    st.subheader("Your Basic Result")

    if hot_score > cold_score and dry_score > moist_score:
        temperament = "🔥 Safravi (Hot & Dry)"
    elif hot_score > cold_score and moist_score >= dry_score:
        temperament = "🌹 Damvi (Hot & Moist)"
    elif cold_score >= hot_score and moist_score > dry_score:
        temperament = "❄ Balghami (Cold & Moist)"
    else:
        temperament = "🌑 Saudavi (Cold & Dry)"

    st.success(f"{name}, your dominant temperament is: {temperament}")

    st.write("🔒 Unlock your detailed personalised Unani diet & lifestyle plan.")

    st.markdown("---")

    st.subheader("💰 Unlock Full Report – ₹49 Only")

    st.write("Pay ₹49 via UPI to the ID below:")

    st.info("UPI ID: yourupiid@okaxis")

    st.write("After payment, send screenshot to WhatsApp: +91XXXXXXXXXX")
    st.write("Mention your name used in the test.")

    st.warning("You will receive your personalised detailed report within 24 hours.")
