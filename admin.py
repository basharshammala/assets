import streamlit as st
import json
import os

file_path = "data.json"
counter = 0

if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump({}, f, ensure_ascii=False, indent=4)

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

if data.keys():
    counter = int(list(data.keys())[-1])
    counter += 1
else:
    counter = 0

with st.form('my form'):
    type_ = st.selectbox("نوع العقار", ["شقه", "ارض", "استثمار"])
    position = st.selectbox("المكان:", ["التجمع", "بدر", "العبور", "نصر", "سته اكتوبر", "الشروق"])
    room_numbers = st.number_input("عدد الغرف", min_value=1, value=3)
    price = st.number_input("السعر", value=1000000, step=200000)
    submitted = st.form_submit_button("إرسال")
    if submitted:
        data[counter] = {
            'type': type_,
            'position': position,
            'room_number': room_numbers,
            "price": price
        }
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        st.success("تم إضافة العقار بنجاح")

st.json(data)
