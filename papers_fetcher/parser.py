import requests
from typing import Dict

def parse_paper_data(paper_id: str) -> Dict[str, str]:
    """
    Parse paper details from PubMed given the paper ID.
    """
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    params = {
        'db': 'pubmed',
        'id': paper_id,
        'retmode': 'json'
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    data = response.json()['result'][paper_id]
    return {
        'PubmedID': paper_id,
        'Title': data.get('title', ''),
        'PublicationDate': data.get('pubdate', ''),
    }
