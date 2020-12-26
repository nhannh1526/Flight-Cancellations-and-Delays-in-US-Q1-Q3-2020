<table class="table table-striped table-bordered">
<thead>
<tr>
<th>Group</th>
<th>Name</th>
<th>Description</th>
<th>Giải thích</th>
<th>Value range</th>
</tr>
</thead>
<tbody>
<tr>
<td>Time Period</td>
<td>YEAR</td>
<td>Year</td>
<td>Năm</td>
<td>2020</td>
</tr>
<tr>
<td></td>
<td>MONTH</td>
<td>Month</td>
<td>Tháng</td>
<td>1-9</td>
</tr>
<tr>
<td></td>
<td>DAY_OF_MONTH</td>
<td>Day of Month</td>
<td>Ngày</td>
<td>1-31</td>
</tr>
<tr>
<td></td>
<td>DAY_OF_WEEK</td>
<td>Day of Week</td>
<td>Thứ</td>
<td>1-7</td>
</tr>
<tr>
<td></td>
<td>FL_DATE</td>
<td>Flight Date</td>
<td>Ngày bay</td>
<td>2020-01-01 - 2020-09-30</td>
</tr>
<tr>
<td>Airline</td>
<td>OP_UNIQUE_CARRIER</td>
<td>Carrier name</td>
<td>Tên hãng hàng không</td>
<td>Carrier names</td>
</tr>
<tr>
<td></td>
<td>TAIL_NUM</td>
<td>Tail Number</td>
<td>Mã số đuôi máy bay</td>
<td>Tail numbers</td>
</tr>
<tr>
<td></td>
<td>OP_CARRIER_FL_NUM</td>
<td>Flight Number</td>
<td>Mã số máy bay</td>
<td>Flight numbers</td>
</tr>
<tr>
<td>Departure Performance</td>
<td>CRS_DEP_TIME</td>
<td>CRS Departure Time (local time: hhmm)</td>
<td>Thời gian cất cánh dự kiến (hhmm)</td>
<td>0001-2400</td>
</tr>
<tr>
<td></td>
<td>DEP_TIME</td>
<td>Actual Departure Time (local time: hhmm)</td>
<td>Thời gian cất cánh thực tế (hhmm)</td>
<td>0001-2400</td>
</tr>
<tr>
<td></td>
<td>DEP_DELAY</td>
<td>Difference in minutes between scheduled and actual departure time. Early   departures show negative numbers.</td>
<td>Chênh lệch giữa dự kiến và thực tế (minutes)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>TAXI_OUT</td>
<td>Taxi Out Time, in Minutes</td>
<td>Thời gian “Taxi Out” (minutes)</td>
<td>Real number</td>
</tr>
<tr>
<td>Arrival Performance</td>
<td>TAXI_IN</td>
<td>Taxi In Time, in Minutes</td>
<td>Thời gian “Taxi In” (minutes)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>CRS_ARR_TIME</td>
<td>CRS Arrival Time (local time: hhmm)</td>
<td>Thời gian hạ cánh dự kiến (hhmm)</td>
<td>0001-2400</td>
</tr>
<tr>
<td></td>
<td>ARR_TIME</td>
<td>Actual Arrival Time (local time: hhmm)</td>
<td>Thời gian hạ cánh thực tế (hhmm)</td>
<td>0001-2400</td>
</tr>
<tr>
<td></td>
<td>ARR_DELAY</td>
<td>Difference in minutes between scheduled and actual arrival time. Early   arrivals show negative numbers.</td>
<td>Chênh lệch giữa dự kiến và thực tế (minutes)</td>
<td>Real number</td>
</tr>
<tr>
<td>Cancellations and Diversions</td>
<td>CANCELLED</td>
<td>Cancelled Flight Indicator (1=Yes)</td>
<td>Cờ hiệu hủy</td>
<td>1=Yes, 0=No</td>
</tr>
<tr>
<td></td>
<td>CANCELLATION_CODE</td>
<td>Specifies The Reason For Cancellation</td>
<td>Mã hủy</td>
<td>A = carrier, B = weather, C = NAS, D = security</td>
</tr>
<tr>
<td></td>
<td>DIVERTED</td>
<td>Diverted Flight Indicator (1=Yes)</td>
<td>Cờ hiệu đổi hướng</td>
<td>1=Yes, 0=No</td>
</tr>
<tr>
<td>Flight Summaries</td>
<td>CRS_ELAPSED_TIME</td>
<td>CRS Elapsed Time of Flight, in Minutes</td>
<td>Tổng thời gian dự kiến (minutes)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>ACTUAL_ELAPSED_TIME</td>
<td>Elapsed Time of Flight, in Minutes</td>
<td>Tổng thời gian thực tế (minutes)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>AIR_TIME</td>
<td>Flight Time, in Minutes</td>
<td>Thời gian bay (minutes)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>DISTANCE</td>
<td>Distance between airports (miles)</td>
<td>Khoảng cánh giữa hai sân bay (miles)</td>
<td>Real number</td>
</tr>
<tr>
<td>Cause of Delay</td>
<td>CARRIER_DELAY</td>
<td>Carrier Delay, in Minutes</td>
<td>Thời gian hoãn do hãng hàng không (minutes)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>WEATHER_DELAY</td>
<td>Weather Delay, in Minutes</td>
<td>Thời gian hoãn do thời tiết (minutes)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>NAS_DELAY</td>
<td>National Air System Delay, in Minutes</td>
<td>Thời gian hoãn do hệ thống hàng không quốc gia (minutes)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>SECURITY_DELAY</td>
<td>Security Delay, in Minutes</td>
<td>Thời gian hoãn do an ninh (minutes)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>LATE_AIRCRAFT_DELAY</td>
<td>Late Aircraft Delay, in Minutes</td>
<td>Thời gian hoãn do trễ máy bay (minutes)</td>
<td>Real number</td>
</tr>
<tr>
<td>Pandemic</td>
<td>DAILY_CASES</td>
<td>Daily New Cases</td>
<td>Số ca nhiễm mới trong ngày</td>
<td>Real number</td>
</tr>
<tr>
<td>Origin</td>
<td>ORIGIN</td>
<td>Origin Airport, IATA code</td>
<td>Mã IATA sân bay đi</td>
<td>IATA codes</td>
</tr>
<tr>
<td></td>
<td>ORIGIN_AIRPORT</td>
<td>Origin Airport, Name</td>
<td>Sân bay đi</td>
<td>Airport  names</td>
</tr>
<tr>
<td></td>
<td>ORIGIN_CITY</td>
<td>Origin Airport, City</td>
<td>Thành phố đi</td>
<td>City names</td>
</tr>
<tr>
<td></td>
<td>ORIGIN_STATE</td>
<td>Origin Airport, State</td>
<td>Bang đi</td>
<td>State codes</td>
</tr>
<tr>
<td></td>
<td>ORIGIN_LAT</td>
<td>Origin Airport, Latitude</td>
<td>Vĩ độ đi</td>
<td>Latitude</td>
</tr>
<tr>
<td></td>
<td>ORIGIN_LONG</td>
<td>Origin Airport, Longitude</td>
<td>Kinh độ đi</td>
<td>Longitude</td>
</tr>
<tr>
<td>Origin weather conditions</td>
<td>ORIGIN_STATION</td>
<td>Station number</td>
<td>Mã số trạm</td>
<td>Station numbers</td>
</tr>
<tr>
<td></td>
<td>ORIGIN_NAME</td>
<td>Name of station</td>
<td>Tên trạm</td>
<td>Station names</td>
</tr>
<tr>
<td></td>
<td>ORIGIN_TEMP</td>
<td>Origin Airport, Mean temperature for the day in degrees Fahrenheit to   tenths. Missing = 9999.9</td>
<td>Nhiệt độ trung bình, sân bay đi (.1 Fahrenheit)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>ORIGIN_DEWP</td>
<td>Origin Airport, Mean dew point for the day in degrees Fahrenheit to   tenths. Missing = 9999.9</td>
<td>Điểm sương trung bình, sân bay đi (.1 Fahrenheit)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>ORIGIN_SLP</td>
<td>Origin Airport, Mean sea level pressure for the day in millibars to   tenths. Missing = 9999.9</td>
<td>Áp suất mực nước biển trung bình, sân bay đi (.1 mb)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>ORIGIN_STP</td>
<td>Origin Airport, Mean station pressure for the day in millibars to tenths.   Missing = 9999.9</td>
<td>Áp suất trạm trung bình, sân bay đi (.1 mb)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>ORIGIN_VISIB</td>
<td>Origin Airport, Mean visibility for the day in miles to tenths. Missing =   999.9</td>
<td>Tầm nhìn trung bình, sân bay đi (.1 miles)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>ORIGIN_WDSP</td>
<td>Origin Airport, Mean wind speed for the day in knots to tenths.  Missing = 999.9</td>
<td>Tốc độ gió trung bình, sân bay đi (.1 knots)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>ORIGIN_PRCP</td>
<td>Origin Airport, Total precipitation (rain and/or melted snow) reported   during the day in inches and hundredths; will usually not end with the   midnight observation (i.e. may include latter part of previous day). “0”   indicates no measurable precipitation (includes a trace). Missing = 99.99</td>
<td>Lượng mưa, sân bay đi (.01 inches)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>ORIGIN_SNDP</td>
<td>Origin Airport, Snow depth in inches to tenths. It is the last report for   the day if reported more than once. Missing = 999.9</td>
<td>Độ sâu tuyết, sân bay đi (.01 inches)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>ORIGIN_FRSHTT</td>
<td>Origin Airport, Indicators (1 = yes, 0 = no/not reported) for the   occurrence during the day of: Fog (‘F’ - 1st digit). Rain or Drizzle (‘R’ -   2nd digit). Snow or Ice Pellets (‘S’ - 3rd digit). Hail (‘H’ - 4th digit).   Thunder (‘T’ - 5th digit). Tornado or Funnel Cloud (‘T’ - 6th digit)</td>
<td>Cờ hiệu các loại thời tiết, sân bay đi</td>
<td>1 = YES, 0 = NO. Fog (‘F’ - 1st digit). Rain or Drizzle (‘R’ -   2nd digit). Snow or Ice Pellets (‘S’ - 3rd digit). Hail (‘H’ - 4th digit).   Thunder (‘T’ - 5th digit). Tornado or Funnel Cloud (‘T’ - 6th digit)</td>
</tr>
<tr>
<td>Destination</td>
<td>DEST</td>
<td>Destination Airport, IATA code</td>
<td>Mã IATA sân bay đến</td>
<td>IATA codes</td>
</tr>
<tr>
<td></td>
<td>DEST_AIRPORT</td>
<td>Destination Airport, Name</td>
<td>Sân bay đến</td>
<td>Airport  names</td>
</tr>
<tr>
<td></td>
<td>DEST_CITY</td>
<td>Destination Airport, City</td>
<td>Thành phố đến</td>
<td>City names</td>
</tr>
<tr>
<td></td>
<td>DEST_STATE</td>
<td>Destination Airport, State</td>
<td>Bang đến</td>
<td>State codes</td>
</tr>
<tr>
<td></td>
<td>DEST_LAT</td>
<td>Destination Airport, Latitude</td>
<td>Vĩ độ đến</td>
<td>Latitude</td>
</tr>
<tr>
<td></td>
<td>DEST_LONG</td>
<td>Destination Airport, Longitude</td>
<td>Kinh độ đến</td>
<td>Longitude</td>
</tr>
<tr>
<td>Destination weather conditions</td>
<td>DEST_STATION</td>
<td>Station number</td>
<td>Mã số trạm</td>
<td>Station numbers</td>
</tr>
<tr>
<td></td>
<td>DEST_NAME</td>
<td>Name of station</td>
<td>Tên trạm</td>
<td>Station names</td>
</tr>
<tr>
<td></td>
<td>DEST_TEMP</td>
<td>Destination Airport, Mean temperature for the day in degrees Fahrenheit   to tenths. Missing = 9999.9</td>
<td>Nhiệt độ trung bình, sân bay đến (.1 Fahrenheit)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>DEST_DEWP</td>
<td>Destination Airport, Mean dew point for the day in degrees Fahrenheit to   tenths. Missing = 9999.9</td>
<td>Điểm sương trung bình, sân bay đến (.1 Fahrenheit)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>DEST_SLP</td>
<td>Destination Airport, Mean sea level pressure for the day in millibars to   tenths. Missing = 9999.9</td>
<td>Áp suất mực nước biển trung bình, sân bay đến (.1 mb)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>DEST_STP</td>
<td>Destination Airport, Mean station pressure for the day in millibars to   tenths. Missing = 9999.9</td>
<td>Áp suất trạm trung bình, sân bay đến (.1 mb)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>DEST_VISIB</td>
<td>Destination Airport, Mean visibility for the day in miles to tenths.   Missing = 999.9</td>
<td>Tầm nhìn trung bình, sân bay đến (.1 miles)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>DEST_WDSP</td>
<td>Destination Airport, Mean wind speed for the day in knots to tenths.  Missing = 999.9</td>
<td>Tốc độ gió trung bình, sân bay đến (.1 knots)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>DEST_PRCP</td>
<td>Destination Airport, Total precipitation (rain and/or melted snow)   reported during the day in inches and hundredths; will usually not end with   the midnight observation (i.e. may include latter part of previous day). “0”   indicates no measurable precipitation (includes a trace). Missing = 99.99</td>
<td>Lượng mưa, sân bay đến (.01 inches)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>DEST_SNDP</td>
<td>Destination Airport, Snow depth in inches to tenths. It is the last   report for the day if reported more than once. Missing = 999.9</td>
<td>Độ sâu tuyết, sân bay đến (.01 inches)</td>
<td>Real number</td>
</tr>
<tr>
<td></td>
<td>DEST_FRSHTT</td>
<td>Destination Airport, Indicators (1 = yes, 0 = no/not reported) for the   occurrence during the day of: Fog (‘F’ - 1st digit). Rain or Drizzle (‘R’ -   2nd digit). Snow or Ice Pellets (‘S’ - 3rd digit). Hail (‘H’ - 4th digit).   Thunder (‘T’ - 5th digit). Tornado or Funnel Cloud (‘T’ - 6th digit)</td>
<td>Cờ hiệu các loại thời tiết, sân bay đến</td>
<td>1 = YES, 0 = NO. Fog (‘F’ - 1st digit). Rain or Drizzle (‘R’ -   2nd digit). Snow or Ice Pellets (‘S’ - 3rd digit). Hail (‘H’ - 4th digit).   Thunder (‘T’ - 5th digit). Tornado or Funnel Cloud (‘T’ - 6th digit)</td>
</tr>
</tbody>
</table>
