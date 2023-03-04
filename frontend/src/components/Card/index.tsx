import { ReactNode } from "react";

export const Card = (props: {
  size?: string;
  title: string;
  icon: string;
  children: ReactNode;
}) => {
  const size = props.size ? "card--" + props.size : "";

  return (
    <div className={`card ${size}`}>
      <div className="card__header">
        <h2>{props.title}</h2>
        <i className={`fa fa-${props.icon}`}></i>
      </div>
      <div className="card__body">{props.children}</div>
    </div>
  );
};
