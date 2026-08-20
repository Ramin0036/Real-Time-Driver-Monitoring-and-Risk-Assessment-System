from ultralytics import YOLO


class PhoneDetector:


    def __init__(
        self,
        model_path,
        confidence=0.3,
        imgsz=320
    ):

        self.model = YOLO(model_path)

        self.confidence = confidence

        self.imgsz = imgsz



    def detect(self, frame):

        phone_boxes = []


        results = self.model(
            frame,
            imgsz=self.imgsz,
            conf=self.confidence,
            verbose=False
        )


        for result in results:


            if result.boxes is None:
                continue


            for box in result.boxes:


                cls_id = int(
                    box.cls[0]
                )


                confidence = float(
                    box.conf[0]
                )


                class_name = self.model.names[
                    cls_id
                ]


                if class_name == "cell phone":


                    coords = list(
                        map(
                            int,
                            box.xyxy[0]
                        )
                    )


                    phone_boxes.append(
                        (
                            coords,
                            confidence
                        )
                    )


        return phone_boxes