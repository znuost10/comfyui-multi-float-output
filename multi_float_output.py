import torch

class MultiFloatOutputNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "float_list": ("STRING", {
                    "default": "0.1, 0.2, 0.3",
                    "multiline": False,
                    "placeholder": "Enter comma-separated floats, e.g., 0.1, 0.2, 0.3"
                }),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "split_floats"
    CATEGORY = "utils"

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("NaN")

    def split_floats(self, float_list):
        try:
            float_values = [float(x.strip()) for x in float_list.split(',') if x.strip()]
            if not float_values:
                raise ValueError("No valid floats provided.")
        except ValueError as e:
            raise ValueError(f"Invalid float list: {e}. Use comma-separated values like '0.1, 0.2, 0.3'.")

        outputs = tuple(torch.tensor([val], dtype=torch.float32) for val in float_values)
        self.RETURN_TYPES = ("FLOAT",) * len(outputs)
        return outputs

NODE_CLASS_MAPPINGS = {
    "MultiFloatOutputNode": MultiFloatOutputNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MultiFloatOutputNode": "Multi Float Output"
}