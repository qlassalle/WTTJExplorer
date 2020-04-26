# How to run

Simply run 

```python main.py```

# Configuration

You should set your preference in `preferences.py`. This file is excluded from VCS to allow anyone to make his own
research and still contribute to this repository if wanted. The file should look like

```
EXCLUDED_CONTRACT_TYPE = ['Stage', 'CDD', 'INTERNSHIP']
# Name of the company you're not interested in. MUST BE IN LOWERCASE.
EXCLUDED_COMPANY = ['Bankin', 'ABC', '...']
EXCLUDED_COMPANY_SIZE = ['> 2000 salariés', '< 15 salariés']
# Name of the references to include. Some entries match your research but may not be interesting or relevant. Add the
# reference here and it won't appear again
EXCLUDED_REFERENCE = ['MATTE_ldmMwPW', 'MOODW_JkDzp2b', 'ALSID_w92q4PD']
```  