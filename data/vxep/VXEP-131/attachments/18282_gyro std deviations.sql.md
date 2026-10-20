# gyro std deviations.sql

Attachment 18282, text, 10 KB, added 2024-01-09 by Ryan Ferguson.

SELECT
    case
	    -- xpos
        WHEN column_name = 'xpos_gyro_1_x' THEN 'xpos_gyro_1_x'
        WHEN column_name = 'xpos_gyro_1_y' THEN 'xpos_gyro_1_y'
        WHEN column_name = 'xpos_gyro_1_z' THEN 'xpos_gyro_1_z'
        WHEN column_name = 'xpos_gyro_2_x' THEN 'xpos_gyro_2_x'
        WHEN column_name = 'xpos_gyro_2_y' THEN 'xpos_gyro_2_y'
        WHEN column_name = 'xpos_gyro_2_z' THEN 'xpos_gyro_2_z'
        --ypos
        WHEN column_name = 'ypos_gyro_1_x' THEN 'ypos_gyro_1_x'
        WHEN column_name = 'ypos_gyro_1_y' THEN 'ypos_gyro_1_y'
        WHEN column_name = 'ypos_gyro_1_z' THEN 'ypos_gyro_1_z'
        WHEN column_name = 'ypos_gyro_2_x' THEN 'ypos_gyro_2_x'
        WHEN column_name = 'ypos_gyro_2_y' THEN 'ypos_gyro_2_y'
        WHEN column_name = 'ypos_gyro_2_z' THEN 'ypos_gyro_2_z'
        --zpos
        WHEN column_name = 'zpos_gyro_1_x' THEN 'zpos_gyro_1_x'
        WHEN column_name = 'zpos_gyro_1_y' THEN 'zpos_gyro_1_y'
        WHEN column_name = 'zpos_gyro_1_z' THEN 'zpos_gyro_1_z'
        WHEN column_name = 'zpos_gyro_2_x' THEN 'zpos_gyro_2_x'
        WHEN column_name = 'zpos_gyro_2_y' THEN 'zpos_gyro_2_y'
        WHEN column_name = 'zpos_gyro_2_z' THEN 'zpos_gyro_2_z'
        -- xneg
        WHEN column_name = 'xneg_gyro_1_x' THEN 'xneg_gyro_1_x'
        WHEN column_name = 'xneg_gyro_1_y' THEN 'xneg_gyro_1_y'
        WHEN column_name = 'xneg_gyro_1_z' THEN 'xneg_gyro_1_z'
        WHEN column_name = 'xneg_gyro_2_x' THEN 'xneg_gyro_2_x'
        WHEN column_name = 'xneg_gyro_2_y' THEN 'xneg_gyro_2_y'
        WHEN column_name = 'xneg_gyro_2_z' THEN 'xneg_gyro_2_z'
        --yneg
        WHEN column_name = 'yneg_gyro_1_x' THEN 'yneg_gyro_1_x'
        WHEN column_name = 'yneg_gyro_1_y' THEN 'yneg_gyro_1_y'
        WHEN column_name = 'yneg_gyro_1_z' THEN 'yneg_gyro_1_z'
        WHEN column_name = 'yneg_gyro_2_x' THEN 'yneg_gyro_2_x'
        WHEN column_name = 'yneg_gyro_2_y' THEN 'yneg_gyro_2_y'
        WHEN column_name = 'yneg_gyro_2_z' THEN 'yneg_gyro_2_z'
        --zneg
        WHEN column_name = 'zneg_gyro_1_x' THEN 'zneg_gyro_1_x'
        WHEN column_name = 'zneg_gyro_1_y' THEN 'zneg_gyro_1_y'
        WHEN column_name = 'zneg_gyro_1_z' THEN 'zneg_gyro_1_z'
        WHEN column_name = 'zneg_gyro_2_x' THEN 'zneg_gyro_2_x'
        WHEN column_name = 'zneg_gyro_2_y' THEN 'zneg_gyro_2_y'
        WHEN column_name = 'zneg_gyro_2_z' THEN 'zneg_gyro_2_z'
        --neutral
        WHEN column_name = 'neutral_gyro_1_x' THEN 'neutral_gyro_1_x'
        WHEN column_name = 'neutral_gyro_1_y' THEN 'neutral_gyro_1_y'
        WHEN column_name = 'neutral_gyro_1_z' THEN 'neutral_gyro_1_z'
        WHEN column_name = 'neutral_gyro_2_x' THEN 'neutral_gyro_2_x'
        WHEN column_name = 'neutral_gyro_2_y' THEN 'neutral_gyro_2_y'
        WHEN column_name = 'neutral_gyro_2_z' THEN 'neutral_gyro_2_z'
    END AS column_name,
    AVG(value) AS avg_value,
    AVG(value) + (2 * STDDEV(value)) AS two_sigma_upper,
    AVG(value) - (2 * STDDEV(value)) AS two_sigma_lower,
    (AVG(value) + 2 * STDDEV(value)) - (AVG(value) - 2 * STDDEV(value)) as stddev_difference,
    MIN(value) as min,
    MAX(value) as max,
    min(value) - max(value) as minmax_difference,
    COUNT(value) as samples
FROM (
	-- xpos
    SELECT 'xpos_gyro_1_x' AS column_name, xpos_gyro_1_x AS value FROM gyroverification where 80 < xpos_gyro_1_x and xpos_gyro_1_x < 100
    UNION ALL
    SELECT 'xpos_gyro_1_y' AS column_name, xpos_gyro_1_y AS value FROM gyroverification where -10 < xpos_gyro_1_y and xpos_gyro_1_y < 10
    UNION ALL
    SELECT 'xpos_gyro_1_z' AS column_name, xpos_gyro_1_z AS value FROM gyroverification where -10 < xpos_gyro_1_z and xpos_gyro_1_z < 10
    UNION ALL
    SELECT 'xpos_gyro_2_x' AS column_name, xpos_gyro_2_x AS value FROM gyroverification where 80 < xpos_gyro_2_x and xpos_gyro_2_x < 100
    UNION ALL
    SELECT 'xpos_gyro_2_y' AS column_name, xpos_gyro_2_y AS value FROM gyroverification where -10 < xpos_gyro_2_y and xpos_gyro_2_y < 10
    UNION ALL
    SELECT 'xpos_gyro_2_z' AS column_name, xpos_gyro_2_z AS value FROM gyroverification where -10 < xpos_gyro_2_z and xpos_gyro_2_z < 10
    UNION ALL
  	-- ypos
    SELECT 'ypos_gyro_1_x' AS column_name, ypos_gyro_1_x AS value FROM gyroverification where -10 < ypos_gyro_1_x and ypos_gyro_1_x < 10
    UNION ALL
    SELECT 'ypos_gyro_1_y' AS column_name, ypos_gyro_1_y AS value FROM gyroverification where 80 < ypos_gyro_1_y and ypos_gyro_1_y < 100
    UNION ALL
    SELECT 'ypos_gyro_1_z' AS column_name, ypos_gyro_1_z AS value FROM gyroverification where -10 < ypos_gyro_1_z and ypos_gyro_1_z < 10
    UNION ALL
    SELECT 'ypos_gyro_2_x' AS column_name, ypos_gyro_2_x AS value FROM gyroverification where -10 < ypos_gyro_1_x and ypos_gyro_1_x < 10
    UNION ALL
    SELECT 'ypos_gyro_2_y' AS column_name, ypos_gyro_2_y AS value FROM gyroverification where 80 < ypos_gyro_1_y and ypos_gyro_1_y < 100
    UNION ALL
    SELECT 'ypos_gyro_2_z' AS column_name, ypos_gyro_2_z AS value FROM gyroverification where -10 < ypos_gyro_1_z and ypos_gyro_1_z < 10
    UNION ALL
    -- zpos
    SELECT 'zpos_gyro_1_x' AS column_name, zpos_gyro_1_x AS value FROM gyroverification where -10 < zpos_gyro_1_x and zpos_gyro_1_x < 100
    UNION ALL
    SELECT 'zpos_gyro_1_y' AS column_name, zpos_gyro_1_y AS value FROM gyroverification where -10 < zpos_gyro_1_y and zpos_gyro_1_y < 100
    UNION ALL
    SELECT 'zpos_gyro_1_z' AS column_name, zpos_gyro_1_z AS value FROM gyroverification where 80 < zpos_gyro_1_z and zpos_gyro_1_z < 100
    UNION ALL
    SELECT 'zpos_gyro_2_x' AS column_name, zpos_gyro_2_x AS value FROM gyroverification where -10 < zpos_gyro_2_x and zpos_gyro_2_x < 100
    UNION ALL
    SELECT 'zpos_gyro_2_y' AS column_name, zpos_gyro_2_y AS value FROM gyroverification where -10 < zpos_gyro_2_y and zpos_gyro_2_y < 100
    UNION ALL
    SELECT 'zpos_gyro_2_z' AS column_name, zpos_gyro_2_z AS value FROM gyroverification where 80 < zpos_gyro_2_z and zpos_gyro_2_z < 100
    UNION ALL
    -- xneg
    SELECT 'xneg_gyro_1_x' AS column_name, xneg_gyro_1_x AS value FROM gyroverification where -100 < xneg_gyro_1_x and xneg_gyro_1_x < -80
    UNION ALL
    SELECT 'xneg_gyro_1_y' AS column_name, xneg_gyro_1_y AS value FROM gyroverification where -10 < xneg_gyro_1_y and xneg_gyro_1_y < 10
    UNION ALL
    SELECT 'xneg_gyro_1_z' AS column_name, xneg_gyro_1_z AS value FROM gyroverification where -10 < xneg_gyro_1_z and xneg_gyro_1_z < 10
    UNION ALL
    SELECT 'xneg_gyro_2_x' AS column_name, xneg_gyro_2_x AS value FROM gyroverification where -100 < xneg_gyro_2_x and xneg_gyro_2_x < -80
    UNION ALL
    SELECT 'xneg_gyro_2_y' AS column_name, xneg_gyro_2_y AS value FROM gyroverification where -10 < xneg_gyro_2_y and xneg_gyro_2_y < 10
    UNION ALL
    SELECT 'xneg_gyro_2_z' AS column_name, xneg_gyro_2_z AS value FROM gyroverification where -10 < xneg_gyro_2_z and xneg_gyro_2_z < 10
    UNION ALL
  	-- yneg
    SELECT 'yneg_gyro_1_x' AS column_name, yneg_gyro_1_x AS value FROM gyroverification where -10 < yneg_gyro_1_x and yneg_gyro_1_x < 10
    UNION ALL
    SELECT 'yneg_gyro_1_y' AS column_name, yneg_gyro_1_y AS value FROM gyroverification where -100 < yneg_gyro_1_y and yneg_gyro_1_y < -80
    UNION ALL
    SELECT 'yneg_gyro_1_z' AS column_name, yneg_gyro_1_z AS value FROM gyroverification where -10 < yneg_gyro_1_z and yneg_gyro_1_z < 10
    UNION ALL
    SELECT 'yneg_gyro_2_x' AS column_name, yneg_gyro_2_x AS value FROM gyroverification where -10 < yneg_gyro_2_x and yneg_gyro_2_x < 10
    UNION ALL
    SELECT 'yneg_gyro_2_y' AS column_name, yneg_gyro_2_y AS value FROM gyroverification where -100 < yneg_gyro_2_y and yneg_gyro_2_y < -80
    UNION ALL
    SELECT 'yneg_gyro_2_z' AS column_name, yneg_gyro_2_z AS value FROM gyroverification where -10 < yneg_gyro_2_z and yneg_gyro_2_z < 10
    UNION ALL
    -- zneg
    SELECT 'zneg_gyro_1_x' AS column_name, zneg_gyro_1_x AS value FROM gyroverification where -10 < zneg_gyro_1_x and zneg_gyro_1_x < 10
    UNION ALL
    SELECT 'zneg_gyro_1_y' AS column_name, zneg_gyro_1_y AS value FROM gyroverification where -10 < zneg_gyro_1_y and zneg_gyro_1_y < 10
    UNION ALL
    SELECT 'zneg_gyro_1_z' AS column_name, zneg_gyro_1_z AS value FROM gyroverification where -100 < zneg_gyro_1_z and zneg_gyro_1_z < -80
    UNION ALL
    SELECT 'zneg_gyro_2_x' AS column_name, zneg_gyro_2_x AS value FROM gyroverification where -10 < zneg_gyro_2_x and zneg_gyro_2_x < 10
    UNION ALL
    SELECT 'zneg_gyro_2_y' AS column_name, zneg_gyro_2_y AS value FROM gyroverification where -10 < zneg_gyro_2_y and zneg_gyro_2_y < 10
    UNION ALL
    SELECT 'zneg_gyro_2_z' AS column_name, zneg_gyro_2_z AS value FROM gyroverification where -100 < zneg_gyro_2_z and zneg_gyro_2_z < -80
    UNION ALL
    -- neutral
    SELECT 'neutral_gyro_1_x' AS column_name, neutral_gyro_1_x AS value FROM gyroverification where -10 < neutral_gyro_1_x and neutral_gyro_1_x < 10
    UNION ALL
    SELECT 'neutral_gyro_1_y' AS column_name, neutral_gyro_1_y AS value FROM gyroverification where -10 < neutral_gyro_1_y and neutral_gyro_1_y < 10
    UNION ALL
    SELECT 'neutral_gyro_1_z' AS column_name, neutral_gyro_1_z AS value FROM gyroverification where -10 < neutral_gyro_1_z and neutral_gyro_1_z < 10
    UNION ALL
    SELECT 'neutral_gyro_2_x' AS column_name, neutral_gyro_2_x AS value FROM gyroverification where -10 < neutral_gyro_2_x and neutral_gyro_2_x < 10
    UNION ALL
    SELECT 'neutral_gyro_2_y' AS column_name, neutral_gyro_2_y AS value FROM gyroverification where -10 < neutral_gyro_2_y and neutral_gyro_2_y < 10
    UNION ALL
    SELECT 'neutral_gyro_2_z' AS column_name, neutral_gyro_2_z AS value FROM gyroverification where -10 < neutral_gyro_2_z and neutral_gyro_2_z < 10
) AS subquery
GROUP BY column_name
order by column_name ASC;
