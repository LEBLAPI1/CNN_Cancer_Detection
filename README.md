# CNN_Cancer_Detection

### Please note: this assignment 3 to detect cancer from images was built using google Colab - Using an A100 GPU (40 GB) and 84 GB RAM.

## Brief Description of the Problem and Data
The below is from a Kaggle competition. Here is the Kaggle link for reference. (https://www.kaggle.com/c/histopathologic-cancer-detection/overview)
The Kaggle competition focuses on using deep learning techniques to detect cancer from histopathologic scan images. The dataset comprises over 200,000 .tif image files, with the problem framed as a binary classification task (cancerous vs. non-cancerous). Each image is labeled 1 for cancerous and 0 for non-cancerous. To manage the dataset size and facilitate processing on Google Colab, the images were consolidated into a single .pickle file. The original data includes a split of 130,908 non-cancerous and 89,117 cancerous samples, totaling 220,025 images.

## Exploratory Data Analysis (EDA)
EDA involved loading and visualizing images from the .pickle file, examining the distribution of labels, and preparing a balanced subset of the data for training. Visualizations like histograms of label distributions were created to understand the data better. Due to memory limitations and image size I had to limit the analysis to 15,0000 images with cancer and 15,000 images without cancer. Google Colab with 84 GB of RAM and a A100 GPU of 40 GB could only handle this number of images at one time. For the future to improve the process there may be ways to feed in the images by doing multiple iterations of the training. I decided to do one training run due to my budget within Google Colab. Also the balanced dataset of 30,000 images (15,000 cancerous and 15,000 non-cancerous) was prepared to avoid bias towards the more prevalent class. Data cleaning involved selecting a balanced subset and normalizing image pixel values to the range [0, 1].

## Final Model Architecture
The model architecture chosen was a Convolutional Neural Network (CNN) with the following layers:

Four convolutional layers with increasing filter sizes (32, 64, 128, 128) and ReLU activation, each followed by max-pooling layers to reduce dimensionality.
A flattening layer to convert 3D feature maps to 1D feature vectors.
A dense layer with 512 units and ReLU activation for high-level reasoning.
A dropout layer with a rate of 0.1 to reduce overfitting.
An output dense layer with a sigmoid activation function for binary classification.
The CNN was compiled with the Adam optimizer and binary cross-entropy loss function, including accuracy, precision, and recall metrics for evaluation. This architecture was chosen for its capacity to learn hierarchical feature representations from the image data, which is crucial for distinguishing between cancerous and non-cancerous tissue patterns.

Numerous other CNN models were evaluated. I tried 30 epochs which clearly showed signs of overfitting the data as the training accuracy went to 100% but the validation accuracy bounced around at 80% with no improvements. I found the best model with the CNN layers above only needed 5 epochs. Also I experimented with dropout rates of .9, .5 and .1. The drop out rate of .9 is too much and underfits the data and performs the same as a coin flit of 50% accuracy score. The drop out rate of .5 is good but I found a drop out rate of .1 is the best due to the model overfitting.

## Results and Analysis
The model was trained on the balanced dataset with a training-validation split. Training was conducted over 5 epochs, with improvements observed in accuracy, precision, and recall on both training and validation sets. The final model achieved a training accuracy of 85.17%, with validation accuracy slightly lower, indicating good generalization. Again, various dropout rates were experimented with, and a rate of 0.1 was found optimal in this context.

## Conclusion
The CNN model demonstrated effective learning from histopathologic scan images, achieving a balance between accuracy, precision, and recall. The use of a balanced dataset and appropriate data normalization techniques were critical in achieving these results. Future improvements could explore more complex architectures, advanced data augmentation techniques, and further hyperparameter tuning to enhance model performance.
