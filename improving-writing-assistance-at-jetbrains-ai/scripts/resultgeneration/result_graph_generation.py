import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

data_path = "improving-writing-assistance-at-jetbrains-ai\\data\\test.csv"
output_folder = "improving-writing-assistance-at-jetbrains-ai\\results\\graph results"
df = pd.read_csv(data_path)

metrics = ["Levenshtein Distance", "Accuracy", "Exact Match"]

df[metrics] = df[metrics].astype(float)

sns.set_theme(style="whitegrid", palette="muted", font_scale=1.1)

os.makedirs(output_folder, exist_ok=True)

def plot_levenshtein_distance(df, spellchecker_name):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x="SpellChecker", y="Levenshtein Distance", showfliers=False)
    plt.title(f"{spellchecker_name} - Levenshtein Distance by Spell Checker")
    plt.xlabel("Spell Checker Library")
    plt.ylabel("Levenshtein Distance (Lower is Better)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save plot
    output_path = os.path.join(output_folder, f"{spellchecker_name}_levenshtein_distance.png")
    plt.savefig(output_path)
    plt.show()

def plot_accuracy_exact_match(df, spellchecker_name):
    accuracy_data = df.groupby("SpellChecker")[["Accuracy", "Exact Match"]].mean().reset_index()
    
    plt.figure(figsize=(10, 6))
    accuracy_data.plot(
        x="SpellChecker",
        kind="bar",
        stacked=True,
        color=["#4C72B0", "#55A868"],
        width=0.6,
        edgecolor="grey"
    )
    plt.title(f"{spellchecker_name} - Accuracy and Exact Match Rates by Spell Checker")
    plt.xlabel("Spell Checker Library")
    plt.ylabel("Average Scores (Accuracy & Exact Match)")
    plt.xticks(rotation=45)
    plt.legend(loc="upper right")
    plt.tight_layout()
    
    output_path = os.path.join(output_folder, f"{spellchecker_name}_accuracy_exact_match.png")
    plt.savefig(output_path)
    plt.show()

def plot_metrics_line(df, spellchecker_name):
    line_data = df.groupby("SpellChecker")[metrics].mean().reset_index()
    
    line_data_melted = line_data.melt(id_vars=["SpellChecker"], var_name="Metric", value_name="Score")
    
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=line_data_melted, x="SpellChecker", y="Score", hue="Metric", marker="o")
    plt.title(f"{spellchecker_name} - Comparison of Metrics by Spell Checker")
    plt.xlabel("Spell Checker Library")
    plt.ylabel("Score")
    plt.xticks(rotation=45)
    plt.legend(title="Metric")
    plt.tight_layout()
    
    output_path = os.path.join(output_folder, f"{spellchecker_name}_metrics_comparison.png")
    plt.savefig(output_path)
    plt.show()

spellchecker_name = "Overall_Performance"
plot_levenshtein_distance(df, spellchecker_name)
plot_accuracy_exact_match(df, spellchecker_name)
plot_metrics_line(df, spellchecker_name)
