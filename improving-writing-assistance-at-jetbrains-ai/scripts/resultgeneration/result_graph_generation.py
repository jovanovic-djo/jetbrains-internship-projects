import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


output_path = "improving-writing-assistance-at-jetbrains-ai\\results\\libraries results\\"

merged_file = "merged_libraries_results.csv"
pyspellchecker_file = "pyspellchecker.csv"
textblob_file = "textblob.csv"
symspell_file = "symspell.csv"
pyenchant_file = "pyenchant.csv"


def plot_metrics(data_path, spellchecker_name):
    output_folder = "improving-writing-assistance-at-jetbrains-ai\\results\\graph results"
    df = pd.read_csv(data_path)

    df.columns = df.columns.str.strip()

    metrics = ["Levenshtein Distance", "Accuracy", "Exact Match"]
    df[metrics] = df[metrics].astype(float)

    sns.set_theme(style="whitegrid", palette="muted", font_scale=1.1)
    os.makedirs(output_folder, exist_ok=True)

    type_colors = {
        "sentence": "#4C72B0",
        "word": "#55A868",
        "name": "#C44E52",
        "code": "#8172B2",
        "number": "#CCB974"
    }

    df['Exact Match Status'] = df['Exact Match'].apply(lambda x: 'Exact Match' if x == 1 else 'Not Exact Match')
    fig, axes = plt.subplots(2, 3, figsize=(14, 8), gridspec_kw={'height_ratios': [1, 1.5]})
    fig.suptitle(f"{spellchecker_name} - Metric Analysis and Distribution by Type of Data", fontsize=14)

    sns.boxplot(data=df, y="Accuracy", ax=axes[0, 0], color="#55A868", linewidth=1.5, saturation=0.75)
    axes[0, 0].set_title("Accuracy")
    axes[0, 0].set_ylabel("Score")
    axes[0, 0].spines["top"].set_visible(False)
    axes[0, 0].spines["right"].set_visible(False)

    sns.boxplot(data=df, y="Levenshtein Distance", ax=axes[0, 1], color="#4C72B0", linewidth=1.5, saturation=0.75)
    axes[0, 1].set_title("Levenshtein Distance")
    axes[0, 1].set_ylabel("Score")
    axes[0, 1].spines["top"].set_visible(False)
    axes[0, 1].spines["right"].set_visible(False)

    axes[0, 2].axis('off')

    for i, metric in enumerate(metrics):
        if 'Type' in df.columns:
            if metric == "Exact Match":
                sns.histplot(
                    data=df,
                    x="Exact Match Status",
                    hue="Type",
                    multiple="stack",
                    palette=type_colors,
                    bins=2,
                    ax=axes[1, i],
                    edgecolor="black"
                )
            else:
                sns.histplot(
                    data=df,
                    x=metric,
                    hue="Type",
                    multiple="stack",
                    palette=type_colors,
                    bins=15,
                    kde=True,
                    ax=axes[1, i],
                    edgecolor="black"
                )
                
            axes[1, i].set_title(f"Distribution of {metric} by Type")
            axes[1, i].set_xlabel("Score" if metric != "Exact Match" else "Exact Match Status")
            axes[1, i].set_ylabel("Frequency")
        else:
            print(f"'Type' column not found in DataFrame. Please check your data.")


    plt.tight_layout(rect=[0, 0, 1, 0.96])
    output_path = os.path.join(output_folder, f"{spellchecker_name}_metrics_graph.png")
    plt.savefig(output_path)

