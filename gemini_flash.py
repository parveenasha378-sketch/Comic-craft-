import os
import json
import re
from dotenv import load_dotenv

load_dotenv()

USE_MOCK = os.getenv("USE_MOCK", "true").lower() == "true"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def get_gemini_flash_model():
    """
        Load Gemini 1.5 Flash model
            models/gemini-1.5-flash
                """
                    if USE_MOCK or not GEMINI_API_KEY:
                            return None
                                try:
                                        import google.generativeai as genai
                                                genai.configure(api_key=GEMINI_API_KEY)
                                                        model = genai.GenerativeModel("models/gemini-1.5-flash")
                                                                return model
                                                                    except Exception as e:
                                                                            print(f"[gemini_flash] Model load failed, using MOCK: {e}")
                                                                                    return None

                                                                                    def generate_outline(story_prompt, character_name, setting, story_tone, art_style):
                                                                                        """
                                                                                            Generate 5-panel comic outline using Gemini Flash
                                                                                                Output: List of panels with Panel #, Title, Scene Description, Image Prompt
                                                                                                    """
                                                                                                        model = get_gemini_flash_model()

                                                                                                            # MOCK MODE - Works without API key
                                                                                                                if model is None:
                                                                                                                        print("[gemini_flash] Using MOCK outlines")
                                                                                                                                return [
                                                                                                                                            {
                                                                                                                                                            "panel_number": 1,
                                                                                                                                                                            "title": f"Panel 1: {character_name} Begins Journey",
                                                                                                                                                                                            "scene_description": f"{character_name} in {setting}, starting the adventure of {story_prompt}. The tone is {