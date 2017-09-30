###----------JSON Data---------###
#
# JSON - javascript object notation; beyond just javascript tho
#    - Standard for "serializing" data for human consumption
#    - Useful for data interchange; storing semistructured data
#
# High Level Attributes
#    - Nested sets and arrays
#    - "self-describing" schema; flexible
#    - No standard query language
#    - Ordered data; but generally order not important
#    - Coupled with programming langugages/NoSQL systems
#
###---------Relational Algebra-------###
#  
# Querying on set of relations, produces relation as a result
# SELECT - pick certain rows: denoted by sigma with sub-script to filter for, paired with relation
#     (sigma)GPA > 3.7 Student
#     (sigma)GPA >3.7 ^ HS < 1000 Student
#     (sigma)Cname='stanford' ^ major='cs' Apply
#
# PROJECT - pick certain columns: denoted by Pi with subscript of column names
#     (Pi)sID, dec Apply
#
# Select rows and columns: use SELECT and PROJECT in tandem -
#    (Pi)sId, sName((sigma)GPA > 3.7 Student)
#
# Union - combining relations on common keys in vertical manner; denoted by U
#
# Select college name with respective student name -
#    (Pi)cName College U (Pi)sName Student 
#
# Difference - Find difference between two relations
#
# Select all students who didn't go to college - 
#    (Pi)sId Student - (Pi)sId Apply
#
# Intersection: ∩ - find commonalities between relations -
#    (Pi)cName College ∩ (Pi)sName Student  
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






































































































































































































