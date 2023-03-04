import { ChangeEvent } from "react";
import { FormEvent } from "react";

export class ApiFetcher {
  static baseUrl = "http://localhost:8000/api/v1/";

  static fetchJson = async (
    endpoint: string,
    method: string = "GET",
    data: any = null,
    isFile: boolean = false
  ) => {
    var headers = {};

    if (!isFile) {
      headers = {
        Accept: "application/json",
        "Content-Type": "application/json",
      };
    }

    const params: { [k: string]: any } = {
      method: method,
      headers: headers,
    };

    if (data) {
      params["body"] = isFile ? data : JSON.stringify(data);
      endpoint += "/";
    }

    return fetch(this.baseUrl + endpoint, params)
      .then((response) => {
        if (response.ok) {
          return response.json();
        }

        throw response;
      })
      .then((data) => {
        return data.prediction;
      })
      .catch((error) => {
        return error;
      });
  };
}

export class SubmitHandler {
  static file = async (
    e: FormEvent<HTMLFormElement>,
    endpoint: string,
    method: string,
    fieldName = "img",
    setState: Function,
    setLoading: Function
  ) => {
    e.preventDefault();

    const target = e.target as HTMLFormElement;
    const input = target[0] as HTMLInputElement;
    var preds = {};
    if (input.files) {
      const file = input.files[0];

      if (!file) {
        return;
      }

      setLoading(true);

      let fdata = new FormData();
      fdata.append(fieldName, file, file.name);
      preds = await ApiFetcher.fetchJson(endpoint, method, fdata, true);

      setLoading(false);
    }

    setState(preds);
  };

  static json = async (
    e: FormEvent<HTMLFormElement>,
    endpoint: string,
    method: string,
    setState: Function,
    setLoading: Function
  ) => {
    e.preventDefault();

    const target = e.target as HTMLFormElement;
    const text = (target[0] as HTMLInputElement).value;

    if (!text) {
      return;
    }

    setLoading(true);
    const preds = await ApiFetcher.fetchJson(endpoint, method, {
      text,
    });
    setLoading(false);

    setState(preds);
  };
}

export class UploadHandler {
  static getFileUrl = async (e: ChangeEvent, setState: Function) => {
    const target = e.target as HTMLFormElement;
    const file = target.files[0];
    const fileUrl = URL.createObjectURL(file);

    setState(fileUrl);
  };
}
