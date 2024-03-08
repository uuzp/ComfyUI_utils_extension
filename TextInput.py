class TextInput:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required":{
                "text":("STRING", {"multiline": True,"default":""}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Text",)

    FUNCTION = "run"
    CATEGORY = "utils"

    def run(self,**kwargs):        
        text = kwargs.get("text")
        return (text,) 

NODE_CLASS_MAPPINGS = {
    "TextInput": TextInput
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "TextInput": "TextInput"
}
