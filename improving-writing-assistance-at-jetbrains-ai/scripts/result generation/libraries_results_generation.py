import os
import pandas as pd
import metrics
import spell_check_libraries as scl


def generate_merged_libraries_results(input_path, output_path):

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path, delimiter=";")
    results = []

    for index, row in df.iterrows():
        incorrect = row['incorrect']
        correct = row['correct']

        pyspell_result = scl.pyspellchecker_correct(incorrect)
        textblob_result = scl.textblob_correct(incorrect)
        symspell_result = scl.symspell_correct(incorrect)
        enchant_result = scl.enchant_correct(incorrect)

        for spell_checker_name, result in [
            ("PySpellChecker", pyspell_result),
            ("TextBlob", textblob_result),
            ("SymSpell", symspell_result),
            ("PyEnchat", enchant_result)]:
            lev_distance = metrics.calculate_levenshtein(result, correct)
            accuracy = metrics.calculate_accuracy(result, correct)
            exact_match = metrics.calculate_exact_match(result, correct)


            results.append({
                "Index": index,
                "SpellChecker": spell_checker_name,
                "Original": incorrect,
                "Corrected": correct,
                "Predicted": result,
                "Levenshtein Distance": lev_distance,
                "Accuracy": accuracy,
                "Exact Match": exact_match
            })

    results_df = pd.DataFrame(results)
    results_df.to_csv(output_path, index=False)
