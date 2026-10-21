# Task 2 Test Specification

## Purpose

This document describes the formal testing and evaluation of the Task 2 EcoTrace MVP for digitising historical North Sydney Council Wildlife Watch records.

Testing focuses on the reliability of the digitisation workflow, including document processing, field extraction, missing or uncertain values, output validation, and comparison of extracted values against manually verified ground truth.

## Test Data

Testing uses selected historical Wildlife Watch sheets provided by North Sydney Council. Manually verified values are recorded in `ground_truth_template.csv` and used as reference values when evaluating extracted fields.

## Test Cases

# Task 2 MVP Test Specification

## Purpose

This section documents the formal testing conducted for the Task 2 EcoTrace MVP. Testing focused on the review and digitisation workflow for historical Wildlife Watch observation sheets, including PDF processing, automated field extraction, handwritten-field review, ditto handling, low-confidence detection, species standardisation, duplicate detection, manual correction, and human approval.

## Test Environment

- MVP: EcoTrace browser-based Wildlife Watch digitisation tool
- Test document: 4988_001.pdf
- Test sample: Page 1, Rows 1–10
- Total records detected in document: 302
- Reviewer: Aran
- Test date: 21 October 2026
- Testing method: Comparison of extracted values against the original scanned form

## Test Cases

### T2-TC01 – PDF Processing and Record Segmentation

- **Test data:** 4988_001.pdf
- **Procedure:** Upload the PDF to EcoTrace and allow the MVP to process the document.
- **Expected result:** The document is processed and individual observation records are created for review.
- **Actual result:** The 30-page PDF was processed in approximately 31 seconds and 302 observation rows were generated for review.
- **Result:** PASS

### T2-TC02 – Automated Numeric and Coded Field Extraction

- **Test data:** Page 1, Rows 1–10
- **Procedure:** Compare automatically extracted fields such as area number, species code, vegetation class, observation type, microhabitat, number and confidence against the scanned form.
- **Expected result:** Clearly written numeric and coded fields should be automatically extracted, while uncertain values should be identified for review.
- **Actual result:** Many clearly written fields were extracted with high confidence. Species codes including 0254, 0133, 0634, 0702, 0043 and 0705 were recognised and linked to corresponding standardised species. Some unclear values received lower confidence scores or required manual review.
- **Result:** PASS

### T2-TC03 – Handwritten Field Review

- **Test data:** Page 1, Rows 1–10
- **Procedure:** Inspect fields marked as handwriting, including observer, area name, original species text, nearest street and comments.
- **Expected result:** Handwritten fields that cannot be reliably automated should be presented to the reviewer together with the relevant scan crop for manual entry.
- **Actual result:** Handwritten fields were displayed with scan crops and input boxes for manual review. Examples included the observer name, species descriptions, area names, nearest streets and comments.
- **Result:** PASS

### T2-TC04 – Ditto / Repeated Value Handling

- **Test data:** Page 1, Rows 2–10
- **Procedure:** Review fields containing ditto marks and compare the populated value with the preceding applicable row.
- **Expected result:** Ditto marks should reuse the appropriate previously entered value and clearly indicate that the value was repeated.
- **Actual result:** EcoTrace detected repeated values and displayed labels such as “ditto – row 1”, “ditto – row 3” and “ditto – row 6”. Repeated dates and area names were carried forward and remained available for reviewer verification.
- **Result:** PASS

### T2-TC05 – Low-Confidence Detection

- **Test data:** Page 1, Rows 1–10
- **Procedure:** Inspect fields marked with low machine confidence and compare them against the original scan.
- **Expected result:** Uncertain machine readings should be clearly flagged rather than silently accepted.
- **Actual result:** Low-confidence fields were visibly flagged with confidence percentages and warning messages. Examples were observed for dates, area numbers, observation numbers and other uncertain values.
- **Result:** PASS

### T2-TC06 – Species Code Standardisation

- **Test data:** Page 1, Rows 1–10
- **Procedure:** Compare detected species codes with the standardised species suggested by EcoTrace.
- **Expected result:** A recognised Council species code should produce the corresponding standardised species suggestion.
- **Actual result:** Recognised codes generated corresponding species suggestions, including 0254 (Rainbow Lorikeet), 0133 (Masked Lapwing), 0634 (Noisy Miner), 0702 (Grey Butcherbird), 0043 (Crested Pigeon) and 0705 (Australian Magpie).
- **Result:** PASS

### T2-TC07 – Duplicate Detection

- **Test data:** Page 1 reviewed records
- **Procedure:** Review and approve records during the workflow and observe whether potentially duplicated observations are detected.
- **Expected result:** A possible duplicate should be flagged for human review rather than being automatically accepted or removed.
- **Actual result:** EcoTrace displayed a “Possible duplicate” warning when an approved record had the same observer, date, species, area and number as an existing approved record. The warning identified the related record and required the reviewer to cancel or approve the record as a separate sighting.
- **Result:** PASS

### T2-TC08 – Human Review and Approval Workflow

- **Test data:** Page 1, Rows 1–10
- **Procedure:** Compare extracted values against the scan, complete required manual fields, review flagged or low-confidence values, and use the approval workflow.
- **Expected result:** Records should remain awaiting review until a human reviewer verifies the extracted information and approves the record.
- **Actual result:** Records remained in “Awaiting review” status until reviewed. Approved records were marked separately and the interface automatically advanced to the next observation record. Rows 1–10 of Page 1 were inspected during testing.
- **Result:** PASS

### T2-TC09 – Incorrect Extraction and Manual Correction

- **Test data:** Page 1, Rows 1–10
- **Procedure:** Compare uncertain automatically extracted values against the original scan and check whether incorrect values can be manually corrected before approval.
- **Expected result:** Incorrect or uncertain machine-generated values should remain editable so that the reviewer can correct them using the original scan.
- **Actual result:** Testing identified machine-generated values that did not reliably correspond with the scanned values, particularly in low-confidence fields such as dates, area numbers and observation numbers. The interface allowed these values to be edited before approval, while displaying the original scan crop for comparison.
- **Result:** PASS

## Test Summary

Testing of Page 1 of 4988_001.pdf demonstrated that the EcoTrace MVP can process a historical Wildlife Watch PDF, segment the document into individual observation records, extract many structured fields, identify uncertain values, support handwritten-field entry, process ditto values, standardise recognised species codes, detect possible duplicate records, allow correction of machine-generated values, and support human review before approval.

The testing also identified limitations. Handwritten text still requires substantial manual input, and some low-confidence machine readings do not reliably match the scanned values. Therefore, the current MVP should be treated as a human-in-the-loop digitisation tool rather than a fully automated transcription system. Human verification remains important before extracted records are accepted into the final dataset.
