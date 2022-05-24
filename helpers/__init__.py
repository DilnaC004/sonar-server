from datetime import datetime

## HELPER FUNCTION
def get_time_str(time_obj = None) -> str:
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S") if time_obj is None else time_obj.strftime("%Y-%m-%d %H:%M:%S")

def is_active(page, element):
    return "active" if page == element else ""




class SonarData:

    _DEFAULT_DATA = {"No sonar data": "check connection"}
    
    def __init__(self, max_time_diff = 5) -> None:
        
        self._data = self._DEFAULT_DATA
        self._time = datetime.utcnow() 
        self.max_time_diff = max_time_diff

    def set_data(self, data : dict):
        self._data = data
        self._time = datetime.utcnow()

    def get_data(self):
        
        if (datetime.utcnow() - self._time).total_seconds() >= self.max_time_diff:
            self._data = self._DEFAULT_DATA

        return self._data, get_time_str(self._time)