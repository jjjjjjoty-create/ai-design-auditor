import streamlit as st
from google import genai


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


uploaded_file = st.file_uploader(
    "Загрузите дизайн",
    type=["png", "jpg", "jpeg"]
)


if uploaded_file is not None:

    st.image(
        uploaded_file,
        caption="Загруженный дизайн",
        use_container_width=True
    )


    if st.button(
        "🔍 Провести аудит",
        type="primary"
    ):

        try:

            client = genai.Client(
                api_key=st.secrets["GEMINI_API_KEY"]
            )


            image_bytes = uploaded_file.getvalue()


            prompt = """
You are an expert in graphic design and visual communication.

Analyze the uploaded graphic design according to
fundamental graphic design principles.

Evaluate:

1. Composition
2. Visual hierarchy
3. Balance
4. Contrast
5. Typography
6. Color
7. Negative space
8. Alignment
9. Readability
10. Overall visual coherence

For each principle:

- give a score from 0 to 100;
- explain the score briefly;
- identify one strength or weakness.

Then provide:

- three strongest aspects of the design;
- three main problems;
- three concrete recommendations for improvement.

Do not judge the personal taste of the viewer.
Focus on observable characteristics of the design.

Return the answer in a clear structured format.
"""


            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=[
                    prompt,
                    {
                        "inline_data": {
                            "mime_type": uploaded_file.type,
                            "data": image_bytes
                        }
                    }
                ]
            )


            st.divider()

            st.header("📊 AI Design Audit")

            st.write(response.text)


        except Exception as e:

            st.error(
                f"Произошла ошибка: {e}"
            )
