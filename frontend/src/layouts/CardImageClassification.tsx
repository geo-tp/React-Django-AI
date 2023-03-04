import { ChangeEvent, FormEvent, useState } from "react";
import { BaseButton } from "../components/BaseButton";
import { Card } from "../components/Card";
import { ImageUpload } from "../components/ImageUpload";
import { Loader } from "../components/Loader";
import { PredictForm } from "../components/PredictForm";
import { PredictionTable } from "../components/PredictionTable";

export const CardImageClassification = (props: {
  submitHandler: Function;
  uploadHandler: Function;
}) => {
  const [classificationValues, setClassificationValues] = useState<{
    [key: string]: { label: string; percent: number };
  }>({});

  const [inMemoryImg, setInMemoryImg] = useState("");
  const [loading, setLoading] = useState(false);

  return (
    <Card size="large" title="Image Classification" icon="image">
      {loading && <Loader />}
      <PredictForm
        isImgForm={true}
        onSubmit={(e: FormEvent<HTMLFormElement>) =>
          props.submitHandler(
            e,
            "image-classification",
            "POST",
            "img",
            setClassificationValues,
            setLoading
          )
        }
      >
        <ImageUpload
          uploadHandler={(e: ChangeEvent) =>
            props.uploadHandler(e, setInMemoryImg)
          }
          inMemoryImg={inMemoryImg}
          setInMemoryImg={setInMemoryImg}
        />
        <BaseButton label="Predict" icon="magic-wand-sparkles" />
      </PredictForm>
      <PredictionTable prediction={classificationValues} />
    </Card>
  );
};
