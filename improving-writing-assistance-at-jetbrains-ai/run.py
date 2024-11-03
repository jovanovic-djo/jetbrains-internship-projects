import os
from scripts.resultgeneration import libraries_results_generation as lrg

def main():

    input_path = "improving-writing-assistance-at-jetbrains-ai\\data\\test.csv"
    output_path = "improving-writing-assistance-at-jetbrains-ai\\results\\libraries results\\"

    merged_file = "merged_libraries_results.csv"
    pyspellchecker_file = "pyspellchecker.csv"
    textblob_file = "textblob.csv"
    symspell_file = "symspell.csv"
    pyenchant_file = "pyenchant.csv"

    lrg.generate_merged_libraries_results(input_path, os.path.join(output_path, merged_file))
    lrg.generate_pyspellchecker_results(input_path, os.path.join(output_path, pyspellchecker_file))
    lrg.generate_pyenchant_results(input_path, os.path.join(output_path, pyenchant_file))
    lrg.generate_symspell_results(input_path, os.path.join(output_path, symspell_file))
    lrg.generate_textblob_results(input_path, os.path.join(output_path, textblob_file))
        

if __name__ == "__main__":
    main()

