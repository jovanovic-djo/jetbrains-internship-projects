import os
import sys
from scripts import metrics
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts', 'result-generation'))
from scripts.resultgeneration import libraries_results_generation as lrg



input_path = "improving-writing-assistance-at-jetbrains-ai\\data\\test.csv"
output_path = "improving-writing-assistance-at-jetbrains-ai\\results\\libraries results\\"

merged_file = "merged_libraries_results.csv"
pyspellchecker_file = "pyspellchecker.csv"
textblob_file = "textblob.csv"
symspell_file = "symspell.csv"
pyenchant_file = "pyenchant.csv"

def main():
    try:
        lrg.generate_merged_libraries_results(input_path, os.path.join(output_path, merged_file))
        lrg.generate_pyspellchecker_results(input_path, os.path.join(output_path, pyspellchecker_file))
        lrg.generate_pyenchant_results(input_path, os.path.join(output_path, pyenchant_file))
        lrg.generate_symspell_results(input_path, os.path.join(output_path, symspell_file))
        lrg.generate_textblob_results(input_path, os.path.join(output_path, textblob_file))
        
        print("All results generated successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

