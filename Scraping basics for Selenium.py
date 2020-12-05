#!/usr/bin/env python
# coding: utf-8

# # Scraping basics for Selenium
# 
# If you feel comfortable with scraping, you're free to skip this notebook.

# ## Part 0: Imports
# 
# Import what you need to use Selenium, and start up a new Chrome to use for scraping. You might want to copy from the [Selenium snippets](http://jonathansoma.com/lede/foundations-2018/classes/selenium/selenium-snippets/) page.
# 
# **You only need to do `driver = webdriver.Chrome()` once,** every time you do it you'll open a new Chrome instance. You'll only need to run it again if you close the window (or want another Chrome, for some reason).

# In[1]:


from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


# In[2]:



driver = webdriver.Chrome()


# In[3]:





# ## Part 1: Scraping by class
# 
# Scrape the content at http://jonathansoma.com/lede/static/by-class.html, printing out the title, subhead, and byline.

# In[3]:


driver.get('http://jonathansoma.com/lede/static/by-class.html')


# In[4]:


title = driver.find_elements_by_tag_name("h1")
for each_title in title:
    print(each_title.text.strip())


# In[5]:


subhead = driver.find_elements_by_tag_name("h3")
for sub in subhead:
    print(sub.text.strip())


# In[6]:


byline = driver.find_elements_by_class_name("byline")
for by in byline:
    print(by.text.strip())


# ## Part 2: Scraping using tags
# 
# Scrape the content at http://jonathansoma.com/lede/static/by-tag.html, printing out the title, subhead, and byline.

# In[8]:


title = driver.find_elements_by_tag_name("p")
for each_title in title:
    print(each_title.text.strip())


# In[ ]:





# In[ ]:





# ## Part 3: Scraping using a single tag
# 
# Scrape the content at http://jonathansoma.com/lede/static/by-list.html, printing out the title, subhead, and byline.
# 
# > **This will be important for the next few:** if you scrape multiples, you have a list. Even though it's Seleninum, you can use things like `[0]`, `[1]`, `[-1]` etc just like you would for a normal list.

# In[9]:


driver.get('http://jonathansoma.com/lede/static/by-list.html')


# In[10]:


each = driver.find_elements_by_tag_name("p")
title = each[0].text
byline = each[2].text

print(title, byline)


# In[ ]:





# ## Part 4: Scraping a single table row
# 
# Scrape the content at http://jonathansoma.com/lede/static/single-table-row.html, printing out the title, subhead, and byline.

# In[11]:


driver.get('http://jonathansoma.com/lede/static/single-table-row.html')


# In[12]:


table = driver.find_elements_by_tag_name("td")
title = table[0].text
subhead = table[1].text
byline = table[2].text


# In[ ]:





# ## Part 5: Saving into a dictionary
# 
# Scrape the content at http://jonathansoma.com/lede/static/single-table-row.html, saving the title, subhead, and byline into a single dictionary called `book`.
# 
# > Don't use pandas for this one!

# In[13]:


driver.get('http://jonathansoma.com/lede/static/single-table-row.html')


# In[14]:


book = {}
table = driver.find_elements_by_tag_name("td")
book['title'] = table[0].text
book['subhead'] = table[1].text
book['byline'] = table[2].text
book


# In[ ]:





# ## Part 6: Scraping multiple table rows
# 
# Scrape the content at http://jonathansoma.com/lede/static/multiple-table-rows.html, printing out each title, subhead, and byline.
# 
# > You won't use pandas for this one, either!

# In[15]:


driver.get('http://jonathansoma.com/lede/static/multiple-table-rows.html')


# In[16]:


table = driver.find_elements_by_tag_name("tr")[1]
print(table.text)
# for each in table:
#     title = each.text
#     print(title[0])


# In[17]:


table = driver.find_elements_by_tag_name("td")
table[0].text


# ## Part 7: Scraping an actual table
# 
# Scrape the content at http://jonathansoma.com/lede/static/the-actual-table.html, creating a list of dictionaries.
# 
# > Don't use pandas here, either!

# In[18]:


driver.get('http://jonathansoma.com/lede/static/the-actual-table.html')


# In[32]:


table = driver.find_elements_by_tag_name("td")
table[1].text
row_list = []

#To list
for each in table:
    row = each.text
    row_list.append(row)

    
#To dictionary

big_list = []
for x in range(0,9, 3):
    row_dict = {}
    row_dict['title'] = row_list[x]
    row_dict['subhead'] = row_list[x+1]
    row_dict['byline'] = row_list[x+2]
    big_list.append(row_dict)
    
big_list


# In[104]:



the_list = []
row = []
table = driver.find_elements_by_tag_name("td")
for x in table:
    meow = x.text
    row.append(meow)
#     book = {}
#     book['title'] = x[0].text
#     book['subhead'] = x[1].text
#     book['byline'] = x[2].text
# book
row


# In[ ]:





# ## Part 8: Scraping multiple table rows into a list of dictionaries
# 
# Scrape the content at http://jonathansoma.com/lede/static/the-actual-table.html, creating a pandas DataFrame.
# 
# > There are two ways to do this one! One uses just pandas, the other one uses the result from Part 7.

# In[33]:


import pandas as pd


# In[34]:


df = pd.DataFrame(big_list)
df.head()


# In[ ]:





# ## Part 9: Scraping into a file
# 
# Scrape the content at http://jonathansoma.com/lede/static/the-actual-table.html and save it as `output.csv`

# In[35]:


df.to_csv(index=False)


# In[ ]:





# In[ ]:




