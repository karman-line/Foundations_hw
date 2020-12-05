#!/usr/bin/env python
# coding: utf-8

# # Texas Cosmetologist Violations
# 
# Texas has a system for [searching for license violations](https://www.tdlr.texas.gov/cimsfo/fosearch.asp). You're going to search for cosmetologists!

# ## Setup: Import what you'll need to scrape the page
# 
# We'll be using Selenium for this, *not* BeautifulSoup and requests.

# In[1]:


from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


# In[2]:


driver = webdriver.Chrome()


# ## Starting your search
# 
# Starting from [here](https://www.tdlr.texas.gov/cimsfo/fosearch.asp), search for **cosmetologist violations** for people with the last name **Nguyen**.

# In[3]:


driver.get('https://www.tdlr.texas.gov/cimsfo/fosearch.asp')


# In[4]:


what = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/section/div/div/table/tbody/tr/td/form/table/tbody/tr[3]/td/select")


# In[5]:


what.send_keys('Cosmetologists')


# In[6]:


nguyen = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/section/div/div/table/tbody/tr/td/form/table/tbody/tr[7]/td/p/input")
nguyen.send_keys('Nguyen')


# In[7]:


#Clicking Search

hit_search = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/section/div/div/table/tbody/tr/td/form/table/tbody/tr[18]/td/input[1]").click()


# ## Scraping
# 
# Once you are on the results page, do this.

# ### Loop through each result and print the entire row
# 
# Okay wait, that's a heck of a lot. Use `[:10]` to only do the first ten (`listname[:10]` gives you the first ten).

# In[8]:


import pandas as pd


# In[36]:


driver.page_source


# In[15]:


tables = pd.read_html(driver.page_source)
tables = tables[0]
tables[:10]


# ### Loop through each result and print each person's name
# 
# You'll get an error because the first one doesn't have a name. How do you make that not happen?! If you want to ignore an error, you use code like this:
# 
# ```python
# try:
#    # try to do something
# except:
#    # Instead of stopping on an error, it'll jump down here instead
#    print("It didn't work')
# ```
# 
# It should help you out. If you don't want to print anything, you can type `pass` instead of the `print` statement. Most people use `pass`, but it's also nice to print out debug statements so you know when/where it's running into errors.
# 
# **Why doesn't the first one have a name?**

# In[ ]:


try: # checks to see if element exist
        what = driver.find_element_by_class_name('results_text')

    except: 
        print("failed to extract text")


# In[35]:


names = tables['Name and Location'].str.split('City:')
name_list = []

for x in names:
    a = x[0]
    name_list.append(a)
    
name_list


# ## Loop through each result, printing each violation description ("Basis for order")
# 
# > - *Tip: You'll get an error even if you're ALMOST right - which row is causing the problem?*
# > - *Tip: You can get the HTML of something by doing `.get_attribute('innerHTML')` - it might help you diagnose your issue.*
# > - *Tip: Or I guess you could just skip the one with the problem...*

# In[ ]:





# ## Loop through each result, printing the complaint number
# 
# - TIP: Think about the order of the elements

# In[ ]:





# ## Saving the results
# 
# ### Loop through each result to create a list of dictionaries
# 
# Each dictionary must contain
# 
# - Person's name
# - Violation description
# - Violation number
# - License Numbers
# - Zip Code
# - County
# - City
# 
# Create a new dictionary for each result (except the header).
# 
# > *Tip: If you want to ask for the "next sibling," you can't use `find_next_sibling` in Selenium, you need to use `element.find_element_by_xpath("following-sibling::div")` to find the next div, or `element.find_element_by_xpath("following-sibling::*")` to find the next anything.

# In[ ]:





# ### Save that to a CSV
# 
# - Tip: Use `pd.DataFrame` to create a dataframe, and then save it to a CSV.

# In[ ]:





# In[ ]:





# ### Open the CSV file and examine the first few. Make sure you didn't save an extra weird unnamed column.

# In[ ]:





# ## Let's do this an easier way
# 
# Use Selenium and `pd.read_html` to get the table as a dataframe.

# In[ ]:




