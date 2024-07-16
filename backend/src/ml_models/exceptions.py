class ModelNotLoaded(Exception):
    """Exception raised when a model is not loaded properly."""

    def __init__(self, message="Model not loaded"):
        self.message = message
        super().__init__(self.message)
