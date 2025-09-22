import torch

class MultiFloatInputNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "value1": ("FLOAT1", {"default": 0.2, "min": -10.0, "max": 10.0, "step": 0.01}),
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

# Simulate node execution
node = MultiFloatInputNode()
sample_values = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5, 1.7, 1.9]
outputs = node.output_floats(*sample_values)

# Print results
for i, output in enumerate(outputs, 1):
    print(f"Output {i}: {output.item()}")
