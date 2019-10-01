# DDF крок 1: Дані зберігаються в DataPoints

Дані в DDF зберігаються в парах ключових значень під назвою DataPoints. Ключ складається з двох або більше вимірів, тоді як значення складається з одного показника.

### 1.1 Поняття, розміри та показники

Необхідно швидке введення понять, подальше детальне пояснення випливає на кроці 3.
* **Концепція** - це все, що може бути заголовком стовпця в таблиці.
* **Тип концепції** позначає тип даних значень під певним поняттям.
Типи, визначені в DDF, - це рядковий, вимірювальний (числовий), булевий, інтервал, час і більше домен сутності, специфічний для DDF, набір сутності та роль. Перші говорять самі за себе, тоді як другі будуть пояснені на кроці 2, сутності.

У DDF DataPoints:
* **Виміри** - це поняття в ключі DataPoint пари ключ-значення. У статистиці поняття в ключі називається незалежною змінною.
* **Індикатор** - це поняття в частині значення пари ключ-значення DataPoint. У статистиці індикатор можна назвати залежною змінною, оскільки його значення залежить від ключа.

### 1.2 Виміри як ключі для DataPoint
Виміри - це поняття, що складають ключове значення в точках даних. Точки даних у DDF часто використовуються для зберігання змін за роки та географічні місця.

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
