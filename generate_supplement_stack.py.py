import subprocess
import sys

# Ensure the reportlab library is installed
try:
    import reportlab
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])
    import reportlab

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def create_pdf(file_path):
    pdf = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # Register a font with emojis support
    pdfmetrics.registerFont(TTFont('Arial', 'Arial Unicode.ttf'))

    pdf.setFont("Arial", 14)
    pdf.drawString(100, height - 50, "June 2024 Supplement Stack")

    y = height - 80

    stack_with_emojis_and_purpose = {
        "General Health and Wellness 🏥": [
            ("Multi Vitamins 💊", "General health and wellness"),
            ("Vitamin D ☀️", "Support bone health and immune function"),
            ("Vitamin C 🍊", "Boost immune system and antioxidant support"),
            ("Calcium 🦴", "Support bone health"),
            ("Magnesium 🧂", "Support muscle function and prevent cramps"),
            ("Fish Oil DHA 1000 🐟", "Support heart and brain health")
        ],
        "Cognitive Function and Mental Health 🧠": [
            ("Gingko 🍃", "Enhance cognitive function and memory"),
            ("Bacopa 🌿", "Improve cognitive function and reduce anxiety"),
            ("St. John's Wort 🌼", "Improve mood and alleviate depression"),
            ("L-Theanine 🍵", "Promote relaxation and reduce stress"),
            ("L-Tyrosine 🧬", "Support cognitive function and stress response")
        ],
        "Physical Performance and Muscle Support 💪": [
            ("Creatine ⚡", "Improve physical performance and muscle mass"),
            ("Protein Bar 🍫", "Convenient protein intake for muscle repair and growth"),
            ("Protein Whey 🥛", "Protein intake for muscle repair and growth"),
            ("CLA (Conjugated Linoleic Acid) 🧈", "Support fat loss and improve body composition"),
            ("Electrolytes Tablets 💧", "Maintain hydration and electrolyte balance")
        ],
        "Skin, Joint, and Relaxation Support 🌟": [
            ("Collagen 🧴", "Improve skin health and joint support"),
            ("Kava 🍵", "Reduce anxiety and promote relaxation")
        ],
        "Energy and Alertness ⚡": [
            ("Energy Drink 🥤", "Boost energy and alertness"),
            ("Coffee ☕", "Increase alertness and focus")
        ]
    }

    for category, items in stack_with_emojis_and_purpose.items():
        pdf.drawString(50, y, category)
        y -= 20
        for item, purpose in items:
            pdf.drawString(70, y, f"- {item}: {purpose}")
            y -= 20
        y -= 10

    pdf.save()

create_pdf("June_2024_Supplement_Stack_with_Emojis_and_Purpose.pdf")
print("PDF generated successfully.")
