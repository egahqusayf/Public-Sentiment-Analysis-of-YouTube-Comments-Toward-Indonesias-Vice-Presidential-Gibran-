import pandas as pd
import os

# ==============================
# 1. PATH & FILE SETUP
# ==============================

INPUT_PATH = "data/all_youtube_comments.xlsx"
OUTPUT_LABELED = "data/annotated_comments_labeled.csv"
OUTPUT_UNLABELED = "data/youtube_comments_unlabeled.csv"

# Pastikan folder data ada
os.makedirs("data", exist_ok=True)

# ==============================
# 2. LOAD DATASET
# ==============================

df = pd.read_excel(INPUT_PATH)

print("Total data:", len(df))
print("\nKolom dataset:")
print(df.columns.tolist())

# ==============================
# 3. VALIDASI KOLOM WAJIB
# ==============================

required_columns = ["video_id", "comment", "likes", "label", "published_at"]

missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    raise ValueError(f"Kolom berikut tidak ditemukan: {missing_columns}")

# ==============================
# 4. PISAHKAN DATA BERLABEL
# ==============================

df_labeled = df[df["label"].notna()].copy()

print("\nJumlah data BERLABEL:", len(df_labeled))
print("Distribusi label:")
print(df_labeled["label"].value_counts())

# ==============================
# 5. PISAHKAN DATA TIDAK BERLABEL
# ==============================

df_unlabeled = df[df["label"].isna()].copy()

print("\nJumlah data TIDAK BERLABEL:", len(df_unlabeled))

# ==============================
# 6. SIMPAN KE FILE CSV
# ==============================

df_labeled.to_csv(OUTPUT_LABELED, index=False, encoding="utf-8")
df_unlabeled.to_csv(OUTPUT_UNLABELED, index=False, encoding="utf-8")

print("\n✅ File berhasil disimpan:")
print(f"- {OUTPUT_LABELED}")
print(f"- {OUTPUT_UNLABELED}")
