from PIL import Image
from transformers import AutoProcessor, VisionEncoderDecoderModel

image_path = "outputs/run_001/processed_species_row02.png"

print("Loading handwriting model...")

processor = AutoProcessor.from_pretrained(
    "microsoft/trocr-base-handwritten"
)

model = VisionEncoderDecoderModel.from_pretrained(
    "microsoft/trocr-base-handwritten"
)

print("Model loaded.")

image = Image.open(image_path).convert("RGB")

pixel_values = processor(
    images=image,
    return_tensors="pt"
).pixel_values

generated_ids = model.generate(pixel_values)

generated_text = processor.batch_decode(
    generated_ids,
    skip_special_tokens=True
)[0]

print("\nHTR result:")
print(generated_text)