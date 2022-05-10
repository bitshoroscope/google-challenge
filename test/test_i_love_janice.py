from google import solution as s


def test_only_lower_case():
    input = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
    expected = "did you see last night's episode?"
    assert expected == s.solution(input)

def test_with_upper_case():
    input = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
    expected = "Yeah! I can't believe Lance lost his job at the colony!!"
    assert expected == s.solution(input)
