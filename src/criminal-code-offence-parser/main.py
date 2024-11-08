import csv
from cc_rules_current import (
    check_offence_type,
    check_prelim_available,
    check_section_469_offence,
    check_cso_availablity,
    check_inadmissibility,
    check_dna_designation,
    check_discharge_available,
    check_intermittent_available,
    check_suspended_sentence_available,
    check_soira,
    check_proceeds_of_crime_forfeiture,
    check_absolute_jurisdiction_offence,
    check_section_164_forfeiture_order,
    check_prison_and_probation,
    check_fine_alone,
    check_fine_and_probation,
)

from utils import (
    parse_quantum,
)

from map import (
    CC_DISAMBIGUATION,
    CC_GRADUATED_OFFENCES
)

from constants import(
    STATUTE_CODES
)

# Open the CSV file
with open("data/cc-offences-2024-09-16.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    data = list(csvreader)

# Basic offence data
# row[0] = statutory code and section number
# row[1] = offence title
# row[2] = indictable minimum
# row[3] = indictable maximum
# row[4] = summary minimum
# row[5] = summary maximum
def generate_basic_offence_details(row):
    """
    Generates the basic offence details that every function call should 
    include.
    """
    offence_data = {}

    # Create the offence variables
    mode = check_offence_type(row)
    indictable_minimum_quantum = parse_quantum(row[2])
    indictable_maximum_quantum = parse_quantum(row[3])
    summary_minimum_quantum = parse_quantum(row[4])
    summary_maximum_quantum = parse_quantum(row[5])

    # Offence data
    offence_data["section"] = row[0]
    offence_data["description"] = row[1]
    offence_data["mode"] = mode
    offence_data["summary_minimum"] = summary_minimum_quantum
    offence_data["summary_maximum"] = summary_maximum_quantum
    offence_data["indictable_minimum"] = indictable_minimum_quantum
    offence_data["indictable_maximum"] = indictable_maximum_quantum

    return offence_data


def generate_procedure_details(row):
    """
    Generates basic information about procedural rights or requirements for 
    certain offences.
    """
    procedure_data = {}

    # Create the offence variables
    prelim_available = check_prelim_available(row[3])
    section_469_offence = check_section_469_offence(row[0])

    procedure_data["prelim_available"] = prelim_available
    procedure_data["absolute_jurisdiction"] = (
        check_absolute_jurisdiction_offence(row[0])
    )
    procedure_data["release_by_superior_court_judge"] = section_469_offence

    return procedure_data


def generate_sentencing_details(row):
    """
    Generates basic information about sentencing options for certain offences.
    """
    sentencing_data = {}

    # Create the offence variables
    mode = check_offence_type(row)
    indictable_minimum_quantum = parse_quantum(row[2])
    indictable_maximum_quantum = parse_quantum(row[3])
    summary_minimum_quantum = parse_quantum(row[4])

    sentencing_data["cso_available"] = check_cso_availablity(
        row[0],
        summary_minimum_quantum,
        indictable_minimum_quantum,
        indictable_maximum_quantum,
        mode,
    )
    sentencing_data["intermittent_available"] = check_intermittent_available(
        summary_minimum_quantum, indictable_minimum_quantum
    )
    sentencing_data["suspended_sentence_available"] = check_suspended_sentence_available(
        summary_minimum_quantum, indictable_minimum_quantum
    )
    sentencing_data["discharge_available"] = check_discharge_available(
        summary_minimum_quantum, 
        indictable_minimum_quantum, 
        indictable_maximum_quantum
    )
    sentencing_data["prison_and_probation_available"] = check_prison_and_probation(
        mode,
        indictable_minimum_quantum,
    )
    sentencing_data["fine_alone"] = check_fine_alone(
        indictable_minimum_quantum,
        indictable_minimum_quantum,
    )
    sentencing_data["fine_and_probation"] = check_fine_and_probation(
        indictable_minimum_quantum,
    )

    return sentencing_data


def generate_ancillary_order_details(row):
    """
    Generates basic information about ancillary orders for certain offences.
    """
    ancillary_order_data = {}

    mode = check_offence_type(row)
    indictable_maximum_quantum = parse_quantum(row[3])

    ancillary_order_data["dna_designation"] = check_dna_designation(row, mode, indictable_maximum_quantum)
    ancillary_order_data["soira"] = check_soira(row[0], mode, indictable_maximum_quantum)
    ancillary_order_data["proceeds_of_crime_forfeiture"] = check_proceeds_of_crime_forfeiture(row[0], mode)
    ancillary_order_data["section_164.2_forfeiture_order"] = check_section_164_forfeiture_order(row[0])

    return ancillary_order_data


def generate_collateral_consequence_details(row):
    """
    Generates basic information about collateral consequences for certain offences.
    """
    collateral_consequence_data = {}

    mode = check_offence_type(row)
    indictable_maximum_quantum = parse_quantum(row[3])

    collateral_consequence_data["inadmissibility"] = check_inadmissibility(
        row[0], mode, indictable_maximum_quantum["jail"]["amount"]
    )

    return collateral_consequence_data


def parse_offence(
        offence,
        mode="summary",
        full=False,
        procedure=False,
        ancillary_orders=False,
        sentencing=False,
        collateral_consequences=False,
):
    """
    Parse the offence data for a given offence. Updated for modularity and 
    increased functionality. Now returns a list of dictionaries, which accounts
    for ambiguous and imperfect user input.

    By default, returns only `offence_data`. Additional categories can be added by
    setting `procedure`, `ancillary_orders`, `sentencing`, or 
    `collateral_consequences` to True. Setting `full` to True will return all 
    categories.
    """

    def offence_parser(row):
        parsed_offence = {
            "offence_data": generate_basic_offence_details(row)
        }

        if full or procedure:
            parsed_offence["procedure"] = generate_procedure_details(row)

        if full or sentencing:
            parsed_offence["sentencing"] = generate_sentencing_details(row)

        if full or ancillary_orders:
            parsed_offence["ancillary_orders"] = generate_ancillary_order_details(row)

        if full or collateral_consequences:
            parsed_offence["collateral_consequences"] = generate_collateral_consequence_details(row)

        return parsed_offence

    offence = offence.strip().lower()
    parsed_offence_list = []
    
    # Check to see if the offence is in the data. If not, check if it is a key in the
    # disambiguation or graduated offences dictionaries. Offences in these dictionaries
    # will be in list format. The program will need to cycle through each offence in the
    # list and add the results of the parser to the parsed_offence_list.

    for row in data:
        if row[0] == offence:
            parsed_offence_list.append(offence_parser(row))
            return parsed_offence_list
        
    if offence in CC_DISAMBIGUATION:
        for disambiguated_offence in CC_DISAMBIGUATION[offence]:
            for row in data:
                if row[0] == disambiguated_offence:
                    parsed_offence_list.append(offence_parser(row))
        return parsed_offence_list
    
    if offence in CC_GRADUATED_OFFENCES:
        for graduated_offence in CC_GRADUATED_OFFENCES[offence]:
            for row in data:
                if row[0] == graduated_offence:
                    parsed_offence_list.append(offence_parser(row))
        return parsed_offence_list

def report(offence_code):
    """
    Generates a human-readable report from the offence parser data
    """
    offence_list = parse_offence(offence_code, full=True)

    for offence in offence_list:
        statute_code = offence["offence_data"]["section"].split("_")[0]
        section_number = offence["offence_data"]["section"].split("_")[1]
        statute_name = STATUTE_CODES[statute_code]["name"]
        offence_name = offence["offence_data"]["description"]

        if statute_code in STATUTE_CODES:
            print(f"{statute_name} s. {section_number} — {offence_name.title()}")
            

