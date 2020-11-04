import tensorflow as tf


def log_as_image(log_dir, plot_name, png_buffer):
    """
    Writes plot as a Tensorboard image

    Args:
        log_dir (str): Logs directory path
        plot_name (str): Name for this image
        png_buffer (bytesio): A bytesio instance of the plot
    """

    decoded_png = tf.image.decode_png(png_buffer.getvalue(), channels=4)

    # Attempt to write an image summary
    file_writer_cm = tf.summary.create_file_writer(log_dir)
    with file_writer_cm.as_default():
        tf.summary.image(
            plot_name,
            tf.expand_dims(decoded_png, 0),
            step=0
        )
