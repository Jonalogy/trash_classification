from os.path import basename, normpath
from tensorflow import lite


def serve_lite_model(saved_model_path: str, save_to: str, tflite_name: str = None):
    """
    Returns the converted tflite_model

    args:
        saved_model_path: The path to the folder holding the saved_model
        save_to: The destination path to save the tflite model to
        tflite_name : (Optional) This defaults to the same name as the saved_model.
    """
    print("Converting saved model at", saved_model_path)
    converter = lite.TFLiteConverter.from_saved_model(saved_model_path)  # path to the SavedModel directory
    tflite_model = converter.convert()

    if not tflite_name:
        tflite_name = basename(normpath(saved_model_path))

    save_tflite_to = f'{save_to}/{tflite_name}.tflite'
    print("Saving as", saved_model_path)
    with open(save_tflite_to, 'wb') as f:
        f.write(tflite_model)
