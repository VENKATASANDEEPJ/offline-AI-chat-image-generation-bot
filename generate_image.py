import time
import torch
from diffusers import StableDiffusionPipeline

model_path = "image_engine/v1-5-pruned-emaonly.safetensors"

pipe = StableDiffusionPipeline.from_single_file(
    model_path,
    torch_dtype=torch.float16,
)
pipe = pipe.to("cuda")

prompt = input("Enter image prompt: ")

image = pipe(prompt).images[0]

filename = f"output_{int(time.time())}.png"
image.save(filename)
print(f"Image generated and saved as {filename}")

print("Image generated and saved as output.png")
