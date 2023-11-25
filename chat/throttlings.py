from rest_framework.throttling import UserRateThrottle

class ChatAPIThrottle(UserRateThrottle):
    rate = "5/day"