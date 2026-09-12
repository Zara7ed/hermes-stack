#!/usr/bin/env python3
"""
Automated deployment script for Hugging Face Space
Runs the full deployment pipeline with embedded credentials
"""
import subprocess
import sys
import os

# Configuration
HF_TOKEN = "HFAkk44lujkjPCZdPJyzMQpvraxInLR"
HF_USERNAME = "zara7ed"
HF_SPACE_NAME = "hermes-stack"

# Set environment variables
os.environ['HF_TOKEN'] = HF_TOKEN
os.environ['HF_USERNAME'] = HF_USERNAME
os.environ['HF_SPACE_NAME'] = HF_SPACE_NAME
os.environ['DRY_RUN'] = 'false'
os.environ['PRIVATE_SPACE'] = 'false'

# Optional secrets (empty for now)
optional_secrets = {
    'TELEGRAM_BOT_TOKEN': '',
    'TELEGRAM_ALLOWED_USERS': '',
    'HERMES_API_KEY': '',
    'NINEROUTER_API_KEY': '',
    'OMNI_ROUTER_KEY': '',
    'OMNI_ADMIN_PASSWORD': '',
    'ROUTER_INITIAL_PASSWORD': '',
    'DASHBOARD_USERNAME': '',
    'DASHBOARD_PASSWORD': '',
    'BACKUP_REPO': '',
    'HERMES_MODEL': '',
    'HERMES_TIMEZONE': '',
    'OMNI_ENABLED': '',
    'HERMES_WEB_BACKEND': '',
}

for key, value in optional_secrets.items():
    os.environ[key] = value

print("🚀 Starting Hermes Stack deployment...")
print(f"Target Space: https://huggingface.co/spaces/{HF_USERNAME}/{HF_SPACE_NAME}")
print()

# Run the provisioning script
result = subprocess.run(
    [sys.executable, "scripts/provision_space.py"],
    cwd=os.path.dirname(__file__) or "."
)

sys.exit(result.returncode)
