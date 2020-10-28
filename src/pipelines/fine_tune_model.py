from tensorflow.keras import optimizers, losses
from tensorflow.keras.callbacks import TensorBoard
import os


def fine_tune_model(model, hyperparams, datasets, history, log_dir, training_tag):
    print("Fine tuning")
    model.base_model.trainable = True  # Setting base model to be trainable again
    fine_tune_from = hyperparams["fine_tune_from"]  # Fine-tune from this layer onwards
    for layer in model.base_model.layers[:fine_tune_from]:  # Freeze all the layers before the `fine_tune_from` layer
        layer.trainable = False

    model().compile(
        loss=losses.CategoricalCrossentropy(),
        optimizer=optimizers.Adam(lr=hyperparams['base_learning_rate'] / 10),
        metrics=['accuracy']
    )
    model().summary()

    total_epochs = hyperparams["initial_epochs"] + hyperparams["fine_tune_epochs"]
    history_fine_tune = model().fit(
        x=datasets['train_ds'],
        epochs=total_epochs,
        initial_epoch=history.epoch[-1],
        validation_data=datasets['validate_ds'],
        callbacks=[TensorBoard(os.path.join(log_dir, 'fit', f'finetune_{training_tag}'))]
    )

    return history_fine_tune
