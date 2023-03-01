from sys import path
from keras.models import load_model
from PIL import Image
import requests
import types


class AiModel:
    def __init__(
        self,
        model=None,
        model_path=None,
        type_="keras",
        preprocessing=[],
        postprocessing=[],
    ):

        if model_path:
            if type_ == "keras":
                self.model = load_model(model_path)
            else:
                pass
        else:
            self.model = model

        self.type_ = type_
        self.preprocessing = preprocessing
        self.postprocessing = postprocessing

    def predict(self, data):
        preprocessed_input = self._apply_process(self.preprocessing, data)
        if self.type_ == "keras":
            preds = self.model.predict(preprocessed_input)

        elif self.type_ == "pytorch":
            try:
                preds = self.model(**preprocessed_input)
            except:
                preds = self.model(preprocessed_input)

        postprocessed_output = self._apply_process(self.postprocessing, data, preds)

        return postprocessed_output

    def _apply_process(self, process, data, preds=None):
        processed = preds if preds is not None else data

        for p in process:
            processed = p(processed, data) if preds is not None else p(processed)

        return processed
