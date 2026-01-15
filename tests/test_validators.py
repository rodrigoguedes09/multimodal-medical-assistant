"""
Unit tests for validators module
"""
import pytest
from src.utils.validators import (
    is_valid_email,
    is_valid_cpf,
    is_valid_phone,
    is_valid_appointment_time,
    is_valid_patient_data,
    is_valid_appointment_data
)


class TestEmailValidator:
    """Test email validation"""
    
    def test_valid_email(self):
        assert is_valid_email("user@example.com") == True
        assert is_valid_email("test.user@domain.co.uk") == True
        assert is_valid_email("user+tag@example.com") == True
    
    def test_invalid_email(self):
        assert is_valid_email("invalid") == False
        assert is_valid_email("@example.com") == False
        assert is_valid_email("user@") == False
        assert is_valid_email("") == False
        assert is_valid_email(None) == False


class TestCPFValidator:
    """Test CPF validation"""
    
    def test_valid_cpf(self):
        # Valid CPF examples
        assert is_valid_cpf("123.456.789-09") == True
        assert is_valid_cpf("12345678909") == True
    
    def test_invalid_cpf(self):
        assert is_valid_cpf("123.456.789-00") == False
        assert is_valid_cpf("000.000.000-00") == False
        assert is_valid_cpf("111.111.111-11") == False
        assert is_valid_cpf("12345") == False
        assert is_valid_cpf("") == False
        assert is_valid_cpf(None) == False


class TestPhoneValidator:
    """Test phone validation"""
    
    def test_valid_phone(self):
        assert is_valid_phone("11987654321") == True  # Mobile
        assert is_valid_phone("1133334444") == True   # Landline
        assert is_valid_phone("(11) 98765-4321") == True
        assert is_valid_phone("(11) 3333-4444") == True
    
    def test_invalid_phone(self):
        assert is_valid_phone("123") == False
        assert is_valid_phone("") == False
        assert is_valid_phone(None) == False


class TestAppointmentTimeValidator:
    """Test appointment time validation"""
    
    def test_valid_appointment_time(self):
        assert is_valid_appointment_time("2025-01-15 14:30") == True
        assert is_valid_appointment_time("2025-12-31 23:59") == True
    
    def test_invalid_appointment_time(self):
        assert is_valid_appointment_time("2025-01-15") == False
        assert is_valid_appointment_time("14:30") == False
        assert is_valid_appointment_time("invalid") == False
        assert is_valid_appointment_time("") == False
        assert is_valid_appointment_time(None) == False


class TestPatientDataValidator:
    """Test patient data validation"""
    
    def test_valid_patient_data(self):
        valid_data = {
            "name": "John Doe",
            "age": 30,
            "contact": "11987654321"
        }
        assert is_valid_patient_data(valid_data) == True
    
    def test_invalid_patient_data(self):
        # Missing field
        assert is_valid_patient_data({"name": "John", "age": 30}) == False
        
        # Invalid age
        assert is_valid_patient_data({"name": "John", "age": -1, "contact": "123"}) == False
        assert is_valid_patient_data({"name": "John", "age": "30", "contact": "123"}) == False
        
        # Empty name
        assert is_valid_patient_data({"name": "", "age": 30, "contact": "123"}) == False
        
        # Not a dict
        assert is_valid_patient_data(None) == False
        assert is_valid_patient_data("invalid") == False


class TestAppointmentDataValidator:
    """Test appointment data validation"""
    
    def test_valid_appointment_data(self):
        valid_data = {
            "patient_id": 1,
            "date": "2025-01-15",
            "time": "14:30"
        }
        assert is_valid_appointment_data(valid_data) == True
    
    def test_invalid_appointment_data(self):
        # Missing field
        assert is_valid_appointment_data({"patient_id": 1, "date": "2025-01-15"}) == False
        
        # Invalid datetime
        invalid_data = {
            "patient_id": 1,
            "date": "invalid",
            "time": "14:30"
        }
        assert is_valid_appointment_data(invalid_data) == False
        
        # Not a dict
        assert is_valid_appointment_data(None) == False
        assert is_valid_appointment_data("invalid") == False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
