import torch

class MultiFloatInputNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "label1": ("STRING", {"default": "Value1", "multiline": False}),
                "value1": ("FLOAT", {"default": 0.2, "min": -10.0, "max": 10.0, "step": 0.01}),
                "label2": ("STRING", {"default": "Value2", "multiline": False}),
                "value2": ("FLOAT", {"default": 0.2, "min": -10.0, "max": 10.0, "step": 0.01}),
                "label3": ("STRING", {"default": "Value3", "multiline": False}),
                "value3": ("FLOAT", {"default": 0.2, "min": -10.0, "max": 10.0, "step": 0.01}),
                "label4": ("STRING", {"default": "Value4", "multiline": False}),
                "value4": ("FLOAT", {"default": 0.2, "min": -10.0, "max": 10.0, "step": 0.01}),
            }
        }

    RETURN_TYPES = ("FLOAT", "FLOAT", "FLOAT", "FLOAT")
    FUNCTION = "output_floats"
    CATEGORY = "utils"

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("NaN")

    def output_floats(self, value1, value2, value3, value4):
        return (torch.tensor([value1], dtype=torch.float32),
                torch.tensor([value2], dtype=torch.float32),
                torch.tensor([value3], dtype=torch.float32),
                torch.tensor([value4], dtype=torch.float32))

NODE_CLASS_MAPPINGS = {
    "MultiFloatInputNode": MultiFloatInputNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MultiFloatInputNode": "Multi Float Input"
}
