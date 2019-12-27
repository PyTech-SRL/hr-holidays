import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-oca-hr-holidays",
    description="Meta package for oca-hr-holidays Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-hr_holidays_public',
        'odoo13-addon-hr_holidays_settings',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
