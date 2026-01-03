import pytest
from dataclasses import FrozenInstanceError

from domain.models.value_objects import SubjectCode, InvalidSubjectCodeError


class TestSubjectCodeCreation:

    def test_subject_code_creation(self):
        """
        It should create a valid VO for a standard 8-digit UnADM code.
        """
        # Arrange
        # Act
        code = SubjectCode("15141101")
        # Assert
        assert code.value == "15141101"
        assert str(code) == "15141101"


    def test_equality(self):
        """
        Two different instances with the same value must be equal.
        (Identity by Value, not Identity by Memory Address).
        """
        # Arrange & Act
        code1 = SubjectCode("15141101")
        code2 = SubjectCode("15141101")
        # Assert
        assert code1 == code2

    def test_hashability(self):
        """
        It must be usable in sets or as dictionary keys (requires frozen=True).
        """
        code1 = SubjectCode("15141101")
        code2 = SubjectCode("15141101")

        unique_codes = {code1, code2}

        assert len(unique_codes) == 1

    def test_immutability(self):
        """
        It should raise FrozenInstanceError if we try to change the value.
        """
        code = SubjectCode("15141101")

        with pytest.raises(FrozenInstanceError):
            code.value = "00000000"

    # --- UNHAPPY PATHS (Validation Rules) ---

    def test_raises_error_on_empty_string(self):
        with pytest.raises(InvalidSubjectCodeError):
            SubjectCode("")

    def test_raises_error_on_wrong_length_short(self):
        with pytest.raises(InvalidSubjectCodeError):
            SubjectCode("123")

    def test_raises_error_on_wrong_length_long(self):
        with pytest.raises(InvalidSubjectCodeError):
            SubjectCode("123456789")

    def test_raises_error_on_alphanumeric(self):
        with pytest.raises(InvalidSubjectCodeError):
            SubjectCode("1514110A")  # 'A' is invalid

    def test_raises_error_on_special_chars(self):
        with pytest.raises(InvalidSubjectCodeError):
            SubjectCode("1514-101")

    def test_raises_error_on_wrong_prefix(self):
        with pytest.raises(InvalidSubjectCodeError):
            SubjectCode("14151101")

    def test_raises_error_on_wrong_module(self):
        with pytest.raises(InvalidSubjectCodeError):
            SubjectCode("15145101")

    def test_raises_error_on_invalid_semester(self):
        with pytest.raises(InvalidSubjectCodeError):
            SubjectCode("15141901")

    def test_raises_error_on_invalid_subject(self):
        with pytest.raises(InvalidSubjectCodeError):
            SubjectCode("15141149")