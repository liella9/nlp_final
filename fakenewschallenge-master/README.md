# NLP——final - FNC-1 Submission


This work is based on the work of UCLMR with certain improvements.
(FNC-1) is based on a single, end-to-end system consisting of lexical as
well as similarity features passed through a multi-layer perceptron with
one hidden layer.

Although relatively simple in nature, the system performs on par with
more elaborate, ensemble-based systems of other teams.

We use two simple bag-of-words representations for the text inputs:
term frequency (TF) and term frequency-inverse document frequency
(TF-IDF). The representations and feature thus extracted from the
headline and body pairs consist of only the following:

* The TF vector of the headline;
* The TF vector of the body;
* The cosine similarity between the TF-IDF vectors of the headline and
body.
* We also introduced some other features from the official baseline into the model, such as REFU (count the number of refuting) and POLA (polarity words)

<br>
<br>
<p align="center">
<img src="https://github.com/uclmr/fakenewschallenge/blob/master/images/uclmr_system.jpeg" alt="Schematic diagram of UCLMR's model" width="80%"/>
</p>


### Prerequisites

The system was developed, trained and tested using the
following:

```
Python==3.5.2
NumPy==1.11.3
scikit-learn==0.18.1
TensorFlow==0.12.1
```

Please note that compatibility of the saved model with newer versions
of `TensorFlow` has not been checked. Accordingly, please use the
`TensorFlow` version listed above.


## Reproducing the submission

The `pred.py` script can be run in two different modes: 'load' or
'train'. Upon running the `pred.py` file, the user is requested to input
the desired mode.

Execution of the `pred.py` file in 'load' mode entails the
following:

* The train set will be loaded from `train_stances.csv` and
`train_bodies.csv` using the corresponding `FNCData` class defined in
`util.py`.
* The test set will be loaded from `test_stances_unlabeled.csv` and
`train_bodies.csv` using the same `FNCData` class. Please note that
`test_stances_unlabeled.csv` corresponds to the second, amended release
of the file.
* The train and test sets are then respectively processed by the
`pipeline_train` and `pipeline_test` functions defined in `util.py`.
* The `TensorFlow` model saved in the `model` directory is then loaded
in place of the model definition in `pred.py`. The associated
`load_model` function can be found in `util.py`.
* The model is then used to predict the labels on the processed test
set.
* The predictions are then saved in a `predictions_test.csv` file in the
top level of the local directory. The corresponding `save_predictions`
function is defined in `util.py`. The predictions made are equivalent to
those submitted during the competition.

Execution of the `pred.py` file in 'train' mode encompasses steps
identical to those outlined above with the exception of the model being
trained as opposed to loaded from file. In this case, the predictions
will not be identical to those submitted during the competition.

The file name for the predictions can be changed in section '# Set file
names' at the top of `pred.py`, if required.

We downloaded the officially released labeled test set data after the competition
and used `test.py` for testing, which includes the official evaluation indicators 
and more objective indicators such as f1.




