"""
Validators module for Medical Automation API
Provides validation functions for common data types
"""
import re
from datetime import datetime
from typing import Dict, Any


def is_valid_email(email: str) -> bool:
    """
    Validate email format
    
    Args:
        email: Email address to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not email or not isinstance(email, str):
        return False
    
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


def is_valid_cpf(cpf: str) -> bool:
    """
    Validate Brazilian CPF format
    
    Args:
        cpf: CPF to validate (with or without formatting)
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not cpf or not isinstance(cpf, str):
        return False
    
    # Remove formatting
    cpf = re.sub(r'[^\d]', '', cpf)
    
    # Check length
    if len(cpf) != 11:
        return False
    
    # Check for repeated digits
    if cpf == cpf[0] * 11:
        return False
    
    # Validate check digits
    for i in range(9, 11):
        value = sum((int(cpf[num]) * ((i + 1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != int(cpf[i]):
            return False
    
    return True


def is_valid_phone(phone: str) -> bool:
    """
    Validate Brazilian phone format
    
    Args:
        phone: Phone number to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not phone or not isinstance(phone, str):
        return False
    
    # Remove formatting
    phone = re.sub(r'[^\d]', '', phone)
    
    # Check length (10 or 11 digits for Brazilian phones)
    return len(phone) in [10, 11]


def is_valid_appointment_time(appointment_time: str) -> bool:
    """
    Validate appointment time format
    
    Args:
        appointment_time: Time string in format 'YYYY-MM-DD HH:MM'
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not appointment_time or not isinstance(appointment_time, str):
        return False
    
    try:
        datetime.strptime(appointment_time, '%Y-%m-%d %H:%M')
        return True
    except ValueError:
        return False


def is_valid_patient_data(patient_data: Dict[str, Any]) -> bool:
    """
    Validate patient data completeness
    
    Args:
        patient_data: Dictionary with patient information
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not isinstance(patient_data, dict):
        return False
    
    required_fields = ['name', 'age', 'contact']
    
    # Check all required fields exist
    if not all(field in patient_data for field in required_fields):
        return False
    
    # Validate age
    if not isinstance(patient_data['age'], int) or patient_data['age'] <= 0:
        return False
    
    # Validate name is not empty
    if not patient_data['name'] or not isinstance(patient_data['name'], str):
        return False
    
    return True


def is_valid_appointment_data(appointment_data: Dict[str, Any]) -> bool:
    """
    Validate appointment data completeness
    
    Args:
        appointment_data: Dictionary with appointment information
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not isinstance(appointment_data, dict):
        return False
    
    required_fields = ['patient_id', 'date', 'time']
    
    # Check all required fields exist
    if not all(field in appointment_data for field in required_fields):
        return False
    
    # Validate datetime format
    datetime_str = f"{appointment_data['date']} {appointment_data['time']}"
    return is_valid_appointment_time(datetime_str)