import cv2
import numpy as np

from perception.landmarks import (
    MODEL_POINTS,
    POSE_LANDMARK_IDS
)


# ============================================================
# BASIC GEOMETRY
# ============================================================

def euclidean(p1, p2):

    return np.linalg.norm(
        np.array(p1) -
        np.array(p2)
    )



# ============================================================
# EAR
# ============================================================

def eye_aspect_ratio(
        landmarks,
        idxs,
        w,
        h
):

    pts = [
        (
            landmarks[i].x * w,
            landmarks[i].y * h
        )
        for i in idxs
    ]


    p1, p2, p3, p4, p5, p6 = pts


    vertical1 = euclidean(
        p2,
        p6
    )

    vertical2 = euclidean(
        p3,
        p5
    )

    horizontal = euclidean(
        p1,
        p4
    )


    if horizontal == 0:
        return 0.0


    return (
        vertical1 +
        vertical2
    ) / (
        2.0 *
        horizontal
    )



# ============================================================
# MAR
# ============================================================

def mouth_aspect_ratio(
        landmarks,
        idxs,
        w,
        h
):

    top, bottom, left, right = [
        (
            landmarks[i].x * w,
            landmarks[i].y * h
        )
        for i in idxs
    ]


    vertical = euclidean(
        top,
        bottom
    )


    horizontal = euclidean(
        left,
        right
    )


    if horizontal == 0:
        return 0.0


    return vertical / horizontal



# ============================================================
# HEAD POSE
# ============================================================

def get_head_pose(
        landmarks,
        w,
        h
):

    image_points = np.array(
        [
            (
                landmarks[i].x * w,
                landmarks[i].y * h
            )
            for i in POSE_LANDMARK_IDS
        ],
        dtype=np.float64
    )


    focal_length = w

    center = (
        w / 2,
        h / 2
    )


    camera_matrix = np.array(
        [
            [
                focal_length,
                0,
                center[0]
            ],
            [
                0,
                focal_length,
                center[1]
            ],
            [
                0,
                0,
                1
            ]
        ],
        dtype=np.float64
    )


    dist_coeffs = np.zeros(
        (4,1)
    )


    success, rotation_vec, _ = cv2.solvePnP(
        MODEL_POINTS,
        image_points,
        camera_matrix,
        dist_coeffs,
        flags=cv2.SOLVEPNP_ITERATIVE
    )


    if not success:
        return 0.0,0.0,0.0


    rotation_mat,_ = cv2.Rodrigues(
        rotation_vec
    )


    proj_matrix = np.hstack(
        (
            rotation_mat,
            np.zeros(
                (3,1)
            )
        )
    )


    euler_angles = cv2.decomposeProjectionMatrix(
        proj_matrix
    )[6]


    pitch,yaw,roll = [
        float(a)
        for a in euler_angles
    ]


    if pitch > 90:
        pitch -= 180

    elif pitch < -90:
        pitch += 180


    return pitch,yaw,roll



# ============================================================
# GAZE
# ============================================================

def gaze_offset(
        landmarks,
        iris_idxs,
        eye_idxs,
        w,
        h
):

    iris_pts = np.array(
        [
            (
                landmarks[i].x*w,
                landmarks[i].y*h
            )
            for i in iris_idxs
        ]
    )


    iris_center = iris_pts.mean(
        axis=0
    )


    eye_pts = np.array(
        [
            (
                landmarks[i].x*w,
                landmarks[i].y*h
            )
            for i in eye_idxs
        ]
    )


    eye_left = eye_pts[:,0].min()

    eye_right = eye_pts[:,0].max()


    eye_width = (
        eye_right -
        eye_left
    )


    if eye_width == 0:
        return 0.0


    relative = (
        iris_center[0] -
        eye_left
    ) / eye_width


    return (
        relative -
        0.5
    ) * 2.0