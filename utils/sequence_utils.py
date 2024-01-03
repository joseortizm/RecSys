import seaborn as sns
import matplotlib.pyplot as plt



def plot_token_count(column, tokenizer):
    token_lens = []
    for txt in column:
      tokens = tokenizer.encode(txt, max_length=512)
      token_lens.append(len(tokens))
    sns.distplot(token_lens)
    plt.xlim([0, 500])
    plt.xlabel('Token count')