# Existing MOD PAYLOAD PVT Messaging.pptx

Attachment 25309, pptx, 72 KB, added 2025-01-07 by Kurt Burian.

## Slide 1

Existing MOD PAYLOAD PVT Messaging
Kurt Burian
12/20/24

## Slide 2

Existing MAIM PVT Output
MAIM File: Sbge.c -> collect_callback()

## Slide 3

send json_att, 100 ms
snprintf((char*)json_att, JSON_SIZE_ATT, "{\"class\":\"ATT\",\"acc_x\":%f,\"acc_y\":%f,\"acc_z\":%f,\"gyro_x\":%f,\"gyro_y\":%f,\"gyro_z\":%f,\"temp\":%f,\"mag_x\":%f,\"mag_y\":%f,\"mag_z\":%f,\"roll\":%f,\"pitch\":%f,\"yaw\":%f,\"heading\":%f}\n",
                //pOutput->utcYear, pOutput->utcMonth, pOutput->utcDay, pOutput->utcHour, pOutput->utcMin, pOutput->utcSec, pOutput->utcNano,
                pOutput->accelerometers[0],
                pOutput->accelerometers[1],
                pOutput->accelerometers[2],
                pOutput->gyroscopes[0],
                pOutput->gyroscopes[1],
                pOutput->gyroscopes[2],
                pOutput->temperatures[0],
                pOutput->magnetometers[0],
                pOutput->magnetometers[1],
                pOutput->magnetometers[2],
                pOutput->stateEuler[0],
                pOutput->stateEuler[1],
                pOutput->stateEuler[2],
                (float)((float)(pOutput->gpsHeading) / 100000.0)
            );

## Slide 4

send json_imunav, 100 ms
snprintf((char*)json_imunav, JSON_SIZE_IMUNAV, "{\"class\":\"IMUNAV\",\"veln\":%f,\"vele\":%f,\"veld\":%f}\n",
                //pOutput->utcYear, pOutput->utcMonth, pOutput->utcDay, pOutput->utcHour, pOutput->utcMin, pOutput->utcSec, pOutput->utcNano,
                pOutput->velocity[0],
                pOutput->velocity[1],
                pOutput->velocity[2]
            );

## Slide 5

send json_tpv, 1 sec
snprintf((char*)json_tpv, JSON_SIZE_TPV, "{\"class\":\"TPV\",\"time\":\"%04u-%02u-%02uT%02u:%02u:%02u.%09uZ\",\"ept\":%f,\"track\":%f,\"lat\":%f,\"lon\":%f,\"alt\":%f,\"mode\":%u,\"epx\":%f,\"epy\":%f,\"epv\":%f,\"climb\":%f,\"epd\":%f,\"epc\":%f}\n",
                pOutput->utcYear, pOutput->utcMonth, pOutput->utcDay, pOutput->utcHour, pOutput->utcMin, pOutput->utcSec, pOutput->utcNano,\
                pOutputExt->ept,\
                (float)((float)(pOutput->gpsHeading) / 100000.0),\
                (float)((float)(pOutput->gpsLatitude) / 10000000.0),\
                (float)((float)(pOutput->gpsLongitude) / 10000000.0),\
                (float)((float)(pOutput->gpsAltitude) / 1000.0),\
                pOutputExt->mode,\
                pOutputExt->epx,\
                pOutputExt->epy,\
                pOutputExt->epv,\
                (float)((float)(pOutput->gpsVelocity[2]) / 100.0),\
                pOutputExt->epd,\
                (float)((float)(pOutputExt->gpsVelocityAcc[2]) / 100.0)\
            );

## Slide 6

send json_sky, 1 sec
snprintf((char*)json_sky, JSON_SIZE_SKY, "{\"class\":\"SKY\",\"time\":\"%04u-%02u-%02uT%02u:%02u:%02u.%09uZ\",\"hdop\":%f}\n",
                pOutput->utcYear, pOutput->utcMonth, pOutput->utcDay, pOutput->utcHour, pOutput->utcMin, pOutput->utcSec, pOutput->utcNano,\
                mHdop\
            );

## Slide 7

send json_status, 1 sec
snprintf((char*)json_status, JSON_SIZE_STATUS, "{\"class\":\"STATUS\",\"general\":\"%x\",\"com\":\"%x\",\"aiding\":\"%x\",\"utc\":\"%x\",\"imu\":\"%x\",\"mag\":\"%x\",\"sol\":\"%x\",\"vel\":\"%x\",\"pos\":\"%x\",\"alt\":\"%x\"}\n",
                pOutput->generalStatus,\
                pOutput->comStatus,\
                pOutput->aidingStatus,\
                pOutput->utcStatus,\
                pOutput->imuStatus,\
                pOutput->magStatus,\
                pOutput->solutionStatus,\
                pOutput->gpsVelStatus,\
                pOutput->gpsPosStatus,\
                pOutput->pressureStatus\
            );

## Slide 8

send json_pressue, 1 sec
snprintf((char*)json_pressure, JSON_SIZE_PRESSURE, "{\"class\":\"PRESSURE\",\"pressure\":%u,\"alt\":%d}\n",
                pOutput->baroPressure,\
                pOutput->baroAltitude\
            );

## Slide 9

send json_addl, 1 sec
snprintf((char*)json_addl, JSON_SIZE_ADDL, "{\"class\":\"ADDL\",\"up\":%u,\"tow\":%u,\"und\":%f,\"gveln\":%f,\"gvele\":%f,\"gveld\":%f,\"epn\":%f,\"epe\":%f,\"epd\":%f,\"nsv\":%u}\n",
                pOutput->timeSinceReset,\
                pOutputExt->timeOfWeek,\
                pOutput->undulation,\
                (float)((float)(pOutput->gpsVelocity[0]) / 100.0),\
                (float)((float)(pOutput->gpsVelocity[1]) / 100.0),\
                (float)((float)(pOutput->gpsVelocity[2]) / 100.0),\
                (float)((float)(pOutputExt->gpsVelocityAcc[0]) / 100.0),\
                (float)((float)(pOutputExt->gpsVelocityAcc[1]) / 100.0),\
                (float)((float)(pOutputExt->gpsVelocityAcc[2]) / 100.0),\
                pOutput->gpsNbSats\
            );

## Slide 10

MOD PAYLOADExisting SBG Eclipse AHRS to MAIM Messaging
Doc Created with V3 API: https://github.com/SBG-Systems/sbgECom/blob/main/src/logs/
MAIM uses V1 API: https://bitbucket.org/edgeautonomy/maim/src/master/sbge/src/binaryLogs/
Production AHRS Flashed to V2 API

## Slide 11

Message Rates
System Status: 1 Hz
UTC: 20 Hz
IMU Data: 20 Hz
Mag: 20 Hz
EKF Euler: 20 Hz
EKF Nav: 20 Hz
GPS Vel: 5 Hz
GPS Pos: 5Hz
Airdata: 1 Hz
GGA: 1 Hz (with NMEA disabled, this might do nothing)

## Slide 12

Status
typedef struct _SbgEComLogStatus
{
    uint32_t    timeStamp;                                              /*!< Time in us since the sensor power up. */
    uint16_t    generalStatus;                                          /*!< General status bitmask and enum. */
    uint32_t    comStatus;                                              /*!< Communication status bitmask and enum. */
    uint16_t    comStatus2;                                             /*!< Second communication status bitmask and enum (used since v4.0). */
    uint32_t    aidingStatus;                                           /*!< Aiding equipments status bitmask and enum. */
    uint32_t    reserved2;                                              /*!< Reserved status field for future use. */
    uint16_t    reserved3;                                              /*!< Reserved status field for future use. */
    uint32_t    uptime;                                                 /*!< System uptime in seconds - 0 if N/A (added v1.7). */
    uint8_t     cpuUsage;                                               /*!< Main CPU usage in percent - 0xFF if N/A (added v5.0). */
} SbgEComLogStatus;

## Slide 13

UTC
/*!
 * Status for the GNSS UTC time information.
 */
typedef enum _SbgEComUtcStatus
{
    SBG_ECOM_UTC_STATUS_INVALID             = 0,                        /*!< UTC time is not known and invalid. The INS uses the firmware default initial date/time. */
    SBG_ECOM_UTC_STATUS_NO_LEAP_SEC         = 1,                        /*!< UTC time is initialized but the leap second is not known - the default firmware value is used. */
    SBG_ECOM_UTC_STATUS_INITIALIZED         = 2                         /*!< UTC time is initialized with a fully resolved leap second information. */
} SbgEComUtcStatus;

## Slide 14

IMU
* This message provides synchronous IMU measurements aligned to UTC time.  
 * Most SBG Systems INS, except ELLIPSE products, use IMUs with asynchronous measurements.
 * 
 * These measurements are extrapolated to match the EKF processing loop, which can introduce  
 * artificial noise, particularly in high-frequency processing loops (e.g., 200Hz with up to 5ms extrapolation).
 *
 * \note This message is not suitable for post-processing due to the introduced noise.
 * For accurate UTC/GPS-timestamped asynchronous IMU measurements, use SBG_ECOM_LOG_IMU_SHORT.
 *
 * \warning This message is not recommended for new designs and will be deprecated in sbgECom 5.x.
 */
typedef struct _SbgEComLogImuLegacy
{
    uint32_t    timeStamp;                  /*!< Time in microseconds since the sensor power up. */
    uint16_t    status;                     /*!< IMU status bitmask. */
    float       accelerometers[3];          /*!< X, Y, Z accelerometer readings in m/s². */
    float       gyroscopes[3];              /*!< X, Y, Z gyroscope readings in rad/s. */
    float       temperature;                /*!< Internal temperature in °C. */
    float       deltaVelocity[3];           /*!< X, Y, Z delta velocity in m/s² (same as accelerometers field). */
    float       deltaAngle[3];              /*!< X, Y, Z delta angle in rad/s (same as gyroscopes field). */
} SbgEComLogImuLegacy;

## Slide 15

MAG
/*!
 * Represents data from the SBG_ECOM_LOG_MAG message.
 *
 * This structure encapsulates the magnetic field data, which is calibrated to correct for soft and hard iron effects. It provides
 * 3D magnetic field readings intended for use by the INS filter.
 */
typedef struct _SbgEComLogMag
{
    uint32_t    timeStamp;                  /*!< Time in us since the sensor power up. */
    uint16_t    status;                     /*!< Magnetometer status bitmask. */
    float       magnetometers[3];           /*!< X, Y, Z magnetometer data in arbitrary units (A.U.). */
    float       accelerometers[3];          /*!< X, Y, Z accelerometer data in (m/s^2). */
} SbgEComLogMag;

## Slide 16

EKF Euler
/*!
 * EKF computed orientation using euler angles.
 * 
 * Note: In AHRS (Attitude and Heading Reference System) or INS (Inertial Navigation System) modes,
 * the yaw angle represents the geographic (true) heading of the device.
 * 
 * To convert a geographic heading to a magnetic heading, use the following formula:
 *   Magnetic Heading = Geographic Heading - Magnetic Declination
 */
typedef struct _SbgEComLogEkfEuler
{
    uint32_t    timeStamp;              /*!< Time in us since the sensor power up. */
    float       euler[3];               /*!< Roll [-pi;+pi], pitch [-pi/2;+pi/2], yaw [-pi;+pi] in radians. */
    float       eulerStdDev[3];         /*!< Roll std. [0;+pi], pitch std. [0;+pi/2] and yaw std. [0;+pi] estimated 1-sigma accuracy in radians */
    uint32_t    status;                 /*!< EKF solution status bitmask and enum. */
    float       magDeclination;         /*!< Local magnetic declination in radians (positive east - set to NAN if not available). */
    float       magInclination;         /*!< Local magnetic inclination in radians (positive down - set to NAN if not available). */
} SbgEComLogEkfEuler;

## Slide 17

EKF Nav
/*!
 * EFK computed navigation data.
 */
typedef struct _SbgEComLogEkfNav
{
    uint32_t    timeStamp;              /*!< Time in us since the sensor power up. */
    float       velocity[3];            /*!< North, East, Down velocity in m.s^-1. */
    float       velocityStdDev[3];      /*!< North, East, Down velocity 1-sigma standard deviation in m.s^-1. */
    double      position[3];            /*!< Latitude, Longitude in degrees positive North and East.
                                         Altitude above Mean Sea Level in meters. */
    float       undulation;             /*!< Altitude difference between the geoid and the Ellipsoid in meters (Height above Ellipsoid = altitude + undulation). */
    float       positionStdDev[3];      /*!< Latitude, longitude and altitude 1 sigma standard deviation in meters. */
    uint32_t    status;                 /*!< EKF solution status bitmask and enum. */
} SbgEComLogEkfNav;

## Slide 18

GPS VEL
* This structure holds information about GPS velocity, including timestamp,
 * status, time of week, velocity components, and their accuracies.
 *
 * \note Some GNSS protocols, such as NMEA, cannot provide a full 3D velocity.
 * An invalid down velocity component should be indicated by using the maximum
 * standard deviation value of 9999 m/s.
 */
typedef struct _SbgEComLogGnssVel
{
    uint32_t        timeStamp;              /*!< Time in microseconds since the sensor power up. */
    uint32_t        status;                 /*!< GPS velocity status, type and bitmask. */
    uint32_t        timeOfWeek;             /*!< GPS time of week in milliseconds. */
    float           velocity[3];            /*!< GPS North, East, Down velocity in m/s. */
    float           velocityAcc[3];         /*!< GPS North, East, Down velocity 1 sigma accuracy in m/s (0 to 9999). */
    float           course;                 /*!< Track ground course in degrees (0 to 360). */
    float           courseAcc;              /*!< Course accuracy in degrees (0 to 180). */
} SbgEComLogGnssVel;

## Slide 19

GPS POS
typedef struct _SbgEComLogGnssPos
{
    uint32_t        timeStamp;              /*!< Time in us since the sensor power up. */
    uint32_t        status;                 /*!< GPS position status, type and bitmask. */
    uint32_t        timeOfWeek;             /*!< GPS time of week in ms. */
    double          latitude;               /*!< Latitude in degrees, positive north. */
    double          longitude;              /*!< Longitude in degrees, positive east. */
    double          altitude;               /*!< Altitude above Mean Sea Level in meters. */
    float           undulation;             /*!< Altitude difference between the geoid and the Ellipsoid in meters (Height above Ellipsoid = altitude + undulation). */
    float           latitudeAccuracy;       /*!< 1 sigma latitude accuracy in meters (0 to 9999). */
    float           longitudeAccuracy;      /*!< 1 sigma longitude accuracy in meters (0 to 9999). */
    float           altitudeAccuracy;       /*!< 1 sigma altitude accuracy in meters (0 to 9999). */
    uint8_t         numSvUsed;              /*!< Number of space vehicles used to compute the solution - set to 0xFF if not available. (added in 1.4) */
    uint16_t        baseStationId;          /*!< Base station id for differential corrections (0-4095) - set to 0xFFFF if differential are not used or not available. (added in 1.4). */
    uint16_t        differentialAge;        /*!< Differential correction age in 0.01 seconds - set to 0xFFFF if differential are not used or not available. (added in 1.4). */  
    uint8_t         numSvTracked;           /*!< Number of space vehicles tracked by the GNSS - set to 0xFF if not available. (added in 4.0) */
    uint32_t        statusExt;              /*!< Additional status for interference, spoofing and OSNMA (added in 4.0). */
} SbgEComLogGnssPos;

## Slide 20

Airdata
/*!
 * Log structure for AirData.
 */
typedef struct _SbgEComLogAirData
{
    uint32_t    timeStamp;                      /*!< Time in us since the sensor power up OR measurement delay in us. */
    uint16_t    status;                         /*!< Airdata sensor status bitmask. */
    float       pressureAbs;                    /*!< Raw absolute pressure measured by the barometer sensor in Pascals. */
    float       altitude;                       /*!< Altitude computed from barometric altimeter in meters and positive upward. */
    float       pressureDiff;                   /*!< Raw differential pressure measured by the pitot tube in Pascal. */
    float       trueAirspeed;                   /*!< True airspeed measured by a pitot tube in m.s^-1 and positive forward. */
    float       airTemperature;                 /*!< Outside air temperature in °C that could be used to compute true airspeed from differential pressure. */
} SbgEComLogAirData;

## Slide 21

MAIM Internal Data Storage
Kurt Notes, Ignore

## Slide 22

SBG Output – sbg_global.h
typedef struct _SbgOutput
    {
        float     stateEuler[3];         /*!< The orientation in euler angles roll, pitch, yaw in radians */

        float     gyroscopes[3];         /*!< Calibrated version of the 3 gyroscopes, gX, gY, gZ */
        float     accelerometers[3];     /*!< Calibrated version of the 3 accelerometers, aX, aY, aZ */
        float     magnetometers[3];      /*!< Calibrated version of the 3 magnetometers, mX, mY, mZ */
        float     temperatures[2];       /*!< Calibrated temperature values, t0, t1 */

        uint32    timeSinceReset;        /*!< Elapsed time in ms since the imu is running */


        int32     gpsLatitude;           /*!< Latitude in degress (1e-7)    */
        int32     gpsLongitude;          /*!< Longitude in degrees (1e-7) */
        int32     gpsAltitude;           /*!< Height above sea level in mm */
        float     undulation;            /*!< Height difference between geoid and ellipsoid in m */

        int32     gpsVelocity[3];        /*!< North, East, Down velocity in cm/s (NED coordinate system) */
        int32     gpsHeading;            /*!< 2D heading in degrees (1e-5) */

        uint32    gpsHorAccuracy;        /*!< Horizontal accuracy in mm */
        uint32    gpsVertAccuracy;       /*!< Vertical accuracy in mm */
        uint32    gpsHeadingAccuracy;    /*!< Heading accuracy in degrees (1e-5) */


        uint8     gpsNbSats;             /*!< GPS number of satellites used in position estimation */

        int32     baroAltitude;          /*!< Altitude above reference zero based on pressure measurement in cms */
        uint32    baroPressure;          /*!< Absolute pressure measurement in pascals*/

        double    position[3];           /*!< 3d position North East Height above sea level in (deg, deg, meters) */
        float     velocity[3];           /*!< 3d velocity in device coordinate and in m/s */

        float     attitudeAccuracy;      /*!< Attitude accuracy in rad estimated by the Kalman Filter */
        float     positionAccuracy;      /*!< Position accuracy in meters estimated by the Kalman Filter */
        float     velocityAccuracy;      /*!< Velocity accuracy in m/s estimated by the Kalman Filter */

        uint16    utcYear;               /*!< UTC time reference: Year = 2000+ year */
        uint8     utcMonth;              /*!< Month, range 1..12 (UTC) */
        uint8     utcDay;                /*!< Day of Month, range 1..31 (UTC) */
        uint8     utcHour;               /*!< Hour of Day, range 0..23 (UTC) */
        uint8     utcMin;                /*!< Minute of Hour, range 0..59 (UTC) */
        uint8     utcSec;                /*!< Seconds of Minute, range 0..59 (UTC) */
        uint32    utcNano;               /*!< Nanoseconds of second, range 0 .. 1 000 000 000(UTC) */

        uint16    generalStatus;         /*!< General status bitmask and enums. */
        uint16    utcStatus;             /* UTC Status Output */
        uint32    comStatus;             /*!< Communication status bitmask and enums. */
        uint32    aidingStatus;          /*!< Aiding equipments status bitmask and enums. */
        uint16    imuStatus;
        uint16    magStatus;
        uint32    solutionStatus;
        uint32    gpsVelStatus;
        uint32    gpsPosStatus;
        uint16    pressureStatus;

    } SbgOutput;

## Slide 23

SBG Output Ext
typedef struct _SbgOutputExt
    {
        /*TPV*/
        float ept;
        float track;
        uint8 mode;
        float epx;
        float epy;
        float epv;
        float climb;
        float epd;
        float epc;

        /*ATT*/


        /*SKY*/
        float hdop;

        /*MAIM_VER*/
        char sw[16];
        char dev[16];
        char devhw[16];
        char devsw[16];

        /*STATUS*/


        /*IMUNAV*/
        int32     velocityAcc[3];

        /*PRESSURE*/


        /*ADDL*/
        int32     gpsVelocityAcc[3];
        uint32    timeOfWeek;

    } SbgOutputExt;
