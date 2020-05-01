1. The dataset for the project is extracted from https://drive.google.com/drive/folders/11w4geFB6p17hFlWseB pHJQbhARINvTOc
2. The extracted dataset can be found in CODE/Twitter_Data. As can be observed, the dataset consists of 50 folders with a lot of additional data.
3. We extracted the data into the CODE/dataset.csv file, with each tweet labelled with the corresponding username. The code for dataset creation can be found in CODE/create_dataset.py
4. We found the most correlated unigrams and bigrams for each username according to preprocessed tweets(lowercasing, tokenization, stopword removal, lemmatization). The code for this module is found at CODE/analysis.ipynb.
5. After performing preprocessing(lowercasing, tokenization, stopword removal, lemmatization), we experimented with various classifiers on our data. The code for this can be found in CODE/project.ipynb.
6. We created graphs of our performance metrics, which can be found in the GRAPHS folder.
7. Our report and review ppts are attached in the folder.