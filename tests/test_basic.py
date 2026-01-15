"""
Basic smoke tests for Medical Automation API
"""
import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestImports:
    """Test that all modules can be imported"""
    
    def test_import_config(self):
        """Test importing config module"""
        from config import settings
        assert hasattr(settings, 'DATABASE_URL')
        assert hasattr(settings, 'API_VERSION')
    
    def test_import_models(self):
        """Test importing model modules"""
        from src.models import patient, appointment
        assert hasattr(patient, 'Patient')
        assert hasattr(appointment, 'Doctor')
        assert hasattr(appointment, 'Appointment')
    
    def test_import_services(self):
        """Test importing service modules"""
        from src.services import cache_service
        assert hasattr(cache_service, 'cache_service')
    
    def test_import_validators(self):
        """Test importing validators module"""
        from src.utils import validators
        assert hasattr(validators, 'is_valid_email')
        assert hasattr(validators, 'is_valid_cpf')


class TestSettings:
    """Test configuration settings"""
    
    def test_api_version(self):
        """Test API version is set"""
        from config.settings import API_VERSION
        assert API_VERSION == "v1"
    
    def test_database_url(self):
        """Test database URL is configured"""
        from config.settings import DATABASE_URL
        assert DATABASE_URL is not None
        assert len(DATABASE_URL) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
