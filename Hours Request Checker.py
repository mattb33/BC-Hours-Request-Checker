# Import modules
import csv

# Initialise output list
results = []
header = ["Employee Code", "Hours", "Percentage"]


# Define the starting variables
z = 0.70                            # Threshold that must be met to qualify for increase in hours


# Import CSV - file called 'hours' should be employee code in first column, then one year's worth of fortnightly hours (26 instances)
f = open('hours.csv')
csv_f = csv.reader(f)
next(csv_f)         # Ignore the header row


# Loop through rows of the csv
for row in csv_f:
    emp_code = row[0];                                  # capture the employee code so it can be appended to the results list
    j = row[1:];                                        # the row with the employee code removed (list has strings though - the next line will convert to float)
    j2 = [float(i) for i in j if i];                    # convert the list of strings to floating point numbers

    for M in range(80,19,-1):                           # iterate through the working hours - decrementing from 80 to 20 hours
	    j3 = (sum(i >= M for i in j2) / len(j2));		      # count the instances that are equal or greater than the working hours, and divide by the total number of instances

	    if (j3 >= z):                                     # if the threshold (z - currently 70%) is met, write the results to the list and break the loop
		    print(emp_code, M, j3);
		    results.append([emp_code, M, j3]);
		    break


print("Results have been finalised")


# Write to CSV
print('writing to CSV...')

with open('results.csv', mode='w') as csv_file:
    writer = csv.writer(csv_file);
    writer.writerow(i for i in header);                 # add the header row

# Add scraped data to csv file
    for item in results:
        writer.writerow(item);                          # add the results from the loop

print('Writing to CSV complete')
