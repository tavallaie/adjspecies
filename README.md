# adjective/species

The `adjspecies3` Python module generates random names formed from
an animal and a descriptor.

## Installation

```bash
$ pip install -U adjspecies3
```

## Usage

From the command line

```bash
$ adjspecies --help
usage: adjspecies.py [-h] [--maxlen MAXLEN] [--sep SEPARATOR] [--count COUNT]
                     [--prevent-stutter]

Print the name of a random adjective/species, more or less…

optional arguments:
  -h, --help         show this help message and exit
  --maxlen MAXLEN    Maximum length for the name, excluding any separator.
                     (default=8)
  --sep SEPARATOR    Separator between the adjective and species words.
                     (default='')
  --count COUNT      Number of adjective/species combinations to print.
  --prevent-stutter  Prevent the same letter from appearing on an
                     adjective/species boundary. (default=True)

$ python adjspecies.py --count 4
sillyfox
redpig
pinkdoge
lynxpaw
```

## In Python code

```python
>>> import adjspecies3
>>> help(adjspecies3.random_adjspecies)
Help on function random_adjspecies in module adjspecies3:

random_adjspecies(sep='', maxlen=8, prevent_stutter=True)
    Return a random adjective/species, separated by `sep`. The keyword
    arguments `maxlen` and `prevent_stutter` are the same as for
    `random_adjspecies_pair`, but note that the maximum length argument is
    not affected by the separator.

>>> adjspecies.random_adjspecies('.', 7)
'wolf.toy'
```

## About

While writing a deployment system targetting [DigitalOcean](https://www.digitalocean.com) Droplets,
the author found the largest bottleneck was finding names for the transient
test servers.

The adjective/species contrivance comes from the furry culture in general
and more directly from the site [ adjective species ](http://adjectivespecies.com). It provides a
wide namespace of easy-to-remember randomness.

Everything up until the initial commit was an exercise in yak shaving and
procrastinating getting out of bed.

## Credits

The [adjspecies](https://github.com/hipikat/adjspecies) module is written and maintained by [Adam Wright](http://hipikat.org),
who plays a cheetah on Twitter under the guise of  [chipikat](https://twitter.com/chipikat), a Python
developer called [pypikat](https://twitter.com/pypikat) and a human being named [hipikat](https://twitter.com/hipikat).
after years [tavallaie](https://twitter.com/AliTavallaie) only updated this package on PYPI for python3.



