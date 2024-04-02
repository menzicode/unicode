import os
import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.models import Model
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras import layers

# Directory containing subdirectories of images
base_dir = 'image_data'
# Load the pretrained ResNet50 model
base_model = ResNet50(weights='imagenet', include_top=False)
base_model.trainable = False
x = base_model(base_model.input, training=False)
outputs = layers.GlobalAveragePooling2D()(x)
# Create a model by removing the top (output layer) of the ResNet50
model = Model(inputs=base_model.input, outputs=outputs)

dataset = image_dataset_from_directory(
            directory=base_dir,
            labels='inferred',
            label_mode='categorical',
            image_size=(224, 224),
            shuffle=False,
            verbose=True,
        )

labels = dataset.class_names
print(labels[0:15])
# Predict (extract features) for the entire dataset
num_images = 9552 
steps = int(np.ceil(num_images / 32))
features = model.predict(dataset, steps=steps, verbose=1)

# Flatten the features to make them easier to work with
flattened_features = features.reshape((num_images, -1))

np.savez('image_features.npz', features=flattened_features, labels=labels)
print(features.shape)

print("Feature extraction completed.")
