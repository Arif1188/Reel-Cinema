from typing import List, Any

def paginate(queryset: List[Any], page: int = 1, page_size: int = 20):
    total = len(queryset)
    start = (page - 1) * page_size
    end = start + page_size
    items = queryset[start:end]
    return {
        "items": items,
        "total": total,
        "page": page,
        "page_size": page_size,
        "pages": (total + page_size - 1) // page_size
    }