React Django AI
================

Various Deep learning models deployed on a Django API with a React Frontend.

- Text Completion
- Translation
- Sentiment Analysis
- Image Classification
- Object Detection

You don't need a GPU to use it, the backend can run on a CPU only, it will require about 2GB of ram.

Links
-----

See created design : [Figma Template](https://www.figma.com/file/K1vigi10V0GWykfVX2mgVA/DjangoAI?node-id=0%3A1&t=qQOOw75kN5njkQeu-1)

See Django AI live : [Demo Website]()

Backend Installation
----------------

Created with python 3.10.6

- ### Create Python Virtual Env
    ```
    python -m venv env_name
    ```

- ### Use Python Virtual Env
    ```
    source env_name/bin/activate
    ```

- ### Install requirement
    ```
    python -m pip install -r requirements.txt
    ```

- ### Initialise Database
    ```
    python -m manage.py makemigrations
    python -m manage.py migrate
    ```

- ### Lauch dev server
    ```
    python manage.py runserver
    ```


Endpoint
--------

While dev server is launched, you can access `http://localhost:8000/api/v1/` with browser. You can use the debug interface to list and get predictions.


Storage
------

Images are stored into `/media/` folder, predictions data are stored into database. 
You can configure database with `/config/settings.py`


Frontend Installation
------------------

Created with Node v17.9.1 and NPM v8.11.0

### `npm install`

Install required node libraries.

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).
