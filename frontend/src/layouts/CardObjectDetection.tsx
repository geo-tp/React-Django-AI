import { ChangeEvent, FormEvent, useState } from "react";
import { BaseButton } from "../components/BaseButton";
import { Card } from "../components/Card";
import { ImageUpload } from "../components/ImageUpload";
import { Loader } from "../components/Loader";
import { PredictForm } from "../components/PredictForm";
import { PredictionTable } from "../components/PredictionTable";

export const CardObjectDetection = (props: {
  submitHandler: Function;
  uploadHandler: Function;
}) => {
  const [detectionValues, setDetectionValues] = useState<{
    [key: string]: { label: string; percent: number };
  }>({});

  const [inMemoryImg, setInMemoryImg] = useState("");
  const [loading, setLoading] = useState(false);

  return (
    <Card size="large" title="Object Detection" icon="object-group">
      {loading && <Loader />}
      <PredictForm
        isImgForm={true}
        onSubmit={(e: FormEvent<HTMLFormElement>) =>
          props.submitHandler(
            e,
            "object-detection",
            "POST",
            "img",
            setDetectionValues,
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
      <PredictionTable prediction={detectionValues} />
    </Card>
  );
};
