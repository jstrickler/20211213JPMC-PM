# from pkg.pkg import module
from john.math import geometry

# find and load geometry.py

a = geometry.circle_area(42)
r1 = geometry.rectangle_area(5, 10)
print(a, r1)
print('-' * 60)
# module search:
# 1. current directory
# 2. dirs in PYTHONPATH
# 3. dirs in sys.prefix (builtin folders)

import sys
for path in sys.path:
    print(path)

