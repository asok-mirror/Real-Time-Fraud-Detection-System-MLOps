from typing import Optional
import typer
import warnings
import sys, os

# sys.path.insert(0, '/home/asok/toolbox/mlops/End_To_End_Model_Deployment_MLOps/core')
print(sys.path)  # TBU
# sys.path.insert(0, "C:\\toolbox\\ML OPS\\End_To_End_Model_Deployment_MLOps\\core")  # TBU
# print(sys.path)  # TBU
from core import data, optimize, train, serve, predict as predict_transaction
from core.config import logger

# Ignore warning
warnings.filterwarnings("ignore")

# Initialize typer app
app = typer.Typer()


@app.command()
def get_data() -> None:
    """download and persist the data"""
    data.download_data()
    logger.info("Cli: Dataset downloaded!")


@app.command()
def optimize() -> None:
    """find the best model hyperparameter"""
    return optimize.optimize_model()
    logger.info("Cli: Hyperparameter tuning is performed")


@app.command()
def train() -> None:
    """train the model"""
    train.train_model()
    logger.info("Cli: Model training is completed")


@app.command()
def serve() -> None:
    """serve the model"""
    serve.promote_model_to_serving()
    logger.info("Cli: model is ready for serving")


@app.command()
def predict(
    time: Optional[float] = 34681.0,
    v1: Optional[float] = -0.231080,
    v2: Optional[float] = -3.201858,
    v3: Optional[float] = -0.674366,
    v4: Optional[float] = -0.976167,
    v5: Optional[float] = -1.302294,
    amount: Optional[float] = 810.00,
) -> str:
    """predit the outcome

    Args:
        time (Optional[float], optional): time. Defaults to 34681.0.
        v1 (Optional[float], optional): PCA reduced V1. Defaults to -0.231080.
        v2 (Optional[float], optional): PCA reduced V2. Defaults to -3.201858.
        v3 (Optional[float], optional): PCA reduced V3. Defaults to -0.674366.
        v4 (Optional[float], optional): PCA reduced V4. Defaults to -0.976167.
        v5 (Optional[float], optional): PCA reduced V5. Defaults to -1.302294.
        amount (Optional[float], optional): amount. Defaults to 810.00.

    Returns:
        str: Predited value 0 if not a fradulant transaction or 1 if its a fradulant transaction
    """

    data = [[time, v1, v2, v3, v4, v5, amount]]
    return predict_transaction.predict(data)


if __name__ == "__main__":
    app()
