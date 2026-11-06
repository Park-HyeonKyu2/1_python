from dotenv import load_dotenv
import os
from openai import OpenAI
import gradio as gr

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

gpt_client = OpenAI(api_key=api_key)

def create_ad_chatgpt(name, detail, feeling):
    system_intruction = (
            "당신은 광고 문구 생성 전문가입니다..\n"
            f"입력된 {name}, {detail}룰 주제로 광고문구를 생성하세요. \n"
            f"요청은 다음과 같습니다. {feeling}만들어 주세요"
            "설명, 부연설명, 따옴표, 제목을 추가하지 마세요.\n"
            "한 줄로만 설명해 주세요."
        )
    messages = [
        { "role": "developer", "content": system_intruction },
        { "role": "user", "content": system_intruction }
    ]

    try:
        response = gpt_client.responses.create(
            model="gpt-5-nano",
            input=messages,
            reasoning={ "effort": "low" },
            max_output_tokens=500
        )

        ad_text = response.output_text.strip()
        if not ad_text:
            return "결과가 생성되지 않았습니다. 다시 시도해주세요"
        return ad_text
    except Exception as e:
        print(f'OpenAI API 오류: {e}')
        return f'생성 중 오류가 발생했습니다: {e}'


def create_ad(name, detail, feeling):
    if (name or detail) is None or not (name.strip() and detail.strip()):
        return "이름 혹은 상세 내용을 입력해 주세요."

    return create_ad_chatgpt(name=name.strip(), detail=detail.strip(), feeling=feeling)

with gr.Blocks() as demo: # 블록 안에 마크다운을 구성할 수 있음
    product_name = gr.Textbox(label="제품 이름 입력", lines=1)
    product_key_contents = gr.Textbox(label="제품 주요 내용 입력", lines=1)

    feelings = gr.Radio(['재밌게', '과장스럽게', '참신하게', '고급스럽게', '센스있게', '신선하게', '전문성있게'], label='광고 문구 느낌')

    create_button = gr.Button("문구 생성")

    output_text = gr.Textbox(
            label="광고 문구 출력창", placeholder="생성된 광고 문구가 여기에 표시됩니다.", lines=5, interactive=False
        )
    create_button.click(
        fn=create_ad, inputs=[product_name, product_key_contents, feelings],
        outputs=output_text
    )

demo.launch()
