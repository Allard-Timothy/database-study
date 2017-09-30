#!/usr/bin/python
# -*- coding: utf-8 -*-
####---------------------Relational Design Theory----------------------###
#
# Design by decomposition:
#  - Start with mega-relations that house all data
#  - Decompose into smaller, better relations with same info
#  - Can do decomposition automatically
#
# Automatic Decomposition
#  - Mega relations + properies of data
#  - System decomposes based on properties
#  - Final set satisfies normal form
#
# Properties and Normal Forms
#  - Functional dependencies ==> Boyce - Codd Normal Form
#  - Multivalued dependencies ==> Fourth Normal Form
#
#
# Normal Forms
# - 1st: atomic values in each cell
#       - Eliminate repeating groups in individual tables.
#       - Create a separate table for each set of related data.
#       - Identify each set of related data with a primary key
#
# - 2nd:
#       - Satisfies 1st and every non-key attribute is fully dependent on the primary key
#
# - 3rd:
#       - Satisfies 2nd and all the attributes in a table are determined only by the candidate
#           keys of that table and not by any non-prime attributes
#
# - BCNF:
#       - Slightly stricter version of 3rd-NF
#
# - 4th:
#       - for every one of its non-trivial multivalued dependencies X ->>> Y, X is a superkey. #         That is, X is either a candidate key or a superset thereof.
#
# Table design concepts:
#  - Avoid anonomolies
#  - Structure data to handle non-unique values
#
# Functional Dependencies
# - Constraint between two sets of attributes in a relation
# - Can determine y from x if and only if x is associated with one y value
#  - employee_id -> employee name, desk_id etc etc
#
# Boyce Codd Normal Form - BCNF
# - Must have relation keys on the left side otherwise in violation
# - BCNF decomposition algorithm
#  - Compute keys for R using FD's
#  - Repeat until all relations are in BCNF
#    - Pick any R' with A->B that violates BCNF
#    - Decompose R' into R1(A, B) and Rs(A, Rest)
#    - Compute FD's for R1 and R2
#    - Compute keys for R1 and R2
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
