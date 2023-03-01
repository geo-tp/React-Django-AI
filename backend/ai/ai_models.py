from sys import path
from transformers import pipeline
from PIL import Image
import requests
import types


class AiModel:
    def __init__(
        self,
        predictor,
        model=None,
        preprocessing=[],
        postprocessing=[],
    ):

        self.predictor = predictor
        self.model = model
        self.preprocessing = preprocessing
        self.postprocessing = postprocessing

    def predict(self, data) -> str:
        preprocessed_input = self._apply_process(self.preprocessing, data)

        preds = self.predictor.predict(self.model, preprocessed_input)

        postprocessed_output = self._apply_process(self.postprocessing, data, preds)

        return postprocessed_output

    def _apply_process(self, process, data, preds=None) -> str or np.array:
        processed = preds if preds is not None else data

        for p in process:
            processed = p(processed, data) if preds is not None else p(processed)

        return processed
