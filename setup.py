from distutils.core import setup

setup(
  name = 'acadia',
  packages = ['acadia'],   # Chose the same as "name"
  version = '0.1.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A tool to create accessible audio diagrams',   # Give a short description about your library
  author = 'Sergey Monakhov',                   # Type in your name
  author_email = 'monahovserg@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/monaxov/acadia',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/monaxov/acadia/archive/v_011.tar.gz',    # I explain this later on
  keywords = ['ACCESSIBILITY', 'ACCESSIBLE', 'ASSISTIVE TECHNOLOGY', 'BLIND', 'VISUALLY IMPAIRED', 'CHARTING', 'PLOTTING', 'DIAGRAM', 'AUDIO'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which python versions that you want to support
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],