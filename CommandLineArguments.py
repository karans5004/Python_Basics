""" The arguments that are given after the name of the program in the command line shell of the operating system are known as Command Line Arguments. Python provides various ways of dealing with these types of arguments. The three most common are: 

    Using sys.argv
    Using getopt module
    Using argparse module """


############################## sys.argv #############################
#python CommandLineArguments.py 1 2 3 4
# Python program to demonstrate
# command line arguments
import sys
 
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
     
# Addition of numbers
Sum = 0
# Using argparse module
for i in range(1, n):
    Sum += int(sys.argv[i])
     
print("\n\nResult:", Sum)

#####################################################################





#################### Using getopt module ############################
# python CommandLineArguments.py -h -m
# Python program to demonstrate
# command line arguments
 
 
import getopt, sys
 
 
# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]
 
# Options
options = "hmo:"
 
# Long options
long_options = ["Help", "My_file", "Output ="]
 
try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    # checking each argument
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-h", "--Help"):
            print ("Diplaying Help")
             
        elif currentArgument in ("-m", "--My_file"):
            print ("Displaying file_name:", sys.argv[0])
             
        elif currentArgument in ("-o", "--Output"):
            print (("Enabling special output mode (% s)") % (currentValue))
             
except getopt.error as err:
    # output error, and return with an error code
    print (str(err)) 
######################################################################################






######################### Using argparse module ####################################
# python CommandLineArguments.py -h
# Python program to demonstrate
# command line arguments
 
 
import argparse
 
msg = "Adding description"
 
# Initialize parser
parser = argparse.ArgumentParser(description = msg)
parser.parse_args()


# Python program to demonstrate
# command line arguments
 
########################################################################






################### Defining optional Value ###########################
 
# python CommandLineArguments.py -0 Green
# python CommandLineArguments.py -0 

import argparse
 
 
# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-o", "--Output", help = "Show Output")
 
# Read arguments from command line
args = parser.parse_args()
 
if args.Output:
    print("Displaying Output as: % s" % args.Output)


#################################################