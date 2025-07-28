import time
from datetime import datetime

class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        end_time = time.time()
        duration = (end_time - start_time) * 1000

        log_data = (
            f"[{datetime.now().isoformat()}]"
            f"URL: {request.path} | "
            f"Method: {request.method} | "
            f"Execution Time: {duration: 2f} ms\n"
        )

        with open("request_logs.json", "a") as log_file:
            log_file.write(log_data)
        return response