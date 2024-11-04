import os
from scripts.resultgeneration import libraries_results_generation as lrg
from scripts.resultgeneration import result_graph_generation as rgg

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

    rgg.plot_metrics(output_path + pyspellchecker_file, pyspellchecker_file[:-4])
    rgg.plot_metrics(output_path + textblob_file, textblob_file[:-4])
    rgg.plot_metrics(output_path + symspell_file, symspell_file[:-4])
    rgg.plot_metrics(output_path + pyenchant_file, pyenchant_file[:-4])
        

if __name__ == "__main__":
    main()

