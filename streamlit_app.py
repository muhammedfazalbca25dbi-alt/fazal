import streamlit as st
import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))

# Import and run the main dashboard
exec(open('scripts/muhammed_fazal_w2d5_code.py').read())
