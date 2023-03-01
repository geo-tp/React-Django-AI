from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from tensorflow.keras.applications import resnet50

DETR_RESNET_PROCESSOR = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50")
DETR_RESNET_LABELS = DetrForObjectDetection.from_pretrained(
    "facebook/detr-resnet-50"
).config.id2label


def classification_resnet50_parse_preds(preds, data=None) -> list:
    """ "Parse results of resnet50 classifier"""

    decoded_preds = resnet50.decode_predictions(preds, top=3)[0]
    parsed_preds = []

    for prediction in decoded_preds:
        name = prediction[1].replace("_", " ").capitalize()
        percent = prediction[2] * 100
        parsed_preds.append({"name": name, "percent": percent})

    return parsed_preds


def detr_resnet50_parse_preds(preds, data) -> list:
    """ "Parse results of resnet50 object detector"""

    # convert outputs (bounding boxes and class logits) to COCO API
    # let's only keep detections with score > 0.9

    print("DATA", data, type(data), data.size)
    target_sizes = torch.tensor([data.size[::-1]])

    results = DETR_RESNET_PROCESSOR.post_process_object_detection(
        preds, target_sizes=target_sizes, threshold=0.9
    )[0]

    parsed_results = []
    for score, label, box in zip(
        results["scores"], results["labels"], results["boxes"]
    ):
        box = [round(i, 2) for i in box.tolist()]

        parsed_results.append(
            {
                "label": DETR_RESNET_LABELS[label.item()],
                "score": score.item(),
                "location": box,
            }
        )

    return parsed_results


def translation_parse_preds(preds, data=None) -> str:
    """ "Parse results of translation model to only keep translated part"""

    return preds[0]["translation_text"]


def sentiment_analysis_parse_preds(preds, data=None) -> str:
    """ "Parse results of sentiment model with pos/neg string"""

    parsed_preds = []

    for pred in preds:
        parsed_preds.append("positive" if pred > 0.5 else "negative")

    return parsed_preds
