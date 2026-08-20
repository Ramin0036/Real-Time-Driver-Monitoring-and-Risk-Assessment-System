import csv
import time


class PerformanceLogger:


    def __init__(self, filename):

        self.filename = filename


        self.start_time = time.strftime(
            "%Y-%m-%d %H:%M:%S"
        )


        with open(
            self.filename,
            "a",
            newline=""
        ) as f:


            writer = csv.writer(f)


            writer.writerow(
                [
                    "timestamp",
                    "frame",
                    "fps",
                    "latency_ms",
                    "yolo_inference_ms",
                    "face_mesh_ms",
                    "cpu_usage_percent"
                ]
            )


    def log(
        self,
        frame_number,
        fps,
        latency,
        yolo_time,
        face_mesh_time,
        cpu_usage
    ):


        timestamp = time.strftime(
            "%Y-%m-%d %H:%M:%S"
        )


        with open(
            self.filename,
            "a",
            newline=""
        ) as f:


            writer = csv.writer(f)


            writer.writerow(
                [
                    timestamp,
                    frame_number,
                    round(fps,2),
                    round(latency,2),
                    round(yolo_time,2),
                    round(face_mesh_time,2),
                    round(cpu_usage,2)
                ]
            )