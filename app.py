import gradio as gr
import ollama

# Ollama 클라이언트 생성
client = ollama.Client()

# 번역 함수
def translate_with_ollama(text, target_lang="Korean"):
    if not text.strip():
        return "번역할 텍스트를 입력해주세요."

    prompt = f"Translate the following segment into {target_lang}\n\n{text}"

    try:
        response = client.chat(
            model='hy-mt15-translation',
            messages=[{'role': 'user', 'content': prompt}],
            options={
                'temperature': 0.7,
                'top_p': 0.6,
                'top_k': 20,
                'num_predict': 2048
            }
        )
        return response['message']['content']
    except Exception as e:
        return f"오류 발생: {str(e)}"

# Gradio 인터페이스 생성
with gr.Blocks(title="HY-MT15 번역기", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🌐 HY-MT15 번역기")
    gr.Markdown("Ollama **hy-mt15-translation** 모델을 사용한 번역 웹 UI입니다.")

    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(
                label="입력 텍스트",
                placeholder="번역할 텍스트를 입력하세요...",
                lines=10
            )
            target_lang = gr.Dropdown(
                label="타겟 언어",
                choices=["Korean", "English", "Japanese", "Chinese", "French", "German", "Spanish"],
                value="Korean"
            )
            translate_btn = gr.Button("번역하기", variant="primary", size="lg")

        with gr.Column():
            output_text = gr.Textbox(
                label="번역 결과",
                lines=10,
                interactive=False
            )

    translate_btn.click(
        fn=translate_with_ollama,
        inputs=[input_text, target_lang],
        outputs=output_text
    )

    # 예제 추가
    gr.Examples(
        examples=[
            ["Poor sales have reportedly forced Apple to cut production of the Vision Pro headset.", "Korean"],
            ["안녕하세요, 오늘 날씨가 좋습니다.", "English"],
            ["Hello, how are you today?", "Japanese"],
        ],
        inputs=[input_text, target_lang],
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
