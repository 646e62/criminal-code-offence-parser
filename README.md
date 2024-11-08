# criminal-code-offence-parser
## Overview
Offence analysis tools for *Criminal Code*, RSC 1985, c C-46 and related statutes.

The program provides domain-specific expert inferences with human-readable explanations for the results. The program's tools are functions that translate statutory legal logic into computational logic. The provided explanations include citations to the statute where the unformatted legislative logic is located.

The tools will work as intended when they return accurate results with complete explanations of the program's logic.

## Examples
### Basic call
As of v0.0.5, the main function call provides customizable output. The program call will always produce basic offence information:

```python
> from main import parse_offence
> parse_offence("cc266")
{'offence_data': {'section': 'cc266',
  'description': 'assault',
  'mode': 'hybrid',
  'summary_minimum': {'amount': None, 'unit': None},
  'summary_maximum': {'amount': '729', 'unit': 'days'},
  'indictable_minimum': {'amount': None, 'unit': None},
  'indictable_maximum': {'amount': '5', 'unit': 'years'},
  'absolute_jurisdiction': [{'status': {'absolute_jurisdiction': False,
     'notes': None},
    'section': 'cc553',
    'notes': None}]}}
```

### Arguments

Adding an argument will append the requested information to the basic offence details:

```python
> parse_offence("cc151", collateral_consequences=True)
{'offence_data': {'section': 'cc151',
  'description': 'sexual interference',
  'mode': 'hybrid',
  'summary_minimum': {'amount': '90', 'unit': 'days'},
  'summary_maximum': {'amount': '729', 'unit': 'days'},
  'indictable_minimum': {'amount': '1', 'unit': 'years'},
  'indictable_maximum': {'amount': '14', 'unit': 'years'},
  'absolute_jurisdiction': [{'status': {'absolute_jurisdiction': False,
     'notes': None},
    'section': 'cc553',
    'notes': None}]},
 'collateral_consequences': {'inadmissibility': [{'section': 'irpa36(1)',
    'status': 'permanent resident',
    'notes': 'serious criminality'},
   {'section': 'irpa36(1)',
    'status': 'foreign national',
    'notes': 'serious criminality'},
   {'section': 'irpa36(2)',
    'status': 'foreign national',
    'notes': 'criminality'}]}}
```

Currently, arguments include `procedure`, `sentencing`, `ancillary_orders`, `collateral_consequences`, and `full`. 

### Multiple arguments

The program accepts multiple arguments, and will append them to the basic offence details:

```python
> parse_offence("cc811", ancillary_orders=True, procedure=True)
{'offence_data': {'section': 'cc811',
  'description': 'breach of recognizance',
  'mode': 'hybrid',
  'summary_minimum': {'amount': None, 'unit': None},
  'summary_maximum': {'amount': '729', 'unit': 'days'},
  'indictable_minimum': {'amount': None, 'unit': None},
  'indictable_maximum': {'amount': '4', 'unit': 'years'},
  'absolute_jurisdiction': [{'status': {'absolute_jurisdiction': False,
     'notes': None},
    'section': 'cc553',
    'notes': None}]},
 'procedure': {'prelim_available': {'status': ({'available': False,
     'notes': None},),
   'section': 'cc535',
   'notes': 'maximum term of less than 14y'},
  'release_by_superior_court_judge': False},
 'ancillary_orders': {'dna_designation': {'status': ({'available': False,
     'notes': None},),
   'section': 'cc487.04',
   'notes': 'not a designated offence'},
  'soira': None,
  'proceeds_of_crime_forfeiture': [{'section': ['cc462.3[designated offence]',
     'cc462.37(1)'],
    'status': 'available',
    'notes': 'offence prosecutable by indictment'}],
  'section_164.2_forfeiture_order': []}}
```

### Full output

Using the `full` argument will return all offence information:

```python
> parse_offence("cc172.2", full=True)
{'offence_data': {'section': 'cc172.2',
  'description': 'agreement or arrangement — sexual offence against child',
  'mode': 'hybrid',
  'summary_minimum': {'amount': 180, 'unit': 'days'},
  'summary_maximum': {'amount': '729', 'unit': 'days'},
  'indictable_minimum': {'amount': 365, 'unit': 'days'},
  'indictable_maximum': {'amount': 14, 'unit': 'years'},
  'absolute_jurisdiction': [{'status': {'absolute_jurisdiction': False,
     'notes': None},
    'section': 'cc553',
    'notes': None}]},
 'procedure': {'prelim_available': {'status': ({'available': True,
     'notes': None},),
   'section': 'cc535',
   'notes': 'maximum prison term of 14y or greater'},
  'release_by_superior_court_judge': False},
 'sentencing': {'cso_available': {'status': ({'available': False,
     'notes': None},),
   'section': 'cc742.1(b)',
   'notes': 'mandatory minimum term of imprisonment'},
  'intermittent_available': {'status': ({'available': False, 'notes': None},),
   'section': 'cc732(1)',
   'notes': 'mandatory minimum term of imprisonment exceeds 90 days'},
  'suspended_sentence_available': {'status': ({'available': False,
     'notes': None},),
   'section': 'cc731(1)',
   'notes': 'mandatory minimum sentence'},
  'discharge_available': {'status': ({'available': False, 'notes': None},),
   'section': 'cc730(1)',
   'notes': 'mandatory minimum sentence'},
  'prison_and_probation_available': {'status': ({'available': True,
     'notes': None},),
   'section': 'cc732(1)',
   'notes': None},
  'fine_alone': {'status': ({'available': False, 'notes': None},),
   'section': 'cc734(1)',
   'notes': 'mandatory minimum term of imprisonment'},
  'fine_and_probation': {'status': ({'available': True, 'notes': None},),
   'section': 'cc732(1)',
   'notes': None}},
 'ancillary_orders': {'dna_designation': {'status': ({'available': True,
     'notes': None},),
   'section': 'cc487.04',
   'notes': 'primary designated offence'},
  'soira': [{'section': ['cc490.011[primary offence](a)', 'cc490.011(2)(b)'],
    'status': 'primary',
    'notes': 'primary designated offence',
    'duration': {'amount': 20, 'unit': 'years'}}],
  'proceeds_of_crime_forfeiture': [{'section': ['cc462.3[designated offence]',
     'cc462.37(1)'],
    'status': 'available',
    'notes': 'offence prosecutable by indictment'}],
  'section_164.2_forfeiture_order': [{'section': 'cc164.2',
    'notes': 'enumerated offence'}]},
 'collateral_consequences': {'inadmissibility': [{'section': 'irpa36(1)',
    'status': 'permanent resident',
    'notes': 'serious criminality'},
   {'section': 'irpa36(1)',
    'status': 'foreign national',
    'notes': 'serious criminality'},
   {'section': 'irpa36(2)',
    'status': 'foreign national',
    'notes': 'criminality'}]}}
```
