import logging
from application.utils.security import hash_password

# Setting up logger for event handling
logger = logging.getLogger(__name__)

def log_new_user_event(user_data):
    """
    Event handler function to log the newly created user details.
    This is called after a user is successfully created.
    """
    user_copy = user_data.copy()  # Make a copy to avoid modifying the original data
    if 'password' in user_copy:
        user_copy['password'] = hash_password(user_copy['password'])  
    
    logger.info(f"New user created: {user_copy}")