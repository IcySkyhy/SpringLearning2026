# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SpringLearning2026'
copyright = '2026, IcySkyhy'
author = 'IcySkyhy'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# 启用我们安装的扩展
extensions = [
    'sphinx_rtd_theme',
    'myst_parser',       # 支持 Markdown
    'sphinx.ext.mathjax',# 公式支持
    'sphinx_proof',      # 定理块支持
]

# MyST Markdown 配置
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "strikethrough",
]

templates_path = ['_templates']
exclude_patterns = []
language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme' # 修改默认的 alabaster 为 rtd 主题
html_static_path = ['_static']