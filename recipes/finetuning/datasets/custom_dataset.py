import datasets

def get_custom_dataset(dataset_config, tokenizer, split):
    dataset = datasets.load_dataset("revnav25/invoicesummary", split=split)
    
    return dataset

