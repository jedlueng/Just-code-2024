import pandas as pd
from fpdf import FPDF
from datetime import datetime

# Data for the theories
data = [
    ["Maslow's Hierarchy of Needs", "Psychology", 
     "A theory of human motivation that proposes a hierarchy of needs, from basic physiological needs to self-actualization, with the lower levels needing to be satisfied before higher levels can be addressed.", 
     "Physiological needs, Safety needs, Love and belonging, Esteem, Self-actualization", 
     "Abraham Maslow", "1943", 
     "Human motivation, organizational behavior, personal development", 
     "Herzberg's Two-Factor Theory, McClelland's Theory of Needs", 
     "A Theory of Human Motivation by Abraham Maslow"],
    ["Herzberg's Two-Factor Theory", "Psychology", 
     "A theory that identifies two factors that influence job satisfaction: hygiene factors and motivators.", 
     "Hygiene factors, Motivators, Job satisfaction", 
     "Frederick Herzberg", "1959", 
     "Employee motivation, job design, organizational behavior", 
     "Maslow's Hierarchy of Needs, McClelland's Theory of Needs", 
     "The Motivation to Work by Frederick Herzberg"],
    ["McGregor's Theory X and Theory Y", "Psychology", 
     "A theory that proposes two contrasting models of workforce motivation: Theory X (authoritarian) and Theory Y (participative).", 
     "Theory X, Theory Y, Motivation, Management styles", 
     "Douglas McGregor", "1960", 
     "Management, leadership, organizational behavior", 
     "Maslow's Hierarchy of Needs, Herzberg's Two-Factor Theory", 
     "The Human Side of Enterprise by Douglas McGregor"],
    ["Attachment Theory", "Psychology/Developmental Psychology", 
     "A theory that emphasizes the importance of early emotional bonds between a child and their caregiver, which influence the child's social, emotional, and cognitive development.", 
     "Secure attachment, Insecure attachment, Attachment styles", 
     "John Bowlby, Mary Ainsworth", "1950s", 
     "Child development, psychotherapy, relationship counseling", 
     "Object Relations Theory, Developmental Psychology", 
     "Attachment and Loss by John Bowlby, Patterns of Attachment by Mary Ainsworth"],
    ["Psychoanalytic Theory", "Psychology/Psychoanalysis", 
     "A theory that explores the influence of unconscious motives and conflicts on behavior, often focusing on childhood experiences and repressed emotions.", 
     "Unconscious mind, Defense mechanisms, Psychosexual stages", 
     "Sigmund Freud", "Late 19th century", 
     "Psychotherapy, personality development, dream analysis", 
     "Jungian Psychology, Object Relations Theory", 
     "The Interpretation of Dreams by Sigmund Freud"],
    ["Cognitive Dissonance Theory", "Psychology", 
     "A theory that explains the discomfort felt when a person holds conflicting beliefs or behaviors, leading to an alteration in one of the attitudes, beliefs, or behaviors to reduce the discomfort and restore balance.", 
     "Cognitive dissonance, Attitude change, Behavior change", 
     "Leon Festinger", "1957", 
     "Social psychology, behavior change, attitude formation", 
     "Self-Perception Theory, Balance Theory", 
     "A Theory of Cognitive Dissonance by Leon Festinger"],
    ["Obsessive-Compulsive Disorder (OCD) Theory", "Psychology/Mental Health", 
     "A theory that explains OCD as a disorder characterized by intrusive, unwanted thoughts (obsessions) and repetitive behaviors or mental acts (compulsions) aimed at reducing distress or preventing a feared event.", 
     "Obsessions, Compulsions, Anxiety, Cognitive-behavioral patterns", 
     "Various psychologists and psychiatrists", "20th century", 
     "Clinical psychology, psychiatry, cognitive-behavioral therapy (CBT)", 
     "Cognitive Behavioral Therapy (CBT), Anxiety Disorders, Neurobiology of OCD", 
     "Various psychology and psychiatry texts"],
    ["Complex Post-Traumatic Stress Disorder (CPTSD)", "Psychology/Mental Health", 
     "A condition resulting from prolonged exposure to traumatic events, often during childhood, such as chronic abuse, neglect, or domestic violence. CPTSD encompasses the symptoms of PTSD but also includes additional issues such as difficulties with emotional regulation, self-perception, and relational problems.", 
     "Emotional dysregulation, Negative self-concept, Interpersonal difficulties, Chronic trauma", 
     "Judith Herman (prominent proponent), various trauma researchers", "1990s", 
     "Trauma therapy, clinical psychology, mental health treatment", 
     "PTSD, Attachment Theory, Developmental Trauma", 
     "Trauma and Recovery by Judith Herman"],
    ["Conformity", "Psychology", 
     "The act of matching attitudes, beliefs, and behaviors to group norms or societal expectations.", 
     "Social influence, Group pressure, Normative influence, Informational influence", 
     "Solomon Asch", "1951", 
     "Social psychology, group dynamics", 
     "Obedience, Social Identity Theory", 
     "Studies in the Principles of Behavior by Solomon Asch"],
    ["Banality of Evil", "Psychology/Philosophy", 
     "A theory that suggests ordinary people can commit atrocious acts simply by conforming to certain social norms and roles, without the influence of monstrous intentions.", 
     "Ordinary individuals, Evil acts, Conformity, Social roles", 
     "Hannah Arendt", "1963", 
     "Social psychology, ethics, political science", 
     "Milgram's Obedience Study, Conformity", 
     "Eichmann in Jerusalem: A Report on the Banality of Evil by Hannah Arendt"],
    ["Enneagram", "Psychology/Personality Theory", 
     "A model of human personality which is principally understood and taught as a typology of nine interconnected personality types.", 
     "Nine personality types, Core motivations, Stress and growth points", 
     "Various (modern form popularized by Oscar Ichazo, Claudio Naranjo)", "20th century", 
     "Personal development, self-awareness, interpersonal relationships", 
     "Personality Psychology, Jungian Archetypes", 
     "The Enneagram by Helen Palmer, works by Oscar Ichazo and Claudio Naranjo"],
    ["Cognitive Functions (MBTI)", "Psychology/Personality Theory", 
     "A framework for understanding how individuals perceive and judge the world, based on eight cognitive functions (Thinking, Feeling, Sensing, Intuition) and their orientations (Introverted, Extraverted).", 
     "Perception, Judging, Cognitive processes, Personality types", 
     "Carl Jung (basis), Isabel Briggs Myers, Katharine Cook Briggs", "1940s", 
     "Personal development, career counseling, team building", 
     "Jungian Psychology, Myers-Briggs Type Indicator (MBTI)", 
     "Psychological Types by Carl Jung, Gifts Differing by Isabel Briggs Myers"],
    ["4-7-8 Breathing Technique", "Wellness/Meditation", 
     "A breathing exercise that promotes relaxation by regulating the breath. The method involves inhaling for 4 seconds, holding the breath for 7 seconds, and exhaling for 8 seconds.", 
     "Relaxation, Stress reduction, Breathing control", 
     "Dr. Andrew Weil", "Early 2000s", 
     "Stress management, meditation, sleep improvement", 
     "Diaphragmatic Breathing, Mindfulness", 
     "Various wellness and meditation texts, Dr. Andrew Weil's publications"],
    ["Pareto Principle", "Economics/Management", 
     "The principle that 80% of outcomes come from 20% of causes, suggesting a focus on the most impactful factors.", 
     "80/20 rule, Focus, Impact", 
     "Vilfredo Pareto", "1896", 
     "Business management, economics, personal productivity", 
     "Time Management Matrix, Lean Thinking", 
     "Cours d'économie politique by Vilfredo Pareto"],
    ["Eisenhower Matrix", "Time Management/Productivity", 
     "A decision-making tool that helps prioritize tasks by urgency and importance, dividing them into four quadrants to manage workload effectively.", 
     "Urgent vs. important, Prioritization, Time management", 
     "Dwight D. Eisenhower", "Mid-20th century", 
     "Time management, productivity, task management", 
     "Pareto Principle, Getting Things Done (GTD)", 
     "Various time management texts and productivity guides"],
    ["SMART Goals", "Management/Productivity", 
     "A framework for setting clear, attainable goals using specific criteria: Specific, Measurable, Achievable, Relevant, and Time-bound.", 
     "Goal setting, Performance management, Clear objectives", 
     "George T. Doran", "1981", 
     "Personal development, project management, performance management", 
     "Management by Objectives (MBO), OKRs (Objectives and Key Results)", 
     "There’s a S.M.A.R.T. Way to Write Management’s Goals and Objectives by George T. Doran"],
    ["Pygmalion Effect", "Psychology/Education", 
     "The phenomenon where higher expectations lead to an increase in performance.", 
     "Expectations, Self-fulfilling prophecy, Performance", 
     "Robert Rosenthal, Lenore Jacobson", "1968", 
     "Education, management, psychology", 
     "Self-Fulfilling Prophecy, Expectancy Theory", 
     "Pygmalion in the Classroom by Robert Rosenthal and Lenore Jacobson"],
    ["Hawthorne Effect", "Psychology/Management", 
     "The alteration of behavior by the subjects of a study due to their awareness of being observed.", 
     "Observation, Performance, Behavior change", 
     "Elton Mayo", "1930s", 
     "Industrial and organizational psychology, management, research methods", 
     "Observer Effect, Demand Characteristics", 
     "The Human Problems of an Industrial Civilization by Elton Mayo"],
    ["Skin in the Game", "Economics/Finance", 
     "The concept that individuals who are decision makers should share in the consequences of those decisions.", 
     "Risk sharing, Incentives, Accountability", 
     "Nassim Nicholas Taleb", "2018", 
     "Economics, finance, management", 
     "Principal-Agent Problem, Moral Hazard", 
     "Skin in the Game by Nassim Nicholas Taleb"],
    ["Black Swan", "Economics/Finance", 
     "A theory that describes unpredictable, rare events that have a massive impact on society or the economy.", 
     "Unpredictable events, Rare events, High impact", 
     "Nassim Nicholas Taleb", "2007", 
     "Risk management, economics, finance", 
     "Fat Tail Events, Chaos Theory", 
     "The Black Swan by Nassim Nicholas Taleb"],
    ["Deep Work", "Productivity", 
     "The ability to focus without distraction on a cognitively demanding task.", 
     "Focus, Productivity, Cognitive enhancement", 
     "Cal Newport", "2016", 
     "Productivity, time management, cognitive science", 
     "Flow, Time Blocking", 
     "Deep Work by Cal Newport"],
    ["4-Hour Work Week", "Productivity/Lifestyle Design", 
     "A lifestyle design philosophy that advocates for outsourcing, automation, and focusing on the essentials to maximize productivity and enjoy life.", 
     "Outsourcing, Automation, Lifestyle design", 
     "Tim Ferriss", "2007", 
     "Productivity, lifestyle design, entrepreneurship", 
     "Pareto Principle, Lean Startup", 
     "The 4-Hour Work Week by Tim Ferriss"],
    ["Minimalism", "Lifestyle", 
     "A lifestyle that emphasizes living with less to focus on what truly matters.", 
     "Simplicity, Decluttering, Essentialism", 
     "Various proponents", "20th century", 
     "Lifestyle, personal development, environmentalism", 
     "Essentialism, Simple Living", 
     "The Life-Changing Magic of Tidying Up by Marie Kondo"],
    ["Getting Things Done (GTD)", "Productivity", 
     "A time management method that emphasizes capturing all tasks and commitments in a trusted system and processing them effectively.", 
     "Task management, Time management, Productivity", 
     "David Allen", "2001", 
     "Productivity, time management, personal development", 
     "Eisenhower Matrix, Time Blocking", 
     "Getting Things Done by David Allen"],
    ["Flow", "Psychology", 
     "A mental state in which a person performing an activity is fully immersed in a feeling of energized focus, full involvement, and enjoyment.", 
     "Focus, Immersion, Enjoyment", 
     "Mihaly Csikszentmihalyi", "1990", 
     "Psychology, productivity, personal development", 
     "Deep Work, Peak Performance", 
     "Flow: The Psychology of Optimal Experience by Mihaly Csikszentmihalyi"],
    ["Pomodoro Technique", "Productivity", 
     "A time management method that uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks.", 
     "Time management, Focus, Breaks", 
     "Francesco Cirillo", "1980s", 
     "Productivity, time management", 
     "Time Blocking, Deep Work", 
     "The Pomodoro Technique by Francesco Cirillo"],
    ["Chunking", "Psychology", 
     "A process by which individual pieces of information are bound together into a meaningful whole.", 
     "Memory, Learning, Information processing", 
     "George A. Miller", "1956", 
     "Psychology, education, cognitive science", 
     "Cognitive Load Theory, Working Memory", 
     "The Magical Number Seven, Plus or Minus Two by George A. Miller"],
    ["Skin in the Game", "Economics/Finance", 
     "The concept that individuals who are decision makers should share in the consequences of those decisions.", 
     "Risk sharing, Incentives, Accountability", 
     "Nassim Nicholas Taleb", "2018", 
     "Economics, finance, management", 
     "Principal-Agent Problem, Moral Hazard", 
     "Skin in the Game by Nassim Nicholas Taleb"],
    ["Will to Power", "Philosophy", 
     "A concept that describes what Nietzsche may have believed to be the main driving force in humans.", 
     "Power, Ambition, Drive", 
     "Friedrich Nietzsche", "1883", 
     "Philosophy, psychology", 
     "Existentialism, Nihilism", 
     "Thus Spoke Zarathustra by Friedrich Nietzsche"],
    ["Relativism", "Philosophy", 
     "The idea that points of view have no absolute truth or validity, having only relative, subjective value according to differences in perception and consideration.", 
     "Subjectivity, Perspective, Truth", 
     "Protagoras", "5th century BC", 
     "Philosophy, ethics, anthropology", 
     "Cultural Relativism, Subjectivism", 
     "Theaetetus by Plato"],
    ["Existentialism", "Philosophy", 
     "A philosophical theory or approach which emphasizes the existence of the individual person as a free and responsible agent determining their own development through acts of the will.", 
     "Freedom, Choice, Individualism", 
     "Jean-Paul Sartre, Søren Kierkegaard", "19th-20th century", 
     "Philosophy, literature, psychology", 
     "Absurdism, Nihilism", 
     "Being and Nothingness by Jean-Paul Sartre"],
    ["Absurdism", "Philosophy", 
     "A philosophy stating that the efforts of humanity to find meaning in the universe will ultimately fail because no such meaning exists, at least in relation to the individual.", 
     "Meaninglessness, Existence, Human condition", 
     "Albert Camus", "1942", 
     "Philosophy, literature", 
     "Existentialism, Nihilism", 
     "The Myth of Sisyphus by Albert Camus"],
    ["Nihilism", "Philosophy", 
     "The rejection of all religious and moral principles, in the belief that life is meaningless.", 
     "Meaninglessness, Rejection, Pessimism", 
     "Friedrich Nietzsche (popularized)", "19th century", 
     "Philosophy, literature, psychology", 
     "Existentialism, Absurdism", 
     "The Will to Power by Friedrich Nietzsche"],
    ["VO2 Max", "Exercise Physiology", 
     "The maximum rate of oxygen consumption measured during incremental exercise; an indicator of aerobic endurance.", 
     "Oxygen consumption, Endurance, Performance", 
     "Various exercise physiologists", "1920s", 
     "Exercise science, sports performance", 
     "Aerobic Capacity, Cardiorespiratory Fitness", 
     "Physiology of Sport and Exercise by W. Larry Kenney, Jack H. Wilmore, David L. Costill"],
    ["Calories and Muscle Building", "Nutrition/Exercise Science", 
     "The relationship between calorie intake, macronutrient distribution, and muscle hypertrophy.", 
     "Caloric surplus, Protein intake, Muscle hypertrophy", 
     "Various nutritionists and exercise scientists", "20th century", 
     "Nutrition, bodybuilding, sports performance", 
     "Macronutrient Ratios, Energy Balance", 
     "Nutrient Timing: The Future of Sports Nutrition by John Ivy and Robert Portman"],
    ["Kaizen", "Management", 
     "A Japanese business philosophy of continuous improvement of working practices, personal efficiency, etc.", 
     "Continuous improvement, Efficiency, Quality", 
     "Masaaki Imai", "1986", 
     "Business management, manufacturing, personal development", 
     "Lean Manufacturing, Total Quality Management (TQM)", 
     "Kaizen: The Key to Japan's Competitive Success by Masaaki Imai"],
    ["Electional Astrology", "Astrology", 
     "A branch of astrology that determines the most auspicious time to undertake a particular action.", 
     "Timing, Auspicious moments, Astrological aspects", 
     "Various astrologers", "Ancient times", 
     "Astrology, decision making", 
     "Horary Astrology, Natal Astrology", 
     "Electional Astrology: The Art of Timing by Joann Hampar"],
]

# Create DataFrame
df = pd.DataFrame(data, columns=["Theory", "Field/Discipline", "Description", "Key Concepts", "Originator/Proponent", "Date of Origin", "Applications", "Related Theories", "Sources/References"])

# Replace curly quotes and other special characters with ASCII equivalents
def replace_special_characters(text):
    replacements = {
        '\u2019': "'",
        '\u2018': "'",
        '\u201c': '"',
        '\u201d': '"',
        '\u2013': '-',
        '\u2014': '--'
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

for col in df.columns:
    df[col] = df[col].apply(replace_special_characters)

# Define the PDF class
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Comprehensive List of Theories", 0, 1, "C")
        self.ln(10)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, 0, 1, "L")
        self.ln(5)

    def chapter_body(self, body):
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_theory(self, theory, field, description, concepts, proponent, date, applications, related, sources):
        self.add_page()
        self.chapter_title(theory)
        body = f"""Field/Discipline: {field}
Description: {description}
Key Concepts: {concepts}
Originator/Proponent: {proponent}
Date of Origin: {date}
Applications: {applications}
Related Theories: {related}
Sources/References: {sources}
"""
        self.chapter_body(body)

    def add_title_page(self):
        self.add_page()
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Comprehensive List of Theories", 0, 1, "C")
        self.ln(10)
        self.set_font("Arial", "", 12)
        today = datetime.today().strftime('%Y-%m-%d')
        self.multi_cell(0, 10, f"This document provides an in-depth overview of various psychological, management, and philosophical theories. Each theory is accompanied by its description, key concepts, originator, date of origin, applications, related theories, and sources/references.\n\nMade by Jedsada, curated by ChatGPT-4\nDate: {today}")
        self.ln(10)

    def add_table_of_contents(self):
        self.add_page()
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Table of Contents", 0, 1, "C")
        self.ln(10)
        self.set_font("Arial", "", 10)
        for i, row in enumerate(df.itertuples(), 1):
            self.cell(0, 10, f"{i}. {row.Theory}", 0, 1, "L")
        self.ln(10)

# Create a PDF object
pdf = PDF()

# Set title
pdf.set_title("Comprehensive List of Theories")

# Add the title page
pdf.add_title_page()

# Add the table of contents
pdf.add_table_of_contents()

# Add theories to the PDF
for _, row in df.iterrows():
    pdf.add_theory(row["Theory"], row["Field/Discipline"], row["Description"], row["Key Concepts"], 
                   row["Originator/Proponent"], row["Date of Origin"], row["Applications"], 
                   row["Related Theories"], row["Sources/References"])

# Save the PDF to a file
pdf_output_path = "Comprehensive_List_of_Theories.pdf"
pdf.output(pdf_output_path)

print(f"PDF generated successfully: {pdf_output_path}")
