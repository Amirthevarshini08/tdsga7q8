"""
Patient Satisfaction Analysis
Author: 22f3000033@ds.study.iitm.ac.in
Generated with LLM assistance (ChatGPT/Codex-style)
"""

import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Load dataset
    data = pd.read_csv("data/patient_satisfaction.csv")
    industry_target = 4.5
    avg = data["Score"].mean()
    print(f"Average Satisfaction Score (2024): {avg:.2f}")  # Expect 2.07

    # Plot trend vs target
    plt.figure(figsize=(8, 5))
    plt.plot(data["Quarter"], data["Score"], marker="o", label="Patient Satisfaction")
    plt.axhline(y=industry_target, linestyle="--", label="Industry Target (4.5)")
    plt.title("Patient Satisfaction Scores - 2024")
    plt.xlabel("Quarter")
    plt.ylabel("Satisfaction Score")
    plt.ylim(-2, 5)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("patient_satisfaction_trend.png", dpi=150)

if __name__ == "__main__":
    main()
