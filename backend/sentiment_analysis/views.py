from sys import path
from PIL import Image

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.models import load_model

from .serializers import SentimentAnalysisSerializer
from .models import SentimentAnalysis
from ai.ai_models import AiModel
from ai.preprocessing import (
    remove_special_char,
    imdb_sentences_to_integer,
    pad_integer_sequences,
)
from ai.postprocessing import sentiment_analysis_parse_preds
from ai.predictors import KerasPredictor


class SentimentAnalysisViewSet(viewsets.ModelViewSet):
    queryset = SentimentAnalysis.objects.all()
    serializer_class = SentimentAnalysisSerializer

    keras_sentiment_analyser_path = (
        path[0] + "/ai/keras_models/embeddings_sentiment_analysis.h5"
    )
    ai_model = AiModel(
        predictor=KerasPredictor,
        model=load_model(keras_sentiment_analyser_path),
        preprocessing=[
            remove_special_char,
            imdb_sentences_to_integer,
            pad_integer_sequences,
        ],
        postprocessing=[sentiment_analysis_parse_preds],
    )

    def create(self, request, *args, **kwargs):

        # to be sure a text is provided
        text_serializer = self.get_serializer(data=request.data)
        text_serializer.is_valid(raise_exception=True)
        text = text_serializer.validated_data["text"]

        # predict sentiment
        preds = self.ai_model.predict([text])

        # Save text and prediction results
        sentiment = SentimentAnalysis.objects.create(text=text, prediction=preds)

        # Serialize it to JSON
        serializer = self.get_serializer(sentiment)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
