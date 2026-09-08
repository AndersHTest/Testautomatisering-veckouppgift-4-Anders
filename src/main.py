import random
import matplotlib.pyplot as plt


def generate_list(size):
    lst = random.sample(range(1, 12501), size)
    return lst


def sort_comparison_chart():
    size = ("2500", "5000", "7500", "10000", "12500")
    function = {
        'Insertion sort': (101.61, 413.50, 937.14, 1651.38, 2576.65),
        'Merge sort': (4.44, 9.58, 14.86, 20.92, 26.45 ),

    }

    fig, ax = plt.subplots(layout='constrained')

    res = ax.grouped_bar(function, tick_labels=size, group_spacing=1)
    for container in res.bar_containers:
        ax.bar_label(container, padding=3)

    ax.set_ylabel('Time (ms)')
    ax.set_xlabel('Storlek lista')
    ax.legend(loc='upper left', frameon=False, ncols=2)
    ax.set_ylim(0,3000)
    plt.show()

if __name__ == '__main__':
    sort_comparison_chart()