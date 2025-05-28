# CampusDiningWrapped

Hello and welcome to Jinkleheimer's First-Year-Optimized Campus Dining Wrapped!

This readme contains instructions, notes, and other things that come to mind. Command-prompt-related information is Windows specific. NEVER RUN ANY PROGRAM FROM AN UNTRUSTWORTHY SOURCE!!!!! 

Enjoy! :3




Use guide:
	I assume since you have this readme downloaded, you also have the python program downloaded. If you want to open it up in an IDE, go right ahead. If you just want to run it via the command prompt, this guide will include that information.
	The first step is to get your transaction history downloaded. Go to your Cal Poly portal and find 'PolyCard Services'. look on the left and click 'Spending History'. Select a set of dates for the start and end that encompasses the entire academic year and choose your first year dining plan for the account. Copy EVERYTHING in the table to a NEW text file(google it if you don't know how to do that) and name it anything you'd like. Example text file is below.
	If you aren't sure if you have python installed, open the command prompt(search 'cmd' on the windows search) and type 'python.exe' and press enter. If the windows store pops up, install what pops up unless it doesn't look like python. If that installation fails, close anything python related running on your computer. If you see three greater than signs on the lowest line of the command prompt, type 'exit' and press enter. You have Python downloaded!
	Find where you downloaded the program to on your computer, right click the file, and select 'copy file path' or something similar. Enter 'python FILEPATH' where FILTPATH is pasted from the previous step. The command prompt should say 'Input full file path of your dining plan history: '. Now, do what you did with the program. Find where you saved the transaction history file(likely in documents) and right click it and select 'copy file path' or something similar and paste it into the command prompt. It should look like this before you press enter(it doesn't matter if there are quotation marks or not).

Input full file path of your dining plan history: "C:\Users\YOURPROFILE\Documents\History.txt"

	If it doesn't look something like that, good luck I guess. If it does, press enter and view your stats! If it doesn't work, ask someone with python knowledge to help.



~~~~~~~~~EXAMPLE START OF TRANSACTION HISTORY TEXT FILE~~~~~~~~~

Post Date	Location	Account	Amount	Balance
08/15/2024 16:53:25	PatronImport Location	First Year Plus	$-2268.00	$2268.00
09/17/2024 19:22:49	Mingle & Nosh Micros 782	First Year Plus	$7.35	$2260.65
09/18/2024 10:22:28	Balance	First Year Plus	$5.85	$2254.80
09/18/2024 13:13:11	Panda Express	First Year Plus	$10.40	$2244.40
09/19/2024 11:37:18	Grubhub Pico's 1318	First Year Plus	$11.85	$2232.55
09/20/2024 08:39:31	Grubhub Streats 1320	First Year Plus	$8.85	$2223.70

It goes for longer of course, I just don't want this readme to be too long.
NOTE: include the column titles AND the negative transaction. it is used to calculate usage statistics.
