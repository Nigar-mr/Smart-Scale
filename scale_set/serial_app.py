from .models import *
from .views import *
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import os
from pandas.plotting import register_matplotlib_converters
# InfoField = None
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def analyze_data(cow_id, object_by_date_analyz):
    try:
        df = pd.DataFrame.from_dict([x['analysis_data'] for x in object_by_date_analyz], orient='columns')
        print('DataFrame: ', df)
        # df = [{'date': datetime.today(), 'weight': 100.2}, {'date': datetime(2019, 9, 17), 'weight': 83.2}, {'date': datetime(2019, 9, 15), 'weight': 83.2}, \
        # {'date': datetime(2019, 9, 16), 'weight': 100.2}]
        date = df['publish_date'].tolist()
        date = [datetime.strptime(x[:10], '%Y-%m-%d') for x in date]

        weight = df['weight'].tolist()
        print(weight)
        print(date)
        plt.scatter(pd.to_datetime(date), weight)
        plt.title('Zaman-Çəki asılılığı')
        plt.xticks(rotation=90)
        plt.xlabel('Tarix')
        plt.ylabel('Çəki (kg)')
        plt.show()
        graph_name = str(cow_id) + '.png'
        my_path = os.path.dirname(
            __file__)  # Figures out the absolute path for you in case your working directory moves around.
        full_path = os.path.join(my_path, 'graphs', graph_name)
        plt.savefig(full_path)
        print(df[['weight', 'publish_date']])
        maxWeight, maxWeightDate = df[['weight', 'publish_date']].max()
        minWeight, minWeightDate = df[['weight', 'publish_date']].min()
        meanWeight = df['weight'].mean()
        data = {'pic': full_path, 'max_weight': maxWeight, 'max_weight_date': maxWeightDate, \
                'min_weight': minWeight, 'min_weight_date': minWeightDate, 'mean_weight': meanWeight}

        print('infunctio', data)
        return data

    except Exception as er:
        print('data not found', er)
