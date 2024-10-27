import pandas as pd
import random

df = pd.read_csv('jetbrains-ai-code-completion-internship\data\code_examples.csv')

def split_method(code):
    lines = code.splitlines()
    if len(lines) < 3:
        return None

    cursor = random.randint(1, len(lines) - 2)
    prefix = '\n'.join(lines[:cursor])
    middle = lines[cursor]
    suffix = '\n'.join(lines[cursor + 1:])
    
    return prefix, middle, suffix

df['prefix'], df['middle'], df['suffix'] = zip(*df['code examples'].apply(split_method))
df.to_csv('jetbrains-ai-code-completion-internship/data/split_code_examples.csv', index=False)
