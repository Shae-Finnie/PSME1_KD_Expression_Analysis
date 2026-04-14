import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("results/psme1_vs_scram_normalized.csv", index_col="ProteinID")

# compute fold changes between KO and Scram
ko_cols   = [c for c in df.columns if "PSME1_KO" in c]
scram_cols = [c for c in df.columns if "Scram" in c]

mean_ko    = df[ko_cols].mean(axis=1)
mean_scram = df[scram_cols].mean(axis=1)

# In log2 space, subtraction = fold change
log2fc = mean_ko - mean_scram

print(f"Proteins with |log2FC| > 1:  {(log2fc.abs() > 1).sum()}")
print(f"Proteins with |log2FC| > 2:  {(log2fc.abs() > 2).sum()}")
print(f"\nTop 10 most changed proteins:")
print(log2fc.abs().sort_values(ascending=False).head(10))