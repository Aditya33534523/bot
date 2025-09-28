# cgi_fix.py
import sys
import os

def setup_cgi():
    """Setup CGI module for Python 3.13 compatibility"""
    try:
        import cgi
        print("✅ Native cgi module found")
        return
    except ImportError:
        pass

    try:
        import legacy_cgi as cgi
        sys.modules['cgi'] = cgi
        print("✅ Using legacy_cgi")
        return
    except ImportError:
        print("⚠️ legacy_cgi not found, creating minimal cgi module")

    # Create a minimal cgi module replacement
    import urllib.parse
    import io
    from email.message import EmailMessage
    
    class FieldStorage:
        def __init__(self, fp=None, headers=None, environ=None, keep_blank_values=0, strict_parsing=0):
            self.fp = fp or io.StringIO()
            self.headers = headers or {}
            self.environ = environ or {}
            self.keep_blank_values = keep_blank_values
            self.strict_parsing = strict_parsing
            self.list = []
            
        def getvalue(self, key, default=None):
            return default
            
        def getfirst(self, key, default=None):
            return default
            
        def getlist(self, key):
            return []
    
    def parse_qs(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace', max_num_fields=None, separator='&'):
        return urllib.parse.parse_qs(qs, keep_blank_values, strict_parsing, encoding, errors, max_num_fields, separator)
    
    def parse_qsl(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace', max_num_fields=None, separator='&'):
        return urllib.parse.parse_qsl(qs, keep_blank_values, strict_parsing, encoding, errors, max_num_fields, separator)
    
    def escape(s, quote=None):
        import html
        if quote is None:
            return html.escape(s)
        return html.escape(s, quote)
    
    def parse_multipart(fp, pdict, encoding="utf-8", errors="replace", separator="&"):
        return {}
    
    def parse_header(line):
        return '', {}
    
    # Create the cgi module
    cgi_module = type(sys)('cgi')
    cgi_module.FieldStorage = FieldStorage
    cgi_module.parse_qs = parse_qs
    cgi_module.parse_qsl = parse_qsl
    cgi_module.escape = escape
    cgi_module.parse_multipart = parse_multipart
    cgi_module.parse_header = parse_header
    
    sys.modules['cgi'] = cgi_module
    print("✅ Created minimal cgi module replacement")

# Run the setup
setup_cgi()