from .TextInput import TextInput
from .ChatGPT_Translate import ChatGPT_Translate
from .TwoClipTextEncode import TwoClipTextEncode

NODE_CLASS_MAPPINGS = { "ChatGPT_Translate": ChatGPT_Translate,"TextInput": TextInput, "TwoClipTextEncode": TwoClipTextEncode, }

NODE_DISPLAY_NAME_MAPPINGS = {"TwoClipTextEncode": "TwoClipTextEncode","ChatGPT_Translate": "ChatGPT_Translate","TextInput": "TextInput"}

all = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']