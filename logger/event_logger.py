import csv
import time
from pathlib import Path


class EventLogger:


    def __init__(self, filename):

        self.filename = filename


        if not Path(filename).exists():

            with open(
                filename,
                "w",
                newline=""
            ) as f:

                writer = csv.writer(f)

                writer.writerow(
                    [
                        "timestamp",
                        "event"
                    ]
                )


    def log(self,event):

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
                    event
                ]
            )


        print(
            f"[EVENT] {event}"
        )