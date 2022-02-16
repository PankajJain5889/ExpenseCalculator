# ExpenseCalculator
These is a common mans tool to log and visualize expenses across month and day 

The idea is that you can log all the expenses based on credit or debit and visualize them in order find out your major challenges. 

It needs to be completely over GUI so that any non technical person can use it. 

Preset categories for source of transaction, type and monthly budget. 

One use case would t deploy this over local server so anybody can access as well as log this over the cloud(google drive)
______________________________________________________________________________________
The idea is to use Dash for web GUI interface and run it through Docker container on my Raspberry PI so it can be accessed on my local network.

The first page of the app will say following Options. 

1. Create a base expense sheet. 
2. Create a new monthly report. 
3. Edit an old monthly report. 
4. Analyze reports.

1. Create a base expense sheet.
	In this you get the base dough to sculpt out your expense report you can add/remove columns and edit thier max values.

2. Create a new monthly report. 
	In this you can create a monthly report and edit it for expenses. Step by step process is as follows
		i. Select a base template from available ones
		ii. Select the month and year.
		iii. start editing/Exit
3. Once you have a report that you created you can either edit then and there or edit from this option. Firstly you select the report you want to edit and then the next page will show the report with an add expense option you can also edit an old expense on a report by clicking next to the edit marker on it. 

4. Analyze reports
	This is the most appealing part of the report and you can visualize your old reports in different graphical formats.

Cheers!!!!!!!!!!!!!

