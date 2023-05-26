import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


def predict_prep(ctrl_data):
    estate_valuation = pd.read_csv('data/weather_data_for_prediction.csv')

    corr_matrix = estate_valuation.corr()
    sns.heatmap(corr_matrix, annot=True)
    plt.savefig('data/corr_matrix.png')

    train, test = train_test_split(estate_valuation, test_size=0.25, random_state=42)

    cols = ['time', 'temperature_2m', 'relativehumidity_2m', 'surface_pressure',
            'cloudcover', 'direct_radiation', 'diffuse_radiation', 'windspeed_10m']

    train_x = np.array(train[cols])
    test_x = np.array(test[cols])

    train_y = np.array(train['precipitation'])
    test_y = np.array(test['precipitation'])

    lr = LinearRegression()
    model = lr.fit(train_x, train_y)
    prediction = lr.predict(test_x)

    dist = mean_squared_error(test_y, prediction)
    print("Середньоквадратична помилка (MSE) між прогнозованою та дійсною кількістю опадів. "
          "Чим ця величина менше, тим краща модель." + str(dist))

    r2 = r2_score(test_y, prediction)
    print("Розрахунок коефіцієнту детермінації R^2 для оцінки якості прогнозів моделі. Чим більше ця величина, "
          "тим краще модель." + str(f'R^2 score: {r2:.2f}'))

    x, y = zip(*sorted(zip(prediction, test_y)))
    plt.clf()
    plt.plot(x, y)
    plt.plot([0, 2], [0, 2], '--r')
    plt.xlabel('Prediction')
    plt.ylabel('Real values')

    plt.savefig('data/graph.png')

    new_data = pd.DataFrame(
        {"time": [ctrl_data[0]], "temperature_2m": [ctrl_data[1]],
         "relativehumidity_2m": [ctrl_data[2]],
         "surface_pressure": [ctrl_data[3]], "cloudcover": [ctrl_data[4]],
         "direct_radiation": [ctrl_data[5]],
         "diffuse_radiation": [ctrl_data[6]], "windspeed_10m": [ctrl_data[7]]})

    return model.predict(new_data)

