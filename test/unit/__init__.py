import unittest
from unittest.mock import patch
from src.translator import translate_content
from sentence_transformers import SentenceTransformer, util

class TestQueryLLM(unittest.TestCase):
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    @patch('src.translator.get_language')
    @patch('src.translator.get_translation')
    def test_normal_translation(self, mock_translation, mock_language):
        # Mocking responses
        mock_language.return_value = "French"
        mock_translation.return_value = "This is an example."

        # Input and expected result
        input_post = "Ceci est un exemple."
        expected_result = (False, "This is an example.")

        # Call the function
        result = translate_content(input_post)
        self.assertEqual(result, expected_result)

    @patch('src.translator.get_language')
    def test_english_post(self, mock_language):
        # Mocking language detection as English
        mock_language.return_value = "English"

        # Input and expected result
        input_post = "This is a test."
        expected_result = (True, "This is a test.")

        # Call the function
        result = translate_content(input_post)
        self.assertEqual(result, expected_result)

    def cosine_similarity(self, expected: str, actual: str) -> float:
        """Compute the cosine similarity between two sentences."""
        embedding_expected = self.model.encode(expected)
        embedding_actual = self.model.encode(actual)
        return util.cos_sim(embedding_expected, embedding_actual).item()


