from modules.loader import load_gdelt, load_huffpost
from modules.cleaning import clean_gdelt, clean_huffpost
from modules.visualize import plot_articles_per_day, plot_categories
from modules.analysis import analyze_gdelt, analyze_huffpost
import os

print("Files inside data folder:")
print(os.listdir("data"))

# ---------------- GDELT ---------------- #

print("\n--- GDELT TEST ---")

gdelt_path = "data/gdelt_sample.csv"

df_gdelt, report_gdelt = load_gdelt(gdelt_path)

print("Validation Report:")
print(report_gdelt)

if df_gdelt is not None:
    print("\nRaw Data Preview:")
    print(df_gdelt.head())
    print("Shape:", df_gdelt.shape)

    print("\n--- CLEANED GDELT ---")
    df_gdelt_clean = clean_gdelt(df_gdelt)
    print(df_gdelt_clean.head())
    print("Shape:", df_gdelt_clean.shape)

else:
    print("❌ Failed to load GDELT")

print("\n--- GDELT ANALYSIS ---")

gdelt_analysis = analyze_gdelt(df_gdelt_clean)

print("\nTop countries:")
print(gdelt_analysis["top_countries"])


# ---------------- HUFFPOST ---------------- #

print("\n--- HUFFPOST TEST ---")

huff_path = "data/huffpost.json"

df_huff, report_huff = load_huffpost(huff_path)

print("Validation Report:")
print(report_huff)

if df_huff is not None:
    print("\nRaw Data Preview:")
    print(df_huff.head())
    print("Shape:", df_huff.shape)

    print("\n--- CLEANED HUFFPOST ---")
    df_huff_clean = clean_huffpost(df_huff)
    print(df_huff_clean.head())
    print("Shape:", df_huff_clean.shape)

else:
    print("❌ Failed to load HuffPost")

print("\n--- HUFFPOST ANALYSIS ---")

huff_analysis = analyze_huffpost(df_huff_clean)

print("\nArticles per day:")
print(huff_analysis["articles_per_day"].head())

print("\nTop categories:")
print(huff_analysis["top_categories"])

# VISUALIZATION

plot_articles_per_day(huff_analysis["articles_per_day"])
plot_categories(huff_analysis["top_categories"])