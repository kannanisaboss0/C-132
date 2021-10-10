#------------------------------------------StarDataOperations.py------------------------------------------#

'''
Importing modules:
-pandas (pd)
-plotly.express (px)
-numpy (np)
-sys
-csv
-matplotlib (plt)
-seaborn (sns)
-time (tm)
'''
import pandas as pd
import plotly.express as px
import numpy as np
import sys
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import time as tm


print("Welcome to StarDataOperations.py")
print("We provide specific operations to perform on a chosen dataframe of stars.")

tm.sleep(2.3)

print("We also provide services for scraping the same dataset from a wikipedia page.")
print("Here is the link: 'https://github.com/kannanisaboss0/C-127.git' ")

tm.sleep(2.5)

print("And also you can visit our other program for performing scientific calculations on the same.")
print("Here is the link: 'https://github.com/kannanisaboss0/C-131.git' ")

print("Loading Data...")
tm.sleep(2.8)


#Defining a function to predict given data through linear regression
def PredictValuesThroughLinearRegression():
  chosen_values,names=ChooseParameters(["Unusable_Element","Distance","Mass","Radius","Gravity"],"use in prediction(x and y respectively)",3)
  names=names[1:]

  support_values=chosen_values[0]
  predict_values=chosen_values[1]

  support_values_array=np.array(support_values) 
  predict_values_array=np.array(predict_values)

  slope_func,intercept_func=np.polyfit(support_values,predict_values,1)

  y_var_list=[]

  #Running a for loop over the x variables to predict the respective y variables through slope and intercept
  for x_var in support_values_array:
    y_var=slope_func*x_var+intercept_func 
    y_var_list.append(y_var)

  x_user_list,y_user_list=PredictUserValues(slope_func,intercept_func,names,[],[])  

  store_user_predictions_prompt=input("Store your predictions?")

  #Assessing the user's choice to store the presonally predicted data in a file
  #Case-1
  if(store_user_predictions_prompt=="Yes" or store_user_predictions_prompt=="yes" or store_user_predictions_prompt=="YES" or store_user_predictions_prompt=="yEs" or store_user_predictions_prompt=="yeS" or store_user_predictions_prompt=="Y" or store_user_predictions_prompt=="y"):
    user_file_input=input("Please enter the filename:")

    user_data_list=[]

    #Running a for loop over the resulting enumerated y values produced indirectly by the user to structure the personally predicted data for insertion in the file
    for user_index,user_value in enumerate(y_user_list):
      temp_user_data_list=[]
      temp_user_data_list.append(x_user_list[user_index])
      temp_user_data_list.append(y_user_list[user_index])
      user_data_list.append(temp_user_data_list)

    #Verifying whether there is a "." present in the file name given by the user
    #Case-1
    if("." in user_file_input):
        user_file_input=user_file_input.split(".")[0].strip()

    #Opening (Creating) a file of the name preferred by the user to store the presonally predicted data
    with open(user_file_input+".csv",'w') as tf:
       write=csv.writer(tf)
       write.writerow(["User Input","Predicted Value"])
       write.writerows(user_data_list)

    user_file_name=user_file_input

  store_predictions_prompt=input("Store the predictions of the original file was well?")

  #Assessing the user's choice to store the original data in a file
  #Case-1
  if(store_predictions_prompt=="Yes" or store_predictions_prompt=="yes" or store_predictions_prompt=="YES" or store_predictions_prompt=="yEs" or store_predictions_prompt=="yeS" or store_predictions_prompt=="Y" or store_predictions_prompt=="y"):
    file_input=input("Please enter the filename:")

    #Verifying whether the file name of the presonally predicted data and the original data are the smae, both provided by the user
    #Case-1
    if(file_input.strip()==user_file_name.strip()):
      file_input=file_input+"-2"

    #Verifying whether there is a "." present in the file name given by the user
    #Case-1
    if("." in file_input):
      file_input=file_input.split(".")[0].strip() 

    headings=["{}".format(names[0]),"{}".format(names[1]),"Predicted Values"]
    data_list=[]

    #Running a for loop over the enumerated prediction list of y variables to structure the original data for insertion in the file
    for index,value in enumerate(y_var_list):
      temp_data_list=[]
      temp_data_list.append(support_values[index])
      temp_data_list.append(predict_values[index])
      temp_data_list.append(value)
      data_list.append(temp_data_list)

    #Opening (Creating) a file of the name preferred by the user to store the original data
    with open(file_input+".csv",'w') as ft:
      write=csv.writer(ft)
      write.writerow(headings)
      write.writerows(data_list)
      

#Defining a function to predict y-values using x-values stipulated by the user, the common slope and intercept      
def PredictUserValues(slope_param,intercept_param,names_param,list_param,list_2_param):
  print("Predicting custom values:")


  user_file_name=None

  
  x_input=float(input("Please enter the x-value({}), who y-value({}) is to be predicted".format(names_param[0],names_param[1])))

  y_value=slope_param*x_input+intercept_param

  list_param.append(x_input)
  list_2_param.append(y_value)

  print("The y-value ({}) is: {}".format(names_param[1],y_value))



  restart_procedure_prompt=input("Predict '{}' again?".format(names_param[1]))

  #Verifying the user's choice to conduct the prediction of the y-value through a custom x-value once again
  #Case-1
  if(restart_procedure_prompt=="Yes" or restart_procedure_prompt=="yes" or restart_procedure_prompt=="YES" or restart_procedure_prompt=="yEs" or restart_procedure_prompt=="yeS" or restart_procedure_prompt=="Y" or restart_procedure_prompt=="y"):
    PredictUserValues(slope_param,intercept_param,names_param,list_param,list_2_param)

  return list_param,list_2_param 


#Defining a function to plot graphs of the original data, with the graph type being of the user's discretion
def PlotGraphsForData():
  chosen_values,names=ChooseParameters(["Unusable_Element","Distance","Mass","Radius","Gravity"],"plot graphs with (x and y respectively",3)
  names=names[1:]

  x_values=chosen_values[0]
  y_values=chosen_values[1]

  x_name=names[0]
  y_name=names[1]

  chosen_value,name=ChooseParameters(["Unusable_Element","Line Graph","Scatter Graph"],"plot the data upon",2)

  df_data={"X":x_values,"Y":y_values}
  df=pd.DataFrame(df_data)
  
  #Assessing the user's input in order to plot the type of graph requested by the user
  #Case-1
  if(name[1]=="Line Graph"):
    line_graph=px.scatter(x=x_values,y=y_values,title="Line Graph({} and {})".format(x_name,y_name)) 
    line_graph.show()

  #Case-1
  if(name[1]=="Scatter Graph"):
    scatter_graph=px.scatter(x=x_values,y=y_values,title="Scatter Graph({} and {})".format(x_name,y_name)) 
    scatter_graph.show()


#Defining a function to verify the user's input through primarily try and ecept blocks
def TryAndExcept(list_param,input_param):
  #Using a try block to verify the validity of the user's input
  #Try block
  try:
    try_verify=list_param[input_param]

    return list_param[input_param],input_param

    #Verifying whether the user's input is equal to 0 or not
    #Case-1
    if(input_param==0):
      return sys.exit("Invalid Input")
  #Except block    
  except:
    return sys.exit("Invalid Input") 

#Defining a function to enable the user to choose from a given list of paramters,a stipulated number of times
def ChooseParameters(list_param,verb_param,num_param):
  chosen_list=[]
  parameter_list=["Unusalbe_Element"]
  param_list=list_param


  #Runnning a for loop over a ragne of numbers from 1 to paramter "num_param" to sepcify the number of paramters to be chosen
  for i in range(1,num_param):

    #Running a for loop over the enumerated the list provided as a parameter
    for param_index,param in enumerate(param_list):

      #Verifying whether the index of the parameter is equal to zero or not in order to prevent displaying "Unusable_Element"
      #Case-1
      if param_index!=0:
        print("{}:{}".format(param_index,param))

    param_input=int(input("Please enter the index of the parameter desired to {}:(Parameter {}):".format(verb_param,i)))    

    user_choice_func,input_result_func=TryAndExcept(param_list,param_input)

    #Using a try block to attempt to find a given section of the main dataset, otherwise, no operation is performed
    #Try block
    try:
      chosen_element=data[user_choice_func]
      chosen_list.append(chosen_element)
    #Except block  
    except:
      None 

    parameter_list.append(user_choice_func)
    

  return chosen_list,parameter_list
      

#Reading data from the dataset
data=pd.read_csv("data.csv")

star_names=data["Star_name"].tolist()
distances=data["Distance"].tolist()
masses=data["Mass"].tolist()
radii=data["Radius"].tolist()
gravities=data["Gravity"].tolist()

action_list=["Unusable_Element","Predict Values","Plot Graphs"]

#Running a for loop over the enumerated list to displat all the operations possible in the program
for action_index,action in enumerate(action_list):

  #Verifying whether the index of the parameter is equal to zero or not in order to prevent displaying "Unusable_Element"
  #Case-1
  if action_index!=0:
    print("{}:{}".format(action_index,action))

action_input=int(input("Please enter of the action desired to perform"))
user_choice,input_result=TryAndExcept(action_list,action_input)

#Assesing the user's choice to preform operation accordingly
#Case-1
if(action_input==1):
  PredictValuesThroughLinearRegression()

#Case-2
if(action_input==2):
  PlotGraphsForData()

#Printing the ending message
print("Thank You for using StarDataOperations.py")

#------------------------------------------StarDataOperations.py------------------------------------------#