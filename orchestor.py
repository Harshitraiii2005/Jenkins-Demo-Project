from prefect import flow, task, get_run_logger

from proj1.ingestion import load_data
from preprocessing import preprocess_data
from training import train_model
from evaluation import evaluate_model


@task(name="Data Ingestion")
def ingest_task(path: str):
    print("starting the data ingestion")
    return load_data(path)


@task(name="Preprocessing")
def preprocess_task(df):
    return preprocess_data(df)
    logging = get_run_logger()
    logging.info("Data preprocessing completed")
    logging.debug(f"Preprocessed DataFrame head:\n{df_processed.head()}")


@task(name="Training")
def train_task(df):
    return train_model(df)


@task(name="Evaluation")
def evaluate_task(pipe, X_test, y_test):
    return evaluate_model(pipe, X_test, y_test)


@flow(name="ML Pipeline Orchestrator")
def ml_pipeline_flow():
    df = ingest_task("priceoye_laptops_version_2.csv")

    df_processed = preprocess_task(df)

    pipe, X_test, y_test = train_task(df_processed)

    metrics = evaluate_task(pipe, X_test, y_test)

    print("Pipeline completed successfully")
    print("Metrics:", metrics)



ml_pipeline_flow()
