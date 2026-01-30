import streamlit as st
import openai  # 匯入 OpenAI 套件，需先安裝：pip install openai
import base64
from utils import load_openai_api

openai.api_key = (
    load_openai_api()
)  # 載入 OpenAI API 金鑰，API 金鑰是與 OpenAI 服務互動的必要憑證

st.title("AI 圖像生成 (GPT-Image-1.5)")


st.header("從文字提示生成圖像")

# 尺寸選擇
size = st.selectbox(
    "圖像尺寸",
    ["1024x1024", "1536x1024", "1024x1536", "auto"],
    help="方形圖片生成速度最快，預設為 1024x1024 像素",
)

# 品質選擇
quality = st.selectbox(
    "圖像品質",
    ["auto", "low", "medium", "high"],
    help="品質越高，生成時間越長，費用也越高",
)

# 輸出格式
output_format = st.selectbox(
    "輸出格式", ["png", "jpeg", "webp"], help="選擇圖像輸出格式"
)

# 背景選項
background = st.selectbox(
    "背景選項", ["auto", "transparent"], help="透明背景僅適用於 PNG 或 WebP 格式"
)

# 如果選擇了不支持透明背景的格式並且要求透明背景，顯示警告
if background == "transparent" and output_format == "jpeg":
    st.warning("JPEG 格式不支援透明背景，請選擇 PNG 或 WebP 格式")

# 壓縮率 (僅適用於 jpeg 和 webp)
if output_format in ["jpeg", "webp"]:
    output_compression = st.slider(
        "壓縮率",
        min_value=0,
        max_value=100,
        value=75,
        help="值越低檔案越小，但品質越差",
    )

# 提示文字輸入區
prompt_text = st.text_area("提示詞", "A cute baby sea otter")

# 調節審核嚴格程度
moderation = st.selectbox(
    "審核嚴格程度", ["auto", "low"], help="auto 為標準過濾，low 為較寬鬆的過濾"
)

if st.button("開始生成圖片"):
    with st.spinner("正在生成圖片，請稍候..."):
        try:  # 準備參數字典
            params = {
                "model": "gpt-image-1",
                "prompt": prompt_text,
                "n": 1,
                "size": size,
                "quality": quality,
            }

            # 添加背景設置，如果不是 "auto"
            if background != "auto":
                params["background"] = background

            # 移除不支援的參數
            # moderation 和 output_format 在此 API 版本中可能不支援

            # 呼叫 API 生成圖片
            generatedImage = openai.images.generate(**params)

            # 處理並顯示圖片
            image_base64 = generatedImage.data[0].b64_json
            image_bytes = base64.b64decode(image_base64)

            # 顯示圖片
            st.image(image_bytes)

            # 顯示費用估算
            token_cost = {
                "1024x1024": {"low": 272, "medium": 1056, "high": 4160},
                "1024x1536": {"low": 408, "medium": 1584, "high": 6240},
                "1536x1024": {"low": 400, "medium": 1568, "high": 6208},
            }

            # 如果不是 auto，顯示預估費用
            if quality != "auto" and size != "auto":
                try:
                    est_tokens = token_cost[size][quality]
                    st.info(f"預估使用約 {est_tokens} 個圖像 token，加上少量文字 token")
                except:
                    pass

            # 提供下載按鈕
            st.download_button(
                label="下載圖片",
                data=image_bytes,
                file_name=f"generated_image.{output_format}",
                mime=f"image/{output_format}",
            )

        except Exception as e:
            st.error(f"生成圖片時發生錯誤: {e}")
