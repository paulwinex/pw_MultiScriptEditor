from setuptools import setup, find_packages

setup(name='multi_script_editor',
      version='2.1',
      description='Python editor for multiple platforms',
      long_description='Python editor for multiple platforms and CG software applications',
      classifiers=[
        'Development Status :: Release 2.1',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='python ide script_editor',
      url='https://github.com/paulwinex/pw_MultiScriptEditor',
      author='Paul Winex',
      author_email='paulwinex@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[],
      include_package_data=True,
      zip_safe=False)
