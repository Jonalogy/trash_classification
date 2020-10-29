from tensorflow import lite


def serve_lite_model(saved_model_path, tflite_name, save_to):
    print("Converting saved model at", saved_model_path)
    converter = lite.TFLiteConverter.from_saved_model(saved_model_path)  # path to the SavedModel directory
    tflite_model = converter.convert()

    save_tflite_to = f'{save_to}/{tflite_name}.tflite'
    print("Saving as", saved_model_path)
    with open(save_tflite_to, 'wb') as f:
        f.write(tflite_model)
