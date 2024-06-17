import os
import pickle

import mlflow
from mlflow.tracking import mlflowClient

from flask import Flask, request, jsonify

# MLFLOW_TRACKING_URI = 'http://127.0.0.1:5000'
# MLFLOW_TRACKING_URI = "http://ec2-54-145-3-23.compute-1.amazonaws.com:500" # fill in with the public DNS of the EC2 instance，头部要加上'http://'，尾部还要加上端口号':5000'
RUN_ID = 'beb964a81ccc4fcfae5064b8a5bba31a'

# mflow.set_tracking_uri(MLFLOW_TRACKING_URI)
# client = MlflowClient(tracking_uri=MLFLOW_TRACKING_URI)

# path = client.download_artifacts(run_id=RUN_ID, path='dict_vectorizer.bin')
# print(f'downloading the dict vectorizer to {path}')

logged_model_path = 's3://mlops-module4-mlflow-gan/3/beb964a81ccc4fcfae5064b8a5bba31a/artifacts/model'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model_path)


# RUN_ID = os.getenv('RUN_ID')

# logged_model = f's3://mlflow-models-alexey/1/{RUN_ID}/artifacts/model'
# logged_model = f'runs:/{RUN_ID}/model'
# model = mlflow.pyfunc.load_model(logged_model)


def prepare_features(ride):
    features = {}
    features['PU_DO'] = '%s_%s' % (ride['PULocationID'], ride['DOLocationID'])
    features['trip_distance'] = ride['trip_distance']
    return features


def predict(features,model=loaded_model):
    preds = model.predict(features)
    return float(preds[0])


app = Flask('duration-prediction')


@app.route('/predict', methods=['POST'])
def predict_endpoint():
    ride = request.get_json()

    features = prepare_features(ride)
    pred = predict(features)

    result = {
        'duration': pred,
        'model_version': RUN_ID
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)