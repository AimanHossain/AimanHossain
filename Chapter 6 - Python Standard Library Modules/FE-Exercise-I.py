import matplotlib.pyplot as plt
import numpy as np

def draw_grouped_bar_chart():
    categories = ['Game', 'Commercials', "Won't watch"]
    male_data = [279, 81, 132]
    female_data = [200, 156, 160]

    bar_width = 0.35
    index = np.arange(len(categories))

    fig, ax = plt.subplots(figsize=(8, 6))

    bar1 = ax.bar(index, male_data, bar_width, label='Male', color='blue')
    bar2 = ax.bar(index + bar_width, female_data, bar_width, label='Female', color='orange')

    ax.set_xlabel('Categories')
    ax.set_ylabel('Number of People')
    ax.set_title('Super Bowl Watching Plans by Gender')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(categories)
    ax.legend()

    def add_labels(bars):
        for bar in bars:
            height = bar.get_height()
            ax.annotate('{}'.format(height),
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')

    add_labels(bar1)
    add_labels(bar2)

    plt.show()

if __name__ == "__main__":
    draw_grouped_bar_chart()
