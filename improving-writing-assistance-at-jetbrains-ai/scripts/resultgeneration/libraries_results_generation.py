import os
import pandas as pd
from .. import metrics
from .. import spell_check_libraries as scl


def generate_merged_libraries_results(input_path, output_path):

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path, delimiter=",")
    results = []

    for index, row in df.iterrows():
        incorrect = row[1]
        correct = row[0]

        pyspell_result = scl.pyspellchecker_correct(incorrect)
        textblob_result = scl.textblob_correct(incorrect)
        symspell_result = scl.symspell_correct(incorrect)
        pyenchant_result = scl.pyenchant_correct(incorrect)

        for library_name, result in [
            ("PySpellChecker", pyspell_result),
            ("TextBlob", textblob_result),
            ("SymSpell", symspell_result),
            ("PyEnchant", pyenchant_result)]:
            levenshtein_distance = metrics.calculate_levenshtein(result, correct)
            accuracy = metrics.calculate_accuracy(result, correct)
            exact_match = metrics.calculate_exact_match(result, correct)


            results.append({
                "Index": index,
                "SpellChecker": library_name,
                "Original": incorrect,
                "Corrected": correct,
                "Predicted": result,
                "Levenshtein Distance": levenshtein_distance,
                "Accuracy": accuracy,
                "Exact Match": exact_match
            })

    results_df = pd.DataFrame(results)
    results_df.to_csv(output_path, index=False)



def generate_pyspellchecker_results(input_path, output_path):

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path, delimiter=",")
    results = []

    for index, row in df.iterrows():
        incorrect = row['incorrect']
        correct = row['correct']

        library_result = scl.pyspellchecker_correct(incorrect)

        levenshtein_distance = metrics.calculate_levenshtein(library_result, correct)
        accuracy = metrics.calculate_accuracy(library_result, correct)
        exact_match = metrics.calculate_exact_match(library_result, correct)

        results.append({
            "Index": index,
            "Original": incorrect,
            "Corrected": correct,
            "Predicted": library_result,
            "Levenshtein Distance": levenshtein_distance,
            "Accuracy": accuracy,
            "Exact Match": exact_match
        })
    
    results_df = pd.DataFrame(results)
    results_df.to_csv(output_path, index=False)



def generate_symspell_results(input_path, output_path):

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path, delimiter=",")
    results = []

    for index, row in df.iterrows():
        incorrect = row['incorrect']
        correct = row['correct']

        library_result = scl.symspell_correct(incorrect)

        levenshtein_distance = metrics.calculate_levenshtein(library_result, correct)
        accuracy = metrics.calculate_accuracy(library_result, correct)
        exact_match = metrics.calculate_exact_match(library_result, correct)

        results.append({
            "Index": index,
            "Original": incorrect,
            "Corrected": correct,
            "Predicted": library_result,
            "Levenshtein Distance": levenshtein_distance,
            "Accuracy": accuracy,
            "Exact Match": exact_match
        })
    
    results_df = pd.DataFrame(results)
    results_df.to_csv(output_path, index=False)



def generate_pyenchant_results(input_path, output_path):

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path, delimiter=",")
    results = []

    for index, row in df.iterrows():
        incorrect = row['incorrect']
        correct = row['correct']

        library_result = scl.pyenchant_correct(incorrect)

        levenshtein_distance = metrics.calculate_levenshtein(library_result, correct)
        accuracy = metrics.calculate_accuracy(library_result, correct)
        exact_match = metrics.calculate_exact_match(library_result, correct)

        results.append({
            "Index": index,
            "Original": incorrect,
            "Corrected": correct,
            "Predicted": library_result,
            "Levenshtein Distance": levenshtein_distance,
            "Accuracy": accuracy,
            "Exact Match": exact_match
        })
    
    results_df = pd.DataFrame(results)
    results_df.to_csv(output_path, index=False)



def generate_textblob_results(input_path, output_path):

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path, delimiter=",")
    results = []

    for index, row in df.iterrows():
        incorrect = row['incorrect']
        correct = row['correct']

        library_result = scl.textblob_correct(incorrect)

        levenshtein_distance = metrics.calculate_levenshtein(library_result, correct)
        accuracy = metrics.calculate_accuracy(library_result, correct)
        exact_match = metrics.calculate_exact_match(library_result, correct)

        results.append({
            "Index": index,
            "Original": incorrect,
            "Corrected": correct,
            "Predicted": library_result,
            "Levenshtein Distance": levenshtein_distance,
            "Accuracy": accuracy,
            "Exact Match": exact_match
        })
    
    results_df = pd.DataFrame(results)
    results_df.to_csv(output_path, index=False)

