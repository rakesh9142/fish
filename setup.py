
---

## 4. 🛠 `setup.py` (Optional Installer)

```python
from setuptools import setup

setup(
    name='phish-qr-generator',
    version='1.0',
    py_modules=['phish_qr_gen_with_photo'],
    install_requires=[
        'qrcode',
        'Pillow',
    ],
    entry_points='''
        [console_scripts]
        phishqr=phish_qr_gen_with_photo:main
    ''',
    author='Your Name',
    description='A tool to embed phishing QR codes onto images for red teaming.',
    license='MIT',
)
