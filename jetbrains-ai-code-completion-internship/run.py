from scripts.split_script import split_code_examples
from scripts.metrics_script import compute_metrics
from scripts.graphs_script import graph_metrics
from models.model import generate_completions

def main():
    split_input_csv = 'jetbrains-ai-code-completion-internship/data/code_examples.csv'
    split_output_csv = 'jetbrains-ai-code-completion-internship/data/split_code_examples.csv'
    split_code_examples(split_input_csv, split_output_csv)

    completion_input_csv = split_output_csv
    completion_output_csv = 'jetbrains-ai-code-completion-internship/data/completion_results.csv'
    generate_completions(completion_input_csv, completion_output_csv)

    metrics_input_csv = completion_output_csv
    metrics_output_csv = 'jetbrains-ai-code-completion-internship/data/metrics_results.csv'
    compute_metrics(metrics_input_csv, metrics_output_csv)

    graph_input_csv = metrics_output_csv
    graph_output_png = 'jetbrains-ai-code-completion-internship/imgs/metrics_plot.png'
    graph_metrics(graph_input_csv, graph_output_png)

if __name__ == "__main__":
    main()
