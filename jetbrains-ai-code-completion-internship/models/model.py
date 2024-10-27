import pandas as pd
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained('bigcode/tiny_starcoder_py')
model = AutoModelForCausalLM.from_pretrained('bigcode/tiny_starcoder_py')

def get_completion(prefix, max_new_tokens=50):
    inputs = tokenizer(prefix, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=max_new_tokens)
    completion = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return completion

def generate_completions(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    df['completion'] = df['prefix'].apply(lambda x: get_completion(x))
    df.to_csv(output_csv, index=False)

    return df
