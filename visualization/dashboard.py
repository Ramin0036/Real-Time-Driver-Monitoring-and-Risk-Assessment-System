import cv2
import numpy as np

from config.settings import DASHBOARD_WIDTH


# ============================================================
# DASHBOARD
# ============================================================

def create_dms_dashboard(
    frame,
    state,
    risk,
    driver_id,
    ear,
    mar,
    gaze,
    yaw,
    pitch,
    blink_count,
    eye_duration,
    phone,
    distracted,
    fps,
    latency,
    yolo_time,
    face_mesh_time,
    cpu_usage
):

    h, w = frame.shape[:2]

    dashboard_width = DASHBOARD_WIDTH

    dashboard = np.zeros(
        (
            h,
            dashboard_width,
            3
        ),
        dtype=np.uint8
    )

    # --------------------------------------------------------
    # Header
    # --------------------------------------------------------

    cv2.putText(
        dashboard,
        "DMS",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.75,
        (255, 255, 255),
        2
    )

    cv2.putText(
        dashboard,
        "DRIVER MONITORING SYSTEM",
        (20, 58),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.38,
        (150, 150, 150),
        1
    )

    cv2.line(
        dashboard,
        (20, 75),
        (
            dashboard_width - 20,
            75
        ),
        (70, 70, 70),
        1
    )

    # --------------------------------------------------------
    # Driver ID
    # --------------------------------------------------------

    cv2.putText(
        dashboard,
        f"Driver ID: #{driver_id or '--'}",
        (20, 105),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.50,
        (220, 220, 220),
        1
    )

    # --------------------------------------------------------
    # State color
    # --------------------------------------------------------

    if state == "SAFE":

        state_color = (
            0,
            220,
            80
        )

    elif state == "WARNING":

        state_color = (
            0,
            180,
            255
        )

    elif state == "DROWSY":

        state_color = (
            0,
            80,
            255
        )

    elif state == "DISTRACTED":

        state_color = (
            0,
            120,
            255
        )

    else:

        state_color = (
            0,
            0,
            255
        )

    # --------------------------------------------------------
    # State
    # --------------------------------------------------------

    cv2.putText(
        dashboard,
        "DRIVER STATE",
        (20, 138),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.40,
        (140, 140, 140),
        1
    )

    cv2.putText(
        dashboard,
        state,
        (20, 168),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.72,
        state_color,
        2
    )

    # --------------------------------------------------------
    # Risk
    # --------------------------------------------------------

    cv2.putText(
        dashboard,
        f"Risk Score: {risk}%",
        (20, 198),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.48,
        (220, 220, 220),
        1
    )

    bar_x = 20
    bar_y = 210

    bar_width = dashboard_width - 40
    bar_height = 12

    cv2.rectangle(
        dashboard,
        (
            bar_x,
            bar_y
        ),
        (
            bar_x + bar_width,
            bar_y + bar_height
        ),
        (60, 60, 60),
        -1
    )

    cv2.rectangle(
        dashboard,
        (
            bar_x,
            bar_y
        ),
        (
            bar_x +
            int(
                bar_width *
                risk /
                100
            ),
            bar_y +
            bar_height
        ),
        state_color,
        -1
    )

    # --------------------------------------------------------
    # Face Analysis
    # --------------------------------------------------------

    y = 260

    cv2.putText(
        dashboard,
        "FACE ANALYSIS",
        (20, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.40,
        (140, 140, 140),
        1
    )

    y += 28

    values = [
        (
            "EAR",
            f"{ear:.3f}"
        ),
        (
            "MAR",
            f"{mar:.3f}"
        ),
        (
            "Gaze",
            f"{gaze:.2f}"
        ),
        (
            "Yaw",
            f"{yaw:.1f} deg"
        ),
        (
            "Pitch",
            f"{pitch:.1f} deg"
        )
    ]

    for name, value in values:

        cv2.putText(
            dashboard,
            name,
            (20, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.43,
            (130, 130, 130),
            1
        )

        cv2.putText(
            dashboard,
            value,
            (115, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.45,
            (230, 230, 230),
            1
        )

        y += 24

    # --------------------------------------------------------
    # Eye analytics
    # --------------------------------------------------------

    y += 8

    cv2.putText(
        dashboard,
        "EYE ANALYTICS",
        (20, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.40,
        (140, 140, 140),
        1
    )

    y += 27

    cv2.putText(
        dashboard,
        f"Blinks: {blink_count}",
        (20, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.45,
        (220, 220, 220),
        1
    )

    y += 24

    cv2.putText(
        dashboard,
        f"Eye closed: {eye_duration:.2f}s",
        (20, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.45,
        (220, 220, 220),
        1
    )

    # --------------------------------------------------------
    # Behavior
    # --------------------------------------------------------

    y += 38

    cv2.putText(
        dashboard,
        "BEHAVIOR",
        (20, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.40,
        (140, 140, 140),
        1
    )

    y += 27

    phone_text = (
        "DETECTED"
        if phone
        else
        "NO"
    )

    phone_color = (
        (0, 165, 255)
        if phone
        else
        (0, 220, 80)
    )

    cv2.putText(
        dashboard,
        f"Phone: {phone_text}",
        (20, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.45,
        phone_color,
        1
    )

    y += 24

    distraction_text = (
        "YES"
        if distracted
        else
        "NO"
    )

    distraction_color = (
        (0, 80, 255)
        if distracted
        else
        (0, 220, 80)
    )

    cv2.putText(
        dashboard,
        f"Distraction: {distraction_text}",
        (20, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.45,
        distraction_color,
        1
    )

    # --------------------------------------------------------
    # Performance
    # --------------------------------------------------------

    y += 38

    cv2.line(
        dashboard,
        (20, y - 12),
        (
            dashboard_width - 20,
            y - 12
        ),
        (70, 70, 70),
        1
    )

    cv2.putText(
        dashboard,
        "PERFORMANCE",
        (20, y + 15),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.40,
        (140, 140, 140),
        1
    )

    cv2.putText(
        dashboard,
        f"FPS: {fps:.1f}",
        (20, y + 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.48,
        (255, 255, 0),
        2
    )

    cv2.putText(
        dashboard,
        f"Latency: {latency:.1f} ms",
        (20, y + 62),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.40,
        (210, 210, 210),
        1
    )

    cv2.putText(
        dashboard,
        f"YOLO: {yolo_time:.1f} ms",
        (20, y + 83),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.40,
        (210, 210, 210),
        1
    )

    cv2.putText(
        dashboard,
        f"Face Mesh: {face_mesh_time:.1f} ms",
        (20, y + 104),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.40,
        (210, 210, 210),
        1
    )

    cv2.putText(
        dashboard,
        f"CPU: {cpu_usage:.1f}%",
        (20, y + 125),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.40,
        (210, 210, 210),
        1
    )

    # --------------------------------------------------------
    # LIVE
    # --------------------------------------------------------

    cv2.circle(
        dashboard,
        (
            dashboard_width - 35,
            30
        ),
        6,
        (0, 220, 80),
        -1
    )

    cv2.putText(
        dashboard,
        "LIVE",
        (
            dashboard_width - 80,
            35
        ),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.40,
        (0, 220, 80),
        1
    )

    # --------------------------------------------------------
    # Combine
    # --------------------------------------------------------

    combined = np.hstack(
        (
            frame,
            dashboard
        )
    )

    return combined
