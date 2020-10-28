from tensorflow.keras import optimizers, losses
from tensorflow.keras.callbacks import TensorBoard
from src.model_builder.RobinMobilenetV2 import RobinMobilenetV2
import os


def train_new_model(model_builder, hyperparams, datasets, log_dir, training_tag):
    image_shape = (*hyperparams["img_size"], hyperparams['channels'])
    class_count = len(datasets['class_names'])
    model = model_builder(image_shape, class_count)
    model().summary()
    model().compile(
        optimizer=optimizers.Adam(lr=hyperparams["base_learning_rate"]),
        loss=losses.CategoricalCrossentropy(),
        metrics=['accuracy']
    )
    history = model().fit(
        x=datasets['train_ds'],
        epochs=hyperparams['initial_epochs'],
        validation_data=datasets['validate_ds'],
        callbacks=[TensorBoard(os.path.join(log_dir, 'fit', f'new_{training_tag}'))]
    )
    return model, history
