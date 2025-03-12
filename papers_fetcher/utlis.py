from typing import List

def filter_non_academic(authors: List[str]) -> List[str]:
    """
    Filter out non-academic authors based on simple heuristics.
    """
    return [author for author in authors if 'university' not in author.lower()]