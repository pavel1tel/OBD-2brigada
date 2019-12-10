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

	def __repr__(self):
		return f'Concept with id = {self.id} and name = {self.name}'

class Entity(Base):
	__tablename__ = 'entity'
	id = Column(Integer, primary_key = True)
	name = Column(String(45))
	table_name = Column(String(45))
	dataPoint = relationship("DataPoint")
	properties = relationship("Properties")

	def __repr__(self):
		return f'Entity with id = {self.id} and name = {self.name}'

class Properties(Base):
	__tablename__ = 'properties'
	id = Column(Integer, primary_key = True)
	name = Column(String(45))
	type = Column(String(45))
	info = Column(String(45))
	entity_id = Column(Integer, ForeignKey('entity.id'))

	def __repr__(self):
		return f'Propertie with id = {self.id} and name = {self.name}'

class DataPoint(Base):
	__tablename__ = 'dataPoint'
	id = Column(Integer, primary_key = True)
	name = Column(String(45))
	entity_id = Column(Integer, ForeignKey('entity.id'))
	table_name = Column(String(45))
	user = relationship("User")
	dataPointPropertie = relationship("DataPointPropertie")
	def __repr__(self):
		return f'DataPoint with id = {self.id} and name = {self.name}'

class DataPointPropertie(Base):
	__tablename__ = 'dataPointPropertie'
	id = Column(Integer, primary_key = True)
	name = Column(String(45))
	type = Column(String(45))
	info = Column(String(45))
	dataPoint_id = Column(Integer, ForeignKey('dataPoint.id'))

	def __repr__(self):
		return f'DataPointPropertie with id = {self.id} and name = {self.name}'

class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key = True)
	roots = Column(String(45))
	concept_id = Column(Integer, ForeignKey('concept.id'))
	dataPoint_id = Column(Integer, ForeignKey('dataPoint.id'))

	def __repr__(self):
		return f'User with id = {self.id} and roots = {self.roots}'

