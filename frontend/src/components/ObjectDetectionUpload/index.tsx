import { FormEvent, useEffect, useRef } from "react";
import { ImageUpload } from "../ImageUpload";

export const ObjectDetectionUpload = (props: {
  urlImg: string;
  setUrlImg: Function;
  uploadHandler: Function;
  prediction: { [key: string]: any };
  setPrediction: Function;
}) => {
  const detectionCanvasRef = useRef<HTMLCanvasElement>(null);
  const imgRef = useRef<HTMLImageElement>(null);

  useEffect(() => {
    if (detectionCanvasRef.current == null) {
      return;
    }

    const context = detectionCanvasRef.current.getContext(
      "2d"
    ) as CanvasRenderingContext2D;

    context.clearRect(0, 0, context.canvas.width, context.canvas.height);
  }, [props.urlImg]);

  useEffect(() => {
    const drawObjectFrames = () => {
      if (!props.prediction && !props.urlImg) {
        return;
      }

      if (detectionCanvasRef.current == null) {
        return;
      }

      if (imgRef.current == null) {
        return;
      }

      const frameColors = [
        "red",
        "blue",
        "yellow",
        "green",
        "purple",
        "orange",
        "pink",
      ];
      const image = new Image();
      image.src = props.urlImg;

      const context = detectionCanvasRef.current.getContext(
        "2d"
      ) as CanvasRenderingContext2D;

      var i = 0;
      for (let key of Object.keys(props.prediction)) {
        const pred = props.prediction[key];
        const loc = pred.location;

        const ratioW = imgRef.current.width / imgRef.current.naturalWidth;
        const ratioH = imgRef.current.height / imgRef.current.naturalWidth;

        const x = loc.x1 * ratioW;
        const y = loc.y1 * ratioH;
        const w = loc.x2 * ratioW - loc.x1 * ratioW;
        const h = loc.y2 * ratioH - loc.y1 * ratioH;

        context.strokeStyle = frameColors[i % frameColors.length];
        context.strokeRect(x, y, w, h);
        context.fillStyle = frameColors[i % frameColors.length];
        context.fillText(pred.label, x, y);

        i++;
      }
    };

    drawObjectFrames();
  }, [props.urlImg, props.prediction]);

  return (
    <div className="object-detection-upload">
      <ImageUpload
        uploadHandler={(e: FormEvent<HTMLFormElement>) =>
          props.uploadHandler(e, props.setUrlImg)
        }
        urlImg={props.urlImg}
        setUrlImg={props.setUrlImg}
        setPrediction={props.setPrediction}
        imgRef={imgRef}
      />
      {props.prediction && <canvas ref={detectionCanvasRef}></canvas>}
    </div>
  );
};
