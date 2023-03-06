export const PredictionTable = (props: {
  prediction: { [key: string]: { label: string; percent: number } };
}) => {
  return (
    <div className="prediction-table">
      <h3>Prediction</h3>
      <div>
        <div className="prediction-table__row-container">
          {Object.keys(props.prediction).map((index: string) => (
            <div
              className="prediction-table__row"
              key={`${
                props.prediction[parseInt(index)].label
              }-${index}-preds-row`}
            >
              <p>{props.prediction[parseInt(index)].label}</p>
              <p>{props.prediction[parseInt(index)].percent} %</p>
            </div>
          ))}

          {Object.keys(props.prediction).length === 0 && (
            <div className="prediction-table__placeholder">
              <i className="fa fa-magic-wand-sparkles"></i>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
