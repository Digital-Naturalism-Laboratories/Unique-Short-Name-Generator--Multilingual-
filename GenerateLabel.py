#!/usr/bin/python3
import time
from time import sleep
import csv
import datetime
from datetime import datetime
import subprocess
from subprocess import Popen  # For executing external scripts
import os

import numpy as np

print("----------------- STARTING Scheduler for Pi5 (no Pijuice!)-------------------")
now = datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")  # Adjust the format as needed

print(f"Current time: {formatted_time}")


#These all get set in the loaded settings
utc_off=0 #this is the offsett from UTC time we use to set the alarm
runtime=0 #this is how long to run the mothbox in minutes for once we wakeup 0 is forever
onlyflash=0


def get_serial_number():
  """
  This function retrieves the Raspberry Pi's serial number from the CPU info file.
  """
  try:
    with open('/proc/cpuinfo', 'r') as cpuinfo:
      for line in cpuinfo:
        if line.startswith('Serial'):
          return line.split(':')[1].strip()
  except (IOError, IndexError):
    return None


def read_csv_into_lists(filename, encoding='utf-8'):
  """
  Reads a CSV file with headers into separate lists for each column, handling diacritical marks.

  Args:
      filename: The path to the CSV file.
      encoding: The character encoding of the CSV file (default: 'utf-8').

  Returns:
      A dictionary where keys are column names (strings) and values are lists of data (strings).
  """
  data = {}
  with open(filename, 'r', newline='', encoding=encoding) as csvfile:
    reader = csv.reader(csvfile)
    # Read header row
    headers = next(reader)
    # Initialize empty lists for each column
    for header in headers:
      data[header] = []
    # Read data rows and populate corresponding lists by column index
    for row in reader:
      for i, value in enumerate(row):
        if value:  # Only append non-empty values
          data[headers[i]].append(value)
  
  # Access data by category (column name)
  #animals = data["Animal"]
  ianimals = data["Animal2"] #for some reason it's not reading the first column, this is my janky workaround
  #print(animals)

  iadjectives = data["Adjectives"]
  #print(adjectives)

  icolors = data["Colors"]
  #print(colors)

  iverbs = data["Verbs"]
  #print(verbs)


  ianimales = data["Animales"]
  #print(animales)

  iadjectivos = data["Adjectivos"]
  #print(adjectivos)

  iverbos = data["Verbos"]
  #print(verbos)

  icolores = data["Colores"]
  #print(colores)

  isustantivos = data["Sustantivos"]
  #print(sustantivos)



  return ianimals, ianimales, iadjectives, iadjectivos, icolors, icolores,iverbs,iverbos,isustantivos

filename ="/home/pi/Desktop/Mothbox/wordlist.csv"  # Replace with your actual filename
animals, animales, adjectives, adjectivos, colors, colores, verbs, verbos, sustantivos  = read_csv_into_lists(filename)


def word_to_seed(word, encoding='utf-8'):
  """Converts a word to a number suitable for np.random.seed using encoding, sum, and modulo.

  Args:
      word: The string to be converted.
      encoding: The character encoding of the word (default: 'utf-8').

  Returns:
      An integer seed value within the valid range for np.random.seed.
  """
  encoded_word = word.encode(encoding)
  seed = sum(encoded_word)
  max_seed_value = 2**32 - 1 #np.random.default_rng().bit_generator.state_size  # Get max seed value
  return seed #% max_seed_value

def generate_unique_name(serial, lang):
  """
  Generates a unique name based on the Raspberry Pi's serial number.

  Args:
      serial: The Raspberry Pi's serial number as a string.

  Returns:
      A string containing a random word and a suffix based on the serial number.
  """

  # Use the serial number to create a unique seed for the random word generation.
  #word_seed = int(serial.replace("-", ""), 16)
  #max_seed_value = 2**32 - 1
  word_seed=word_to_seed(serial)
  #word_seed=hash(serial) % max_seed_value
  #print(word_seed)
  np.random.seed(word_seed)

  #os.urandom(word_seed)  # Fallback: use os.urandom for randomness

  #Create two word phrases

  if(lang==0): #English
    extra=adjectives+colors+verbs
    random_extra = str(np.random.choice(extra,1)[0]).lower()
    random_animal=str(np.random.choice(animals,1)[0]).capitalize()
    finalCombo=random_extra+random_animal
  elif(lang==1): #Spanish
    extra=adjectivos+colores+verbos+sustantivos
    random_extra = np.random.choice(extra,1)[0]
    random_animal=np.random.choice(animales,1)[0]
    finalCombo=str(random_animal).lower()+str(random_extra).capitalize() #generally putting a noun before descriptor in spanish
  elif(lang==3): #Spanglish
    extra=adjectivos+colores+verbos+sustantivos+adjectives+verbs+adjectivos+colores+verbos+sustantivos
    dosanimales=animals+animales
    random_extra = np.random.choice(extra,1)[0]
    random_animal=np.random.choice(dosanimales,1)[0]
    finalCombo=str(random_extra).lower()+str(random_animal).capitalize()

  return finalCombo



def set_computerName(filepath,compname):
    with open(filepath, "r") as file:
        lines = file.readlines()

    with open(filepath, "w") as file:
        for line in lines:
            print(line)
            if line.startswith("name"):
                file.write("name="+str(compname)+"\n")  # Replace with False
                print("set name "+compname)
            else:
                file.write(line)  # Keep other lines unchanged



#SetUniqueRaspberrypiName
serial_number = get_serial_number()
#0 is english 1 is spanish 2 is either spanish or enlgish 3 is spanglish
unique_name = generate_unique_name(serial_number,3)
print(f"Unique name for device: {unique_name}")

# Change the name in controls
set_computerName("/home/pi/Desktop/Mothbox/controls.txt", unique_name)



