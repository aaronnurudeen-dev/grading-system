def validate_score(score):
    """
    Check if score is valid (0-100)
    Returns: True if valid, False otherwise
    """
    if 0 <= score <= 100:
        return True
    return False


def calculate_grade(score):
    """
    Calculate grade based on score
    A = 70-100, B = 60-69, C = 50-59, D = 45-49, E = 40-44, F = below 40
    Returns: grade letter
    """
    if score >= 70:
        return 'A'
    elif score >= 60:
        return 'B'
    elif score >= 50:
        return 'C'
    elif score >= 45:
        return 'D'
    elif score >= 40:
        return 'E'
    else:
        return 'F'
