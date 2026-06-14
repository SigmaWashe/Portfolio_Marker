import datetime


def get_center_number(full_token_string) -> int:
    return int(str(full_token_string)[2:-6])


def format_exam_date(date_str: str) -> str:
    if not date_str:
        return ""
    try:
        dt = datetime.datetime.strptime(date_str.strip(), "%Y-%m-%d")
        return dt.strftime("%d-%m")
    except ValueError:
        return date_str