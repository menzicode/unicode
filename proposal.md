# Detecting Spoofed Characters
##### Organization: *Unicode*
##### Project: **

---

Name: Matt Menzi  
Email: mhmenzi@gmail.com  
Github: @menzicode  
Location: San Francisco

---

## Project Description
### Problem Statement

- Unicode provides scripts in 200 different languages. Some characters in different scripts may be confused for each other.
- For example, the cyrillic 'а' and the latin 'a'. 
- this can create security vulnerabilities, i.e. 'gᄋᄋgle.com' (takes user to http://xn--ggle-bkra.com/) that leads to a malicious link, phishing with spoofed
email addresses, or bypassing content filters that rely on regex matching in one language. 

### Solution

This project can be split into 4 distinct segments. 

1. Dataset creation
2. Model training
3. Data gathering and reporting
4. Automation of system

- Gather dataset
    - collect variety of fonts in latin, arabic, cyrillic, georgian, hangul, etc.
    - include mix of serif, sans serif, italic, etc.
    - organize in a directory system for labeling
        - organized by language -> character
    - split into train and test sets
- select model for classification task
    - CNN
- train model on classification task
- use trained model to generate embeddings
- identify individual characters that cluser near the wrong character



## Timeline 
### Week 1
Plan dataset structure. Gather dataset of UTF enabled fonts for each script. Standardize data format, including dimensions of input images. 
Split each font into character thumbnails and sort characters into appropriate directory labeled with UTF code points.
### Week 2
Continue creating dataset until coverage has been sufficiently achieved. Evaluate dataset to ensure data is in appropriate format, labels are
correct, etc. Split into train and test sets.
Begin building TensorFlow input pipeline by converting data to TFRecord format and test-loading the data with tf.data.TFRecordDataset(). 
### Week 3
Plan classification ML task. Weigh considerations such as dataset size, compute resources, and time resources when deciding whether to train 
a model from scratch, fine-tune a pretrained classification model, or use transfer learning. Research models for the task, again considering available 
resources, nature of model pre-training dataset, and accuracy on other classification tasks. Run small tests on Unicode dataset to compare 
resource usage, accuracy, etc. and ensure that dataset will work with model parameters. 
### Week 4
Select model and begin training process. Determine hyperparameters like learning rate, epochs, and batch size, again weighing performance and resource
considerations, as well as best practices. Ensure that checkpoints are being saved.
### Week 5
Test model accuracy on characters in the test set. Identify modes of failure, such as when a character is strongly identified as the incorrect character
or has high logit values for multiple characters, indicating potential confusion even if the model was accurate. Visually confirm that the cases where
the model is confused are cases where humans could be confused too, verifying that the model is replicating the pertinent mode of human intelligence.
Strip last layer off model to create an embedding model using last fully connected layer to output feature vectors. Plan creation and storage of 
feature vector dataset. 
### Week 6
Create feature vector dataset by feeding character dataset through embedding model. Perform clustering on data. Identify cases where characters
are misidentified by being placed in the wrong cluster, collecting data about the most confused pairs of characters (clusters with most overlap).
### Week 7
Create tool to perform confusability lookup. 
Potentially create visualization in 3-d. Visualize how characters cluster together, seeing cluster overlap and errors.
### Week 8
### Week 9
### Week 10
### Week 11
### Week 12
### Week 13
## Bio

### Relevant Work
 - Character Classifier
 - Character Superresolution
 - Car Classifier
     - trained LoRA model
 - Other ML work

### Technical Skills
 - TensorFlow
 - Python
 - OpenCV
 - Keras
 - Evaluating models 



