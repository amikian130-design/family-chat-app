import streamlit as st

# تنظیمات صفحه
st.set_page_config(page_title="Family Chat", page_icon="❤️")

# ظاهر برنامه
st.markdown("""
    <style>
    .stApp { background-color: #e5ddd5; }
    </style>
    """, unsafe_allow_html=True)

st.title("👨‍👩‍👧‍👦 چت خونواده ما")

# ایجاد حافظه برای پیام‌ها (اینجا پیام‌ها ذخیره می‌شن)
if "messages" not in st.session_state:
    st.session_state.messages = []

# نمایش پیام‌های ذخیره شده
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
        if "image" in message:
            st.image(message["image"])

# بخش ورودی (این بار خیلی ساده و مطمئن!)
# ۱. برای متن
prompt = st.chat_input("پیامت رو اینجا بنویس...")

# ۲. برای عکس
uploaded_file = st.file_uploader("ارسال عکس 📸", type=['png', 'jpg', 'jpeg'])

# منطق ارسال پیام
if prompt:
    # اضافه کردن پیام کاربر به لیست
    new_msg = {"role": "user", "content": prompt}
    
    # اگر همزمان عکس هم انتخاب شده باشه
    if uploaded_file:
        new_msg["image"] = uploaded_file
        
    st.session_state.messages.append(new_msg)
    st.rerun()

elif uploaded_file and st.button("ارسال عکس 🚀"):
    # اگر کاربر فقط عکس رو انتخاب کرده باشه و دکمه رو زده باشه
    new_msg = {"role": "user", "content": "📷 یک عکس فرستاده شد", "image": uploaded_file}
    st.session_state.messages.append(new_msg)
    st.rerun()
