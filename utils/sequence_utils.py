import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_token_count(column, tokenizer):
    token_lens = []
    for txt in column:
      tokens = tokenizer.encode(txt, max_length=512)
      token_lens.append(len(tokens))
    sns.distplot(token_lens)
    plt.xlim([0, 500])
    plt.xlabel('Token count')

def filter_string(df, name_col, max):
  return df[df[name_col].astype(str).apply(lambda x: len(x.split())) <= max]






