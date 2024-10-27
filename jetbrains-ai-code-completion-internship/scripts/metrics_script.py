import pandas as pd
from nltk.translate.bleu_score import sentence_bleu
from nltk.metrics.distance import edit_distance
import sacrebleu

def compute_exact_match(reference, prediction):
    return int(reference.strip() == prediction.strip())

def compute_bleu(reference, prediction):
    reference_tokens = reference.split()
    prediction_tokens = prediction.split()
    return sentence_bleu([reference_tokens], prediction_tokens)

def compute_chrf(reference, prediction):
    chrf_scorer = sacrebleu.CHRF()
    return chrf_scorer.sentence_score(prediction, [reference]).score

def compute_edit_distance(reference, prediction):
    return edit_distance(reference, prediction)

def compute_metrics(df):
    exact_matches = []
    bleu_scores = []
    chrf_scores = []
    edit_distances = []

    for _, row in df.iterrows():
        reference = row['middle']
        prediction = row['completion']
        
        exact_matches.append(compute_exact_match(reference, prediction))
        bleu_scores.append(compute_bleu(reference, prediction))
        chrf_scores.append(compute_chrf(reference, prediction))
        edit_distances.append(compute_edit_distance(reference, prediction))
    
    df['exact_match'] = exact_matches
    df['bleu'] = bleu_scores
    df['chrf'] = chrf_scores
    df['edit_distance'] = edit_distances
    
    df.to_csv('jetbrains-ai-code-completion-internship\data\metrics_results.csv', index=False)
    
    print(df)
    return df

df = pd.read_csv('jetbrains-ai-code-completion-internship\data\completion_results.csv')

df = compute_metrics(df)

print(df)
