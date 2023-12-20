# global configuration for every documentation added at the end

import os, sys, datetime

import sphinx_rtd_theme

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.abspath(f'{dir_path}/_ext'))
now = datetime.datetime.now()

extensions = ['sphinx_rtd_theme', 'sphinx_rtd_dark_mode']

# General information about the project.
copyright = f'{now.year} Nextcloud GmbH'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = 'latest'
# The full version, including alpha/beta/rc tags.
release = version

# RTD theme options
html_theme_options = {
    'logo_only': True,
    'style_external_links': True,
    'display_version': False,
}

# relative path to subdirectories
html_logo = "../_shared_assets/static/logo-white.png"

# substitutions go here
rst_epilog = f'.. |version| replace:: {version}'

# building the versions list
version_start = 26		# THIS IS THE SUPPORTED VERSION NUMBER
version_stable = 28		# INCREASE THIS NUMBER TO THE LATEST STABLE VERSION NUMBER

# Also search for "TODO ON RELEASE" in the rst files

def generateVersionsDocs(current_docs):
	versions_doc = []
	for v in range(version_start, version_stable + 1):
		url = f'https://docs.nextcloud.com/server/{str(v)}/{current_docs}'
		versions_doc.append((v, url))
	versions_doc.extend(
		(
			(
				'stable',
				f'https://docs.nextcloud.com/server/stable/{current_docs}',
			),
			(
				'latest',
				f'https://docs.nextcloud.com/server/latest/{current_docs}',
			),
		)
	)
	return versions_doc

github_branch = f'stable{version}' if version.isdigit() else 'master'
html_context = {
	'current_version': version,
	'READTHEDOCS': True,
	'extra_css_files': ['_static/custom.css'],
	'display_github': True,
	'github_user': 'nextcloud',
	'github_repo': 'documentation',
	'theme_vcs_pageview_mode': f'edit/{github_branch}/',
}

edit_on_github_project = 'nextcloud/documentation'
edit_on_github_branch = 'master'

# user starts in light mode
default_dark_mode = False

latex_engine = "xelatex"
