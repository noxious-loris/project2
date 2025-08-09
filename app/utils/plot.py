import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64


def plot_scatter(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="Rank", y="Peak", data=df)
    sns.regplot(x="Rank", y="Peak", data=df, scatter=False, color="red", linestyle="dotted")
    plt.xlabel("Rank")
    plt.ylabel("Peak")
    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches='tight')
    plt.close()
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()
