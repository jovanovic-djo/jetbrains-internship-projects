## Jetbrains AI Code Completion Internship

### Task
* Generate a dataset of code completion examples from one of your own repositories. You can take a few files from your personal projects.
Write a script that would split them into three parts simulating the user cursor position: the prefix - code before the cursor, the suffix - code after the cursor, and the middle - code that is missing and we assume should be typed next. You should aim to obtain between 20 and 50 examples.
* Take an open source code completion model, for example tiny_starcoder, or bigger starcoder or codellama variations if you prefer. Run the selected model on the examples from the previous point to obtain its completions.
* Review them manually and analyze the differences with actual missing code from the middle, try to assign labels according to your judgment of whether the proposed code is correct.
* Try to propose some automatic metrics for evaluating the quality of this model. Find which of the proposed metrics correlates better with your own judgment. Try computing at least exact match, chrf, and two or more metrics of your choice.
* Submit the code you wrote in the process, the resulting dataset with your annotations and computed metrics, and a report in any format describing your thought process, findings and learnings.

#### This project evaluates the performance of an open-source code completion model, Tiny StarCoder, in generating accurate code completions. By testing the model against custom dataset examples, we explore the model capability to predict and complete missing code segments. Key metrics and visualization techniques were used to assess the quality of completions, enabling a deeper understanding of the model strengths and potential improvements for real-world programming assistance purposes.

### Dataset Generation 
Dataset is constructed from Python code snippets of the personal repositories, which consists of:
* DSA solution of wide variety of string, array, binary search, linked list problems
* Several personal projects that are related to data science and machine learning field.

Word cloud graph representing occurence of certain words in dataset.

![wordcloud_output](https://github.com/user-attachments/assets/77e88aa6-2548-4ceb-8f27-45ff7afc1b02)


Splitting each code snippet into three parts:
* Prefix: Code before the cursor position.
* Middle: Intended code that should be completed.
* Suffix: Code following the cursor position.

For creating splitted examples, script `split_script.py` is written and executed. Mentioned script randomly splits stored code into 3 mentioned parts.

Splitted dataset is  `split_code_examples.csv`, allowed us to simulate a realistic code completion environment where the model had to predict the missing middle segment given the prefix.

### Model Selection and Prediction Generation
The open-source model Tiny StarCoder was selected for its balance of performance and lightweight architecture.
The model was loaded from Hugging Face and run on each prefix in the dataset, and predictions were saved in a new column, completion.
Outcome of our model execution is new dataset `completion_results.csv` on which we would use metrics.

### Metrics
* Exact Match: A strict measure of success, scoring 1 if the completion exactly matches the middle segment and 0 otherwise.
* BLEU Score: Evaluates the n-gram overlap between the model’s output and the expected completion, providing insight into the fluency and coherence of the generated code.
* CHRF Score: Measures character-level F-score, particularly useful in capturing similarity on a fine-grained level, even when there is a close match without exact n-gram overlap.
* Levenshtein Distance: Captures the number of single-character edits needed to match the predicted completion to the middle code, providing a sense of closeness and edit difficulty.

### Result generation
Purpose of `metrics_script.py` is to implement metrics on `completion_results.csv` dataset and to provide insights of our model accuracy. Mention script consists of several methods, where each method plays role in calculation of the metrics.

### Result Visualization
For results visualization, `graphs_script.py` is executed. It generates violin graph with final results for our model.
Outcome is graph which consists of 4 subplots where each subplot represents results of distinct metric.

![metrics_plot](https://github.com/user-attachments/assets/8e73cc4d-71b7-47db-bf44-b9a0060f7ae1)

### Conclusion
In most cases, predicted code makes sense, but it is not accurate nor usable as solution. As a result of bad performance, outcome for exact match is 0, we do not have any exact matches for our examples.

For potential enhancements, multiple datasets should be generated, consisted of different type of code examples. Important aspect would be to try mulitple models so we can calculate several results and compare them.





