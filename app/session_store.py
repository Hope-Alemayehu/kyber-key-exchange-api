# session_store.py
from typing import Dict, Any, Optional
import time

class SessionStore:
    def __init__(self):
        self.sessions: Dict[str, Dict[str, Any]] = {}
        self.timeouts: Dict[str, float] = {}
        self.default_timeout = 3600  # 1 hour in seconds
    
    def set(self, session_id: str, data: Dict[str, Any], timeout: Optional[int] = None) -> None:
        """
        Store session data
        
        Args:
            session_id: Unique identifier for the session
            data: Dictionary of data to store
            timeout: Optional timeout in seconds (default: 1 hour)
        """
        self.sessions[session_id] = data
        self.timeouts[session_id] = time.time() + (timeout or self.default_timeout)
        self._cleanup()
    
    def get(self, session_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve session data
        
        Args:
            session_id: The session ID to retrieve
            
        Returns:
            The session data if found and not expired, None otherwise
        """
        self._cleanup()
        return self.sessions.get(session_id)
    
    def delete(self, session_id: str) -> bool:
        """
        Delete a session
        
        Args:
            session_id: The session ID to delete
            
        Returns:
            bool: True if session was deleted, False if it didn't exist
        """
        if session_id in self.sessions:
            del self.sessions[session_id]
            del self.timeouts[session_id]
            return True
        return False
    
    def _cleanup(self) -> None:
        """Remove expired sessions"""
        current_time = time.time()
        expired = [sid for sid, expiry in self.timeouts.items() if expiry < current_time]
        
        for sid in expired:
            if sid in self.sessions:
                del self.sessions[sid]
            if sid in self.timeouts:
                del self.timeouts[sid]
    
    def clear(self) -> None:
        """Clear all sessions"""
        self.sessions.clear()
        self.timeouts.clear()

# Global session store instance
session_store = SessionStore()
