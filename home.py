import streamlit as st
import folium
from streamlit_folium import st_folium
import time

st.markdown("""
<style>
body, [data-testid="stMarkdownContainer"] {
    direction: rtl;
    text-align: right;
    font-family: "Cairo", "Tahoma", sans-serif;
}
</style>
""", unsafe_allow_html=True)
def about () :
    txt =  """
🌟 مرحباً بكم في شركة الفاتح بالله للاستثمار العقاري والاستشارات العقارية في مصر 🌟\n
يسعدنا أن نرحّب بكم أجمل ترحيب في شركتكم التي تسعى دوماً إلى تقديم أرقى الخدمات العقارية على امتداد أرض الكنانة.
نضع بين أيديكم خبرةً واسعة في مجال الاستثمار العقاري، وإدارة المشروعات، وتقديم الاستشارات المتخصّصة، لنكون شركاء نجاحكم في كل خطوةٍ على طريق التميّز والريادة.   
    """.strip()
    for i in txt.split(" ") :
        yield  i + " "
        time.sleep(0.02)


# st.title('من نحن : ')
header = st.container(key='header')
col1, col2, col3 = header.columns([1,3,1])
st.header('موقعنا')
location = st.container(key='map')
with col1 :
    st.image(r"image/image2.png"    )
with col2 :
    st.markdown("#")
    st.write_stream(about())

# with location :
#
#
#     # أنشئ الخريطة داخل الكونتينر
#     m = folium.Map(location=[30.25217, 31.47629], zoom_start=15)
#
#     # أضف نقطة بارزة
#     folium.Marker(
#         location=[30.25217, 31.47629],
#         popup="شارع نعمان جمعه",
#         tooltip="عرض العنوان"
#     ).add_to(m)
#     # اعرض الخريطة داخل الكونتينر
#     st_folium(m, width=1500, height=500)
#
#
