import http.client
import json
from os import getenv
def translate(text):
  # prompt = "红头发的高中女孩"
   prompt = text
   URL = getenv("ChatGPT_API_URL")
   API_KEY = getenv("ChatGPT_API_KEY")
   if URL is None or API_KEY is None:
     print("未设置URL或API_KEY变量！\nThe URL or API_KEY variable is not set!")
   conn = http.client.HTTPSConnection(URL)
   API_KEY = 'Bearer %s'%API_KEY
   payload = json.dumps({
      "model": "gpt-3.5-turbo",
      "messages": [
         { 
         "role": "user",
         "content": "翻译以下内容为准确的英文,翻译使用简短的单词，避免长句，不需要添加修饰，使用最接近原文准确意思的单词。\n以下{}内是需要翻译的内容:\n{"+prompt+"}"
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
