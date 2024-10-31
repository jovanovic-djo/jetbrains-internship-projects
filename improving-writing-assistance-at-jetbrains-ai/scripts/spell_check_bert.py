import os
import pandas as pd
import torch
from torch.utils.data import Dataset
from transformers import BertTokenizer, BertForMaskedLM, Trainer, TrainingArguments, DataCollatorForLanguageModeling

class SpellCheckDataset(Dataset):
    def __init__(self, dataframe, tokenizer, max_length=128):
        self.data = dataframe
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        incorrect_text = self.data.loc[idx, 'incorrect']
        correct_text = self.data.loc[idx, 'correct']
        
        inputs = self.tokenizer(incorrect_text, max_length=self.max_length, padding="max_length", truncation=True, return_tensors="pt")
        labels = self.tokenizer(correct_text, max_length=self.max_length, padding="max_length", truncation=True, return_tensors="pt")['input_ids']
        
        inputs['labels'] = labels.squeeze()
        return {key: val.squeeze() for key, val in inputs.items()}

def train_spellchecker(input_path):
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model = BertForMaskedLM.from_pretrained("bert-base-uncased")
    
    df = pd.read_csv(input_path, delimiter=",")
    
    # Check columns
    expected_columns = {'incorrect', 'correct'}
    actual_columns = set(df.columns)
    if not expected_columns.issubset(actual_columns):
        raise ValueError(f"CSV is missing required columns. Expected columns: {expected_columns}. Found columns: {actual_columns}")

    dataset = SpellCheckDataset(df, tokenizer)
    
    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=True, mlm_probability=0.15)
    
    training_args = TrainingArguments(
        output_dir="./spellcheck_model",
        num_train_epochs=3,
        per_device_train_batch_size=8,
        save_steps=10_000,
        save_total_limit=2,
    )
    
    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=dataset
    )
    
    trainer.train()
    model.save_pretrained("improving-writing-assistance-at-jetbrains-ai/spellcheck_model")
    tokenizer.save_pretrained("improving-writing-assistance-at-jetbrains-ai/spellcheck_model")


def spell_check_with_bert(sentence):
    tokenizer = BertTokenizer.from_pretrained("improving-writing-assistance-at-jetbrains-ai/spellcheck_model")
    model = BertForMaskedLM.from_pretrained("improving-writing-assistance-at-jetbrains-ai/spellcheck_model")
    
    inputs = tokenizer(sentence, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    
    predictions = torch.argmax(outputs.logits, dim=-1)
    corrected_sentence = tokenizer.decode(predictions[0], skip_special_tokens=True)
    
    return corrected_sentence

if __name__ == "__main__":
    input_path = "improving-writing-assistance-at-jetbrains-ai\\data\\test.csv"

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    train_spellchecker(input_path)
