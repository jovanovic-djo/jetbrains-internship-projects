from nltk.translate.bleu_score import sentence_bleu
from sklearn.metrics import accuracy_score
from nltk.metrics.distance import edit_distance

def compute_metrics(df):
    bleu_scores = []
    edit_distances = []
    
    for _, row in df.iterrows():
        reference = row['middle'].split()
        prediction = row['completion'].split()
        bleu_scores.append(sentence_bleu([reference], prediction))
        edit_distances.append(edit_distance(row['middle'], row['completion']))
    
    df['bleu'] = bleu_scores
    df['edit_distance'] = edit_distances
    df.to_csv('metrics_results.csv', index=False)