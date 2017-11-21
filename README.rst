.. image:: https://travis-ci.org/MahShaaban/pycr.svg?branch=master
    :target: https://travis-ci.org/MahShaaban/pycr

pycr
----
Calculates the amplification efficiency and curves from real-time quantitative
PCR (Polymerase Chain Reaction) data. Estimates the relative expression from PCR
data using the double delta CT and the standard curve methods Livak & Schmittgen
(2001) <doi:10.1006/meth.2001.1262>. Tests for statistical significance using
two-group tests and linear regression Yuan et al. (2006)
<doi:10.1186/1471-2105-7-85>.

To use a the mock function form this package, typ
  >>> import pycr
  >>> print mock.mock()
