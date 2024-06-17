import mlflow
import os

import pickle
from mlflow.tracking import MlflowClient

from flask import Flask, request, jsonify

os.environ["AWS_PROFILE"] = "GawainGan_95" # fill in with your AWS profile. More info: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup.html#setup-credentials

MLFLOW_TRACKING_URI = 'http://ec2-54-145-3-23.compute-1.amazonaws.com:5000'
RUN_ID = 'beb964a81ccc4fcfae5064b8a5bba31a'

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
print(f"tracking URI: '{mlflow.get_tracking_uri()}'")

client = MlflowClient(tracking_uri=MLFLOW_TRACKING_URI)
# client.search_registered_models()

logged_model_path = 's3://mlops-module4-mlflow-gan/3/beb964a81ccc4fcfae5064b8a5bba31a/artifacts/model'
loaded_model = mlflow.pyfunc.load_model(logged_model_path)

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