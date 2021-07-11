# face-make-de-identification

### 모델 : YOLOv5 사용 
### 특징
- 기존 연구들과 다르게 '속도' 중심. 빠르다!
    - 기존 연구들이 '정확도'를 중요하게 생각했으나, 실시간 반영 문제가 발생하여 이를 극복하고자 함
    - You Only Look Once
    - Multi-task 문제를 하나의 회귀 문제로 재정의
        - 이미지 전체에 대해서 '하나의 신경망'이 '한번의 계산'으로 'bounding box', 'class probabilty' 예측
            - bounding box: object detection 대상에 빨간 박스
            - class probability: 분류 및 예측하고자하는 대상의 종류와 확률
- 기존 방식들보다 background error가 적다.
    - 기존 'Sliding Window', 'Region proposal' 방식과 다르게, 훈련과 테스트 단계에서 이미지 전체를 인식.
    - 기존 방식의 단점: Background Error(아무 물체가 없는 배경에 반점, 노이즈 등이 있으면 물체로 인식)
- 물체의 일반적인 부분을 학습하기에 다른 모델에 비해 보지 못한 새로운 이미지에 대해 더 robust함
- 단점
    - 다른 모델들에 비해 정확도가 떨어진다.
    
    
![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FlqVvp%2FbtqKv79n5Pr%2FlJJ0EoK0sb8kVrLShiMo7k%2Fimg.png)



## YOLOv5 세부모델의 종류
![img](https://github.com/ultralytics/yolov5/releases/download/v1.0/model_comparison.png)


| Model                                                        | size (pixels) | mAPval 0.5:0.95 | mAPtest 0.5:0.95 | mAPval 0.5 | Speed V100 (ms) |      | params (M) | FLOPS 640 (B) |
| ------------------------------------------------------------ | ------------- | --------------- | ---------------- | ---------- | --------------- | ---- | ---------- | ------------- |
| [YOLOv5s6](https://github.com/ultralytics/yolov5/releases)   | 1280          | 43.3            | 43.3             | 61.9       | **4.3**         |      | 12.7       | 17.4          |
| [YOLOv5m6](https://github.com/ultralytics/yolov5/releases)   | 1280          | 50.5            | 50.5             | 68.7       | 8.4             |      | 35.9       | 52.4          |
| [YOLOv5l6](https://github.com/ultralytics/yolov5/releases)   | 1280          | 53.4            | 53.4             | 71.1       | 12.3            |      | 77.2       | 117.7         |
| [YOLOv5x6](https://github.com/ultralytics/yolov5/releases)   | 1280          | **54.4**        | **54.4**         | **72.0**   | 22.4            |      | 141.8      | 222.9         |
| [YOLOv5x6](https://github.com/ultralytics/yolov5/releases) TTA | 1280          | **55.0**        | **55.0**         | **72.0**   | 70.8            |      | -          | -             |


## <div align="center">Why YOLOv5</div>

<p align="center"><img width="800" src="https://user-images.githubusercontent.com/26833433/114313216-f0a5e100-9af5-11eb-8445-c682b60da2e3.png"></p>
<details>
  <summary>YOLOv5-P5 640 Figure (click to expand)</summary>
  
<p align="center"><img width="800" src="https://user-images.githubusercontent.com/26833433/114313219-f1d70e00-9af5-11eb-9973-52b1f98d321a.png"></p>
</details>
<details>
  <summary>Figure Notes (click to expand)</summary>
  
  * GPU Speed measures end-to-end time per image averaged over 5000 COCO val2017 images using a V100 GPU with batch size 32, and includes image preprocessing, PyTorch FP16 inference, postprocessing and NMS. 
  * EfficientDet data from [google/automl](https://github.com/google/automl) at batch size 8.
  * **Reproduce** by `python test.py --task study --data coco.yaml --iou 0.7 --weights yolov5s6.pt yolov5m6.pt yolov5l6.pt yolov5x6.pt`
</details>




## 네트워크 구조
![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbcD1Ts%2FbtqKBPsHQGp%2FKu8dlxjrsyWFbcjv6XMnqk%2Fimg.png)

- Layer
    - 24 Convolution layers: 이미지 특징 추출
    - 2 Fully-connected layers: 클래스 확률, bounding box 좌표 예측
- '1 x 1 reduction layer' + '3 x 3 convolution layer' GoogLeNet의 네트워크에서 인셉션 구조 대신 사용
- 최종 output(prediction tensors): 7 x 7 x 30
