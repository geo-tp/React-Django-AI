class KerasPredictor:
    @staticmethod
    def predict(model, data):
        return model.predict(data)


class TorchPredictor:
    @staticmethod
    def predict(model, data):
        return model(data)


class TorchImagePredictor:
    @staticmethod
    def predict(model, data):
        return model(**data)
