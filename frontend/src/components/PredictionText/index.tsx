export const PredictionText = (props: {
  text: string;
  borderColor: string;
}) => {
  if (props.text) {
    return (
      <p className={`prediction-text prediction-text--${props.borderColor}`}>
        {props.text}
      </p>
    );
  }

  return null;
};
