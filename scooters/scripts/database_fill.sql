INSERT INTO scooters
SELECT
       uuid_generate_v4() AS id,
       POINT(37 + random(), 55 + random()) AS location,
       (CASE WHEN random() > 0.5 THEN uuid_generate_v4() ELSE NULL END) AS "user"
FROM generate_series(1, 10)