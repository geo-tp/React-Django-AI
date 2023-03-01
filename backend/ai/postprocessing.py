import json
import torch
from transformers import DetrImageProcessor, DetrForObjectDetection
from tensorflow.keras.applications import resnet50

DETR_RESNET_PROCESSOR = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50")
DETR_RESNET_LABELS = DetrForObjectDetection.from_pretrained(
    "facebook/detr-resnet-50"
).config.id2label


def classification_resnet50_parse_preds(preds, data=None) -> str:
    """ "Parse results of resnet50 classifier to a JSON string"""

    decoded_preds = resnet50.decode_predictions(preds, top=3)[0]
    parsed_preds = {}

    for i, prediction in enumerate(decoded_preds):
        name = prediction[1].replace("_", " ").capitalize()
        percent = prediction[2] * 100
        parsed_preds[i] = {"label": name, "percent": percent}

    return json.dumps(parsed_preds)


def detr_resnet50_parse_preds(preds, data) -> str:
    """ "Parse results of resnet50 object detector to a JSON string"""

    target_sizes = torch.tensor([data.size[::-1]])

    # convert outputs (bounding boxes and class logits) to COCO API
    # let's only keep detections with score > 0.9
    results = DETR_RESNET_PROCESSOR.post_process_object_detection(
        preds, target_sizes=target_sizes, threshold=0.9
    )[0]

    parsed_results = {}
    j = 1
    for score, label, box in zip(
        results["scores"], results["labels"], results["boxes"]
    ):
        box = [round(i, 2) for i in box.tolist()]

        parsed_results[j] = {
            "label": DETR_RESNET_LABELS[label.item()],
            "percent": score.item() * 100,
            "location": {"x1": box[0], "y1": box[1], "x2": box[2], "y2": box[3]},
        }

        j += 1

    return json.dumps(parsed_results)


def translation_parse_preds(preds, data=None) -> str:
    """ "Parse results of translation model to only keep translated string"""

    return preds[0]["translation_text"]


def text_completion_parse_preds(preds, data=None) -> str:
    """ "Parse results of completion model to only keep generated string"""

    return preds[0]["generated_text"]


def sentiment_analysis_parse_preds(preds, data=None) -> str:
    """Parse results of sentiment model with pos/neg string"""

    return "positive" if preds[0] > 0.5 else "negative"
