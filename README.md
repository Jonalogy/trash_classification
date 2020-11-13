# Lab 5: ROBin

**ROBin** stands for **R**ecycling **O**riented **Bin**

This repository holds the code to train ROBin's image classification models.

## What the lab is about

To prototype a smart bin to classify trash based with the help of computer vision. ROBin does with a pair of image classification models to predict the material and items type

## Some context during the lab

- Throughout the lab, ROBin's training has only happened with Google Colab to tap on the free GPU.
- Because Colab is a free resource and company's repository is private, we had to mirror the company repository with a personal github repo in order to fetch the helper and utility methods from the `src` directory within Colab

## Where to start

### `robin_train.ipynb`

This notebook acts as the training orchestrator and not the model itself.
Using it on colab is not mandatory if you have your own GPU.

What is orchestrated:

* Utilities to fetch from mirror repo and Colab if required
* Allow the distributing of dataset to *train*, *validation* and *test* datasets
* Visualise class distribution before scientist initiates the training
* Allow scientist the declare variations of some hyperparameters (Other hyperparams are within the model_builders eg. `RobinMobilenetV2.py` itself)
* The training itself
* Zipping of logs and models for export
* Methods to export zipped logs and models central storage #TODO


### `view_logs_select_model` 

This notebook is to simulate the scientist downloading a range of training logs and choosing one to deploy.

## Misc
 * We had a model to identify the presence of trash on the bin tray, but it was scrapped with rule based detection. The previous code can be found at `train_robin_presence.ipynb`
