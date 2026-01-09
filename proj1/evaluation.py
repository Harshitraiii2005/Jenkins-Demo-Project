from sklearn.metrics import mean_absolute_error, r2_score

def evaluate_model(pipe, X_test, y_test):
    y_pred = pipe.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("MAE:", mae)
    print("R2 :", r2)

    return {"MAE": mae, "R2": r2}
