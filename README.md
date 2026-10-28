# Local LLM Log Analyzer (Python + Ollama)

A small Streamlit application that analyzes readable log files using a local Ollama LLM. It calculates basic keyword statistics, sends log chunks to the model, and returns a Markdown incident report with evidence, possible causes, severity, and next diagnostic steps.

## Project directory

```text
ollama_log_analyzer/
├── app.py                 # Streamlit web interface; upload or select a log
├── log_analyzer.py        # Chunking, simple statistics, Ollama API calls
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── logs/                  # Put log files here to use Folder mode
    └── .gitkeep
```

## 1. Prerequisites

- Python 3.10 or newer
- [Ollama](https://ollama.com/) installed and running
- Enough RAM for your selected model

Download a model in a terminal:

```bash
ollama pull llama3.2
```

If Ollama is not already running, start it in another terminal:

```bash
ollama serve
```

Some installations start Ollama automatically; if so, you may not need `ollama serve`.

## 2. Install and run

Open a terminal inside the `ollama_log_analyzer` project folder.

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
ollama pull llama3.2
python -m streamlit run app.py
```

If PowerShell blocks activation, use the environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
ollama pull llama3.2
python -m streamlit run app.py
```

Streamlit prints a local URL, usually `http://localhost:8501`. Open it in your browser.

## 3. Where to import / put log files

**Option A — Upload in the web app:** Open the app and use **Upload a log file**. Choose any readable text log.

**Option B — Put files in the project folder:** Copy logs into this directory:

```text
ollama_log_analyzer/logs/
```

Examples:

```text
ollama_log_analyzer/logs/nginx_error.log
ollama_log_analyzer/logs/application.log
ollama_log_analyzer/logs/syslog
ollama_log_analyzer/logs/server-output.txt
```

Then open the **Analyze files in logs/ folder** tab in the app and select the file.

Supported common extensions include `.log`, `.txt`, `.out`, `.err`, `.json`, and `.csv`; extensionless text files are also listed. Files must be readable text, not binary files.

## 4. Use a different Ollama model

Pull a model first, for example:

```bash
ollama pull qwen2.5:7b
```

Then enter `qwen2.5:7b` in the app's Model name field. Model availability and speed depend on your computer.

You can also set environment variables before launching:

```powershell
$env:OLLAMA_URL="http://localhost:11434"
$env:OLLAMA_MODEL="llama3.2"
python -m streamlit run app.py
```

## 5. What the report contains

- Total lines and simple keyword counts for errors, warnings, timeouts, access issues, and network/DNS clues
- LLM-generated summary of important log evidence
- Possible causes clearly labelled as hypotheses
- Severity assessment and recommended next checks
- Downloadable Markdown report

## Notes and safety

- Processing is intended to be local: the app sends log content to the Ollama server configured in the sidebar. It does not intentionally upload logs to a cloud LLM.
- **Logs can contain secrets** such as tokens, passwords, email addresses, hostnames, or customer data. Redact sensitive values before analysis.
- The model can be wrong. Verify findings against the original logs and monitoring systems before taking action.
- Very large files are chunked and limited to the first 8 chunks (roughly 96,000 characters) to keep analysis manageable.
- This starter project handles readable text logs. It is not a replacement for a SIEM, and it does not safely parse arbitrary binary logs.
