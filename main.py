"""
Main application module for Medical Automation API
Run this file to start the Flask server
"""
from src.app import app
from config.settings import DEBUG

if __name__ == '__main__':
    print("🏥 Medical Automation API")
    print("=" * 50)
    print(f"Server starting on http://0.0.0.0:5000")
    print(f"Debug mode: {DEBUG}")
    print(f"API Documentation: http://0.0.0.0:5000/api/v1/health")
    print("=" * 50)
    
    app.run(debug=DEBUG, host='0.0.0.0', port=5000)
