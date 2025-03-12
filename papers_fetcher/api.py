import requests
from typing import List, Dict, Optional


def fetch_papers(query: str) -> List[Dict[str, str]]:
    """
    Fetch papers from PubMed API based on the query.
    """
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        'db': 'pubmed',
        'term': query,
        'retmode': 'json',
        'retmax': 50,
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return response.json()['esearchresult']['idlist']