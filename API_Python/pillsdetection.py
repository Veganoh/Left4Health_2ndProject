import base64
import os
import tensorflow as tf
import tensorflow.keras as keras
import keras_cv
import numpy

# Import the trained model
modelPath = os.path.abspath("../Pills Detection/Pre-existing Datasets/pill-model-15epoch-alldata.keras")
model = tf.keras.models.load_model(modelPath)

# Recreate the prediction_decodor, since it seems to be corrupted on load
model.prediction_decoder = keras_cv.layers.NonMaxSuppression(
    bounding_box_format="xywh",
    from_logits=True,
    iou_threshold=0.5,
    confidence_threshold=0.6,
)

def make_sigle_prediction(img_base64: str):
    decoded = base64.b64decode(img_base64)
    img_urlsafe_base64 = base64.urlsafe_b64encode(decoded)
    img = tf.io.decode_base64(img_urlsafe_base64)
    img = tf.image.decode_image(img, channels=3)

    # Put image in the correct format, an array of pixels
    image = [numpy.array(img)]

    # Resize it to be of the size expected by the model
    inference_resizing = keras_cv.layers.Resizing(
        640, 640, pad_to_aspect_ratio=True, bounding_box_format='xywh'
    )
    image_batch = inference_resizing(image)

    # Predict the bounding boxes
    y_pred = model.predict(image_batch)

    return y_pred

def get_prediction_boxes(img_base64: str):
    # Make the prediction
    y_pred = make_sigle_prediction(img_base64)

    # y_pred is an numpy.ndarray of bounding_boxes for all images, we only need the first image because there's only one
    boxes = y_pred['boxes'][0]

    # convert to python list, so it can be converted to json and returned by the api
    boxes = boxes.tolist()

    # filter out the entries that are filled with -1, that appear because of how the prediction model returns
    boxes = list(filter(lambda box: box[0] != -1, boxes))
    print(boxes)
    print(type(boxes))

    return boxes

"""
fullpath = os.path.abspath("./pillsPicture/images/blue_pills_palm478489_M.jpg")
filepath = keras.utils.get_file(origin=fullpath)
image = keras.utils.load_img(filepath)
print(image)

def visualize_single_prediction(modelToUse, image, confidence):
    image = [numpy.array(image)]
    # print(image)
    # print(type(image[0]))

    keras_cv.visualization.plot_image_gallery(
        numpy.array(image),
        value_range=(0, 255),
        scale=3
    )

    inference_resizing = keras_cv.layers.Resizing(
        640, 640, pad_to_aspect_ratio=True, bounding_box_format='xywh'
    )

    image_batch = inference_resizing(image)


    model.prediction_decoder
    modelToUse.prediction_decoder = keras_cv.layers.NonMaxSuppression(
       bounding_box_format="xywh",
       from_logits=True,
       iou_threshold=0.5,
       confidence_threshold=confidence,
    )

    y_pred = modelToUse.predict(image_batch)

    keras_cv.visualization.plot_bounding_box_gallery(
        image_batch,
        value_range=(0, 255),
        y_pred=y_pred,
        rows=1,
        cols=1,
        scale=3,
        font_scale=0.7,
        bounding_box_format='xywh',
        class_mapping={0: 'pill'}
    )
"""