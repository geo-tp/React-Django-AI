import json
from PIL import Image

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from tensorflow.keras.applications.resnet50 import ResNet50

from .serializers import ImageClassificationSerializer
from .models import ImageClassification
from ai.ai_models import AiModel
from ai.postprocessing import classification_resnet50_parse_preds
from ai.preprocessing import classification_resnet50_normalize_image


class ImageClassificationViewSet(viewsets.ModelViewSet):
    queryset = ImageClassification.objects.all()
    serializer_class = ImageClassificationSerializer

    ai_model = AiModel(
        ResNet50(weights="imagenet"),
        type_="keras",
        preprocessing=[classification_resnet50_normalize_image],
        postprocessing=[classification_resnet50_parse_preds],
    )

    def create(self, request, *args, **kwargs):

        # to be sure an image is provided
        img_serializer = self.get_serializer(data=request.data)
        img_serializer.is_valid(raise_exception=True)

        # get img from serializer
        img_mem = img_serializer.validated_data["img"]
        img = Image.open(img_mem)

        # predict img and format preds
        preds = self.ai_model.predict(img)

        # Save image and prediction results
        image_classification = ImageClassification.objects.create(
            img=img_mem, prediction=preds
        )

        # Serialize it to JSON
        serializer = self.get_serializer(image_classification)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
