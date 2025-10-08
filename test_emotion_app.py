import unittest
from emotion_app_pkg.app import emotion_predictor

class TestEmotionPredictor(unittest.TestCase):
    def test_basic_output(self):
        sample_result = {
            "emotion": {"document": {"emotion": {
                "joy": 0.9, "sadness": 0.1, "anger": 0.0, "fear": 0.0, "disgust": 0.0
            }}}
        }
        expected = {"Joy": 0.9, "Sadness": 0.1, "Anger": 0.0, "Fear": 0.0, "Disgust": 0.0}
        self.assertEqual(emotion_predictor(sample_result), expected)

if __name__ == "__main__":
    unittest.main()
