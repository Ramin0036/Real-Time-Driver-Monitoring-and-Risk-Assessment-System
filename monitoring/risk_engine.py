def calculate_risk(
    drowsy,
    distracted,
    phone,
    yawning,
    long_closure
):

    score = 0


    if drowsy:
        score += 40


    if long_closure:
        score += 25


    if distracted:
        score += 20


    if phone:
        score += 30


    if yawning:
        score += 10


    return min(
        score,
        100
    )



def get_driver_state(
    risk,
    drowsy,
    phone,
    distracted
):

    if phone and risk >= 50:
        return "CRITICAL"


    if drowsy:
        return "DROWSY"


    if distracted:
        return "DISTRACTED"


    if risk >= 40:
        return "WARNING"


    return "SAFE"