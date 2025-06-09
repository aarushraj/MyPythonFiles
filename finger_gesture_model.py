import os
import numpy as np
import tensorflow as tf
from tensorflow import _tf_uses_legacy_keras
from tensorflow._tf_uses_legacy_keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Directory containing subfolders for gestures (0, 1, 2, ..., 6)
base_dir = 'path_to_your_dataset'

# Image dimensions
img_height, img_width = 100, 100
batch_size = 32

# Create ImageDataGenerators for training and validation
train_datagen = ImageDataGenerator(
    rescale=1./255,          # Rescale pixel values to [0, 1]
    rotation_range=40,       # Randomly rotate images
    width_shift_range=0.2,   # Randomly shift images horizontally
    height_shift_range=0.2,  # Randomly shift images vertically
    shear_range=0.2,         # Random shear
    zoom_range=0.2,          # Random zoom
    horizontal_flip=True,    # Randomly flip images horizontally
    fill_mode='nearest'      # Fill empty pixels after transformations
)

validation_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    os.path.join(base_dir, 'train'),  # Directory for training images
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical'  # Multi-class classification
)

validation_generator = validation_datagen.flow_from_directory(
    os.path.join(base_dir, 'validation'),  # Directory for validation images
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical'  # Multi-class classification
)

# Build the CNN model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(7, activation='softmax')  # 7 classes (0-6)
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    epochs=10,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // batch_size
)

# Save the model
model.save('hand_gesture_model.h5')

# Plot the training & validation accuracy
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# Evaluate the model on validation data
validation_loss, validation_acc = model.evaluate(validation_generator)
print(f'Validation Accuracy: {validation_acc*100:.2f}%')

# Function to predict hand gesture for a new image
def predict_gesture(image_path):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(img_height, img_width))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Normalize the image

    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction)
    
    return predicted_class

# Example of using the model for prediction
image_path = 'path_to_image.png'  # Replace with an image path for testing
gesture = predict_gesture(image_path)
print(f"Predicted Gesture: {gesture}")
