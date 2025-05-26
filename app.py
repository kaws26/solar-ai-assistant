import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from solar_calculations import SolarCalculator
from image_processing import RooftopAnalyzer
from dotenv import load_dotenv
load_dotenv()

def generate_report(analysis_data, cost_data):
    # Load system prompt
    with open('prompts/system_prompt.txt',encoding="utf-8") as f:
        system_prompt = f.read()
    
    # Create LangChain prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "Analysis Data: {analysis}\nCost Data: {cost}")
    ])
    
    # Initialize Groq chat
    chat = ChatGroq(
        temperature=0.2,
        model_name="meta-llama/llama-4-scout-17b-16e-instruct",
        api_key=os.getenv("GROQ_API_KEY")
    )
    
    # Create and invoke chain
    chain = prompt | chat
    response = chain.invoke({
        "analysis": str(analysis_data),
        "cost": str(cost_data)
    })
    
    return response.content

def load_metrics():
    try:
        with open("performance_metrics.md", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return "Performance metrics not available."

def main():
    st.title("Solar Potential Analyzer 🇮🇳")
    st.markdown("Professional rooftop solar analysis for Indian homes, with state-wise subsidies and compliance.")
    
    # User inputs
    uploaded_file = st.file_uploader("Upload rooftop image", type=["jpg", "png"])
    location = st.text_input("Location (City)")
    state = st.selectbox("State", ["Delhi", "Maharashtra", "Karnataka", "Other"])
    energy_rate = st.number_input("Current energy rate (₹/kWh)", value=7.0, min_value=1.0)
    
    if uploaded_file and location and state:
        # Save uploaded file temporarily
        with open("temp_image.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Process image
        analyzer = RooftopAnalyzer()
        rooftop_data = analyzer.analyze_image("temp_image.jpg")
        location_data = {'energy_rate': energy_rate, 'state': state}
        
        # Calculate solar potential
        calculator = SolarCalculator()
        cost_data = calculator.calculate(rooftop_data, location_data)
        
        # Generate report
        with st.spinner("Generating detailed report..."):
            report = generate_report(rooftop_data, cost_data)
        
        # Display results
        st.subheader("Analysis Results")
        st.json({**rooftop_data, **cost_data})
        st.markdown(report)
    
    # Show performance metrics
    st.sidebar.header("Performance Metrics")
    st.sidebar.markdown(load_metrics())

if __name__ == "__main__":
    main()