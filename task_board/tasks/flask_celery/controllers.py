from flask_classful import FlaskView


class AppView(FlaskView):
    """Setup Board for the session."""
    #: Set Routing Prefix for URL
    route_prefix = "/app"
    #: Sets route base
    route_base = "/"

    def get(self):
        """Get Application Message.

        Returns
        -------
        JSON
            Returns the application message.

        """
        return {'Message': "Hello World"}
