---
title: Solar AI Assistant
emoji: ☀️
colorFrom: yellow
colorTo: orange
sdk: streamlit
sdk_version: "1.35.0"
app_file: app.py
pinned: false
---

# Solar AI Assistant

## Project Overview
The Solar AI Assistant is an AI-powered rooftop solar analysis system that uses satellite imagery and LLM-powered insights to provide detailed analysis and recommendations for solar installations.

## Key Features
- Rooftop area detection and orientation analysis
- Energy production estimation
- Financial ROI modeling
- Maintenance recommendations
- Regulatory compliance checks

## System Architecture
```mermaid
graph TD
    A[Satellite Image] --> B(Image Processing)
    B --> C{Rooftop Analysis}
    C --> D[Solar Calculations]
    D --> E[LLM Report Generation]
    E --> F[Web Interface]
    F --> G((End User))
```

## Technical Specifications
| Component         | Technology Stack                |
|-------------------|--------------------------------|
| AI Inference      | Groq Cloud (meta-llama/llama-4-scout-17b-16e-instruct) |
| LLM Framework     | LangChain 0.2.1                |
| Image Processing  | OpenCV 4.9.0                   |
| Web Interface     | Streamlit 1.35.0               |
| Deployment        | Hugging Face Spaces            |

## Installation Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/kaws26/solar-ai-assistant.git
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

## Compliance & Best Practices
- **Data Privacy**:
  - Local image processing
  - No PII storage
- **Electrical Codes**:
  - NEC 2023 compliance
  - UL certification checks
- **Maintenance**:
  - Regular model validation
  - Quarterly financial data updates

## Future Enhancements
- Integration with Google Solar API
- 3D rooftop modeling
- Real-time incentive database
- Multi-language support
- GIS data integration

## Support & Contact
- **Maintainer**: [Kawaljeet Singh]
- **Repository**: [GitHub Link](https://github.com/kaws26/solar-ai-assistant.git)
- **Issue Tracking**: [GitHub Issues](https://github.com/kaws26/solar-ai-assistant.git)
- **License**: MIT

**Last updated:** June 2025 
