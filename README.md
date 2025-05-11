# Phiton

python project with subprojects

## Preproccesor example
### test.py:
```python
#define PI 3.14
#define RADIUS 5
area = PI * RADIUS * RADIUS

#include "header.py"
print("Area:", area)
```
### test.ph.py:
```python
area = 3.14 * 5 * 5

print("This is print in header.py")
print("Area:", area)
```