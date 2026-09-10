#!/usr/bin/env python3
import json
import urllib.parse
import urllib.request

API = "https://api.semanticscholar.org/graph/v1/paper/search"
UA = "mathmodel-skills/0.1.13 (+https://github.com/mop74720-commits/mathmodel-skills)"

def search(query, limit=20):
    params = {
        "query": query,
        "limit": max(1, min(int(limit), 100)),
        "fields": "title,year,authors,venue,citationCount,externalIds,url,openAccessPdf",
    }
    req = urllib.request.Request(
        API + "?" + urllib.parse.urlencode(params),
        headers={"User-Agent": UA, "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=20) as response:
        payload = json.load(response)
    out = []
    for paper in payload.get("data", []):
        ext = paper.get("externalIds") or {}
        oa = paper.get("openAccessPdf") or {}
        out.append({
            "source": "semantic_scholar",
            "title": paper.get("title"),
            "doi": ext.get("DOI"),
            "year": paper.get("year"),
            "url": oa.get("url") or paper.get("url"),
            "authors": [a.get("name") for a in (paper.get("authors") or []) if a.get("name")],
            "venue": paper.get("venue"),
            "type": None,
            "cited_by_count": int(paper.get("citationCount") or 0),
        })
    return out
