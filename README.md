# ews-gis-assets

GIS assets for EWS-Consulting

Yes, that’s a practical and efficient approach! Instead of creating a new commit each time the file is downloaded, you can optimize the process by:

1. **Storing and Comparing Hashes**:

- Calculate the hash of the downloaded file (e.g., SHA256 or MD5 checksum) after fetching it.
- Compare it with the hash of the previously fetched version stored in the repository (or locally in a separate file).
- Only create a new commit if the hash differs (i.e., the content has changed).

2. **Benefits of This Approach**:

- **Avoid unnecessary commits**: Prevents cluttering the commit history with redundant updates.
- **Efficient repository size**: Avoid duplicating identical data.
- **Simple version control**: Helps you keep track of when the dataset truly changes.

---

### Implementation Plan

Here’s how you can modify the Python script and GitHub Actions workflow:

#### 1. **Python Script**: Generate Hashes and Compare

Enhance the script to:

- Calculate the hash of the new file.
- Compare it with a stored hash (if it exists).
- Save the new hash only if the content has changed.

```python
import requests
import os
import hashlib
import json
GEOJSON_URL = "https://atlas.noe.gv.at/atlas/api/rest/services/ags_raumordnung__energie@atlas_raumordnung/queries/windkraftanlagen/query?f=json&queryId=windkraftanlagen"
OUTPUT_DIR = "data"
FILE_NAME = "windkraftanlagen.geojson"
HASH_FILE = "data/last_hash.txt"
def calculate_file_hash(file_path):
   """Calculate the SHA256 hash of a file."""
   hash_sha256 = hashlib.sha256()
   with open(file_path, "rb") as f:
       for chunk in iter(lambda: f.read(4096), b""):
           hash_sha256.update(chunk)
   return hash_sha256.hexdigest()
def download_geojson():
   """Download and save GeoJSON data."""
   response = requests.get(GEOJSON_URL)
   response.raise_for_status()
   geojson = response.json()
   # Save data to a local file
   file_path = os.path.join(OUTPUT_DIR, FILE_NAME)
   with open(file_path, "w", encoding="utf-8") as file:
       json.dump(geojson, file, indent=2)  # Pretty print GeoJSON
   return file_path
def is_file_updated(new_file):
   """Check if the downloaded file differs from the previous version."""
   # Calculate the new file's hash
   new_hash = calculate_file_hash(new_file)
   # Check if the hash file exists
   if os.path.exists(HASH_FILE):
       with open(HASH_FILE, "r") as f:
           last_hash = f.read().strip()
           if new_hash == last_hash:
               # File has not changed
               print("GeoJSON file is identical to the previous version. No update needed.")
               return False
   # Save the new hash for future comparisons
   with open(HASH_FILE, "w") as f:
       f.write(new_hash)
   print("New GeoJSON file detected. Updating...")
   return True
def main():
   """Main method for the script."""
   if not os.path.exists(OUTPUT_DIR):
       os.makedirs(OUTPUT_DIR)
   # Download the GeoJSON file
   new_file = download_geojson()
   # Check if file has been updated
   if is_file_updated(new_file):
       print("Changes detected. The file is updated and can be pushed to the repository.")
   else:
       print("No changes detected. Exiting without committing.")
if __name__ == "__main__":
   main()
```

---

#### 2. **GitHub Actions Workflow**

Modify the workflow file to detect changes:

- Check the hash of the newly downloaded data.
- Commit and push only if the hash indicates changes.

```yaml
name: Update GeoJSON Daily
on:
  schedule:
    - cron: "0 0 * * *" # Runs daily at midnight UTC
  workflow_dispatch: # Allows manual trigger
jobs:
  update-geojson:
    runs-on: ubuntu-latest
    steps:
      # Step 1: Check out the repository
      - name: Checkout repository
        uses: actions/checkout@v3
      # Step 2: Set up Python
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.9"
      # Step 3: Install Python dependencies
      - name: Install dependencies
        run: pip install requests
      # Step 4: Run the script
      - name: Run the update script
        run: python download_geojson.py
      # Step 5: Commit and push changes if there are updates
      - name: Commit and push changes
        if: success()
        run: |
          if [ "$(git status --porcelain)" != "" ]; then
            git config --global user.name "github-actions[bot]"
            git config --global user.email "github-actions[bot]@users.noreply.github.com"
            git add .
            git commit -m "Update GeoJSON file (automated)"
            git push
          else
            echo "No changes detected. Skipping commit."
```

---

### Summary of Workflow:

1. The Python script fetches the GeoJSON file and calculates its hash.
2. The script compares the new file’s hash with the previously saved hash:

- If the hash matches, the script exits without making changes.
- If the hash differs, the new file and hash are saved.

3. GitHub Actions commits and pushes the update only if the repository has uncommitted changes.

---

### Why This Works:

1. **Efficient Versioning**:

- Only updates the repo when the data changes.
- Keeps the commit history clean.

2. **Static Hosting with GitHub Pages**:

- If GitHub Pages is enabled, the new GeoJSON file will automatically be served (no extra work required).

3. **Low Maintenance**:

- Everything is automated, and duplication is avoided.
  Let me know if you'd like further refinements or more help implementing this!
