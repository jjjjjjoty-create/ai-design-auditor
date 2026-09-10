import streamlit as st


st.set_page_config(
    page_title="AI Design Auditor",
    page_icon="🎨",
    layout="wide"
)


st.title("🎨 AI DESIGN AUDITOR")

st.subheader(
    "Анализ графического дизайна "
    "на основе принципов визуальной коммуникации"
)

st.write(
    "Загрузите афишу, баннер, обложку или другой "
    "графический материал для анализа."
)


uploaded_file = st.file_uploader(
    "Загрузите изображение",
    type=["png", "jpg", "jpeg"]
)


if uploaded_file is not None:

    st.image(
        uploaded_file,
        caption="Загруженный дизайн",
        use_container_width=True
    )

    st.success("Изображение успешно загружено.")

    if st.button(
        "🔍 Провести аудит",
        type="primary"
    ):

        st.info(
            "Модуль анализа будет подключён "
            "на следующем этапе."
        )
