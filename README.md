# HY-MT15 번역기

Ollama 기반 **HY-MT15-1.8B** 번역 모델을 사용한 다국어 번역 웹 UI입니다.

## 기능

- Ollama `hy-mt15-translation` 모델을 활용한 고품질 번역
- Gradio 기반 직관적인 웹 인터페이스
- 다국어 지원 (한국어, 영어, 일본어, 중국어, 프랑스어, 독일어, 스페인어)

## 설치

### 1. Ollama 설치

```bash
# Linux/macOS
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. 모델 생성

```bash
# Modelfile을 사용하여 모델 생성
ollama create hy-mt15-translation -f Modelfile
```

### 3. Python 패키지 설치

```bash
# 가상환경 활성화 (선택사항)
source myenv/bin/activate

# 필요한 패키지 설치
pip install gradio ollama
```

## 사용 방법

### 웹 UI 실행

```bash
python app.py
```

브라우저에서 `http://localhost:7860`으로 접속합니다.

### Python 코드로 사용

```python
import ollama

client = ollama.Client()

def translate(text, target_lang="Korean"):
    prompt = f"Translate the following segment into {target_lang}\n\n{text}"
    response = client.chat(
        model='hy-mt15-translation',
        messages=[{'role': 'user', 'content': prompt}]
    )
    return response['message']['content']

result = translate("Hello, world!", "Korean")
print(result)
```

## 모델 설정

Modelfile 설정:

```
FROM ./HY-MT1.5-1.8B-Q4_K_M.gguf
PARAMETER temperature 0.7
PARAMETER top_p 0.6
PARAMETER top_k 20
PARAMETER num_predict 2048
TEMPLATE """
{{- range .Messages }}
{{- if .Role == "user" }}User: {{ .Content }}
{{- else if .Role == "assistant" }}Assistant: {{ .Content }}
{{- end }}
{{- end }}
Assistant:
"""
PARAMETER stop "User:"
PARAMETER stop "Assistant:"
SYSTEM ""You are a professional translator. Translate the given text accurately and naturally.""
```

## 프로젝트 구조

```
.
├── app.py              # Gradio 웹 UI
├── test.py             # 번역 테스트 스크립트
├── Modelfile           # Ollama 모델 설정
├── HY-MT1.5-1.8B-Q4_K_M.gguf  # 번역 모델 파일
├── requirements.txt    # Python 의존성
└── README.md           # 프로젝트 문서
```

## 지원 언어

- 한국어 (Korean)
- 영어 (English)
- 일본어 (Japanese)
- 중국어 (Chinese)
- 프랑스어 (French)
- 독일어 (German)
- 스페인어 (Spanish)

## 라이선스

MIT License
