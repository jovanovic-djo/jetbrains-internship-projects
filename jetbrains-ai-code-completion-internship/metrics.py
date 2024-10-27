import pandas as pd
from transformers import AutoTokenizer, AutoModelForCausalLM
from sklearn.metrics import accuracy_score
from nltk.translate.bleu_score import sentence_bleu
from nltk.metrics.distance import edit_distance

def compute_exact_match(df):
    df['exact_match'] = (df['middle'] == df['completion']).astype(int)
    exact_match_score = accuracy_score(df['middle'], df['completion'])
    print(f"Exact Match Accuracy: {exact_match_score}")
    return df

def compute_edit_distance(df):
    edit_distances = [edit_distance(row['middle'], row['completion']) for _, row in df.iterrows()]
    df['edit_distance'] = edit_distances
    print(f"Average Edit Distance: {sum(edit_distances) / len(edit_distances)}")
    return df

def compute_bleu_scores(df):
    bleu_scores = [sentence_bleu([row['middle'].split()], row['completion'].split()) for _, row in df.iterrows()]
    df['bleu'] = bleu_scores
    print(f"Average BLEU Score: {sum(bleu_scores) / len(bleu_scores)}")
    return df

def compute_token_level_accuracy(df):
    token_accuracy_scores = []
    for _, row in df.iterrows():
        reference_tokens = row['middle'].split()
        predicted_tokens = row['completion'].split()
        correct_tokens = sum(1 for i, token in enumerate(predicted_tokens) if i < len(reference_tokens) and token == reference_tokens[i])
        token_accuracy_scores.append(correct_tokens / len(reference_tokens) if reference_tokens else 0)
    df['token_accuracy'] = token_accuracy_scores
    print(f"Average Token-Level Accuracy: {sum(token_accuracy_scores) / len(token_accuracy_scores)}")
    return df


def main():
    df = pd.read_csv('jetbrains-ai-code-completion-internship\data\completion_results.csv')

    # Compute metrics
    df = compute_exact_match(df)
    df = compute_edit_distance(df)
    df = compute_bleu_scores(df)
    df = compute_token_level_accuracy(df)

    # Save results with metrics
    df.to_csv('jetbrains-ai-code-completion-internship\data\metrics_results.csv', index=False)

if __name__ == "__main__":
    main()
