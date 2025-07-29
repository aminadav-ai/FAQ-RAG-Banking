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
    # 1) wire / ACH
    ("What is a same-day domestic wire transfer?",
     "sending money"),
    ("How much does a same-day wire cost?",
     "$"),
    ("What is the daily cutoff time for sending a wire?",
     "time"),
    ("Can I reverse a completed bank transfer?",
     "bank"),
    ("Where can I find my bank’s SWIFT/BIC code?",
     "bank"),

    # 2) credit cards
    ("What is a credit-card grace period?",
     "period"),
    ("How is APR on a credit card calculated?",
     "interest"),
    ("What is a balance-transfer fee?",
     "charge"),
    ("Do cash advances have different fees?",
     "cash"),

    # 3) mortgages / savings
    ("What is PMI and when can I remove it?",
     "PMI"),
    ("How much down payment is required for a conventional mortgage?",
     "20"),
    ("What does FDIC insured up to $250,000 mean?",
     "250,000"),
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

