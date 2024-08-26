# ONNX YOLOv10 Object Detection
 Python scripts performing object detection using the YOLOv10 model in ONNX.
 
![!ONNX YOLOv10 Object Detection](https://github.com/user-attachments/assets/a926d7d7-7ee5-474d-b90f-310ef874f0cb)

> [!CAUTION]
> I skipped adding the pad to the input image when resizing, which might affect the accuracy of the model if the input image has a different aspect ratio compared to the input size of the model. Always try to get an input size with a ratio close to the input images you will use.

## Requirements

 * Check the **requirements.txt** file.
 * For ONNX, if you have a NVIDIA GPU, then install the **onnxruntime-gpu**, otherwise use the **onnxruntime** library.

## Installation [![PyPI](https://img.shields.io/pypi/v/yolov10-onnx?color=2BAF2B)](https://pypi.org/project/yolov10-onnx/)

```bash
pip install yolov10-onnx
```
Or, clone this repository:
```bash
git clone https://github.com/ibaiGorordo/ONNX-YOLOv10-Object-Detection.git
cd ONNX-YOLOv10-Object-Detection
pip install -r requirements.txt
```
### ONNX Runtime
For Nvidia GPU computers:
`pip install onnxruntime-gpu`

Otherwise:
`pip install onnxruntime`

## ONNX model
- If the model file is not found in the models directory, it will be downloaded automatically from the [HuggingFace](https://huggingface.co/onnx-community?search_models=yolov10).
- **Available models**: yolov10n.onnx, yolov10s.onnx, yolov10m.onnx, yolov10b.onnx, yolov10l.onnx, yolov10x.onnx

## Original YOLOv10 model
The original YOLOv10 model can be found in this repository: https://github.com/THU-MIG/yolov10
- The License of the models is AGPL-3.0 license: https://github.com/THU-MIG/yolov10/blob/main/LICENSE

## Examples

 * **Image inference**:
 ```
 python image_object_detection.py
 ```

 * **Webcam inference**:
 ```
 python webcam_object_detection.py
 ```

 * **Video inference**: https://youtu.be/X_XVkEqgCUM
 ```
 python video_object_detection.py
 ```


## References:
* YOLOv10 model: https://github.com/THU-MIG/yolov10
