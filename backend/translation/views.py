from transformers import pipeline
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import EnFrTranslationSerializer
from .models import EnFrTranslation

from ai.ai_models import AiModel
from ai.postprocessing import translation_parse_preds


class EnFrTranslationViewSet(viewsets.ModelViewSet):
    queryset = EnFrTranslation.objects.all()
    serializer_class = EnFrTranslationSerializer
    ai_model = AiModel(
        pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr"),
        type_="pytorch",
        postprocessing=[translation_parse_preds],
    )

    def create(self, request, *args, **kwargs):

        # to be sure a string is provided
        en_serializer = self.get_serializer(data=request.data)
        en_serializer.is_valid(raise_exception=True)
        en_text = en_serializer.validated_data["text"]

        # translate with model
        fr_text = self.ai_model.predict(en_text)

        # save results
        en_fr_translation = EnFrTranslation.objects.create(
            text=en_text, prediction=fr_text
        )

        # serialize to JSON
        response_serializer = self.get_serializer(en_fr_translation)
        headers = self.get_success_headers(response_serializer.data)

        return Response(
            response_serializer.data, status=status.HTTP_200_OK, headers=headers
        )
