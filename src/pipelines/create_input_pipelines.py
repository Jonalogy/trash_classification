from tensorflow.keras.preprocessing import image_dataset_from_directory


def create_input_pipelines(dir_paths, hyperparams):
    pipes = lambda path: image_dataset_from_directory(
        path,
        shuffle=True,
        label_mode='categorical',
        batch_size=hyperparams['batch_size'],
        image_size=hyperparams['img_size']
    )
    return [pipes(path) for path in dir_paths]
