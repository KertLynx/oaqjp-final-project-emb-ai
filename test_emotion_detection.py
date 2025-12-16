import pytest

from EmotionDetection import emotion_detector

_TEST_CASES = [
    ("I am glad this happened", "joy"),
    ("I am really mad about this", "anger"),
    ("I feel disgusted just hearing about this", "disgust"),
    ("I am so sad about this", "sadness"),
    ("I am really afraid that this will happen", "fear"),
]


@pytest.mark.parametrize(("statement", "expected_dominant"), _TEST_CASES)
def test_emotion_detector(statement: str, expected_dominant: str) -> None:
    result = emotion_detector(statement)
    assert result["dominant_emotion"] == expected_dominant
