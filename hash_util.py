
import hashlib
import json

# Step 1: Create the original file
with open("original.txt", "w") as f:
    f.write("This is Ana's original file used for integrity verification.")

# Step 2: Compute and save hashes
with open("original.txt", "rb") as f:
    content = f.read()

hashes = {
    "SHA256": hashlib.sha256(content).hexdigest(),
    "SHA1": hashlib.sha1(content).hexdigest(),
    "MD5": hashlib.md5(content).hexdigest()
}

with open("hashes.json", "w") as f:
    json.dump(hashes, f, indent=4)

# Step 3: Simulate tampering
with open("tampered.txt", "w") as f:
    f.write("This is Ana's file, but now it has been secretly modified!")

# Step 4: Compare hashes
with open("hashes.json", "r") as f:
    original_hashes = json.load(f)

with open("tampered.txt", "rb") as f:
    tampered_content = f.read()

tampered_hashes = {
    "SHA256": hashlib.sha256(tampered_content).hexdigest(),
    "SHA1": hashlib.sha1(tampered_content).hexdigest(),
    "MD5": hashlib.md5(tampered_content).hexdigest()
}

print("🔍 Comparing original and tampered file hashes:\n")
for algo in original_hashes:
    print(f"{algo}:")
    print(f"  Original : {original_hashes[algo]}")
    print(f"  Tampered : {tampered_hashes[algo]}")
    if original_hashes[algo] == tampered_hashes[algo]:
        print("  ✅ Match – File is intact.\n")
    else:
        print("  ❌ Mismatch – File integrity FAILED!\n")
