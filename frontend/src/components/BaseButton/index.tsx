export const BaseButton = (props: { label: string; icon: string }) => {
  return (
    <button type="submit" className="base-button">
      <i className={`fa fa-${props.icon}`}></i>
      <span>{props.label}</span>
    </button>
  );
};
