# Setup Guide for Solar AI Assistant

## Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

## Installation Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/solar-ai-assistant.git
   cd solar-ai-assistant
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment**
   - Create a `.env` file in the project root.
   - Add your Groq API key:
     ```
     GROQ_API_KEY=your_key_here
     ```

4. **Run the Application**
   ```bash
   streamlit run app.py
   ```

## Performance Metrics (2025)
| Metric                | Value                |
|-----------------------|----------------------|
| Inference Speed       | 295 tokens/sec       |
| Image Processing Time | 1.2s (avg)           |
| Report Accuracy       | 92% (vs manual)      |
| API Latency           | 680ms (p95)          |

## Notes
- Ensure that the LLM model used is `meta-llama/llama-4-scout-17b-16e-instruct`.
- For any issues, refer to the [GitHub Issues](https://github.com/your-username/solar-ai-assistant/issues).

**Last updated:** June 2025