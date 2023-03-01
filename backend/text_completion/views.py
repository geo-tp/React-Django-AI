from transformers import pipeline, set_seed
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import EnTextCompletionSerializer
from .models import EnTextCompletion

from ai.ai_models import AiModel
from ai.postprocessing import text_completion_parse_preds
from ai.predictors import TorchPredictor


class EnTextCompletionViewSet(viewsets.ModelViewSet):
    queryset = EnTextCompletion.objects.all()
    serializer_class = EnTextCompletionSerializer
    ai_model = AiModel(
        predictor=TorchPredictor,
        model=pipeline("text-generation", model="gpt2"),
        postprocessing=[text_completion_parse_preds],
    )
    set_seed(42)

    def create(self, request, *args, **kwargs):

        # to be sure a string is provided
        text_serializer = self.get_serializer(data=request.data)
        text_serializer.is_valid(raise_exception=True)
        text = text_serializer.validated_data["text"]

        # completion with model
        preds = self.ai_model.predict(text)

        # save results
        en_completion = EnTextCompletion.objects.create(text=text, prediction=preds)

        # serialize to JSON
        response_serializer = self.get_serializer(en_completion)
        headers = self.get_success_headers(response_serializer.data)

        return Response(
            response_serializer.data, status=status.HTTP_200_OK, headers=headers
        )
