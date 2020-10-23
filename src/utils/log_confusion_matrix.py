import io
import tensorflow as tf


def log_confusion_matrix(log_dir, plot_name, cm_figure):
    buff = io.BytesIO()
    cm_figure.savefig(buff, format='png')
    decoded_png = tf.image.decode_png(buff.getvalue(), channels=4)

    # Attempt to write an image summary
    file_writer_cm = tf.summary.create_file_writer(log_dir)
    with file_writer_cm.as_default():
        tf.summary.image(
            plot_name,
            tf.expand_dims(decoded_png, 0),
            step=0
        )
