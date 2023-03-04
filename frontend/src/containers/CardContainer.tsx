import { ReactNode } from "react";

export const CardContainer = (props: { children: ReactNode }) => {
  return <section className="card-container">{props.children}</section>;
};
