import http.client
import json
from os import getenv
def translate(text):
  # prompt = "红头发的高中女孩"
   prompt = text
   conn = http.client.HTTPSConnection("api.chatanywhere.com.cn")
   API_KEY = getenv("ChatGPT_API_KEY")
   API_KEY = 'Bearer %s'%API_KEY
   payload = json.dumps({
      "model": "gpt-3.5-turbo",
      "messages": [
         { 
         "role": "user",
         "content": "翻译以下内容为准确的英文,用以生成AI绘图的提示词:{"+prompt+"}"
         }
      ]
   })
   headers = {
      'Authorization': API_KEY,
      #'Authorization': 'Bearer sk-xxx', # 可以直接使用密钥，需要注释上一行和API_KEY函数
      'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
      'Content-Type': 'application/json'
   }
   conn.request("POST", "/v1/chat/completions", payload, headers)
   res = conn.getresponse()
   data = res.read()
   data = json.loads(data)
   data = data['choices'][0]['message']["content"]
   print("提示词:\n{%s}\nPomrt:\n{%s}"%(prompt,data))
   return(data)

class ChatGPT_Translate:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {    
                "text": ("STRING", {"multiline": True,"default":""}),
                }
            }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Text",)

    FUNCTION = "translate_text"
    CATEGORY = "utils"

    def translate_text(self, **kwargs):        
        text = kwargs.get("text")
        text_tranlsated = translate(text)
        return (text_tranlsated,) 

NODE_CLASS_MAPPINGS = {
    "ChatGPT_Translate": ChatGPT_Translate
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "ChatGPT_Translate": "ChatGPT_Translate"
}