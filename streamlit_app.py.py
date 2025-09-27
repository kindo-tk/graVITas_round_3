import streamlit as st

#institution logo
st.image("logo.jpeg", width=100)

st.title("Mission 3:")
st.title("Cipher Challenge")

teams = {
    "alpha": {  
        "name": "Team Alpha",#bat
        "cipher_name": "Vigenère Cipher ",
        "Key": "ebbcg",
        "encrypted_sentence": "cvp ckv xoq xequ ql xif gkxmj ayt pfmcxso",               
        "decoded_message": "you are now part of the elite spy network",
        "jumbled sentence": "yuo aer wno rapt of the eetli ysp oekwtrn"
    },
    "bravo": {
        "name": "Team Bravo",  #pattern
        "cipher_name": "Vigenère Cipher ",
        "Key": "bjdhd",
        "encrypted_sentence": "uqh ohjmqk rflg hhwuuzh vhry uflhzw ujqnh udwhvt", 
        "decoded_message": "the hidden code reveals your secret agent status",
        "jumbled sentence":"the heidnd oecd aevlrse uyor recest tange tutass"
    },
    "charlie": {
        "name": "Team Charlie", #spider
        "cipher_name": "Vigenère Cipher ",
        "Key": "esqxz",
        "encrypted_sentence": "vmlbsm yuftwv orn yyeogll jed zwyi nj ktpzagx",
        "decoded_message": "virtue guides you through the veil of shadows",
        "jumbled sentence": "ruveti geiusd yuo ugorhht the veil of sdsawoh"
    },
    "delta": {
        "name": "Team Delta", #cat
        "cipher_name": "Vigenère Cipher",
        "Key": "rxupt",
        "encrypted_sentence": "tblxiubb hbyq nd neiizv lvig kkbwdo klygovmux hcoy",
        "decoded_message": "decipher this to unlock your covert operative role",
        "jumbled sentence":"ceripdeh siht to unlokc uyor rtecov toervepai olre"
    },
    "echo": {
        "name": "Team Echo", #yin yang
        "cipher_name": "Vigenère Cipher",
        "Key": "aabac",
        "encrypted_sentence": "uypr mlljsu arfn auo b tupo jn tou hcgnaz",
        "decoded_message": "your skills earn you a spot in our agency",
        "jumbled sentence":"uyor klliss aren yuo a tspo in rou gcenay"
    },
    "shadow": {
        "name": "Team Shadow", #cat
        "cipher_name": "Vigenère Cipher",
        "Key": "rxupt",
        "encrypted_sentence": "tblxiubb hbyq nd neiizv lvig kkbwdo klygovmux hcoy",
        "decoded_message": "decipher this to unlock your covert operative role",
        "jumbled sentence":"ceripdeh siht to unlokc uyor rtecov toervepai olre"
    }
}

# Replace with the actual 5-letter agent codes for each team
team_codes = {
    "ebbcg": "alpha",
    "bjdhd": "bravo",
    "esqxz": "charlie",
    "rxupt": "delta",
    "aabac": "echo",
    "rxupt": "shadow"
}

# ===================== APP FLOW =====================
st.subheader("Passkey (5 Letters)")
team_code = st.text_input("", max_chars=5, type="password").lower()

if team_code:
    try:
        if len(team_code) != 5 or not team_code.isalpha():
            st.error("Passkey must be exactly 5 letters!")
        elif team_code not in team_codes:
            st.error("Invalid Passkey!")
        else:
            team_key = team_codes[team_code]
            team_info = teams[team_key]
            st.success(f"Welcome, {team_info['name']} Operatives!")

            # --- Step 2: Display Encrypted Sentence & Cipher Type ---
            st.subheader("Intercepted Encrypted Transmission")
            st.subheader(f"**Cipher Used**: `{team_info['cipher_name']}`")
            st.subheader(f"**Key**: `{team_info['Key']}`")
            # st.subheader(f"**Encrypted Message**: `{team_info['encrypted_sentence']}`")
            st.markdown(f"**Encrypted Message**: Find it in the document shared!")
            # --- Step 3: Decoded Sentence Submission ---
            st.subheader("Submit Decoded Intelligence Report")
            st.info("Decrypt the message to get a jumbled version, then un jumble the words to reveal the original intelligence.")
            user_decoded = st.text_input("Decoded Message").lower()

            if st.button("Verify Intelligence"):
                normalized_user = user_decoded.replace(" ", "").lower()
                normalized_original = team_info["decoded_message"].replace(" ", "").lower()
                if normalized_user == normalized_original:
                    st.balloons()
                    st.success(f"Mission Success, {team_info['name']} Operatives! You are now onboarded to the Agency!")
                else:
                    st.info("Intelligence mismatch. Reattempt decryption and un jumbling.")

    except Exception as e:
        st.error(f"⚠️ Unexpected mission error: {e}")

# --- Footer ---
footer = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f1f1f1;
    color: #333;
    text-align: center;
    padding: 8px;
    font-size: 14px;
}
</style>
<div class="footer">
    Limited Access
</div>
"""
st.markdown(footer, unsafe_allow_html=True)