from .models import *
import matplotlib.pyplot as plt


# InfoField = None

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


def analyze_data(cow_id,object_by_date_analyz):
    try:
        df = object_by_date_analyz.values()

        # df = [{'date': datetime.today(), 'weight': 100.2}, {'date': datetime(2019, 9, 17), 'weight': 83.2}, {'date': datetime(2019, 9, 15), 'weight': 83.2}, \
        # {'date': datetime(2019, 9, 16), 'weight': 100.2}]

        date = [x['publish_date'].strftime('%d/%m/%y') for x in df]
        weight = [x['weight'] for x in df]

        plt.scatter(date, weight)
        plt.title('Zaman-Çəki asılılığı')
        plt.xticks(rotation=90)
        plt.xlabel('Tarix')
        plt.ylabel('Çəki (kg)')

        graph_name = str(cow_id) + '.png'
        plt.savefig(graph_name)

        maxWeight, maxWeightDate = max(df, key=lambda x: x['weight']).values()
        minWeight, minWeightDate = min(df, key=lambda x: x['weight']).values()

        meanWeight = mean([x['weight'] for x in df])

        data = {'pic': graph_name, 'max_weight': maxWeight, 'max_weight_date': maxWeightDate, \
                'min_weight': minWeight, 'min_weight_date': minWeightDate, 'mean_weight': meanWeight}
        return data
    except Exception as er:
        print('data not found', er)



# print(analyze_data(0, 0, 0))