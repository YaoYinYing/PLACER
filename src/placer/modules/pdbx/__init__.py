import sys

# expose package under original name for internal imports
sys.modules.setdefault("pdbx", sys.modules[__name__])
