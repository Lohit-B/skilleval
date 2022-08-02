class BaseException(Exception):
    message = "Error"
    status = 500

    def __init__(self, message, status):
        self.message = message
        self.status = status

    def __str__(self):
        return self.message

    def getStatusCode(self):
        return self.status

class BadRequest(BaseException):
    status = 400
    def __init__(self, message=None):
        message = message or "Invalid Request"
        super().__init__(message, self.status)

class Forbidden(BaseException):
    status = 403
    def __init__(self, message=None):
        message = message or "Not Allowed"
        super().__init__(message, self.status)

class NotFound(BaseException):
    status = 404
    def __init__(self, message=None):
        message = message or "Resource Not Found"
        super().__init__(message, self.status)
        
class JWTTokenExpired(BaseException):
    status = 401
    def __init__(self, message=None):
        message = message or "Un-Authorized"
        super().__init__(message, self.status)

class AgworldTokenExpired(BaseException):
    status = 403
    def __init__(self, message=None):
        message = message or "Agworld Un-Authorized"
        super().__init__(message, self.status)

class AgworldRequestError(BaseException):
    status = 500
    def __init__(self, message=None):
        message = message or "Agworld Server Error"
        super().__init__(message, self.status)

    def __init__(self, status, message):
        super().__init__(message, status)
