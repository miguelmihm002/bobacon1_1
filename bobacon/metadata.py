from typing import Optional

METADATA =\
{
	'name': 'bobacon',
	'description': 'Industry leading face manipulation platform',
	'version': '3.1.1',
	'license': 'MIT',
	'author': 'Henry Ruhs',
	'url': 'https://bobacon.io'
}


def get(key : str) -> Optional[str]:
	if key in METADATA:
		return METADATA.get(key)
	return None
