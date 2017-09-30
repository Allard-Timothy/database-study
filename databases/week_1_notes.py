####----Purpose of Database Management Systems-----####
#  - Provide efficient, reliable, convenient and safe multi-user storage
#       of and access to massive amounts of persistent data.
#
#  - DB apps programmed via frameworks
#  - DBMS may run in conjunction with middleware
#  - Data-intesive app's may not use DBMS at all
#
######----Key concepts-----#####
#
# - Data Model
# - Schema versus data
# - Data definitial language DDL
# - Data manipulation or query language
# 
###-------The Relational Model----------###
#
# Database: set of named relations(or tables)
# Each relation has set of named attributes (columns)
# Each tuple(or row) has a value for each attribute
# Each attribute has a type(or domain)
#
# Steps to creation of relational database:
#     - Design schema; create using DDL
#     - "Bulk Load" initial data
#     - Repeat: execute queries and modifications
# 
###------Querying Relational Databases--------###
#
# Compositionality: ability to run secondary query on results from first query  
# Relational Algebra: formal language
# SQL: implemented language
#
# Eg: Ids of students with GPA > 3.7 applying to Stanford
# 
# RA: πid Σgpa > 3.7 ^ Cname='Stanford'(student ∞ apply)
# SQL: SELECT  Student.id
#        FROM Student, Apply
#       WHERE Student.id = Apply.id
#         AND gpa>3.7 and cname='Stanford'
#
###-------XML Data-------###
#
# Extensible Markup Language:
#     - Standard for data representation and exchange
#     - Document format similar to HTML
#           - Tags describe content instead of formatting
#     - Also contains streaming format
# 
# Basic Constructs:
#     - Tagged elements
#     - Attributes
#     - Text
#
# Relational Model vs XML
#    - Structure:
#          - Relational: Tables
#          - XML: Hierarchical Tree, graph
#
#    - Schema:
#          - Relational: Fixed in advance
#          - XML: Flexible 'self-describing'
#
#    - Queries:
#          - Relational: Simple languages 
#          - XML: Not quite as simple
#
#    - Ordering
#          - Relational: Unordered
#          - XML: Implied order
#
#    - Implementation
#          - Relational: Native Model
#          - XML: Add-on; or layer over database system
#
###-----DTDs, IDs, IDREFs-------###
#
# Well formed XML:
#     - Single root element
#     - Matched tags, proper nesting
#     - Unique attributes within elements
#
# Valid XML:
#     - Adheres to basic structural requirements
#     - Adheres to content-specfic specification 
#           - Document Type Descriptor (DTD)
#           - XML Schema (XSD)
#
# DTD - Document Type Descriptor
#     - Grammer-like language for specifying elements,
#       attributes, nesting, ordering, #ocrrurences
#     - Special attribute types ID and IDREF(s) - specify non-typed pointers
#
# Pros and Cons of using DTD/XSD vs not using DTD/XSD
#   - Pros of using DTD/XSD
#     - Programs can assume structure
#     - CSS/XSL can be simpler
#     - Specification for XML views
#     - Documentation
#
#   - Pros of not using DTD/XSD 
#     - Flexibility, ease of change of data formation
#     - DTD can be messy with irregular data; especially XSD's. Can lead to doc structure 
#           growing larger than doc
# 
# ID and IDREF
#     - Similar to var assignment
#     - Non-typed; can assign valid ID/IDREF to multiple elements
#     - Must be used if instantiated otherwise dangling pointer
#
###--------XML and XSD------------###
#
# XML Schema (XSD)
#     - Extensive Language
#     - Like DTD's, can specify elements, attributes
#       nesting, ordering and #occurrences
#     - Specify data types, keys, typed pointers
#     - Written in XML
#
# Typed Values
#     - Assigns types to element values ie. assign price as Integer; pass in string == error
#     - Value passed in as string, but string contents must match type
#    
# Key Declaration
#     - Particular attribute must be unique within element of same type
#
# References
#     - Ensures that idents refer to their respective element types
#
# Occurence constraints
#     - Specify min/max # of occurences
#     - default is to 1
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









































