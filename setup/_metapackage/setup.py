import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo11-addons-oca-l10n-germany",
    description="Meta package for oca-l10n-germany Odoo addons",
    version=version,
    install_requires=[
        'odoo11-addon-l10n_de_country_states',
        'odoo11-addon-l10n_de_holidays',
        'odoo11-addon-l10n_de_location_nuts',
        'odoo11-addon-l10n_de_skr03_mis_reports',
        'odoo11-addon-l10n_de_skr04_mis_reports',
        'odoo11-addon-l10n_de_steuernummer',
        'odoo11-addon-l10n_de_tax_statement',
        'odoo11-addon-l10n_de_tax_statement_zm',
        'odoo11-addon-l10n_de_toponyms',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 11.0',
    ]
)
