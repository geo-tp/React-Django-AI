import { FormEvent, useState } from "react";
import { BaseButton } from "../components/BaseButton";
import { Card } from "../components/Card";
import { Loader } from "../components/Loader";
import { PredictForm } from "../components/PredictForm";
import { TextInput } from "../components/TextInput";

export const CardEnFrTranslation = (props: { submitHandler: Function }) => {
  const [frTranslation, setFrTranslation] = useState("");
  const [loading, setLoading] = useState(false);

  return (
    <Card title="Translation" icon="language">
      {loading && <Loader />}
      <PredictForm
        onSubmit={(e: FormEvent<HTMLFormElement>) =>
          props.submitHandler(
            e,
            "en-fr-translation",
            "POST",
            setFrTranslation,
            setLoading
          )
        }
      >
        <TextInput
          label="English"
          size="small"
          placeholder="Enter english text"
        />
        <TextInput
          label="French"
          size="small"
          placeholder="Traduction"
          disabled={true}
          value={frTranslation}
        />
        <BaseButton label="Predict" icon="magic-wand-sparkles" />
      </PredictForm>
    </Card>
  );
};
