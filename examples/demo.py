"""
Quick Start Demo — DAL-Aware Agentic RAG for DO-178C Compliance.
"""

from src.agent.dal_agent import DALAwareAgent


def main():
    print("=" * 60)
    print("  DAL-Aware Agentic RAG — DO-178C Compliance Demo")
    print("=" * 60)

    # Initialize agent
    agent = DALAwareAgent()

    # Step 1: Set the project DAL level
    # Change to "B", "C", or "D" for different projects
    agent.set_dal("A")

    # Step 2: Ingest your compliance documents
    # Add your DO-178C PDFs to data/sample_docs/
    print("\n📄 Ingesting compliance documents...")
    agent.ingest_documents("data/sample_docs/")

    # Step 3: Query with full DAL-aware filtering
    queries = [
        "What are the structural coverage requirements?",
        "What verification activities are required?",
        "What are the traceability requirements for DAL-A?",
    ]

    print("\n🤖 Running compliance queries...\n")
    for question in queries:
        print(f"❓ Question: {question}")
        response = agent.query(question)
        print(f"📋 DAL Level: DAL-{response['dal_level']}")
        print(f"📚 Citations: {', '.join(response['citations'])}")
        print(f"💡 Retrieved {len(response['answer_chunks'])} relevant chunks")
        print("-" * 60)


if __name__ == "__main__":
    main()
