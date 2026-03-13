import matplotlib.pyplot as plt

def credibility_chart(score):

    labels = ["Credibility", "Remaining"]
    values = [score, 100-score]

    fig, ax = plt.subplots()

    ax.pie(values, labels=labels, autopct="%1.1f%%")

    ax.set_title("Research Credibility Score")

    return fig