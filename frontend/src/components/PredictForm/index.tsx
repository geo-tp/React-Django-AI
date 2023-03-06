import { ReactNode } from "react";

export const PredictForm = (props: {
  children: ReactNode;
  onSubmit: Function;
  isImgForm?: boolean;
}) => {
  const isImgForm = props.isImgForm || false;
  return (
    <form
      onSubmit={(e) => props.onSubmit(e)}
      className={isImgForm ? "prediction-form--file" : "prediction-form"}
    >
      {props.children}
    </form>
  );
};
