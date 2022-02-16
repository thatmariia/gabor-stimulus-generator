import seaborn as sns
import matplotlib.pyplot as plt

def plot_heatmap(im):
    fig, ax = plt.subplots(figsize=(300, 300))
    sns.heatmap(
        im,
        annot=False,
        vmin=0,
        vmax=1,
        cmap="spring",
        square=True,
        cbar=False,
        xticklabels=False,
        yticklabels=False,
        ax=ax
    )
    fig.savefig('img.png')