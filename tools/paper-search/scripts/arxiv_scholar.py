#!/usr/bin/env python3
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

API = "https://export.arxiv.org/api/query"
UA = "mathmodel-skills/0.1.13 (+https://github.com/mop74720-commits/mathmodel-skills)"
NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}

def search(query, limit=20):
    params = {
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": max(1, min(int(limit), 100)),
    }
    req = urllib.request.Request(
        API + "?" + urllib.parse.urlencode(params),
        headers={"User-Agent": UA, "Accept": "application/atom+xml"},
    )
    with urllib.request.urlopen(req, timeout=20) as response:
        root = ET.parse(response).getroot()
    out = []
    for entry in root.findall("atom:entry", NS):
        title = " ".join((entry.findtext("atom:title", default="", namespaces=NS) or "").split())
        published = entry.findtext("atom:published", default="", namespaces=NS) or ""
        authors = [
            a.findtext("atom:name", default="", namespaces=NS)
            for a in entry.findall("atom:author", NS)
        ]
        authors = [a for a in authors if a]
        doi = entry.findtext("arxiv:doi", default=None, namespaces=NS)
        out.append({
            "source": "arxiv",
            "title": title,
            "doi": doi,
            "year": int(published[:4]) if len(published) >= 4 and published[:4].isdigit() else None,
            "url": entry.findtext("atom:id", default=None, namespaces=NS),
            "authors": authors,
            "venue": "arXiv",
            "type": "preprint",
            "cited_by_count": 0,
        })
    return out
