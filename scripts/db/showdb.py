from db import *
from db.models import *

print("Entity:")
for ent in session.query(Entity):
	print(ent) 

print("\nProperties:")
for prop in session.query(Properties):
	print(prop)



print("\nDataPoints:")
for datap in session.query(DataPoint):
	print(datap) 

print("\nDataPointsProperties:")
for datap in session.query(DataPointPropertie):
	print(datap)

print("\nConcepts:")
for con in session.query(Concept):
	print(con) 

print("\nUsers:")
for usr in session.query(User):
	print(usr)  