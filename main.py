import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Заголовок приложения
st.title('Анализ данных из Excel')

# Загрузка Excel-файла
uploaded_file = st.file_uploader("Загрузите файл Excel", type=["xlsx", "xls"])

if uploaded_file is not None:
    # Чтение данных из Excel-файла
    xls = pd.ExcelFile(uploaded_file)

    # Список всех листов в Excel-файле
    sheet_names = xls.sheet_names

    # Отображение списка листов
    selected_sheet = st.selectbox("Выберите лист Excel", sheet_names)

    # Чтение данных из выбранного листа
    df = xls.parse(selected_sheet)

    # Удалите столбец с именем "Год" (замените его на имя вашего столбца)
    if "Год" in df.columns:
        df = df.drop(columns=["Год"])

    # Отображение данных в виде таблицы
    st.dataframe(df)

    # Создание графика на основе данных
    st.write("### График данных")
    x_col = st.selectbox("Выберите столбец для оси X", df.columns)
    y_col = st.selectbox("Выберите столбец для оси Y", df.columns)
    plt.figure(figsize=(10, 6))
    plt.plot(df[x_col], df[y_col], marker='o')  # Используйте plt.plot для линейного графика
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    st.pyplot(plt)

else:
    st.warning("Загрузите файл Excel для начала анализа.")
