from rest_framework.negotiation import DefaultContentNegotiation


class CustomClientContentNegotiation(DefaultContentNegotiation):

    def select_renderer(self, request, renderers, format_suffix=None):
        """
        If 'application/json' in acceptable media types, use the first renderer in
        DEFAULT_RENDERER_CLASSES which should be 'rest_framework_json_api.renderers.JSONRenderer'.
        Media_type "application/vnd.api+json".  Otherwise, use default select_renderer.
        Returns a tuple (renderer, media_type).
        """
        accepts = self.get_accept_list(request)

        if 'application/json' in accepts:
            return (renderers[0], renderers[0].media_type)

        return DefaultContentNegotiation.select_renderer(self, request, renderers)
