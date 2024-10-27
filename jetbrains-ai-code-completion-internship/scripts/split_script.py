import pandas as pd
import random

def split_method(code):
    lines = code.splitlines()
    if len(lines) < 3:
        return None

    cursor = random.randint(1, len(lines) - 2)
    prefix = '\n'.join(lines[:cursor])
    middle = lines[cursor]
    suffix = '\n'.join(lines[cursor + 1:])
    
    return prefix, middle, suffix

def split_code_examples(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    df['prefix'], df['middle'], df['suffix'] = zip(*df['code examples'].apply(split_method))
    df.to_csv(output_csv, index=False)

    return df
