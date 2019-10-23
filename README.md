# MalariaNet
### Description
* A small web application of a convolution neural network model trained to detect malaria infected RBCs.
* For now it just classifies if a cell is parasitized or uninfected.



### Get it running
* First create a conda environment (recommended) using `conda create --name myenv python=3.7`
* Activate the environment using `source activate myenv` for linux and mac users or `activate myenv` for windows users.
* Next, install dependencies using `pip install -r requirements.txt`
* Do database migrations using

  `flask db init`

  `flask db migrate`

  `flask db upgrade`
* To start the webserver, just simply do `python app.py`.
### Other info
* `MalariaCNN.ipynb` contains code used to generate the model.
* Dataset - https://www.kaggle.com/iarunava/cell-images-for-detecting-malaria
