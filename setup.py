
---

## 🛠 4. Optional Packaging — `setup.py`

```python
from setuptools import setup

setup(
    name='phish-qr-generator',
    version='1.1',
    py_modules=['phish_qr_gen_with_photo'],
    install_requires=['qrcode', 'Pillow'],
    entry_points={
        'console_scripts': [
            'phishqr = phish_qr_gen_with_photo:main',
        ],
    },
    author='Your Name',
    description='Phishing QR generator tool for red teaming',
    license='MIT',
)
