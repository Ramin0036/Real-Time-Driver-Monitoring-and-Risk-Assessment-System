from utils.geometry import calculate_iou


class FaceTracker:

    def __init__(self):

        self.next_id = 1

        self.previous_box = None

        self.current_id = None


    def update(self, bbox):

        if self.previous_box is None:

            self.current_id = self.next_id

            self.next_id += 1


        else:

            iou = calculate_iou(
                self.previous_box,
                bbox
            )


            if iou < 0.20:

                self.current_id = self.next_id

                self.next_id += 1


        self.previous_box = bbox

        return self.current_id