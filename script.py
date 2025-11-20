from openai import OpenAI
import base64
import logging
import datetime

logging.basicConfig(
    filename="nemotron_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log(msg):
    print(msg)
    logging.info(msg)

def encode_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
    
def getResponseFromLLM(client, image_base64):
    completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": "https://youtube.com",
        "X-Title": "gaming",
    },
    model="nvidia/nemotron-nano-12b-v2-vl:free",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Extract all details from this image. with key points and key values in json format."},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{b64_image}"
                    }
                }
            ]
        }
    ]
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    log("Started at " + str(datetime.datetime.now()))
    image_path = "C:/Users/Pictures/Screenshot 2025-11-18 120509.png"
    log(f'Image loaded from {image_path}')
    b64_image = encode_image(image_path)
    log("Image encoded to base64")

    try:
        log("Sending request to LLM...")
        client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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",
        )
        log("Client initialized")
        log("Getting response from LLM...")
        response = getResponseFromLLM(client, b64_image)
        log("Response received !!!")
        print(response)
        log("Completed at " + str(datetime.datetime.now()))
    except Exception as e:
        log(f"Error initializing OpenAI client: {e}")
        exit(1)
