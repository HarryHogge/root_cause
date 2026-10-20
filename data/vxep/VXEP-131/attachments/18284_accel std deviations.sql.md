# accel std deviations.sql

Attachment 18284, text, 9 KB, added 2024-01-09 by Ryan Ferguson.

SELECT
    case
	    -- xpos
        WHEN column_name = 'xpos_accel_1_x' THEN 'xpos_accel_1_x'
        WHEN column_name = 'xpos_accel_1_y' THEN 'xpos_accel_1_y'
        WHEN column_name = 'xpos_accel_1_z' THEN 'xpos_accel_1_z'
        WHEN column_name = 'xpos_accel_2_x' THEN 'xpos_accel_2_x'
        WHEN column_name = 'xpos_accel_2_y' THEN 'xpos_accel_2_y'
        WHEN column_name = 'xpos_accel_2_z' THEN 'xpos_accel_2_z'
        --ypos
        WHEN column_name = 'ypos_accel_1_x' THEN 'ypos_accel_1_x'
        WHEN column_name = 'ypos_accel_1_y' THEN 'ypos_accel_1_y'
        WHEN column_name = 'ypos_accel_1_z' THEN 'ypos_accel_1_z'
        WHEN column_name = 'ypos_accel_2_x' THEN 'ypos_accel_2_x'
        WHEN column_name = 'ypos_accel_2_y' THEN 'ypos_accel_2_y'
        WHEN column_name = 'ypos_accel_2_z' THEN 'ypos_accel_2_z'
        --zpos
        WHEN column_name = 'zpos_accel_1_x' THEN 'zpos_accel_1_x'
        WHEN column_name = 'zpos_accel_1_y' THEN 'zpos_accel_1_y'
        WHEN column_name = 'zpos_accel_1_z' THEN 'zpos_accel_1_z'
        WHEN column_name = 'zpos_accel_2_x' THEN 'zpos_accel_2_x'
        WHEN column_name = 'zpos_accel_2_y' THEN 'zpos_accel_2_y'
        WHEN column_name = 'zpos_accel_2_z' THEN 'zpos_accel_2_z'
        -- xneg
        WHEN column_name = 'xneg_accel_1_x' THEN 'xneg_accel_1_x'
        WHEN column_name = 'xneg_accel_1_y' THEN 'xneg_accel_1_y'
        WHEN column_name = 'xneg_accel_1_z' THEN 'xneg_accel_1_z'
        WHEN column_name = 'xneg_accel_2_x' THEN 'xneg_accel_2_x'
        WHEN column_name = 'xneg_accel_2_y' THEN 'xneg_accel_2_y'
        WHEN column_name = 'xneg_accel_2_z' THEN 'xneg_accel_2_z'
        --yneg
        WHEN column_name = 'yneg_accel_1_x' THEN 'yneg_accel_1_x'
        WHEN column_name = 'yneg_accel_1_y' THEN 'yneg_accel_1_y'
        WHEN column_name = 'yneg_accel_1_z' THEN 'yneg_accel_1_z'
        WHEN column_name = 'yneg_accel_2_x' THEN 'yneg_accel_2_x'
        WHEN column_name = 'yneg_accel_2_y' THEN 'yneg_accel_2_y'
        WHEN column_name = 'yneg_accel_2_z' THEN 'yneg_accel_2_z'
        --zneg
        WHEN column_name = 'zneg_accel_1_x' THEN 'zneg_accel_1_x'
        WHEN column_name = 'zneg_accel_1_y' THEN 'zneg_accel_1_y'
        WHEN column_name = 'zneg_accel_1_z' THEN 'zneg_accel_1_z'
        WHEN column_name = 'zneg_accel_2_x' THEN 'zneg_accel_2_x'
        WHEN column_name = 'zneg_accel_2_y' THEN 'zneg_accel_2_y'
        WHEN column_name = 'zneg_accel_2_z' THEN 'zneg_accel_2_z'
    END AS column_name,
    AVG(value) AS avg_value,
    AVG(value) + 2 * STDDEV(value) AS two_sigma_upper,
    AVG(value) - 2 * STDDEV(value) AS two_sigma_lower,
    (AVG(value) + 2 * STDDEV(value)) - (AVG(value) - 2 * STDDEV(value)) as stddev_difference,
    MIN(value) as min,
    MAX(value) as max,
    MAX(value) - MIN(value) as minmax_difference,
    COUNT(value) as samples
FROM (
	-- xpos
    SELECT 'xpos_accel_1_x' AS column_name, xpos_accel_1_x AS value FROM accelverification where 0.5 < xpos_accel_1_x and xpos_accel_1_x < 1.5
    UNION ALL
    SELECT 'xpos_accel_1_y' AS column_name, xpos_accel_1_y AS value FROM accelverification where -0.5 < xpos_accel_1_y and xpos_accel_1_y < 0.5
    UNION ALL
    SELECT 'xpos_accel_1_z' AS column_name, xpos_accel_1_z AS value FROM accelverification where -0.5 < xpos_accel_1_z and xpos_accel_1_z < 0.5
    UNION ALL
    SELECT 'xpos_accel_2_x' AS column_name, xpos_accel_2_x AS value FROM accelverification where 0.5 < xpos_accel_2_x and xpos_accel_2_x < 1.5
    UNION ALL
    SELECT 'xpos_accel_2_y' AS column_name, xpos_accel_2_y AS value FROM accelverification where -0.5 < xpos_accel_2_y and xpos_accel_2_y < 0.5
    UNION ALL
    SELECT 'xpos_accel_2_z' AS column_name, xpos_accel_2_z AS value FROM accelverification where -0.5 < xpos_accel_2_z and xpos_accel_2_z < 0.5
    UNION ALL
  	-- ypos
    SELECT 'ypos_accel_1_x' AS column_name, ypos_accel_1_x AS value FROM accelverification where -0.5 < ypos_accel_1_x and ypos_accel_1_x < 0.5
    UNION ALL
    SELECT 'ypos_accel_1_y' AS column_name, ypos_accel_1_y AS value FROM accelverification where 0.5 < ypos_accel_1_y and ypos_accel_1_y < 1.5
    UNION ALL
    SELECT 'ypos_accel_1_z' AS column_name, ypos_accel_1_z AS value FROM accelverification where -0.5 < ypos_accel_1_z and ypos_accel_1_z < 0.5
    UNION ALL
    SELECT 'ypos_accel_2_x' AS column_name, ypos_accel_2_x AS value FROM accelverification where -0.5 < ypos_accel_2_x and ypos_accel_2_x < 0.5
    UNION ALL
    SELECT 'ypos_accel_2_y' AS column_name, ypos_accel_2_y AS value FROM accelverification where 0.5 < ypos_accel_2_y and ypos_accel_2_y < 1.5
    UNION ALL
    SELECT 'ypos_accel_2_z' AS column_name, ypos_accel_2_z AS value FROM accelverification where -0.5 < ypos_accel_2_z and ypos_accel_2_z < 0.5
    UNION ALL
    -- zpos
    SELECT 'zpos_accel_1_x' AS column_name, zpos_accel_1_x AS value FROM accelverification where -0.5 < zpos_accel_1_x and zpos_accel_1_x < 0.5
    UNION ALL
    SELECT 'zpos_accel_1_y' AS column_name, zpos_accel_1_y AS value FROM accelverification where -0.5 < zpos_accel_1_y and zpos_accel_1_y < 0.5
    UNION ALL
    SELECT 'zpos_accel_1_z' AS column_name, zpos_accel_1_z AS value FROM accelverification where 0.5 < zpos_accel_1_z and zpos_accel_1_z < 1.5
    UNION ALL
    SELECT 'zpos_accel_2_x' AS column_name, zpos_accel_2_x AS value FROM accelverification where -0.5 < zpos_accel_2_x and zpos_accel_2_x < 0.5
    UNION ALL
    SELECT 'zpos_accel_2_y' AS column_name, zpos_accel_2_y AS value FROM accelverification where -0.5 < zpos_accel_2_y and zpos_accel_2_y < 0.5
    UNION ALL
    SELECT 'zpos_accel_2_z' AS column_name, zpos_accel_2_z AS value FROM accelverification where 0.5 < zpos_accel_2_z and zpos_accel_2_z < 1.5
    UNION ALL
    -- xneg
    SELECT 'xneg_accel_1_x' AS column_name, xneg_accel_1_x AS value FROM accelverification where -1.5 < xneg_accel_1_x and xneg_accel_1_x < -0.5
    UNION ALL
    SELECT 'xneg_accel_1_y' AS column_name, xneg_accel_1_y AS value FROM accelverification where -0.5 < xneg_accel_1_y and xneg_accel_1_y < 0.5
    UNION ALL
    SELECT 'xneg_accel_1_z' AS column_name, xneg_accel_1_z AS value FROM accelverification where -0.5 < xneg_accel_1_z and xneg_accel_1_z < 0.5
    UNION ALL
    SELECT 'xneg_accel_2_x' AS column_name, xneg_accel_2_x AS value FROM accelverification where -1.5 < xneg_accel_2_x and xneg_accel_2_x < -0.5
    UNION ALL
    SELECT 'xneg_accel_2_y' AS column_name, xneg_accel_2_y AS value FROM accelverification where -0.5 < xneg_accel_2_y and xneg_accel_2_y < 0.5
    UNION ALL
    SELECT 'xneg_accel_2_z' AS column_name, xneg_accel_2_z AS value FROM accelverification where -0.5 < xneg_accel_2_z and xneg_accel_2_z < 0.5
    UNION ALL
  	-- yneg
    SELECT 'yneg_accel_1_x' AS column_name, yneg_accel_1_x AS value FROM accelverification where -0.5 < yneg_accel_1_x and yneg_accel_1_x < 0.5
    UNION ALL
    SELECT 'yneg_accel_1_y' AS column_name, yneg_accel_1_y AS value FROM accelverification where -1.5 < yneg_accel_1_y and yneg_accel_1_y < -0.5
    UNION ALL
    SELECT 'yneg_accel_1_z' AS column_name, yneg_accel_1_z AS value FROM accelverification where -0.5 < yneg_accel_1_z and yneg_accel_1_z < 0.5
    UNION ALL
    SELECT 'yneg_accel_2_x' AS column_name, yneg_accel_2_x AS value FROM accelverification where -0.5 < yneg_accel_2_x and yneg_accel_2_x < 0.5
    UNION ALL
    SELECT 'yneg_accel_2_y' AS column_name, yneg_accel_2_y AS value FROM accelverification where -1.5 < yneg_accel_2_y and yneg_accel_2_y < -0.5
    UNION ALL
    SELECT 'yneg_accel_2_z' AS column_name, yneg_accel_2_z AS value FROM accelverification where -0.5 < yneg_accel_2_z and yneg_accel_2_z < 0.5
    UNION ALL
    -- zneg
    SELECT 'zneg_accel_1_x' AS column_name, zneg_accel_1_x AS value FROM accelverification where -0.5 < zneg_accel_1_x and zneg_accel_1_x < 0.5
    UNION ALL
    SELECT 'zneg_accel_1_y' AS column_name, zneg_accel_1_y AS value FROM accelverification where -0.5 < zneg_accel_1_y and zneg_accel_1_y < 0.5
    UNION ALL
    SELECT 'zneg_accel_1_z' AS column_name, zneg_accel_1_z AS value FROM accelverification where -1.5 < zneg_accel_1_z and zneg_accel_1_z < -0.5
    UNION ALL
    SELECT 'zneg_accel_2_x' AS column_name, zneg_accel_2_x AS value FROM accelverification where -0.5 < zneg_accel_2_x and zneg_accel_2_x < 0.5
    UNION ALL
    SELECT 'zneg_accel_2_y' AS column_name, zneg_accel_2_y AS value FROM accelverification where -0.5 < zneg_accel_2_y and zneg_accel_2_y < 0.5
    UNION ALL
    SELECT 'zneg_accel_2_z' AS column_name, zneg_accel_2_z AS value FROM accelverification where -1.5 < zneg_accel_2_z and zneg_accel_2_z < -0.5
) AS subquery
	WHERE value >= -2 AND value <= 2 -- Add the filter condition
GROUP BY column_name
order by column_name ASC;
