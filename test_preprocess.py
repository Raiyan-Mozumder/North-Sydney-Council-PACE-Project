import cv2
from src.baseline_ocr import preprocess_for_ocr, pytesseract

input_path = "outputs/run_001/cells/row_02/species.png"
output_path = "outputs/run_001/processed_species_row02.png"

image = cv2.imread(input_path)

if image is None:
    print("Could not open the original species image.")
else:
    processed = preprocess_for_ocr(image)

    cv2.imwrite(output_path, processed)

    original_text = pytesseract.image_to_string(
        image,
        config="--psm 7"
    ).strip()

    processed_text = pytesseract.image_to_string(
        processed,
        config="--psm 7"
    ).strip()

    print("Original OCR:")
    print(original_text)

    print("\nProcessed OCR:")
    print(processed_text)

    print("\nProcessed image saved successfully.")