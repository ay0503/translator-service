from src.translator import translate_content
from unittest.mock import patch

# test implementation assisted with ChatGPT

@patch('src.translator.get_language')
@patch('src.translator.get_translation')
def test_unintelligible_post(self, mock_translation, mock_language):
    # unintelligible input scenario
    mock_language.return_value = "Unintelligible"
    mock_translation.return_value = "Unintelligible"

    input_post = "!!!@@@###"
    expected_result = (False, "Unintelligible")

    result = translate_content(input_post)
    self.assertEqual(result, expected_result)

@patch('src.translator.get_language')
@patch('src.translator.get_translation')
def test_unexpected_language_response(self, mock_translation, mock_language):
    # unexpected response format
    mock_language.return_value = "Unexpected Format"
    mock_translation.return_value = ""

    input_post = "Ceci est un exemple."
    expected_result = (False, "Error processing the request")

    result = translate_content(input_post)
    self.assertEqual(result, expected_result)

@patch('src.translator.get_language')
@patch('src.translator.get_translation')
def test_empty_translation_response(self, mock_translation, mock_language):
    # empty translation response
    mock_language.return_value = "French"
    mock_translation.return_value = ""

    input_post = "Ceci est un exemple."
    expected_result = (False, "Error processing the request")

    result = translate_content(input_post)
    self.assertEqual(result, expected_result)

@patch('src.translator.get_language')
def test_invalid_language_response(self, mock_language):
    # invalid response for language detection
    mock_language.return_value = "InvalidFormat"

    input_post = "Dies ist ein Test."
    expected_result = (False, "Error processing the request")

    result = translate_content(input_post)
    self.assertEqual(result, expected_result)
