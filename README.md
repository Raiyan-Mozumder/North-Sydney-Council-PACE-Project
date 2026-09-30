# EcoTrace Task 2 MVP Starter

This is a baseline D3 prototype scaffold for the North Sydney Council Wildlife Watch historical-record work.

It follows the D2 Scoping Document pipeline:

historical scan -> image preparation -> OCR/HTR -> structured candidate observation
-> standardisation -> comparison with existing digital records -> human review.

## MVP v0.1

1. Render a selected historical PDF page locally.
2. Detect the printed table grid.
3. Split the upper Wildlife Watch table into 10 observation rows and field cells.
4. Split the lower section into row-linked nearest-street/comments regions.
5. Run Tesseract only as a simple baseline OCR.
6. Save the rendered page, crops and raw baseline OCR.
7. Keep record matching as a separate module so it can be tested independently.

Tesseract is deliberately a baseline, not the final handwriting solution. The historical sheets contain handwriting, ditto marks, corrections and row-linked notes. The purpose of v0.1 is to establish an end-to-end baseline and document where it fails before introducing a stronger local HTR model.

## Data handling

Do not copy North Sydney Council PDFs/Excel data into this repository. Keep sponsor data in the approved project storage and point the scripts to local/approved paths. The `.gitignore` excludes common project-data formats as an additional safeguard.

## Setup

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

Tesseract must also be installed locally and available on PATH.

## Run

Copy `config.example.json` to `config.json`, update the paths, then:

```bash
python run_mvp.py --config config.json
```

## D3 evidence to capture

Keep screenshots/results for:
- original selected page;
- detected grid and extracted row cells;
- baseline OCR outputs;
- manually verified ground truth;
- field-level accuracy;
- record-matching output;
- uncertain cases correctly sent to review;
- improvements after preprocessing.

These become evidence for the D3 Prototype/MVP and Data Science Project Documentation.
