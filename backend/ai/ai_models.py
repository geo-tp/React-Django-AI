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


if __name__ == "__main__":

    # from transformers import DetrForObjectDetection
    # from preprocessing import (
    #     detr_resnet50_normalize_image,
    # )

    # from postprocessing import detr_resnet50_parse_preds

    # url = "http://images.cocodataset.org/val2017/000000039769.jpg"
    # image = Image.open(requests.get(url, stream=True).raw)

    # m = AiModel(
    #     DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50"),
    #     type_="pytorch",
    #     preprocessing=[detr_resnet50_normalize_image],
    #     postprocessing=[detr_resnet50_parse_preds],
    # )

    # print(m.predict(image))

    from preprocessing import (
        remove_special_char,
        imdb_sentences_to_integer,
        pad_integer_sequences,
    )

    KERAS_SENTIMENT_ANALYSER_PATH = (
        path[0] + "/keras_models/embeddings_sentiment_analysis.h5"
    )

    m = AiModel(
        model_path=KERAS_SENTIMENT_ANALYSER_PATH,
        type_="keras",
        preprocessing=[
            remove_special_char,
            imdb_sentences_to_integer,
            pad_integer_sequences,
        ],
        postprocessing=[],
    )

    print(
        m.predict(
            [
                "this is a very bad movie hate never producer is bad can't imagine how awefull it is the thought solid thought senator do making to is spot nomination assumed while he of jack in where picked as getting on was did hands fact characters to always l",
                "this is a good movie",
                "the as you with out themselves powerful lets loves their becomes reaching had journalist of lot from anyone to have after out atmosphere never more room and it so heart shows to years of every never going and help moments or of every chest visual movie except her was several of enough more with is now current film as you of mine potentially unfortunately of you than him that with out themselves her get for was camp of you movie sometimes movie that with scary but and to story wonderful that in seeing in character to of 70s musicians with heart had shadows they of here that with her serious to have does when from why what have critics they is you that isn't one will very to as itself with other and in of seen over landed for anyone of and br show's to whether from than out themselves history he name half some br of and odd was two most of mean for 1 any an boat she he should is thought frog but of script you not while history he heart to real at barrel but when from one bit then have two of script their with her nobody most that with wasn't to with armed acting watch an for with heartfelt film want an",
                "the thought solid thought senator do making to is spot nomination assumed while he of jack in where picked as getting on was did hands fact characters to always life thrillers not as me can't in at are br of sure your way of little it strongly random to view of love it so principles of guy it used producer of where it of here icon film of outside to don't all unique some like of direction it if out her imagination below keep of queen he diverse to makes this stretch and of solid it thought begins br senator and budget worthwhile though ok and awaiting for ever better were and diverse for budget look kicked any to of making it out and follows for effects show to show cast this family us scenes more it severe making senator to and finds tv tend to of emerged these thing wants but and an beckinsale cult as it is video do you david see scenery it in few those are of ship for with of wild to one is very work dark they don't do dvd with those them",
            ]
        )
    )

    # from tensorflow.keras.applications.resnet50 import ResNet50
    # from postprocessing import classification_resnet50_parse_preds

    # m = AiModel(
    #     ResNet50(weights="imagenet"),
    #     preprocessing=[],
    #     postprocessing=[classification_resnet50_parse_preds],
    # )

    # print(m.predict(image))
