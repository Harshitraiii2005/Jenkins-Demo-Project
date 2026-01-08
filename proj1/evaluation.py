from sklearn.metrics import mean_absolute_error, r2_score

y_pred = pipe.predict(X_test)

print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2 :", r2_score(y_test, y_pred))
