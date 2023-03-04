import { SubmitHandler, UploadHandler } from "../api";
import { CardContainer } from "../containers/CardContainer";
import { CardEnFrTranslation } from "../layouts/CardEnFrTranslation";
import { CardEnTextCompletion } from "../layouts/CardEnTextCompletion";
import { CardImageClassification } from "../layouts/CardImageClassification";
import { CardObjectDetection } from "../layouts/CardObjectDetection";
import { CardSentimentAnalysis } from "../layouts/CardSentimentAnalysis";

export const HomePage = () => {
  return (
    <main className="homepage">
      <CardContainer>
        <CardEnFrTranslation submitHandler={SubmitHandler.json} />
        <CardSentimentAnalysis submitHandler={SubmitHandler.json} />
        <CardEnTextCompletion submitHandler={SubmitHandler.json} />
        <CardImageClassification
          submitHandler={SubmitHandler.file}
          uploadHandler={UploadHandler.getFileUrl}
        />
        <CardObjectDetection
          submitHandler={SubmitHandler.file}
          uploadHandler={UploadHandler.getFileUrl}
        />
      </CardContainer>
    </main>
  );
};
