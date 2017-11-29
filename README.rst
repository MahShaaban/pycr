.. image:: https://travis-ci.org/MahShaaban/pycr.svg?branch=master
    :target: https://travis-ci.org/MahShaaban/pycr

pycr
====

Overview  
--------

Quantitative real-time PCR is an imprtant technique in medical and biomedical applicaitons. The ``pycr`` package provides a unified interface for quality assessing, analyzing and testing qPCR data for statistical significance. The aim of this document is to describe the different methods and modes used to relatively quantify gene expression of qPCR and their implemenation in the ``pycr`` package.

Getting started 
---------------

The ``pycr`` is available on `PyPI <https://pypi.python.org/pypi/pycr>`_. To install it, use:  

.. code-block:: bash

    $ pip install pycr
    
The development version of the package can be obtained through:  

.. code-block:: bash

    $ git clone https://github.com/MahShaaban/pycr.git
    $ cd pycr
    $ sudo python setup.py install

First load the necessary packages.  

.. code-block:: python

    import pycr
    import numpy as np
    import pandas as pd
    import pkg_resources as pkg

The following chunck of code locates a dataset of CT values of two genes from 12 different samples and performs a quick analysis to obtain the expression of a target gene c-myc normalized by a control GAPDH in the Kidney samples relative to the brain samples. The ``pcr_ddct`` applies the popular Double Delta CT method.  

.. code-block:: python

    >>> # locate and read raw ct data
    >>> fl = pkg.resource_filename('pycr', 'ct1.csv')
    >>> ct1 = pd.read_csv(fl)
    >>> 
    >>> # make a grouping variabl
    >>> group = np.repeat(['brain', 'kidney'], 6)
    >>> 
    >>> # calculate double delta ct
    >>> pycr.pcr_ddct(ct1, group, 'GAPDH', 'brain')

The output of ``pcr_ddct`` is explained in the documnetation of the function ``help(pycr.pcr_ddct)``. Briefly, the input includes the CT value of c-myc normalized to the control GAPDH, The calibrated value of c-myc in the kidney relative to the brain samples, **ddct**, and the final **relative_expression** of c-myc. In addition, an **error** term and a **lower** and **upper** intervals are provided.

The previous analysis makes a few assumptions. One of which is a perfect amplification efficiency of the PCR reation. To assess the validity of this assumption, ``pcr_efficiency`` provides a method called efficiency. The input DataFrame is the CT values of c-myc and GAPDH at different input amounts/dilutions.

.. code-block:: python
    
    >>> # locate and read raw ct data
    >>> fl = pkg.resource_filename('pycr', 'ct3.csv')
    >>> ct3 = pd.read_csv(fl)
    >>> 
    >>> ## make a vector of RNA amounts
    >>> amount = np.repeat([1, .5, .2, .1, .05, .02, .01], 3)
    >>> 
    >>> ## calculate amplification efficiency
    >>> pycr.pcr_efficiency(ct3, amount, 'GAPDH')

In the case of using the Double Delta C_T, the assumption of the amplification efficiency is critical for the reliability of the model. In particulare, the **slope** and **r_value** of the line between the log input amount and Delta C_T or differnce between the CT value of the target c-myc and GAPDH. Typically, The **slope** should be very small (less than 0.01).

Other analysis methods
----------------------
* Delta CT method ``pcr_dct``
* Relative standard curve method ``pcr_standard``
    
Testing statistical significance
--------------------------------
* Two-group testing ``pcr_ttest`` and ``pcr_wilcox``
* Linear regression testing

Check the twin R package `pcr <https://github.com/MahShaaban/pcr>`_

    
