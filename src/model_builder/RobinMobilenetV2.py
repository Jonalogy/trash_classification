import tensorflow as tf


class RobinMobilenetV2:
    def __init__(self, image_shape, class_count):
        self.base_model = self._build_from_pretrained(image_shape)
        self.model = self._append_classifier(image_shape, class_count)

    def __call__(self):
        return self.model

    def _build_from_pretrained(self, image_shape):
        # Obtaining keras MobileNet without the final layer
        base_model = tf.keras.applications.MobileNetV2(
            input_shape=image_shape, include_top=False, weights='imagenet'
        )
        base_model.trainable = False
        return base_model

    def _append_classifier(self, image_shape, class_count):
        # Create data augmentation layer
        data_augmentation = tf.keras.Sequential([
            tf.keras.layers.experimental.preprocessing.RandomFlip('horizontal'),
            tf.keras.layers.experimental.preprocessing.RandomRotation(0.2),
        ])

        # Creating the preprocess input layer
        preprocess_input = tf.keras.applications.mobilenet_v2.preprocess_input

        # Recreating the classifier layers
        global_average_layer = tf.keras.layers.GlobalAveragePooling2D()
        prediction_layer = tf.keras.layers.Dense(class_count, activation='softmax')

        # Assembling the new model to be trained
        inputs = tf.keras.Input(shape=image_shape)
        x = data_augmentation(inputs)
        x = preprocess_input(x)
        x = self.base_model(x, training=False)
        x = global_average_layer(x)
        x = tf.keras.layers.Dropout(0.2, )(x)
        outputs = prediction_layer(x)
        return tf.keras.Model(inputs, outputs)
