# Devmesh Backend

## Important Details:
- Backend Stack: Flask, Celery, Redis
- The Flask backend is implemented asynchronously to accommodate for heavy traffic.
- Use of task IDs and interval function calls are used to track status/result
  1. Use initial AJAX call to get the task ID
  2. At interval, use another AJAX call using the task ID to grab status
  3. End interval checking once AJAX call responds with success/failure
- The test react app demonstrates how to properly use the Flask backend
- Object detection model based on images from the internet, labeled by Christian
  - Mimics the general workflow of a ML software developer developing on Tensorflow

## Notable Dependencies:
- Backend:
  - flask
  - celery
  - openCV
  - OpenVINO 2019 R2
  - numpy
  - base64
  - PIL.Image
  - io
- Frontend:
  - React dependencies
  - axios
  - react-webcam

## Common Errors:
- Dealing with ELIFECYCLE Errors?
  1. `sudo npm cache clean --force`
  2. `sudo rm -rf node_modules`
  3. `sudo npm install --save`
  3. `npm start`


## Procedure for starting application:
1. open four terminals
2. first terminal -> `$ redis-server`
3. second terminal -> `$ celery worker -A openvino_backend.celery --loglevel=info`
4. third terminal -> `python3 openvino_backend.celery`
5. fourth terminal -> `cd <INSTALL_DIR>/devmash_backend/test_react_app && npm start`

## Frontend References:
- https://www.npmjs.com/package/react-webcam
- https://www.npmjs.com/package/react-images-upload

## Backend Setup:
https://blog.miguelgrinberg.com/post/using-celery-with-flask
https://redis.io/topics/quickstart

## Object detection model tutorial:
- https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html
- https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md
- https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10/issues/184

## Past Research

### OCR:
- ???

### PixelNet Detection:
- https://github.com/banderlog/open_model_zoo/blob/24ca50034555721d876c8314ad36b4d6b03bf321/demos/python_demos/text_detection_demo.py

### EAST Text Detection:
- https://www.pyimagesearch.com/2018/08/20/opencv-text-detection-east-text-detector/
- https://medium.com/@tomhoag/opencv-text-detection-548950e3494c
- https://bitbucket.org/tomhoag/opencv-text-detection/src/master/
