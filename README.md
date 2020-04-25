# Time Series Clustering

## Goal

To leverage the power of Computer Vision to creat clusters of time series. 

## Idea

Today, deep learning can do some amazing tasks that traditional machine learning cannot. Deep learning has two major components: 

	- Computer Vision (CV)
	- Natural Language Processing (NLP)

Since we have many optimised algorithms in the domain of Computer Vision, one must wonder if it is possible to translate the task of clustering time series into a graphical one, as opposed to using numerical methods like k-Means clustering. An attempt was made to do so numerically by one of the authors of this repo. It was presented in the form a Meetup presentation and it can be found at https://github.com/Rocketloop/appliedml-talk-clustering-time-series. 

## Data 

We need time series data in bulk to be able to do such analysis. We are going to use cryptocurrency exchnage data from Binance. It is available from Kaggle https://www.kaggle.com/jorijnsmit/binance-full-history. 

## Pre-processing 

### Step 1:

All the time series were converted to images using matplotlib. 

## Tasks to be done

1. Find more graphical ways to represent time series. 
2. Build a way to cluster similar images together in an unsupervised fashion. 
