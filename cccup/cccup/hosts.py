from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'api', 'cccup.api_urls', name='api'),  # Routes requests from api.cccup.id or api.localhost:8000 to api_urls.py
    host(r'www', 'cccup.urls', name='www'),        # Main site
)
