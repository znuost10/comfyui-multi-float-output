import torch

class MultiFloatInputNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "custom_names": ("STRING", {"default": "float1,float2,float3,float4,float5,float6,float7,float8,float9,float10", "multiline": False}),
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
    OUTPUT_NAMES = ("float1", "float2", "float3", "float4", "float5", "float6", "float7", "float8", "float9", "float10")
    FUNCTION = "output_floats"
    CATEGORY = "utils"

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("NaN")

    def output_floats(self, custom_names, value1, value2, value3, value4, value5, value6, value7, value8, value9, value10):
        # Parse custom names (for internal use or logging, not UI renaming)
        custom_names_list = [name.strip() for name in custom_names.split(',') if name.strip()]
        if len(custom_names_list) < 10:
            custom_names_list.extend([f"float{i}" for i in range(len(custom_names_list) + 1, 11)])
        
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
