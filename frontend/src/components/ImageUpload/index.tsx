import { RefObject } from "react";

export const ImageUpload = (props: {
  uploadHandler: Function;
  urlImg: string;
  setUrlImg: Function;
  setPrediction: Function;
  imgRef?: RefObject<HTMLImageElement>;
}) => {
  const handleCloseClick = () => {
    props.setUrlImg("");
    props.setPrediction({});
  };

  return (
    <div className="image-upload">
      <label htmlFor="file-upload">
        <i className="fa fa-download"></i>
        <span>Image Here</span>
      </label>
      {props.urlImg && (
        <div className="image-upload__preview">
          <img src={props.urlImg} alt="currently uploaded" ref={props.imgRef} />
          <i className="fa fa-close" onClick={() => handleCloseClick()}></i>
        </div>
      )}

      <input
        style={{ visibility: props.urlImg ? "hidden" : "visible" }}
        onChange={(e) => props.uploadHandler(e)}
        id="file-upload"
        type="file"
        accept=".jpg, .gif, .png, .jpeg"
      />
    </div>
  );
};
