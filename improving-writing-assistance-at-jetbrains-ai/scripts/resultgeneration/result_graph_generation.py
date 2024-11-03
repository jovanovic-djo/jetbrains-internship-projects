import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load data
data_path = "improving-writing-assistance-at-jetbrains-ai\\results\\libraries results\\pyenchant.csv"
output_folder = "improving-writing-assistance-at-jetbrains-ai\\results\\graph results"
df = pd.read_csv(data_path)

# Ensure that the metrics columns are numeric
metrics = ["Levenshtein Distance", "Accuracy", "Exact Match"]
df[metrics] = df[metrics].astype(float)

# Set up plot styling
sns.set_theme(style="whitegrid", palette="muted", font_scale=1.1)
os.makedirs(output_folder, exist_ok=True)

def plot_advanced_metrics_with_histograms(df, spellchecker_name):
    fig, axes = plt.subplots(2, 3, figsize=(18, 12), gridspec_kw={'height_ratios': [1, 1.5]})
    fig.suptitle(f"{spellchecker_name} - Metric Analysis and Distributions", fontsize=16)

    # Define colors for box plots and histograms
    box_colors = ["#4C72B0", "#55A868"]  # Blue for Levenshtein, Green for Accuracy
    hist_colors = ["#4C72B0", "#55A868", "#C44E52"]  # Different colors for each metric histogram

    # Enhanced Box Plots for 'Accuracy' and 'Levenshtein Distance'
    sns.boxplot(data=df, y="Accuracy", ax=axes[0, 0], color=box_colors[1], linewidth=1.5, saturation=0.75)
    axes[0, 0].set_title("Accuracy")
    axes[0, 0].set_ylabel("Score")
    axes[0, 0].spines["top"].set_visible(False)
    axes[0, 0].spines["right"].set_visible(False)

    sns.boxplot(data=df, y="Levenshtein Distance", ax=axes[0, 1], color=box_colors[0], linewidth=1.5, saturation=0.75)
    axes[0, 1].set_title("Levenshtein Distance")
    axes[0, 1].set_ylabel("Score")
    axes[0, 1].spines["top"].set_visible(False)
    axes[0, 1].spines["right"].set_visible(False)

    # Leave the third subplot on the first row empty
    axes[0, 2].axis('off')

    # Histograms for each metric in the second row
    for i, metric in enumerate(metrics):
        sns.histplot(df[metric], bins=15, color=hist_colors[i], kde=True, ax=axes[1, i], edgecolor="black")
        axes[1, i].set_title(f"Distribution of {metric}")
        axes[1, i].set_xlabel("Score")
        axes[1, i].set_ylabel("Frequency")

    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout to fit title
    output_path = os.path.join(output_folder, f"{spellchecker_name}_advanced_metrics_with_histograms.png")
    plt.savefig(output_path)
    plt.show()

# Execute the plot function
spellchecker_name = "pyenchant"
plot_advanced_metrics_with_histograms(df, spellchecker_name)
