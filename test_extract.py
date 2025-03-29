# test_extract.py
import unittest
from extract import text_to_json

sample_text_1 = "v. /-UM-:-EN/ to stay or stand by the side of. Umabay ka ken ni tatang mo. Stand by the side of your father. /MAKI-: KA-/ to stay or stand by the side of. Kinaabay na diay tatang na. He stood by the side of his father. /AG-/ [with pl. subject] to stand side by side. Nagabay diay lakay ken baket. The old man and the old woman stood side by side. /MANGI-: I-/ to put or place by, or take (someone or something) to the side of. Iyabay mo dayta kanyana. Put that by his side."
sample_text_2 = "v. /AG-, MANG-/ to win (in gambling, a contest, etc.). Nangabak diay balasang. The young woman won. /MANG- : PANG--AN/ to win (in gambling, a contest, etc.). Nangabakak ti pisos. I won one peso. Pisos ti pinangabakak. I won one peso. /-UM-:-EN/ to defeat or win over (someone) (in gambling, a contest, etc.). Siak ti immabak kanyana. It was I who defeated him. Isu ti inabak ko. It was he whom I defeated."
sample_text_3 = "[pl. AGAABALAYAN], the term used to designate two parents whose children are married to each other, or the mutual relationship between such parents. Agabalayan kami ken Ana. Ann’s child and my child are married to each other."
sample_text_4 = "[abεnturέro; f. Sp.], n. adventurer, explorer."
sample_text_5 = "v. /AG-/ [with pl. subject] to be joined or placed together facing each other (e.g. hands, plates, shells), to be clasped as hands. Nagakob ti ima na. His hands are clasped. /MANG-: (PAG-)-EN [with pl. go goal] to join or place together the inner side facing each other, to clasp as hands. Sino ti madi mangakob ti ima na? Who does not want to clasp his hands? -- var. AKKOB."
sample_text_6 = "; AGASEM [with singular actor], AGASEN YO [with plural actor], just imagine. Agasem, agsueldo ti dua nga gasut. Just imagine, he earns two hundred (pesos)."
sample_text_7 = "= AGEK + -AN."

class TestTextToJson(unittest.TestCase):
    def test_sample_text_1(self):
        sample_text = sample_text_1
        result = text_to_json(sample_text)
        correct_result = [{'part_of_speech': 'v.', 'definition': 'to stay or stand by the side of.', 'eng_example': 'Stand by the side of your father.', 'ilok_example': 'Umabay ka ken ni tatang mo.', 'conjugation': '/-UM-:-EN/', 'origin': '', 'synonyms': [], 'antonyms': [], 'variations': [], 'cross_reference': '', 'common_forms': [], 'plural_form': ''}, {'part_of_speech': 'v.', 'definition': 'to stay or stand by the side of.', 'eng_example': 'He stood by the side of his father.', 'ilok_example': 'Kinaabay na diay tatang na.', 'conjugation': '/MAKI-: KA-/', 'origin': '', 'synonyms': [], 'antonyms': [], 'variations': [], 'cross_reference': '', 'common_forms': [], 'plural_form': ''}, {'part_of_speech': 'v.', 'definition': 'to stand side by side.', 'eng_example': 'The old man and the old woman stood side by side.', 'ilok_example': 'Nagabay diay lakay ken baket.', 'conjugation': '/AG-/ with pl. subject', 'origin': '', 'synonyms': [], 'antonyms': [], 'variations': [], 'cross_reference': '', 'common_forms': [], 'plural_form': ''}, {'part_of_speech': 'v.', 'definition': 'to put or place by, or take (someone or something) to the side of.', 'eng_example': 'Put that by his side.', 'ilok_example': 'Iyabay mo dayta kanyana.', 'conjugation': '/MANGI-: I-/', 'origin': '', 'synonyms': [], 'antonyms': [], 'variations': [], 'cross_reference': '', 'common_forms': [], 'plural_form': ''}]
        self.assertIsInstance(result, list)
        self.assertEqual(result, correct_result)

    def test_sample_text_2(self):
        sample_text = sample_text_2
        result = text_to_json(sample_text)
        correct_result = [{'part_of_speech': 'v.', 'definition': 'to win (in gambling, a contest, etc.).', 'eng_example': 'The young woman won.', 'ilok_example': 'Nangabak diay balasang.', 'conjugation': '/AG-, MANG-/', 'origin': '', 'synonyms': [], 'antonyms': [], 'variations': [], 'cross_reference': '', 'common_forms': [], 'plural_form': ''}, {'part_of_speech': 'v.', 'definition': 'to win (in gambling, a contest, etc.).', 'eng_example': 'I won one peso.', 'ilok_example': 'Nangabakak ti pisos.', 'conjugation': '/MANG- : PANG--AN/', 'origin': '', 'synonyms': [], 'antonyms': [], 'variations': [], 'cross_reference': '', 'common_forms': [], 'plural_form': ''}, {'part_of_speech': 'v.', 'definition': 'to defeat or win over (someone) (in gambling, a contest, etc.).', 'eng_example': 'It was I who defeated him.', 'ilok_example': 'Siak ti immabak kanyana.', 'conjugation': '/-UM-:-EN/', 'origin': '', 'synonyms': [], 'antonyms': [], 'variations': [], 'cross_reference': '', 'common_forms': [], 'plural_form': ''}]
        self.assertIsInstance(result, list)
        self.assertEqual(result, correct_result)

    def test_sample_text_3(self):
        sample_text = sample_text_3
        result = text_to_json(sample_text)
        correct_result = [{'part_of_speech': '', 'definition': 'the term used to designate two parents whose children are married to each other, or the mutual relationship between such parents.', 'eng_example': 'Ann’s child and my child are married to each other.', 'ilok_example': 'Agabalayan kami ken Ana.', 'conjugation': '', 'origin': '', 'synonyms': [], 'antonyms': [], 'variations': [], 'cross_reference': '', 'common_forms': [], 'plural_form': 'pl. AGAABALAYAN'}]
        self.assertIsInstance(result, list)
        self.assertEqual(result, correct_result)

    def test_sample_text_4(self):
        sample_text = sample_text_4
        result = text_to_json(sample_text)
        correct_result = [{'part_of_speech': 'n.', 'definition': 'adventurer, explorer.', 'eng_example': '', 'ilok_example': '', 'conjugation': '', 'origin': 'abεnturέro; f. Sp.', 'synonyms': [], 'antonyms': [], 'variations': [], 'cross_reference': '', 'common_forms': [], 'plural_form': ''}]
        self.assertIsInstance(result, list)
        self.assertEqual(result, correct_result)

    def test_sample_text_5(self):
        sample_text = sample_text_5
        result = text_to_json(sample_text)
        correct_result = [
            {'part_of_speech': 'v.', 'definition': 'to be joined or placed together facing each other (e.g. hands, plates, shells), to be clasped as hands.', 'eng_example': 'His hands are clasped.', 'ilok_example': 'Nagakob ti ima na.', 'conjugation': '/AG-/ with pl. subject', 'origin': '', 'synonyms': [], 'antonyms': [], 'variations': [], 'cross_reference': '', 'common_forms': [], 'plural_form': ''},
            {'part_of_speech': 'v.', 'definition': 'to join or place together the inner side facing each other, to clasp as hands.', 'eng_example': 'Who does not want to clasp his hands?', 'ilok_example': 'Sino ti madi mangakob ti ima na?', 'conjugation': '/MANG-: (PAG-)-EN with pl. go goal', 'origin': '', 'synonyms': [], 'antonyms': [], 'variations': ['AKKOB'], 'cross_reference': '', 'common_forms': [], 'plural_form': ''}
        ]
        self.assertIsInstance(result, list)
        self.assertEqual(result, correct_result)

    def test_sample_text_6(self):
        sample_text = sample_text_6
        result = text_to_json(sample_text)
        correct_result = [{'part_of_speech': '', 'definition': '[with plural actor] just imagine.', 'eng_example': 'Just imagine, he earns two hundred (pesos).', 'ilok_example': 'Agasem, agsueldo ti dua nga gasut.', 'conjugation': '', 'origin': '', 'synonyms': [], 'antonyms': [], 'variations': [], 'cross_reference': '', 'common_forms': ['AGASEM, AGASEN YO'], 'plural_form': ''}]
        self.assertIsInstance(result, list)
        self.assertEqual(result, correct_result)

    def test_sample_text_7(self):
        sample_text = sample_text_7
        result = text_to_json(sample_text)
        correct_result = [{'part_of_speech': '', 'definition': '', 'eng_example': '', 'ilok_example': '', 'conjugation': '', 'origin': 'AGEK + -AN.', 'synonyms': [], 'antonyms': [], 'variations': [], 'cross_reference': '', 'common_forms': [], 'plural_form': ''}]
        self.assertIsInstance(result, list)
        self.assertEqual(result, correct_result)

if __name__ == '__main__':
    unittest.main()