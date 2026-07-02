#!/usr/bin/env python3
from pathlib import Path
import chromadb

script_dir = Path(__file__).parent
client = chromadb.PersistentClient(path=str(script_dir / "chroma_db"))
col = client.get_or_create_collection('techcorp_rag')

count = col.count()
print(f"\n✅ Documents in database: {count}\n")

if count > 0:
    print("🎉 Database is populated! Ready to run Task 5.")
else:
    print("⚠️ Database is empty. Task 2 may still be running or needs to be completed.")
