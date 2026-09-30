import argparse
import json
from pathlib import Path
import cv2

from src.render_and_segment import render_pdf_page, extract_rows_and_cells
from src.baseline_ocr import run_tesseract_baseline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()

    config = json.loads(Path(args.config).read_text(encoding="utf-8"))
    out = Path(config["output_dir"])
    out.mkdir(parents=True, exist_ok=True)

    image = render_pdf_page(
        config["historical_pdf"],
        int(config.get("page_number", 1)),
        zoom=2.5,
    )
    cv2.imwrite(str(out / "rendered_page.png"), image)

    rows = extract_rows_and_cells(image, str(out / "cells"))
    df = run_tesseract_baseline(rows, str(out / "baseline_ocr.csv"))

    print(f"Rendered page: {out / 'rendered_page.png'}")
    print(f"Cell crops: {out / 'cells'}")
    print(f"Baseline OCR: {out / 'baseline_ocr.csv'}")
    print()
    print(df.to_string(index=False))

if __name__ == "__main__":
    main()
