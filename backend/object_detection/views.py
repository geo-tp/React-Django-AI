from PIL import Image

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from transformers import DetrForObjectDetection

from .serializers import ObjectDetectionSerializer
from .models import ObjectDetection

from ai.ai_models import AiModel
from ai.preprocessing import (
    detr_resnet50_normalize_image,
)
from ai.postprocessing import detr_resnet50_parse_preds


class ObjectDetectionViewSet(viewsets.ModelViewSet):
    queryset = ObjectDetection.objects.all()
    serializer_class = ObjectDetectionSerializer

    ai_model = AiModel(
        DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50"),
        type_="pytorch",
        preprocessing=[detr_resnet50_normalize_image],
        postprocessing=[detr_resnet50_parse_preds],
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
        object_detection = ObjectDetection.objects.create(img=img_mem, prediction=preds)

        # Serialize it to JSON
        serializer = self.get_serializer(object_detection)
        headers = self.get_success_headers(serializer.data)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
