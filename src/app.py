import streamlit as st
import pandas as pd
from data_prep_kit import DataPrepKit

def main():
    st.title("Data Preparation with DataPrepKit")

    # تحميل الملف
    uploaded_file = st.file_uploader("تحميل ملف البيانات", type=["csv", "xlsx", "json", "txt"])
    
    if uploaded_file is not None:
        # Check file extension and read the data accordingly
        file_extension = uploaded_file.name.split('.')[-1].lower()
        
        try:
            if file_extension == "csv":
                data = pd.read_csv(uploaded_file)
            elif file_extension == "xlsx":
                data = pd.read_excel(uploaded_file)
            elif file_extension == "json":
                data = pd.read_json(uploaded_file)
            elif file_extension == "txt":
                delimiter = st.text_input("أدخل الفاصل في ملف النص", value="\t")  # Default tab delimiter
                data = pd.read_csv(uploaded_file, delimiter=delimiter)
            else:
                st.error("نوع الملف غير مدعوم. يرجى تحميل ملف بصيغة CSV أو Excel أو JSON أو TXT.")
                return
        except Exception as e:
            st.error(f"حدث خطأ أثناء قراءة الملف: {str(e)}")
            return
        
        # Create DataPrepKit instance with the loaded data
        prep_kit = DataPrepKit(data)
        
        # عرض البيانات
        st.write("عرض البيانات:", data.head())

        # عرض ملخص البيانات
        summary = prep_kit.data_summary()
        st.write("ملخص البيانات:", summary)

        # التعامل مع القيم المفقودة
        strategy = st.selectbox("اختيار استراتيجية التعامل مع القيم المفقودة", ["remove", "impute"])
        if strategy == "impute":
            value = st.number_input("أدخل قيمة للإحلال", value=0)
            cleaned_data = prep_kit.handle_missing_values(strategy, value)
        else:
            cleaned_data = prep_kit.handle_missing_values(strategy)
        st.write("البيانات بعد التعامل مع القيم المفقودة:", cleaned_data.head())

        # ترميز البيانات الفئوية
        categorical_columns = st.text_input("أدخل الأعمدة الفئوية للفصل بينها (مفصولة بفواصل)", "")
        if categorical_columns:
            categorical_columns = categorical_columns.split(",")
            encoded_data = prep_kit.encode_categorical_data(categorical_columns)
            st.write("البيانات بعد الترميز الفئوي:", encoded_data.head())

if __name__ == "__main__":
    main()
