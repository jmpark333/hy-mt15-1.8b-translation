import ollama

# Ollama 클라이언트 생성
client = ollama.Client()

# 번역 함수
def translate_with_ollama(text, target_lang="Korean"):
    prompt = f"Translate the following segment into {target_lang}\n\n{text}"

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

# 사용 예시
result = translate_with_ollama(
    "Poor sales have reportedly forced Apple to cut production of the Vision Pro headset that it had hoped would herald a new era in “spatial computing”.The tech company also reduced marketing for Vision Pro by more than 95percent last year, according to the market intelligence group Sensor Tower in figures first reported by the Financial Times.",
    "Korean"
)
print("번역 결과:", result)