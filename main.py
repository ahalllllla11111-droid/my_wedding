import streamlit as st
st.markdown("""
    <style>
    /* إخفاء الإرشادات الإنجليزية فقط دون التأثير على المربعات */
    div[data-testid="InputInstructions"] {
        visibility: hidden !important;
        height: 0px !important;
        overflow: hidden !important;
    }
    </style>
""", unsafe_allow_html=True)
import pandas as pd
import os
import base64

# اسم الملف الذي ستُحفظ فيه أسماء الحاضرين تلقائياً
DATA_FILE = "wedding_responses.csv"

# 1. إعدادات الصفحة العامة
st.set_page_config(page_title="دعوة حفل زفاف", page_icon="💍", layout="centered")

# دالة لتحويل الصورة المحلية إلى كود يقرأه المتصفح كخلفية مباشرة
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

# قراءة الصورة من مجلدك (تأكد أن اسمها islamic_wedding.jpg أو غير الامتداد هنا)
img_base64 = get_base64_image("islamic_wedding.jpg")

# 2. تطبيق التنسيقات البصرية والـ CSS لجعل الصورة خلفية كاملة والكلام فوقها بشكل متناسق
st.markdown(f"""
    <style>
    /* جعل الصورة خلفية كاملة وثابتة للموقع */
    .stApp {{
        background-image: url("data:image/jpg;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    
    /* جعل كل محتويات الصفحة تظهر داخل كارت واحد متصل وأنيق */
    div[data-testid="stVerticalBlock"] {{
        background-color: rgba(255, 255, 255, 0.94);
        padding: 35px;
        border-radius: 20px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.2);
        border: 2px solid #dfc48c;
        direction: rtl;
        text-align: center;
    }}
    
    /* إلغاء الفواصل البيضاء المقطعة بين العناصر */
    div[data-testid="stVerticalBlock"] > div {{
        background: transparent !important;
        box-shadow: none !important;
        padding: 0px !important;
        margin: 0px !important;
        border: none !important;
    }}
    
    /* تنسيق العناوين والخطوط */
    h1, h2, h3, p {{ 
        text-align: center; 
        font-family: 'Cairo', sans-serif; 
        color: #444444;
    }}
    
    /* تحسين شكل زر التأكيد */
    .stButton>button {{ 
        width: 100%; 
        background-color: #b38f4d !important; 
        color: white !important; 
        font-size: 20px !important; 
        font-weight: bold !important;
        border-radius: 8px !important;
        padding: 10px !important;
        border: none !important;
    }}
    
    /* تنسيق صندوق حقوق المبرمج أحمد علاء */
    .dev-footer {{
        text-align: center; 
        padding: 12px; 
        color: #666666; 
        font-size: 14px; 
        background-color: #f1ebd9; 
        border-radius: 10px;
        border-right: 5px solid #b38f4d;
        margin-top: 20px;
    }}
    </style>
    """, unsafe_allow_html=True)

# 3. واجهة الدعوة العلوية (داخل الكارت الموحد)
st.title("💍 دَعْوَةُ حَفْلِ زِفَافٍ 💍")
st.markdown("<h1 style='text-align: center; color: #8A6D3B; font-family: Cairo, sans-serif; font-weight: bold;'>💍 دَعْوَةُ حَفْلِ زِفَافٍ 💍</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #5c4a28; font-family: Cairo, sans-serif; font-style: italic;'>\"وَمِنْ آيَاتِهِ أَنْ خَلَقَ لَكُم مِّنْ أَنفُسِكُمْ أَزْوَاجًا لِّتَسْكُنُوا إِلَيْهَا وَجَعَلَ بَيْنَكُم مَّوَدَّةً وَرَحْمَةً\"</h3>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #8A6D3B; font-family: Cairo, sans-serif; font-weight: bold;'>💖 احمد & فاطمة 💖</h2>", unsafe_allow_html=True)

st.markdown("<hr style='border-top: 1px solid #dfc48c;'>", unsafe_allow_html=True)
st.subheader("بإذن الله تعالى، يسعدنا ويشرفنا دعوتكم لمشاركتنا فرحة العمر")
st.write("وجودكم يكتمل به الفرح والسرور في ليلة العمر ✨")
st.write("**📍 المكان:** المجمع الاسلامي بجانب بيت بابا حبيبي❤️ | **📅 التاريخ:** يوم الخميس القادم")
st.markdown("<hr style='border-top: 1px solid #dfc48c;'>", unsafe_allow_html=True)

# 4. نموذج تسجيل وبيانات الحضور
st.subheader("تأكيد حضورك الكريم:")

name_input = st.text_input("الرجاء إدخال اسمك الكريم هنا:", placeholder="اكتب اسمك الثلاثي...")
phone_input = st.text_input("رقم الجوال (اختياري):", placeholder="05xxxxxxxx")

if st.button("تأكيد قبول الدعوة ✅"):
    if name_input.strip() == "":
        st.error("رجاءً، اكتب اسمك أولاً لتأكيد الحضور.")
    else:
        new_guest = pd.DataFrame([{"الاسم": name_input, "رقم الجوال": phone_input}])
        if os.path.exists(DATA_FILE):
            df = pd.read_csv(DATA_FILE)
            df = pd.concat([df, new_guest], ignore_index=True)
        else:
            df = new_guest
        df.to_csv(DATA_FILE, index=False)
        st.success(f"شكراً لك يا {name_input}! تم تسجيل حضورك بنجاح 🎉")

# 5. علامة بصمة المبرمج أحمد علاء المعتمدة
st.markdown(f"""
    <div class="dev-footer">
        تم تطوير وتصميم هذا النظام البرمجي بحب 💻 ⚡ <br>
        بواسطة المبرمج: <span style='font-weight: bold; color: #b38f4d; font-size: 16px;'>أحمد علاء</span> © 2026
    </div>
    """, unsafe_allow_html=True)
