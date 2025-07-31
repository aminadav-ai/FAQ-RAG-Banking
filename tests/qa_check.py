"""
Extended batch-QA test (12 questions).
Run:  PYTHONPATH=./src python3 -m tests.qa_check
"""
import re, unicodedata, sys
from src.query import fetch_answer

# ---------- canonicalization ----------
def canonical(text: str) -> str:
    """Lower-case + remove punctuation & accents → 'token soup'."""
    text = unicodedata.normalize("NFKD", text).lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())

# ---------- test cases ----------
TESTS = [
    ("What is a same-day domestic wire transfer?",
     "money")
]

# ---------- runner ----------
passed = 0
for q, expect in TESTS:
    ans = fetch_answer(q) or ""
    ok = canonical(expect) in canonical(ans)
    status = "✔ PASS" if ok else "✖ FAIL"
    print(f"{status} | Q: {q}")
    if not ok:
        print("  Expected snippet:", expect)
        print("  Got answer      :", ans, "\n")
    passed += ok

print(f"\nSummary: {passed}/{len(TESTS)} passed.")
if passed != len(TESTS):
    sys.exit(1)               # non-zero exit code for CI

