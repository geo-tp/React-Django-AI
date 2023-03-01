import numpy as np
import string
import cv2
from tensorflow.keras.utils import pad_sequences
from tensorflow.keras.datasets import imdb
from transformers import DetrImageProcessor
from tensorflow import keras
from tensorflow.keras.applications import resnet50


def remove_special_char(data) -> list:
    ponctuations = list(string.punctuation)

    formatted_data = []
    for d in data:
        formatted_data.append(
            "".join([char for char in list(d) if not (char in ponctuations)])
        )

    return formatted_data


def imdb_sentences_to_integer(data) -> np.array:
    int_sequences = []
    words_indexes = imdb.get_word_index(path="imdb_word_index.json")
    max_words = 10000

    for sentence in data:
        seq = []
        for word in sentence.split(" "):
            try:
                index = words_indexes[word]
                if index < max_words:
                    seq.append(index)

            except:
                pass

        int_sequences.append(seq)

    return np.array(int_sequences)


def pad_integer_sequences(integer_sequences) -> np.array:
    max_len = 200
    return pad_sequences(integer_sequences, maxlen=max_len)


def detr_resnet50_normalize_image(image) -> np.array:
    processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50")
    x = processor(images=image, return_tensors="pt")

    return x


def classification_resnet50_normalize_image(image) -> np.array:
    array_img = keras.preprocessing.image.img_to_array(image)
    final_img = cv2.resize(array_img, (224, 224), interpolation=cv2.INTER_AREA)
    x = np.expand_dims(final_img, axis=0)
    x = resnet50.preprocess_input(x)

    return x
