export const ImageUpload = (props: {
  uploadHandler: Function;
  inMemoryImg: string;
  setInMemoryImg: Function;
}) => {
  return (
    <div className="image-upload">
      <label htmlFor="file-upload">
        <i className="fa fa-download"></i>
        <span>Image Here</span>
      </label>
      {props.inMemoryImg && (
        <div className="image-upload__preview">
          <img src={props.inMemoryImg} alt="" />
          <i
            className="fa fa-close"
            onClick={() => props.setInMemoryImg("")}
          ></i>
        </div>
      )}

      <input
        style={{ visibility: props.inMemoryImg ? "hidden" : "visible" }}
        onChange={(e) => props.uploadHandler(e)}
        id="file-upload"
        type="file"
        accept=".jpg, .gif, .png, .jpeg"
      />
    </div>
  );
};
