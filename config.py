import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = "gpt-4"  # or "gpt-4o", "gpt-3.5-turbo"

# LangSmith Configuration (for AI monitoring and tracing)
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2", "false").lower() == "true"
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY", "")
LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT", "ai-safety-compliance-officer")
LANGCHAIN_ENDPOINT = os.getenv("LANGCHAIN_ENDPOINT", "https://api.smith.langchain.com")

# Set LangSmith environment variables if enabled
if LANGCHAIN_TRACING_V2 and LANGCHAIN_API_KEY:
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
    os.environ["LANGCHAIN_PROJECT"] = LANGCHAIN_PROJECT
    os.environ["LANGCHAIN_ENDPOINT"] = LANGCHAIN_ENDPOINT
    print("✅ LangSmith monitoring enabled")
else:
    print("ℹ️  LangSmith monitoring disabled (set LANGCHAIN_TRACING_V2=true and LANGCHAIN_API_KEY in .env to enable)")

# Email Configuration
EMAIL_ENABLED = True
SMTP_SERVER = "smtp.gmail.com"  # Change for Outlook: smtp.office365.com
SMTP_PORT = 587
EMAIL_SENDER = os.getenv("EMAIL_SENDER", "")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "")  # Use App Password for Gmail
EMAIL_RECIPIENTS = os.getenv("EMAIL_RECIPIENTS", "").split(",")  # Comma-separated emails

# Site Configuration
SITE_NAME = "Construction Site A"
SITE_LOCATION = "Zone 3, Building B"
COMPANY_NAME = "Your Construction Company"

# Detection Configuration
CONFIDENCE_THRESHOLD = 0.5  # Minimum confidence for violation detection
MODEL_PATH = "models/best.onnx"
VIDEO_SOURCE = 0  # 0 for webcam, or path to video file, or RTSP URL

# Violation Classes (what to monitor)
VIOLATION_CLASSES = {
    "no_helmet": "Worker without hard hat/helmet",
    "no_vest": "Worker without safety vest",
    "no_goggles": "Worker without safety goggles",
    "no_gloves": "Worker without safety gloves",
    "no_boots": "Worker without safety boots"
}

# OSHA Regulations Mapping
OSHA_REGULATIONS = {
    "no_helmet": "29 CFR 1926.100(a) - Head Protection",
    "no_vest": "29 CFR 1926.201 - High-Visibility Safety Apparel",
    "no_goggles": "29 CFR 1926.102 - Eye and Face Protection",
    "no_gloves": "29 CFR 1926.95 - Hand Protection",
    "no_boots": "29 CFR 1926.96 - Foot Protection"
}

# Report Configuration
REPORTS_DIR = "reports"
VIOLATIONS_DIR = "violations"
DATABASE_PATH = "violations.db"

# Detection Settings
FRAME_SKIP = 30  # Process every Nth frame for performance (higher = faster, but may miss violations)
VIOLATION_COOLDOWN = 300  # Seconds before same violation can be reported again
SAVE_VIOLATION_IMAGES = True

# CPU Optimization Settings (for systems without GPU)
RESIZE_FRAME = True  # Resize frames before detection for speed
RESIZE_WIDTH = 640  # Width to resize (smaller = faster, 640 is good balance)
RESIZE_HEIGHT = 480  # Height to resize
USE_HALF_PRECISION = False  # FP16 (only works on GPU, keep False for CPU)
MAX_DETECTIONS = 50  # Limit number of detections per frame (lower = faster)
IOU_THRESHOLD = 0.45  # Intersection over Union threshold for NMS (higher = fewer boxes)
ENABLE_TRACKING = False  # Disable object tracking for speed (tracking adds overhead)

# Create necessary directories
os.makedirs(REPORTS_DIR, exist_ok=True)
os.makedirs(VIOLATIONS_DIR, exist_ok=True)
os.makedirs("models", exist_ok=True)
