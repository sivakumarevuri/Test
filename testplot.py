import os.path
import pandas as pd
import matplotlib.pyplot as plt


def test_plot(path):
    location = os.path.join(path, 'student_data.csv')
    data = pd.read_csv(location)
    data.plot(x='Student_id', y='Percentage')

    plt.savefig(os.path.join(path, 'graph.png'))
    plt.show()


#test_plot('/home/lucifer/Desktop/siva/data/')


