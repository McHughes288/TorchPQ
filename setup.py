from distutils.core import setup
setup(
  name = 'TorchPQ',
  packages = ['TorchPQ'],
  version = '0.1',
  license='MIT',
  description = 'Efficient implementations of Product Quantization and its variants',
  author = 'demoriarty', 
  author_email = 'sahbanjan@gmail.com',
  url = 'https://github.com/DeMoriarty/TorchPQ',
  download_url = 'https://github.com/DeMoriarty/TorchPQ/archive/v_01.tar.gz',
  keywords = ['KMeans', 'K-means', 'ANN', 'pytorch','machine learning', 'pq', 'product quantization', 'IVFPQ', 'approximate nearest neighbors'],
  install_requires=[            # I get to this in a second
          'numpy',
          'torch',
          'cupy'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)