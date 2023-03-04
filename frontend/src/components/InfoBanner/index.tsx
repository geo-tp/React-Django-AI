import { useState } from "react";

export const InfoBanner = (props: { content: string }) => {
  const [display, setDisplay] = useState("flex");

  return (
    <div
      onClick={() => setDisplay("none")}
      style={{ display: display }}
      className="info-banner"
    >
      <p>{props.content}</p>
      <i className="fa fa-close"></i>
    </div>
  );
};
