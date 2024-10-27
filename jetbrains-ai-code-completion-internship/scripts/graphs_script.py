import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import gridspec

def graph_metrics(inputdir, outputdir):
    df = pd.read_csv(inputdir)

    sns.set_theme(style="whitegrid", palette="muted")
    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
    
    fig = plt.figure(figsize=(14, 8))
    gs = gridspec.GridSpec(2, 2, width_ratios=[1, 1.5], height_ratios=[2, 1])

    metrics = ['exact_match', 'bleu', 'chrf', 'edit_distance']

    for i, metric in enumerate(metrics):
        ax = fig.add_subplot(gs[i // 2, i % 2])
        
        color = colors[i]
        sns.violinplot(x=metric, data=df, ax=ax, inner=None, color=color, alpha=0.7)
        sns.stripplot(x=metric, data=df, ax=ax, color='black', size=3, jitter=True, linewidth=0.5)
        
        ax.set_title(f'Distribution of {metric.capitalize()}', fontsize=14, fontweight='bold')
        ax.set_xlabel(f'{metric.capitalize()} Score', fontsize=12)
        ax.set_ylabel('Density', fontsize=12)
        
        ax.grid(True, linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.savefig(outputdir)
    plt.show()