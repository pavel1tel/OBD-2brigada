from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Concept(Base):
	__tablename__ = 'concept'
	id = Column(Integer, primary_key = True)
	units = Column(String(45))
	name = Column(String(45))
	type = Column(String(45))
	user = relationship("User")

class Entity(Base):
	__tablename__ = 'entity'
	id = Column(Integer, primary_key = True)
	name = Column(String(45))
	table_name = Column(String(45))
	dataPoint = relationship("DataPoint")
	properties = relationship("Properties")

class Properties(Base):
	__tablename__ = 'properties'
	id = Column(Integer, primary_key = True)
	name = Column(String(45))
	type = Column(String(45))
	info = Column(String(45))
	entity_id = Column(Integer, ForeignKey('entity.id'))

class DataPoint(Base):
	__tablename__ = 'dataPoint'
	id = Column(Integer, primary_key = True)
	name = Column(String(45))
	entity_id = Column(Integer, ForeignKey('entity.id'))
	table_name = Column(String(45))
	user = relationship("User")
	dataPointPropertie = relationship("DataPointPropertie")

class DataPointPropertie(Base):
	__tablename__ = 'dataPointPropertie'
	id = Column(Integer, primary_key = True)
	name = Column(String(45))
	type = Column(String(45))
	info = Column(String(45))
	dataPoint_id = Column(Integer, ForeignKey('dataPoint.id'))

class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key = True)
	roots = Column(String(45))
	concept_id = Column(Integer, ForeignKey('concept.id'))
	dataPoint_id = Column(Integer, ForeignKey('dataPoint.id'))

