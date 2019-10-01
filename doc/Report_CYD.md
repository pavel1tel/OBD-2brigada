# CУД

__Система управління даними__ – це різновид програмного забезпечення для роботи з базами даних.  
 Зараз основний вигляд СУД – це клієнтсько-серверна частина СУБД, сама СУБД знаходиться на сервері і опрацьовує запити від клієнтської частини програми, яка знаїодиться на комп'ютерах користувачів. Програма клієнта відправляє запити на сервер і демонструє відповіді користувачу, коли сервер відправляє ці відповіді.
 
----------------------

## Види данних:

- **МЕТА-ДАНІ** - відомості про ознаки і властивості, що характеризують будь-які
сутності
- **МАЙСТЕР-ДАНІ** - основні дані по об'єктах (наприклад, фізичні особи,
юридичні особи, майно, товари та ін.), які створюються органами влади в
по ходу їх діяльності або формуються за запитами органів влади і
обробляються в ГІС
- **ТРАНЗАКЦІЙНІ ДАНІ** - дані про операції (наприклад, дані про надання
держпослуг і ін.)
- **НЕСТРУКТУРОВАНІ ДАНІ**  - інформація, яка або не має наперед визначеної структури даних, або не організована в установленому порядку
- **СТРУКТУРОВАНІ ДАНІ** - дані, що відображають окремі факти предметної області і впорядковані певним чином, з метою забезпечення можливості застосування до них різних методів обробки.

---------------------------

## Процеси управління даними
* Аналіз даних
* Архітектура даних
* Добування даних
* Захист даних
* Вибір, перетворення і завантаження даних
* Моделювання даних
* Забезпечення якості даних
* Робота з базами даних
* Управління метаданими
* Шифрування даних

----------------------------------
## Моделі що описують Системи Управління Данними
* [EDM Council Data Management Capability Assessment Model (DCAM)](https://dgpo.org/wp-content/uploads/2016/06/EDMC_DCAM_-_WORKING_DRAFT_VERSION_0.7.pdf)
* [CMMI Data Management Maturity Model (DMM)](https://cmmiinstitute.zendesk.com/hc/en-us/articles/218924137-What-is-a-DMM-assessment-and-how-to-get-more-information-about-it-)                                                                                                                                                 
* [CC CDQ Data Excellence Model (DXM)](https://www.cc-cdq.ch/data-excellence-model)
* [IDC Information Transformation Maturity Model](https://www.linkedin.com/pulse/managing-enterprise-content-idc-maturity-model-holly-muscolino)
* Gather Enterprise Information Management Maturity Model

## Опис DMM моделі
DMM оціннювання (Оцінка зрілості управління данними) базується на основі нарад між колегами
і швидко виявляє в організації її поточні можливості, рівні зрілості її проектів, і визначає                         
зони де потрібні додаткові ресурси.  
Результат оцінювання це детальний звіт що використовується для розробки нових стратегій і застосувань     
запланованих дій.    
**Переваги DMM моделі:**
* Незалежне, об'єктивне оціннювання(оціннювання зазвичай здійснюється кваліфікованими третіми особами)
* Швидкі результати(оцінювання відбувається за трьох тижневий термін)
* Дієві рекомендації (рекомендації узгоджуються і пріорітизуються акціонерами)

**DMM оцінювання поділяється на 3 фази**  
![](img/diagram1.png)
DMM побудований таким чином, що його можуть використовувати організації
 не лише для оцінки їх поточного стану можливостей,
 але і для складання спеціалізованої схеми для впровадження управління даними.

------------------

# Моделі, що використовуються в СУД

## Модель «сутність — зв'язок»

__[Модель «сутність-зв'язок»](https://uk.wikipedia.org/wiki/Модель_«сутність_—_зв%27язок»)__ (ER-модель) (англ. Entity-relationship model або entity-relationship diagram) — модель даних, 
яка дозволяє описувати концептуальні схеми за допомогою узагальнених конструкцій блоків. 

__ER-модель__ — це мета-модель даних, тобто засіб опису моделей даних. Існує ряд моделей для представлення знань,
але одним з найзручніших інструментів уніфікованого представлення даних, незалежного від програмного забезпечення,
що його реалізує, є модель «сутність-зв'язок».

Важливим є той факт, що з моделі «сутність-зв'язок» можуть бути породжені всі існуючі моделі даних (ієрархічна, мережева, реляційна, об'єктна), тому вона є найзагальнішою.

__Модель сутність-зв'язок__ є результатом систематичного процесу, який описує та визначає деяку предметну область.
Вона не визначає сам процес, а лише візуалізує його.
Дані представлені у вигляді компонентів (сутностей), які пов'язані між собою певними зв'язками,
які виражають залежності і вимоги між ними, такі як: одна будівля може бути розділена на нуль або більше квартир,
але одна квартира може бути розташована лише в одній будівлі. Сутності можуть мати різні властивості (атрибути),
які характеризують їх. Діаграми, створені для представлення цих сутностей, 
атрибутів і зв'язків графічно, називають сутність-зв'язок діаграмами.

ER-модель зазвичай реалізується в вигляді баз даних. У разі реляційної бази даних, в якій зберігаються дані в таблицях,
кожен рядок кожної таблиці являє собою один екземпляр сутності. Деякі поля даних в цих таблицях вказують на індекси
в інших таблицях. Такі поля є покажчиками фізичної реалізації зв'язків між сутностями.

\-------------------------------------------------------------------------------------------------------

Коли ми говоримо про сутність, ми зазвичай говоримо про деякий аспект реального світу, який можна виділити поміж інших аспектів. __Сутність__ — це збірне поняття, деяка абстракція реального об'єкта, процесу, явища чи деякого уявлення про об'єкт. Хоча термін сутність найвживаніший, потрібно розрізняти поняття типу сутності та екземпляру сутності. Поняття тип сутності відноситься до набору однорідних особистостей, предметів, подій або ідей, що виступають як ціле. Екземпляр сутності відноситься до конкретної речі в наборі. Наприклад, типом сутності може бути МІСТО, а екземпляром — Київ, Львів і т. д.

Виділяють три види сутностей: \
* стрижнева,
* асоціативна (асоціація),
* характеристична (характеристика).

__Стрижнева (сильна) сутність__ — незалежна від інших сутність. Стрижнева сутність не може бути асоціацією, характеристикою чи позначенням.

__Асоціативна сутність (або асоціація)__ виражає собою зв'язок «багато до багатьох» між двома сутностями. Є цілком самостійною сутністю. Наприклад, між сутностями ЧОЛОВІК і ЖІНКА існує асоціативний зв'язок, висловлюваний асоціативної сутністю ШЛЮБ.

>Характеристичну сутність ще називають слабкою сутністю. Вона пов'язана з більш сильною сутністю зв'язками «один до багатьох» >і «один до одного». Характеристична сутність описує або уточнює іншу сутність. Вона повністю залежить від неї і зникає зі >зникненням останньої. Наприклад, сутність Зарплата є характеристикою >конкретних працівників підприємства і не може в такому >контексті існувати самостійно — при видаленні екземпляра сутності Працівника повинні бути видалені і екземпляри сутності >Зарплата, пов'язані з видаленим працівником.

Позначення це така сутність, з якої інші сутності пов'язані за принципом «багато до одного» або «один до одного». Позначення, на відміну характеристики є самостійною сутністю. Наприклад, сутність Факультет позначає приналежність студента до даного підрозділу інституту, але є цілком самостійною.

При моделюванні прийнято виражати (іменувати) сутність іменником або іменником з прикметником, що характеризує його, а зв'язок дієсловом, що поєднує два чи більше іменників.

Сутності та зв'язки можуть мати свої атрибути. Наприклад, сутність громадянин має атрибут номер паспорту, а зв'язок має між сутностями гравець та аккаунт володіє атрибутом останній вхід.

Кожна сутність (якщо це не слабка сутність) має мати мінімальний набір унікальних атрибутів, що зветься [первинним ключем](https://uk.wikipedia.org/wiki/%D0%9F%D0%B5%D1%80%D0%B2%D0%B8%D0%BD%D0%BD%D0%B8%D0%B9_%D0%BA%D0%BB%D1%8E%D1%87).

# Нотації (Графічні діаграми)

__Нотація Пітера Чена__
Сутності відображуються у вигляді прямокутнків, зв'язки у вигляді ромбів. Якщо сутність бере участь у відносинах, вони пов'язані лінією. Якщо відносини не є обов'язковими, то лінія пунктирна. Атрибути позначаються в вигляді овалів і пов'язані з однією сутністю або зв'язком. Овал похідних атрибутів зображується пунктирним контуром.

__Вороняча лапка__

Нотація «вороняча лапка» використана для позначення двох пов'язаних сутностей. Зображено необов'язковий зв'язок між будинком і квартирою. Позначки, ближчі до об'єкта квартира, представляють «нуль, один або багато», тоді як квартира має «один і лише один» будинок. Таким чином, зв'язок читається так: будинок (може) мати «нуль, одну, чи багато» квартир.

>Нотація «вороняча лапка» (англ. crow's foot) була запропонована Гордоном Еверестом (англ. Gordon Everest) у статті 1976 >року[1] під назвою «обернена стрілка» (англ. inverted arrow), однак частіше за все цю нотацію називають «вороняча лапка» >або ж «виделка» (англ. fork).

Згідно даної нотації, сутність подається у вигляді прямокутника, де сутність виражається іменником. Ім'я сутності має бути унікальним в рамках однієї моделі.

Зв'язок зображується лінією, яка пов'язує дві сутності, що беруть участь у відношенні. Ступінь кінця зв'язку вказується графічно, множинність зв'язку зображується у вигляді «виделки» на кінці зв'язку. Модальність зв'язку так само зображується графічно — необов'язковість зв'язку позначається кружком на кінці зв'язку.

Атрибути сутності записуються усередині прямокутника, що зображує сутність і виражаються іменником в однині (можливо, з уточнюючими словами). Серед атрибутів виділяється ключ сутності — ненадлишковий набір атрибутів, значення яких в сукупності є унікальними для кожного екземпляра сутності.

-----

## Open data  

__Open data__ – об'ємне поняття, що захоплює одночасно і концепцію, і явище, в якому вона втілюється.  

Open data як концепція - це ідея про те, що інформація, яка не є предметом авторського права, не захищена патентами та іншими механізмами контролю, повинна бути доступна всім. Вважається, що обмеження доступу до даних йдуть проти суспільного блага. Відкриті дані не мають на увазі обмежень і / або оплати. Більш того, місія відкритих даних полягає в підзвітності влади перед громадянами.

Відкриті дані фактично - це будь-яка інформація, яка може виявитися корисною. Дані державних реєстрів, відомості про житлово-комунальному господарстві або, грубо кажучи, місця розташування громадських туалетів - все це опен дата. При цьому формат даних повинен бути зручним для читання комп'ютерними алгоритмами і застосування. Відповідні формати open data-файлів: JSON, XML, RDF. Електронні таблиці Microsoft Excel, текстові документи txt і PDF не рекомендуються для опен дата через відсутність чіткої структури даних.  

Разом з open data часто використовується термін «big data» ( «великі дані», база даних) для позначення різних типів баз даних, в тому числі суспільно значущих комп'ютерних даних, які можуть зберігатися в загальному доступі і безперешкодно використовуватися широкою аудиторією.

Цілі руху відкритих даних схожі на інші «відкриті» рухи, такі як відкрите програмне забезпечення (open source), відкритий контент (open content) і відкритий доступ (open access).

Відкриті дані часто асоціюються з нетекстової матеріалами такими як карти, геноми, хімічні компоненти, математичні і наукові формули, медичні дані, дані про біологічне різноманіття. Проблеми найчастіше виникають з тієї причини що ці дані можуть бути комерційно цінними або можуть бути зібрані в якісь цінні продукти.

Доступ до Даних, контролюється державою і приватними організаціями. Контроль может бути через обмеження, Ліцензії, Копірайт, патенти и вимоги оплати для доступу або повторного використання. Прихильники Ідеї «відкритих Даних» вважають, що подібні обмеження йдуть проти суспільного блага и дані повінні бути доступні без обмежень або оплати. Також важливо що дані повінні бути доступні без запитів на дозвіл, хоча способи повторного використання, такі як виробництво товарів на базі даних, могут контролюватіся ліцензією.
Повне визначення відкритості розкриває в деталях:

* Доступність і читаність: дані повинні бути доступні цілком не дорожче розумної вартості їх відтворення; бажано через інтернет. Формат даних повинен бути зручним для читання і зміни.
* Повторне використання і поширення: дані повинні надаватися на умовах, які дозволяють їх повторне використання та поширення, в тому числі - в комбінації з іншими наборами даних.
* Загальна участь: кожен повинен мати можливість використовувати і поширювати дані. Не повинно бути дискримінації областей застосування, людей або груп. Наприклад, обмеження «тільки для некомерційного використання», яке забороняє «комерційне» застосування, або обмеження можливих областей застосування (наприклад, тільки в освіті), неприпустимі.

-------------------

# DDF
DDF - це модель даних для спільної гармонізації багатовимірної статистики.

* Модель даних
  DDF - це модель даних, що означає, що вона описує спосіб організації даних і визначення того, як фрагменти даних пов'язані один з одним.

* Гармонізація
  DDF можна використовувати для гармонізації даних, тобто він може об'єднувати дані з різних джерел в інтегровані, узгоджені і однозначні набори даних. DDF підтримує практичний робочий процес, який забезпечує простий в обслуговуванні і постійно зростаючий збір порівнянних даних. (ПРИМІТКА. Ця функціональність ще явно не задокументована, але буде в майбутніх версіях.)

* Спільне
  DDF - це загальна модель даних у відкритих числах. Відкриті номера - це ініціатива по краудсорсингом і гармонізації світових даних.

* Багатовимірна статистика
  DDF призначений для зберігання статистики з декількома вимірами. Наприклад, населення по країні та році, а також по країні, році, підлозі та віковій групі.
  
## Модель: DDF
  Це система для організації даних і визначення того, як частини даних пов'язані один з одним. Сам DDF не визначає формат, в якому зберігаються дані. Не має значення, чи зберігаються вони в csv-файлах, базі даних SQL або базі даних документів. Іншими словами: DDF є концептуальною моделлю.
  Однак концептуальної моделі недостатньо для прагматичного використання. Нам потрібно визначити, як зберігати DDF-дані в реальному світі, в файлах, на дисках. DDF потрібен формат даних. Два формату були визначені для двох різних цілей: DDFcsv і DDFmongo.
  * ***DDFcsv*** - це табличне представлення даних DDF в добре відомому форматі значень через кому (csv). З DDFcsv легко працювати для людей, знайомих з табличними даними, і дозволяє легко переходити з інших табличних моделей в DDF. Він призначений для читання як людьми, так і машинами. Цей формат використовується в відкритих номерах.
Читайте про DDFcsv

* ***DDFmongo*** - це уявлення документа DDF в базі даних Монго. Це використовується для сторінки інструментів Gapminder. Цей формат ще не документований.

## Мова запитів: DDFQL
  Для отримання даних з DDF ми розробили DDF Query Language DDFQL. Ця мова запитів має сильне схожість з SQL зі специфічними функціями, які підтримують можливості моделі даних DDF.
  ***Запит DDF*** виражається в нотації об'єкта JavaScript (JSON). DDFQL базується на SQL з додатковими можливостями для адаптації специфічних функцій DDF. Він складається з наступних основних пунктів: вибрати, звідки, замовити та приєднатись.

# Реляційна база даних

Реляційна база даних - база даних, заснована на реляційної моделі даних.

Реляційна модель даних — логічна модель даних.

До складу реляційної моделі даних зазвичай включають теорію нормалізації. Крістофер Дейт визначив три складові частини реляційної моделі даних:
* структурна
* маніпуляційна
* цілісна

Структурна частина моделі визначає, що єдиною структурою даних є нормалізоване n-арне відношення. 

Маніпуляційна частина моделі визначає два фундаментальних механізми маніпулювання даними — реляційну алгебру і реляційне числення. 

Цілісна частина моделі визначає вимоги цілісності сутностей і цілісності посилань. 

# ORM
 Об'єктно-реляційне відображення (ORM) - це метод, який дозволяє запитувати і маніпулювати даними з бази даних з використанням об'єктно-орієнтованої парадигми. Говорячи про ORM, більшість людей посилаються на бібліотеку, яка реалізує техніку об'єктно-реляційного зіставлення, звідси і фраза "ORM".
 
## ПРИКЛАД

Наприклад, ось зовсім уявний випадок з псевдомова:

У вас є клас книг, ви хочете отримати всі книги, автором яких є "Лінус". Вручну, ви б зробили щось на зразок цього:

```
book_list = new List();
sql = "SELECT book FROM library WHERE author = 'Linus'";
data = query(sql); // I over simplify ...
while (row = data.next())
{
     book = new Book();
     book.setAuthor(row.get('author');
     book_list.add(book);
}
```
З бібліотекою ORM це буде виглядати так:

```
book_list = BookTable.query(author="Linus");
```
## Використання ORM економить багато часу, тому що:Використання ORM економить багато часу, тому що:

1. СУХИЙ: ви пишете свою модель даних тільки в одному місці, і вам буде простіше оновлювати, підтримувати і повторно використовувати код.
2. Багато що робиться автоматично, від обробки бази даних до I18N.
3. Це змушує вас писати код MVC, що в результаті робить ваш код трохи чистіше.
4. Вам не потрібно писати погано сформований SQL 
5. Cанобробка; використання підготовлених операторів або транзакцій так само просто, як виклик методу.

------------------------------
# Порівняння популярних ресурсів, що оперують великою кількістю данних 

## Оцінка [https://data.worldbank.org](https://data.worldbank.org)  

Дані поділені на категорії | Є державним сервісом відкритих даних| Дозволяє в інтерактивному режимі попередньо опрацювати поля | Містить форум для обговорення | Є посилання на додатки, розроблені з використанням даного сервісу | Є список досліджень, пов'язаних з даними | Є API для доступу до даних | Є інструменти для інтерактивної обробки і аналізу даних | Є опенсорс проектом  | 
 --- | --- | --- |--- |--- |--- |--- |--- |--- 
| + | - | + | - | - | - | - | - | - 

## Оцінка [data.gov.ua](https://data.gov.ua)  

| Дані поділені на категорії | Є державним сервісом відкритих даних | Дозволяє в інтерактивному режимі попередньо опрацювати поля | Містить форум для обговорення | Є посилання на додатки, розроблені з використанням даного сервісу | Є список досліджень, пов'язаних з даними | Є API для доступу до даних | Є інструменти для інтерактивної обробки і аналізу даних | Є опенсорс проектом |
 --- | --- | --- |--- |--- |--- |--- |--- |--- 
 | +  | +  | +  | +  | +  | -  | -  | -  | -  |

## Оцінка [https://stat.gov.pl/en/](https://stat.gov.pl/en/)  

| Дані поділені на категорії | Є державним сервісом відкритих даних | Дозволяє в інтерактивному режимі попередньо опрацювати поля | Містить форум для обговорення | Є посилання на додатки, розроблені з використанням даного сервісу | Є список досліджень, пов'язаних з даними | Є API для доступу до даних | Є інструменти для інтерактивної обробки і аналізу даних | Є опенсорс проектом |
 --- | --- | --- |--- |--- |--- |--- |--- |--- 
 | +  | +  | -  | -  | - | + | + | -  | -  |

## Оцінка [https://www.gapminder.org](https://www.gapminder.org/)  

| Дані поділені на категорії | Є державним сервісом відкритих даних | Дозволяє в інтерактивному режимі попередньо опрацювати поля | Містить форум для обговорення | Є посилання на додатки, розроблені з використанням даного сервісу | Є список досліджень, пов'язаних з даними | Є API для доступу до даних | Є інструменти для інтерактивної обробки і аналізу даних | Є опенсорс проектом |
 --- | --- | --- |--- |--- |--- |--- |--- |--- 
 | +  | -  | -  | +  | +  | +  | +  | -  | -  |


### Посилання

* [Bachman notation](https://uk.wikipedia.org/w/index.php?title=Bachman_notation&action=edit&redlink=1)
* [EXPRESS[en]](https://uk.wikipedia.org/w/index.php?title=EXPRESS_(data_modeling_language)&action=edit&redlink=1)
* [IDEF1X[en]](https://uk.wikipedia.org/w/index.php?title=IDEF1X&action=edit&redlink=1)
* [Martin notation](https://uk.wikipedia.org/w/index.php?title=Martin_notation&action=edit&redlink=1)
* [(min, max)-Notation](https://uk.wikipedia.org/w/index.php?title=(min,_max)-Notation&action=edit&redlink=1)
* [Діаграма класів](https://uk.wikipedia.org/wiki/%D0%94%D1%96%D0%B0%D0%B3%D1%80%D0%B0%D0%BC%D0%B0_%D0%BA%D0%BB%D0%B0%D1%81%D1%96%D0%B2)
* [CУД](http://usu.kz/wiki/sistema_upravleniya_dannimi.php)  
* [PMD](https://ru.wikipedia.org/wiki/PDM-система)  
* [Open data](https://youcontrol.com.ua/ru/topics/open-data-otkryityie-dannyie-youcontrol/)
* [НСУД.-Концепция](https://digital.msu.ru/wp-content/uploads/НСУД.-Концепция_в8_25112018.pdf "НСУД.-Концепция")
* [Виды данных в поведенческих и социальных науках](http://soc-research.info/principles/3.html "Виды данных в поведенческих и социальных науках")
* [Open Numbers](https://open-numbers.github.io)