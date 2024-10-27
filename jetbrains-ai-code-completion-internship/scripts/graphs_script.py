import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def graph_metrics(inputdir, outputdir):
    df = pd.read_csv(inputdir)

    sns.set(style="whitegrid", palette="muted")

    fig, axes = plt.subplots(2, 2, figsize=(16, 10))

    # 1. Violin + Strip Plot for each metric
    metrics = ['exact_match', 'bleu', 'chrf', 'edit_distance']

    for i, metric in enumerate(metrics):
        ax = axes[i // 2, i % 2]
        sns.violinplot(x=metric, data=df, ax=ax, inner=None, color='lightblue')
        sns.stripplot(x=metric, data=df, ax=ax, color='black', size=3, jitter=True)
        ax.set_title(f'Distribution of {metric.capitalize()}')
        ax.set_xlabel(f'{metric.capitalize()} Score')
        ax.set_ylabel('Density')

    plt.savefig(outputdir)
    plt.show()
