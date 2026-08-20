def get_face_bbox(
    landmarks,
    w,
    h
):

    xs = [
        int(p.x * w)
        for p in landmarks
    ]

    ys = [
        int(p.y * h)
        for p in landmarks
    ]

    return (
        max(0, min(xs)),
        max(0, min(ys)),
        min(w, max(xs)),
        min(h, max(ys))
    )