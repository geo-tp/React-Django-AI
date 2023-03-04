import { FormEvent, useState } from "react";
import { BaseButton } from "../components/BaseButton";
import { Card } from "../components/Card";
import { Loader } from "../components/Loader";
import { PredictForm } from "../components/PredictForm";
import { PredictionText } from "../components/PredictionText";
import { TextInput } from "../components/TextInput";

export const CardSentimentAnalysis = (props: { submitHandler: Function }) => {
  const [sentiment, setSentiment] = useState("");
  const [loading, setLoading] = useState(false);

  return (
    <Card title="Sentiment Analysis" icon="heart">
      {loading && <Loader />}
      <PredictForm
        onSubmit={(e: FormEvent<HTMLFormElement>) =>
          props.submitHandler(
            e,
            "sentiment-analysis",
            "POST",
            setSentiment,
            setLoading
          )
        }
      >
        <TextInput
          label="Write a good or bad review"
          size="medium"
          placeholder="Enter a comment or a review to know the feeling (Good or bad), "
        />
        <div className="card__footer">
          <BaseButton label="Predict" icon="magic-wand-sparkles" />
          <PredictionText
            text={sentiment}
            borderColor={sentiment === "positive" ? "green" : "red"}
          />
        </div>
      </PredictForm>
    </Card>
  );
};
