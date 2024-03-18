import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from load_model import load_model

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

df = pd.read_csv('resources/advertising.csv')

X = df[['TV', 'radio', 'newspaper']].values
y = df['sales'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = MinMaxScaler()

scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

model = load_model()

model.fit(x=X_train, y=y_train, epochs=500)

predictions = model.predict(X_test)
predictions = pd.Series(predictions.reshape(60))

predictions_df = pd.DataFrame(y_test)
predictions_df = pd.concat([predictions_df, predictions], axis=1)
predictions_df.columns = ['Test True Y', 'Model Prediction']

sns.scatterplot(x='Test True Y', y='Model Prediction', data=predictions_df)

print()
print('Mean Absolute Error (MAE):', mean_absolute_error(predictions_df['Test True Y'], predictions_df['Model Prediction']))
print('Mean Squared Error (MSE):', mean_squared_error(predictions_df['Test True Y'], predictions_df['Model Prediction']))
print('Root Mean Squared Error (RMSE):', mean_squared_error(predictions_df['Test True Y'], predictions_df['Model Prediction'])**0.5)
print()
print(df.describe())
print()

model.save('storage/advertising-model.keras')

plt.show()
