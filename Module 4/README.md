# Deployment a model as a web-service

- Creating a virtual environment with Pipenv
- Creating a script for predicting
Putting the script into a Flask app
Packing the app to Docker

### Build the Docker image
Builds a Docker image from the Dockerfile in the current directory, names the image `ride-duration-prediction-service`, and tags it with `v1`
```bash
docker build -t ride-duration-prediction-service:v1 .
```

```bash
docker run -it --rm -p 9696:9696 ride-duration-prediction-service:v1
```
