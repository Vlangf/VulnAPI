from fastapi import Query, APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get('/search', response_class=HTMLResponse)
def search(query: str = Query(...)):
    """
    XSS
    """
    result = f'Search results for "{query}"'
    return f'<html><body><h1>{result}</h1></body></html>'

@router.get('/search_1', response_class=HTMLResponse)
def search(query: str = Query(...)):
    """
    XSS
    """
    result = f'Search results for "{query}"'
    return f'<html><body><h1>{result}</h1></body></html>'

@router.get('/search_2', response_class=HTMLResponse)
def search(query: str = Query(...)):
    """
    XSS
    """
    result = f'Search results for "{query}"'
    return f'<html><body><h1>{result}</h1></body></html>'

@router.get('/search_3', response_class=HTMLResponse)
def search(query: str = Query(...)):
    """
    XSS
    """
    result = f'Search results for "{query}"'
    return f'<html><body><h1>{result}</h1></body></html>'

@router.get('/search_4', response_class=HTMLResponse)
def search(query: str = Query(...)):
    """
    XSS
    """
    result = f'Search results for "{query}"'
    return f'<html><body><h1>{result}</h1></body></html>'

@router.get('/search_5', response_class=HTMLResponse)
def search(query: str = Query(...)):
    """
    XSS
    """
    result = f'Search results for "{query}"'
    return f'<html><body><h1>{result}</h1></body></html>'

@router.get('/search_6', response_class=HTMLResponse)
def search(query: str = Query(...)):
    """
    XSS
    """
    result = f'Search results for "{query}"'
    return f'<html><body><h1>{result}</h1></body></html>'

@router.get('/search_7', response_class=HTMLResponse)
def search(query: str = Query(...)):
    """
    XSS
    """
    result = f'Search results for "{query}"'
    return f'<html><body><h1>{result}</h1></body></html>'

@router.get('/search_8', response_class=HTMLResponse)
def search(query: str = Query(...)):
    """
    XSS
    """
    result = f'Search results for "{query}"'
    return f'<html><body><h1>{result}</h1></body></html>'

@router.get('/search_9', response_class=HTMLResponse)
def search(query: str = Query(...)):
    """
    XSS
    """
    result = f'Search results for "{query}"'
    return f'<html><body><h1>{result}</h1></body></html>'

@router.get('/search_10', response_class=HTMLResponse)
def search(query: str = Query(...)):
    """
    XSS
    """
    result = f'Search results for "{query}"'
    return f'<html><body><h1>{result}</h1></body></html>'

@router.get('/search_11', response_class=HTMLResponse)
def search(query: str = Query(...)):
    """
    XSS
    """
    result = f'Search results for "{query}"'
    return f'<html><body><h1>{result}</h1></body></html>'


@router.get('/search/1', response_class=HTMLResponse)
def search(query: str = Query(...)):
    """
    XSS
    """
    result = f'Search results for "{query}"'
    return f'<html><body><h1>{result}</h1></body></html>'

@router.get('/search/2', response_class=HTMLResponse)
def search(query: str = Query(...)):
    """
    XSS
    """
    result = f'Search results for "{query}"'
    return f'<html><body><h1>{result}</h1></body></html>'

@router.get('/search/3', response_class=HTMLResponse)
def search(query: str = Query(...)):
    """
    XSS
    """
    result = f'Search results for "{query}"'
    return f'<html><body><h1>{result}</h1></body></html>'