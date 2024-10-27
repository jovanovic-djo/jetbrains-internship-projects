import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('jetbrains-ai-code-completion-internship\data\metrics_results.csv')

sns.set(style="whitegrid", palette="muted")

plt.figure(figsize=(10, 6))
metrics_means = df[['exact_match', 'bleu', 'chrf', 'edit_distance']].mean()
sns.barplot(x=metrics_means.index, y=metrics_means.values, palette='Blues_d')
plt.title('Average Values for Each Metric', fontsize=16)
plt.ylabel('Score', fontsize=12)
plt.xlabel('Metrics', fontsize=12)
plt.tight_layout()
plt.savefig('mean_metrics_barplot.png')
plt.show()

plt.figure(figsize=(12, 6))
df_melted = df.melt(value_vars=['exact_match', 'bleu', 'chrf', 'edit_distance'], var_name='Metric', value_name='Value')
sns.boxplot(x='Metric', y='Value', data=df_melted, palette='Set3')
plt.title('Distribution of Metrics with Box Plot', fontsize=16)
plt.ylabel('Value', fontsize=12)
plt.xlabel('Metrics', fontsize=12)
plt.tight_layout()
plt.savefig('metrics_boxplot.png')
plt.show()

plt.figure(figsize=(8, 6))
corr_matrix = df[['exact_match', 'bleu', 'chrf', 'edit_distance']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, linewidths=0.5)
plt.title('Correlation Heatmap of Metrics', fontsize=16)
plt.tight_layout()
plt.savefig('metrics_correlation_heatmap.png')
plt.show()
