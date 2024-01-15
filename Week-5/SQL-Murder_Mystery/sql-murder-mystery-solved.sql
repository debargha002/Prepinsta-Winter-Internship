-- loading database and tables
USE database sql-murder-mystery;

-- viewing tables one by one
SELECT * 
FROM crime_scene_report;
--
SELECT * 
FROM drivers_license;
--
SELECT * 
FROM facebook_event_checkin;
--
SELECT * 
FROM get_fit_now_check_in;
--
SELECT * 
FROM get_fit_now_member;
--
SELECT * 
FROM income;
--
SELECT * 
FROM interview
--
SELECT * 
FROM person;
--

/* Run a query to retrieve the crime scene report for the murder that occurred on Jan.15, 2018, in SQL City. 
Gather all available details from the report.*/
SELECT * 
FROM crime_scene_report 
WHERE date = 20180115 AND type= 'murder' AND city = 'SQL City';

/* Check the personal details of witnesses involved in the case. 
Retrieve their names, addresses, and any other relevant information.*/
SELECT * 
FROM person 
where address_street_name=='Northwestern Dr';
--
SELECT * 
FROM person 
WHERE address_number=='4919';
--
SELECT * 
FROM person 
WHERE address_street_name = 'Franklin Ave' AND name LIKE 'Annabel%';

/* Access the recorded interviews of witnesses conducted after the murder. 
Gather insights into their statements and potential clues.*/
SELECT * 
FROM interview 
WHERE person_id = 16371;
--
SELECT * 
FROM interview 
WHERE person_id =14887;

/* Investigate the gym database using details obtained from the crime scene report and witness interviews. 
Look for any gym-related information that might be relevant.*/
SELECT * 
FROM get_fit_now_member 
WHERE membership_status= 'gold' AND id LIKE '48Z%';

/* Examine the car details associated with the crime scene.
Retrieve information about the vehicles present during the incident.*/
SELECT * 
FROM drivers_license 
WHERE plate_number LIKE '%H42W%' AND gender = 'male';

/*Identify and collect personal details mentioned in the previous query. 
This includes names, addresses, and any additional details.*/
SELECT * 
FROM  drivers_license 
WHERE id= 423327;
--
SELECT * 
FROM person 
WHERE license_id= 423327;

/* Determine who is identified in the previous query as a member of the gym. 
Utilize the gym database to confirm their membership status.*/
SELECT * 
FROM get_fit_now_member 
WHERE name = 'Jeremy Bowers';
--
SELECT * 
FROM interview 
WHERE person_id= 67318;
--
SELECT * 
FROM drivers_license 
WHERE hair_color ='red' AND car_make= 'Tesla'  AND gender ='female';
--
SELECT *
FROM person 
WHERE license_id = '202298' OR license_id = '291182' OR license_id = '918773';
--
SELECT person_id, count(*), event_name 
FROM facebook_event_checkin  
GROUP BY person_id 
HAVING COUNT(*) = 3 AND event_name = 'SQL Symphony Concert' AND date like '%201712%';

-- Therefore, we found that the mastermind behind this murder is MIRANDA PRIESLY who paid JEREMY BOWERS for the murder.

--------------------------------------------------------------------------------THE CASE IS SOLVED.----------------------------------------------------------------