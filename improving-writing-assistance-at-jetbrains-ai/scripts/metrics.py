from nltk.metrics.distance import edit_distance

def calculate_levenshtein(incorrect_sentences, correct_sentences):
    distances = [edit_distance(incorrect, correct) for incorrect, correct in zip(incorrect_sentences, correct_sentences)]
    avg_distance = sum(distances) / len(distances)
    return avg_distance

def calculate_accuracy(predicted_sentences, correct_sentences):
    correct_matches = sum([1 for predicted, correct in zip(predicted_sentences, correct_sentences) if predicted == correct])
    accuracy = correct_matches / len(correct_sentences) * 100
    return accuracy