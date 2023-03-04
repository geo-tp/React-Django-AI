export const TextInput = (props: {
  label: string;
  placeholder?: string;
  value?: string;
  size: string;
  disabled?: boolean;
}) => {
  const disabled = props.disabled || false;
  const size = props.size ? `text-input--${props.size}` : "";

  return (
    <div className={`text-input ${size}`}>
      <label htmlFor="text-input">{props.label}</label>
      <textarea
        name="text-input"
        placeholder={props.placeholder}
        value={props.value}
        disabled={disabled}
      />
    </div>
  );
};
