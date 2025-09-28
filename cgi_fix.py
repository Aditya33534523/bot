# cgi_fix.py
import sys

try:
    import cgi
    print("✅ cgi module already available")
except ImportError:
    try:
        import legacy_cgi as cgi
        sys.modules['cgi'] = cgi
        print("✅ Using legacy_cgi as cgi replacement")
    except ImportError:
        print("❌ Could not import legacy_cgi")
        raise