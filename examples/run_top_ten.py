"""Idea taken from https://www.notion.so/Analogies-Generator-9b046963f52f446b9bef84aa4e416a4c"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.85,
          max_tokens=120)


# Define UI configuration
config = UIConfig(description="Top ten generator",
                  button_text="Generate",
                  placeholder="List of top ten baby names for boys\n\n1.")

demo_web_app(gpt, config)
