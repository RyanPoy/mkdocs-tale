# neotale/filters.py
from datetime import datetime, date

def format_date(datestr: str, format: str = '%B %d, %Y') -> str:
    date_obj = None
    if isinstance(datestr, (date, datetime)):
        date_obj = datestr
    elif isinstance(datestr, str):
        try:
            date_obj = datetime.strptime("%Y-%m-%d")
        except:
            try:
                date_obj = datetime.strptime("%Y/%m/%d")
            except:
                date_obj = None
    if date_obj is None:
        return datestr
    return date_obj.strftime(format)

FILTERS = {
    'format_date': format_date
}