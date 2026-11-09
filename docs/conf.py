import sys, os
sys.path.insert(0, os.path.abspath('..'))

project = 'py-fun'
copyright = '2026, sgraupner'
author = 'sgraupner'
release = '1.0.0'

# define the information put on documentation pages
extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc']

source_suffix = '.rst'
master_doc = 'index'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'
html_theme = 'default'
