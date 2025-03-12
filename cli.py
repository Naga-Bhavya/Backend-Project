import argparse
import csv
from papers_fetcher.api import fetch_papers
from papers_fetcher.parser import parse_paper_data

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed")
    parser.add_argument('query', type=str, help="Search query for PubMed")
    parser.add_argument('-f', '--file', type=str, help="Output CSV file name")
    parser.add_argument('-d', '--debug', action='store_true', help="Enable debug mode")
    args = parser.parse_args()

    paper_ids = fetch_papers(args.query)
    papers = [parse_paper_data(pid) for pid in paper_ids]

    if args.file:
        with open(args.file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=papers[0].keys())
            writer.writeheader()
            writer.writerows(papers)
        print(f"Results saved to {args.file}")
    else:
        for paper in papers:
            print(paper)

if __name__ == "__main__":
    main()
