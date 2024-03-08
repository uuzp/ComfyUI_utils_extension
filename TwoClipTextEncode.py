from nodes import CLIPTextEncode
    
class TwoClipTextEncode():
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(self):
        return {
        "required":{
            "clip": ("CLIP", {}), "prompt": ("STRING", {"default":""}), "negative_prompt": ("STRING", {"default":""})
            }
        }
    
    RETURN_TYPES = ("CONDITIONING", "CONDITIONING",)
    RETURN_NAMES = ("positive", "negative",)

    FUNCTION = "run"
    CATEGORY = "utils"
    encoder = CLIPTextEncode().encode

    def run(self, clip, prompt, negative_prompt):
        return(self.encoder(clip,prompt)[0], self.encoder(clip,negative_prompt)[0], )

NODE_CLASS_MAPPINGS = {
    "TwoClipTextEncode": TwoClipTextEncode,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "TwoClipTextEncode": "TwoClipTextEncode"
}