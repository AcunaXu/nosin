from setuptools import setup, find_packages

setup(name='scrapy-mymodule',
      entry_points={
          'scrapy.commands': [
              'crawlall=mySpider.commands:crawlall',
          ],
      },
      )