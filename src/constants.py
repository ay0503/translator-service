
# Constants
ENGLISH = "english"
NODEBB_TRANSLATION_CONTEXT = """
Please translate the following text into clear and accurate English, while preserving academic terms, platform names, and course-related jargon.

This text is from an online academic discussion board similar to Piazza, where students, TAs (Teaching Assistants), and instructors discuss topics, ask questions, and share information about coursework. If the text includes specific terms related to education (like 'TA', 'coursework', 'exam prep', 'project deadline'), or platform names (like 'Piazza' or 'Canvas'), retain them in the translation without changing their meaning.

Your translation should be student-friendly, as if explaining concepts or instructions in a clear way to help students understand the material or answer their questions. Avoid overly formal language, and focus on readability and clarity while keeping all technical and academic terms accurate.
"""
NODEBB_CLASSIFICATION_CONTEXT = """
Please identify the language of the following text from an academic discussion forum.

This forum is used by students, TAs (Teaching Assistants), and instructors to discuss course-related topics, assignments, and other educational content. The text may contain platform names (like 'Piazza', 'Canvas') and academic abbreviations (like 'TA', 'exam', 'homework'). Do not classify these terms as specific languages; instead, focus on the main language of the text itself.

If the primary language of the text is English, respond with 'English.' If it is in another language, respond with the language name (e.g., 'Spanish', 'French', 'Chinese'). Only respond with the name of a single primary language.
"""