# 1.Check Version
<img src='https://github.com/GawainGan/MLOps/blob/main/2-Experiment-Tracking/pic/1-Conda_Env-MLflow_Version.png' style="width: 40%;">

# 2.Download and preprocess the data
```python
# load the data from the folder taxi_data_folder (the folder where you have downloaded the data),
!python preprocess_data.py --raw_data_path taxi_data_folder --dest_path ./output
# check the number of files in the output folder:
!ls -l ./output
```

```output
total 17088
-rw-r--r--  1 gan-m2  staff   131004 May 29 12:20 dv.pkl
-rw-r--r--  1 gan-m2  staff  2458697 May 29 12:20 test.pkl
-rw-r--r--  1 gan-m2  staff  2374517 May 29 12:20 train.pkl
-rw-r--r--  1 gan-m2  staff  2215823 May 29 12:20 val.pkl
```

# 3.Train a model with autolog
<img src='https://github.com/GawainGan/MLOps/blob/main/2-Experiment-Tracking/pic/3-Update-train.py%20file.png' style="width: 40%;">
<img src='https://github.com/GawainGan/MLOps/blob/main/2-Experiment-Tracking/pic/3.1-auto_log%20info.png' style="width: 40%;">

the `min_samples_split` parameter is 2

# 4.Launch the tracking server locally
<img src='https://github.com/GawainGan/MLOps/blob/main/2-Experiment-Tracking/pic/4-artifact%20folder%20%26%20run%20locally.png' style="width: 40%;">

# 5.Tune model hyperparameters
<img src='https://github.com/GawainGan/MLOps/blob/main/2-Experiment-Tracking/pic/5-Update-hypo.py%20file.png'>
<img src='https://github.com/GawainGan/MLOps/blob/main/2-Experiment-Tracking/pic/5.1-Sorted-rmse.png'>

The model with best rmse is:5.335

# 6.Promote the best model to the model registry

<img src='https://github.com/GawainGan/MLOps/blob/main/2-Experiment-Tracking/pic/6-Best-test-rmse.png'>

The best model with the test rmse is: 5.567

