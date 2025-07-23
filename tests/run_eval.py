"""Very small smoke test."""
import subprocess, sys
subprocess.run([sys.executable, "-m", "src.ingest"])
subprocess.run([sys.executable, "-m", "src.query"], input=b"What are same day wire fees?\n\n", check=False)
