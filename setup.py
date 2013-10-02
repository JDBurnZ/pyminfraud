import setuptools

setuptools.setup(
	name=pyminfraud.__project__,
	version=pyminfraud.__version__,
	author=pyminfraud.__author__,
	author_email=pyminfraud.__email__,
	license=pyminfraud.__license__,

	name = 'pyminfraud',
	version = '1.0',
	description = 'Python library for interfacing with MaxMind\'s minFraud Web Service API.',
	keywords = 'python maxmind minfraud',
	packages = setuptools.find_packages(),
	author = 'Joshua D. Burns',
	maintainer = 'Joshua D. Burns',
	author_email = 'joshuadburns@hotmail.com',
	url = 'https://github.com/JDBurnZ/pyminfraud',
	packages=['pyminfraud']
)
