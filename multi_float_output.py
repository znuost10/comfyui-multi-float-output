import torch

class MultiFloatInputNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value1": ("FLOAT", {"default": 0.2, "min": -10.0, "max": 10.0, "step": 0.01}),
                "value2": ("FLOAT", {"default": 0.2, "min": -10.0, "max": 10.0, "step": 0.01}),
                "value3": ("FLOAT", {"default": 0.2, "min": -10.0, "max": 10.0, "step": 0.01}),
                "value4": ("FLOAT", {"default": 0.2, "min": -10.0, "max": 10.0, "step": 0.01}),
                "value5": ("FLOAT", {"default": 0.2, "min": -10.0, "max": 10.0, "step": 0.01}),
                "value6": ("FLOAT", {"default": 0.2, "min": -10.0, "max": 10.0, "step": 0.01}),
                "value7": ("FLOAT", {"default": 0.2, "min": -10.0, "max": 10.0, "step": 0.01}),
                "value8": ("FLOAT", {"default": 0.2, "min": -10.0, "max": 10.0, "step": 0.01}),
                "value9": ("FLOAT", {"default": 0.2, "min": -10.0, "max": 10.0, "step": 0.01}),
                "value10": ("FLOAT", {"default": 0.2, "min": -10.0, "max": 10.0, "step": 0.01}),
            }
        }

    RETURN_TYPES = ("FLOAT", "FLOAT", "FLOAT", "FLOAT", "FLOAT", "FLOAT", "FLOAT", "FLOAT", "FLOAT", "FLOAT")
    FUNCTION = "output_floats"
    CATEGORY = "utils"

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("NaN")

    def output_floats(self, value1, value2, value3, value4, value5, value6, value7, value8, value9, value10):
        return (torch.tensor([value1], dtype=torch.float32),
                torch.tensor([value2], dtype=torch.float32),
                torch.tensor([value3], dtype=torch.float32),
                torch.tensor([value4], dtype=torch.float32),
                torch.tensor([value5], dtype=torch.float32),
                torch.tensor([value6], dtype=torch.float32),
                torch.tensor([value7], dtype=torch.float32),
                torch.tensor([value8], dtype=torch.float32),
                torch.tensor([value9], dtype=torch.float32),
                torch.tensor([value10], dtype=torch.float32))

NODE_CLASS_MAPPINGS = {
    "MultiFloatInputNode": MultiFloatInputNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MultiFloatInputNode": "Multi Float Input"
}
