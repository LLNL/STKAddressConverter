Overview
========

Oracle StorageTek tape libraries have an addressing scheme that looks like:

    L,R,C,S,W
    L: Library
    R: Rail
    C: Column
    S: Side
    R: Row

The software that controls Oracle StorageTek tape libraries, ACSLS, has an
incompatible addressing scheme that looks like:

    A,L,1,D
    A: ACS
    L: LSM
    D: Drive #

Even though ACSLS and StorageTek libraries work hand-in-hand, their drive
addressing and indentification schemes differ and are incompatible. For example,
a drive known by ACSLS as:

    1,4,1,4

is referred to by StorageTek tape libraries exclusively as:

    2,1,-1,1,1 

Converters
==========

A couple different flavors of converters are initially offered here. More may be
offered in the future as the need arises. Contributions of more converters are
encouraged.

For now, the converters offered are:

* *SL8500toACSLS.pm*: a Perl module that offers one-way conversion from the
StorageTek library addressing scheme to ACSLS' scheme
* *SL8500<->ACSLS_converter_python*: a Python module that can be imported or run as
a standalone program. It converts both ways between StorageTek library address
and ACSLS address schemes.
