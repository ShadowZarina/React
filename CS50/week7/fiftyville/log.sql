-- Keep a log of any SQL queries you execute as you solve the mystery.

-- STEPS TO ACCESS TABLES & SCHEMAS
sqlite fiftyville.db
.tables
.schema crime_scene_reports

-- Access description of crime scene
SELECT description
FROM crime_scene_reports
WHERE month = 7
AND day = 28
AND street = 'Humphrey Street';

-- Access ID of crime scene
SELECT id
FROM crime_scene_reports
WHERE month = 7
AND day = 28
AND street = 'Humphrey Street';

ID = 295

-- TIPS FROM CS50
-- Explore schemas to see how the tables connect to one another
-- To query across multiple tables, nest/join tables
-- Maintain a list of suspects

-- Crime scene description
Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. |

-- Access witnesses interviews
.tables
.schema interviews

SELECT transcript
FROM interviews
WHERE year = 2024
AND month = 7
AND day = 28
AND transcript LIKE "%bakery%";

-- Transcripts of Interviews from July 28
Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.

I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emmas bakery,
I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.

As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
The thief then asked the person on the other end of the phone to purchase the flight ticket.

-- Look for security footage (10 mins after theft, cars leaving parking lot)
.tables
.schema bakery_security_logs

SELECT people.name, bakery_security_logs.activity, bakery_security_logs.license_plate
FROM bakery_security_logs
JOIN people ON people.license_plate = bakery_security_logs.license_plate
WHERE bakery_security_logs.year = 2024
AND bakery_security_logs.month = 7
AND bakery_security_logs.day = 28
AND bakery_security_logs.hour = 10
AND bakery_security_logs.minute BETWEEN 15 and 25;

+---------+----------+---------------+
|  name   | activity | license_plate |
+---------+----------+---------------+
| Vanessa | exit     | 5P2BI95       |
| Bruce   | exit     | 94KL13X       |
| Barry   | exit     | 6P58WS2       |
| Luca    | exit     | 4328GD8       |
| Sofia   | exit     | G412CB7       |
| Iman    | exit     | L93JTIZ       |
| Diana   | exit     | 322W7JE       |
| Kelsey  | exit     | 0NTHK55       |
+---------+----------+---------------+

-- Check ATM transactions (Leggett Street, early in the morning on July 28)
.tables
.schema atm_transactions

SELECT people.name, atm_transactions.transaction_type FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_transactions.year = 2024
AND atm_transactions.month = 7
AND atm_transactions.day = 28
AND atm_location = "Leggett Street"
AND atm_transactions.transaction_type = "withdraw";

+---------+------------------+
|  name   | transaction_type |
+---------+------------------+
| Bruce   | withdraw         |
| Diana   | withdraw         |
| Brooke  | withdraw         |
| Kenny   | withdraw         |
| Iman    | withdraw         |
| Luca    | withdraw         |
| Taylor  | withdraw         |
| Benista | withdraw         |
+---------+------------------+

-- Bruce, Diana and Luca can be seen in both tables

-- Look for phone calls (less than a minute)
.tables
.schema phone_calls

UPDATE phone_calls
SET receiver = people.name
FROM people
WHERE phone_calls.receiver = people.phone_number;

SELECT caller, receiver
FROM phone_calls
WHERE year = 2024
AND month = 7
AND day = 28
AND duration < 60;

+----------------+------------+
|     caller     |  receiver  |
+----------------+------------+
| (130) 555-0289 | Jack       |
| (499) 555-9472 | Larry      |
| (367) 555-5533 | Robin      |
| (499) 555-9472 | Melissa    |
| (286) 555-6063 | James      |
| (770) 555-1861 | Philip     |
| (031) 555-6622 | Jacqueline |
| (826) 555-1652 | Doris      |
| (338) 555-6650 | Anna       |
+----------------+------------+

SELECT people.name
FROm atm_transactions
JOIN bank_accounts ON bank_accounts.account_number = atm_transactions.account_number
JOIN people ON people.id = bank_accounts.person_id
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE atm_transactions.year = 2024
AND atm_transactions.month = 7
AND atm_transactions.day = 28
AND atm_transactions.atm_location = "Leggett Street"
AND bakery_security_logs.hour > 9 AND bakery_security_logs.hour < 11
ORDER BY bakery_security_logs.minute ASC;

+--------+
|  name  |
+--------+
| Bruce  |
| Luca   |
| Iman   |
| Diana  |
| Taylor |
+--------+

-- The people listed were involved in the bakery security logs and ATM transactions

-- Check flights (earliest out of Fiftyville on July 29)
.tables
.schema flights

SELECT id, hour, minute, origin_airport_id, destination_airport_id
FROM flights
WHERE year = 2024
AND month = 7
AND day = 29
ORDER BY hour ASC
LIMIT 1;

+----+------+--------+-------------------+------------------------+
| id | hour | minute | origin_airport_id | destination_airport_id |
+----+------+--------+-------------------+------------------------+
| 36 | 8    | 20     | 8                 | 4                      |
+----+------+--------+-------------------+------------------------+

-- The origin airport id is 8 and the destination airport id is 4

SELECT flights.destination_airport_id, name, phone_number, license_plate
FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
JOIN flights ON flights.id = passengers.flight_id
WHERE flights.id = 36
ORDER BY flights.hour ASC;

+------------------------+--------+----------------+---------------+
| destination_airport_id |  name  |  phone_number  | license_plate |
+------------------------+--------+----------------+---------------+
| 4                      | Doris  | (066) 555-9701 | M51FA04       |
| 4                      | Sofia  | (130) 555-0289 | G412CB7       |
| 4                      | Bruce  | (367) 555-5533 | 94KL13X       |
| 4                      | Edward | (328) 555-1152 | 130LD9Z       |
| 4                      | Kelsey | (499) 555-9472 | 0NTHK55       |
| 4                      | Taylor | (286) 555-6063 | 1106N58       |
| 4                      | Kenny  | (826) 555-1652 | 30G67EN       |
| 4                      | Luca   | (389) 555-5198 | 4328GD8       |
+------------------------+--------+----------------+---------------+

-- Bruce had a phone call with Robin; Luca did not have a phone call at all

-- Check people (purchased tickets, match license plate, had ATM transaction, had phone call)
.tables
.schema atm_transactions

-- Identify city where thief escaped to
SELECT city
FROM airports
WHERE id = 4;

+---------------+
|     city      |
+---------------+
| New York City |
+---------------+


-- CONCLUSIONS:
The thief escaped to New York City.
Bruce is the thief.
Robin is the accomplice.
