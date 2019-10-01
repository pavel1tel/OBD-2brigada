# DDF step 1: Data is stored in DataPoints

Data in DDF is stored in key-value pairs called DataPoints. The key consists of two or more dimensions while the value consists of one indicators. 
The below table shows 

### 1.1 Concepts, dimensions and indicators

A quick introduction to concepts is necessary, further detailed explanation follows in step 3.
* A **concept** is anything that can be a column header in a table.
In the table above, country, year and government_type are all concepts.
* A **concept type** signifies the datatype of the values under a certain concept. 
Types defined in DDF are string, measure (numeric), boolean, interval, time and the more DDF-specific entity domain, entity set and role. The former speak for themselves while the latter will be explained in step 2, entities.
In the table above, country and government_type are concepts with a entity_domain concept type, year has a time concept type and population has a measure concept type.

In DDF DataPoints:
* A **dimension** is a concept in the key of the DataPoint key-value pair. In statistics, a concept in the key is called an independent variable.
In the table above, country and year are dimensions forming the key to the indicator.
* An **indicator** is a concept in the value-part of the DataPoint key-value pair. In statistics the indicator would be called a dependent variable, because its value is dependent on the key.
In the table above government_type and population are the indicators.

### 1.2 Dimensions as a key for a DataPoint
Dimensions are the concepts making up the key in DataPoints. DataPoints in DDF are often used to store changes over years and geographic locations.

### 1.3 Indicators 
The set of indicators can be expanded to represent more data for a certain set of dimensions.

# DDF step 2: Entities
The following terms are introduced in this step:
* A **property** provides additional information about a discrete concept. 
For example, the concept country can have properties full_name, latitude or longitude. 
* An **entity domain** is a discrete concept which has all of its possible values enumerated. This way, it explicitly defines the domain of the concept. Moreover, enumerating all possible values makes it possible to define properties for each value. 
For example, we can turn country into an entity domain by enumerating all countries. By doing so, we can define the full name, latitude and longitude for each country.
* An **entity** is one value within an entity domain.
For example Sweden or Russia are entities in the entity domain country.
* An **entity set** is a set of entities within an entity domain.
For example, instead of an entity domain, country can be an entity set within an entity domain geographic places, next to other entity sets such as city, world_region and province.

# DDF step 3: Concepts and concept properties
Concepts are the table headers anywhere in a DDF dataset. Concept properties are concepts which give information about concepts. A first peek into concept-properties was the entity domain and entity set enumeration and the properties concept_type, domain and drill_up.

Any property of any concept can be defined in a similar way in DDF. All concepts used in the data-set should be enumerated and any property of these concepts can be defined in this enumeration. Below an example for a dataset similar to the ones used in previous examples. Also have a look in the [Systema Globalis](https://github.com/open-numbers/ddf--gapminder--systema_globalis/blob/master/ddf--concepts.csv) data set for an even larger enumeration of concepts.


Read more the context of DDF in [this document](https://docs.google.com/document/d/1Cd2kEH5w3SRJYaDcu-M4dU5SY8No84T3g-QlNSW6pIE/edit#).
