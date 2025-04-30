
# Task 5 – Hashing & Integrity Check Utility

## 🔐 Overview

This task demonstrates file integrity verification using cryptographic hash functions (SHA-256, SHA-1, MD5).  
A personalized file containing Ana's name was used to ensure the submission is unique.

---

## 🧪 Process Summary

### ✅ Step 1: File Creation
- Created `ana_original.txt` containing a message with Ana’s name.

### ✅ Step 2: Hash Generation
- Computed SHA-256, SHA-1, and MD5 hashes of the original file.
- Stored the hashes in `ana_hashes.json`.

### ✅ Step 3: Tampering Simulation
- Created a modified version called `ana_tampered.txt` with different content.

### ✅ Step 4: Integrity Verification
- Recalculated hashes for the tampered file.
- Compared the hashes with the original.
- Result showed mismatches for all three hashes, proving the file was altered.

---

## 📂 Files Submitted

- `ana_original.txt` – Original file created by Ana  
- `ana_tampered.txt` – Tampered version  
- `ana_hashes.json` – Original file hashes (SHA256, SHA1, MD5)  
- Python code – Script that performed hash generation and comparison  
- Output – Console result showing mismatched hashes and integrity failure

