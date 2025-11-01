

class UniqueInstance:
    _instance: "UniqueInstance" = None

    def __new__(cls, *args, **kwargs) -> "UniqueInstance":
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
