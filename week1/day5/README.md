# AI Resume Parser & Candidate Evaluation System

## About the Project

Hiring teams often spend a significant amount of time manually reviewing resumes before identifying suitable candidates. Traditional Applicant Tracking Systems (ATS) mostly rely on keyword matching, which can miss strong candidates whose experience is described differently.

This project uses Large Language Models (LLMs) to understand both job descriptions and resumes semantically. Instead of searching for exact keywords, it extracts structured information from each document and evaluates how well a candidate matches a given role.

The application processes multiple resumes, scores every candidate, and ranks them based on their overall compatibility with the job description.

---

## Features

- Parse resumes from both PDF and DOCX files
- Extract structured information using Pydantic schemas
- Parse job descriptions into structured JSON
- Identify candidate skills, education, projects, certifications, and experience
- Compare resumes against job requirements using an LLM
- Generate an AI-based match score with supporting reasoning
- Rank candidates automatically from highest to lowest score
- Validate all LLM responses using Pydantic models

---

## How It Works

The application follows a simple pipeline:

1. Read the job description.
2. Convert the job description into structured JSON.
3. Read every resume from the `resumes` folder.
4. Extract text from PDF or DOCX files.
5. Parse each resume into a structured format using an LLM.
6. Compare the parsed resume with the job description.
7. Generate a compatibility score and evaluation.
8. Sort candidates based on their final score.

---

## Architecture

```text
                     Job Description
                             │
                             ▼
                     LLM + Pydantic
                             │
                             ▼
                  Structured Job Data
                             │
                             │
      ┌──────────────────────┴──────────────────────┐
      │                                             │
      ▼                                             ▼
 Resume PDF                                   Resume DOCX
      │                                             │
      └────────────── Text Extraction ──────────────┘
                             │
                             ▼
                     Resume Parser (LLM)
                             │
                             ▼
                Structured Candidate Data
                             │
                             ▼
                Candidate Matching Engine
                             │
                             ▼
                  Match Score & Feedback
                             │
                             ▼
                    Candidate Ranking
```

---

## Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| LLM | Groq API (GPT-OSS-120B) |
| Data Validation | Pydantic |
| PDF Parsing | PyPDF |
| Word Parsing | python-docx |
| Environment | python-dotenv |

---

## Project Structure

```text
day5/
│
├── resume_parser.py
├── requirements.txt
├── README.md
├── .env
│
└── resumes/
    ├── resume1.pdf
    ├── resume2.pdf
    └── resume3.docx
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/your-username/your-repository.git
```

Move into the project directory.

```bash
cd week1/day5
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the environment.

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install the required packages.

```bash
pip install -r requirements.txt
```

Create a `.env` file.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Running the Project

Place all resumes inside the `resumes` folder.

Example:

```text
resumes/
├── Alice.pdf
├── Bob.pdf
└── Charlie.docx
```

Run the application.

```bash
python resume_parser.py
```

The program will:

- Parse the job description
- Process every resume
- Generate structured candidate data
- Evaluate each candidate
- Produce a compatibility score
- Rank all candidates

---

## Example Output

```text
Processing: Alice.pdf

Score: 91%

Matching Skills:
Python
SQL
AWS

Missing Skills:
Docker

Verdict:
Strong match for the role.
```

After processing all resumes, the application displays the highest-ranked and lowest-ranked candidates.

---

## What I Learned

Building this project helped me understand:

- Prompt engineering for structured extraction
- Designing reliable Pydantic schemas
- Validating LLM responses
- Parsing PDF and DOCX documents
- Building AI-powered backend workflows
- Using JSON mode with LLMs
- Ranking candidates using semantic similarity instead of keyword matching

---

## Future Improvements

Some improvements I would like to add in future versions:

- Web interface using Streamlit
- Drag-and-drop resume upload
- Export results to Excel or CSV
- OCR support for scanned resumes
- ATS compatibility analysis
- Skill gap analysis
- Support for multiple job descriptions
- Recruiter dashboard
- Candidate recommendation system
- Interview question generation based on resume

---

## Note

This project is intended as a learning project to explore practical applications of Large Language Models in recruitment workflows. It demonstrates how LLMs, combined with structured validation and document parsing, can automate resume screening and candidate evaluation.
