import { FormEvent, useState } from "react";
import { BaseButton } from "../components/BaseButton";
import { Card } from "../components/Card";
import { Loader } from "../components/Loader";
import { PredictForm } from "../components/PredictForm";
import { TextInput } from "../components/TextInput";

export const CardEnTextCompletion = (props: { submitHandler: Function }) => {
  const [enTextCompleted, setEnTextCompleted] = useState("");
  const [loading, setLoading] = useState(false);

  return (
    <Card title="Text Completion" icon="file-lines">
      {loading && <Loader />}
      <PredictForm
        onSubmit={(e: FormEvent<HTMLFormElement>) =>
          props.submitHandler(
            e,
            "en-text-completion",
            "POST",
            setEnTextCompleted,
            setLoading
          )
        }
      >
        <TextInput
          label="Write the begining of a text"
          size="small"
          placeholder="Enter an english text to be automatically completed"
        />
        <TextInput
          label="Completed text"
          size="small"
          disabled={true}
          value={enTextCompleted}
          placeholder="Texte completion"
        />
        <BaseButton label="Predict" icon="magic-wand-sparkles" />
      </PredictForm>
    </Card>
  );
};
