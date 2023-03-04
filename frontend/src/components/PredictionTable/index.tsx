export const PredictionTable = (props: {
  prediction: { [key: string]: { label: string; percent: number } };
}) => {
  return (
    <table className="prediction-table">
      <thead>
        <tr>
          <th>Prediction</th>
          <th></th>
        </tr>
      </thead>

      <tbody>
        {Object.keys(props.prediction).map((index: string) => (
          <tr
            key={`${
              props.prediction[parseInt(index)].label
            }-${index}-preds-table`}
          >
            <td>{props.prediction[parseInt(index)].label}</td>
            <td>{props.prediction[parseInt(index)].percent} %</td>
          </tr>
        ))}
        {Object.keys(props.prediction).length === 0 && (
          <div className="prediction-table__placeholder">
            <i className="fa fa-magic-wand-sparkles"></i>
          </div>
        )}
      </tbody>
    </table>
  );
};
