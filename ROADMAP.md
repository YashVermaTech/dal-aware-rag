dal-aware-rag/
│
├── README.md                  ← We'll replace this first
├── CONTRIBUTING.md            ← Open source guidelines
├── ROADMAP.md                 ← Future features
├── LICENSE                    ← Already done ✅
├── .gitignore                 ← Already done ✅
├── requirements.txt           ← Python dependencies
│
├── src/
│   ├── agent/
│   │   ├── dal_agent.py       ← Core DAL-aware agent
│   │   └── memory.py          ← DAL context memory
│   ├── rag/
│   │   ├── ingestor.py        ← PDF ingestion pipeline
│   │   ├── retriever.py       ← ChromaDB retrieval + DAL filtering
│   │   └── embeddings.py      ← Sentence-Transformers setup
│   └── utils/
│       └── config.py          ← Config & constants
│
├── data/
│   └── sample_docs/           ← Sample DO-178C docs for testing
│
├── examples/
│   └── demo.py                ← Quick start demo
│
└── tests/
    └── test_agent.py          ← Basic tests
