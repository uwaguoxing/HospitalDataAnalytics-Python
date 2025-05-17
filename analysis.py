'''This is the code designed to solve the Tasks for the given project.'''

def read_csvfile(CSVfile):
    # Read CSV file, prevent the CSV file from being opened multiple times.
    with open(CSVfile, 'r', encoding='utf-8') as csvfile:
        csv_lines = csvfile.readlines()

    # Check if the CSV file is empty or it only contains the header
    if not csv_lines or len(csv_lines) == 1: # If the csvfile only contains a header or is empty
        raise ValueError("Error: The CSV file is empty or only contains a header, please enter a valid CSV file.")
    
    return csv_lines

def read_txtfile(TXTfile):
    # Read TXT file, prevent the TXT file from being opened multiple times.
    with open(TXTfile, 'r', encoding='utf-8') as txtfile:
        txt_lines = txtfile.readlines()
        
    # Check if the TXT file is empty
    if not txt_lines:  # If the list is empty
        raise ValueError("Error: The TXT file is empty, please enter a valid TXT file.")
    
    return txt_lines

def Task1(CSVfile, TXTfile):
    # Initialize the output dictionaries
    Country_to_hospitals = {}
    Country_to_death = {}
    Country_to_covid_stroke = {}

    # Read files by using read_csvfile and read_txtfile functions
    csv_lines = read_csvfile(CSVfile)
    txt_lines = read_txtfile(TXTfile)

    # Process CSV file
    header = csv_lines[0].strip().split(',')
    country_idx = header.index('country')
    hospital_id_idx = header.index('hospital_ID')
    death_2022_idx = header.index('No_of_deaths_in_2022')
    
    # Create the dictionaries Country_to_hospitals and Country_to_death
    for line in csv_lines[1:]:
        data = line.strip().split(',')
        
        # Check if each line is valid
        if not data[country_idx]:
            continue # Skip this line where the country name is empty
        else:
            country = data[country_idx].lower()
        if not data[hospital_id_idx]:
            hospital_id = None # If the hospital ID is empty, set it as None
        else:
            hospital_id = data[hospital_id_idx]
        if not data[death_2022_idx] or int(data[death_2022_idx])< 0:
            deaths_2022 = 0 # If the death number in 2022 is empty or less than 0, set it as 0
        else:
            deaths_2022 = int(data[death_2022_idx])

        # Update Country_to_hospitals dictionary
        if country not in Country_to_hospitals: # If this is a new key, initialise it
            Country_to_hospitals[country] = []
            Country_to_death[country] = []
        
        Country_to_hospitals[country].append(hospital_id)
        Country_to_death[country].append(deaths_2022)
    # Process TXT file and create the third dictionary Country_to_covid_stroke
    for line in txt_lines:
        # Extract data from each line
        parts = line.strip().split(', ')
        # Ensure the parts are correctly formatted
        if len(parts) < 4 or ':' not in parts[0] or ':' not in parts[1] or ':' not in parts[2] or ':' not in parts[3]:
            continue  # Skip lines which format is incorrect
        country = parts[0].split(':')[1].lower()
        hospital_id = parts[1].split(':')[1].lower()
        covid_cases = int(parts[2].split(':')[1])
        stroke_cases = int(parts[3].split(':')[1])

        # Calculate total number of covid and stroke cases
        total_covid_stroke = covid_cases + stroke_cases

        # Update Country_to_covid_stroke dictionary
        if country not in Country_to_covid_stroke:
            Country_to_covid_stroke[country] = []

        Country_to_covid_stroke[country].append(total_covid_stroke)

    # Ensure the dictionaries are aligned
    return [Country_to_hospitals, Country_to_death, Country_to_covid_stroke]

def Task2(CSVfile, TXTfile):
    # Initialize dictionary
    Cosine_dict = {}
        
    #  Retrieve data from the Task1 function
    Country_to_hospitals, Country_to_death, Country_to_covid_stroke = Task1(CSVfile, TXTfile)
    
    cosine_similarity = 0.0
    # Calculate cosine similarity for each country
    for Country in Country_to_death:
        deaths = Country_to_death[Country]
        covid_stroke = Country_to_covid_stroke[Country]

        # Ensure both lists have the same length
        if len(deaths) == len(covid_stroke):
            numerator = 0.0
            square_sum_x = 0.0
            square_sum_y = 0.0
            for i in range(len(deaths)):
                numerator += deaths[i] * covid_stroke[i]            
            for i in range(len(deaths)):
                square_sum_x += deaths[i] ** 2
            for i in range(len(covid_stroke)):
                square_sum_y += covid_stroke[i] ** 2

            # Avoid division by zero
            try:
                cosine_similarity = numerator / ((square_sum_x ** 0.5) * (square_sum_y ** 0.5))
                Cosine_dict[Country] = round(cosine_similarity, 4)
            except ZeroDivisionError:
                Cosine_dict[Country] = 0.0 # If the denominator is 0, set the cosine as 0.00
            # Store result in Cosine_dict
        else:
            Cosine_dict[Country] = 0.0 # If the length of the lists is not the same, set the cosine as 0.00
    return Cosine_dict

def Task3(CSVfile, TXTfile, category):
    # Initialize dictionary
    Variance_dict = {}
    
    # Read files using read_csvfile and read_txtfile functions
    csv_lines = read_csvfile(CSVfile)
    txt_lines = read_txtfile(TXTfile)

    # Process CSV file
    header = csv_lines[0].strip().split(',')
    country_idx = header.index('country')
    hospital_id_idx = header.index('hospital_ID')
    category_idx = header.index('hospital_category')
    
    # Create a dictionary to store hospitals by category
    hospital_category_dict = {}

    for line in csv_lines[1:]:
        data = line.strip().split(',')
        # Check if each line is valid
        if not data[country_idx]:
            continue # Skip this line where the country name is empty
        else:
            csv_country = data[country_idx].lower()
        if not data[hospital_id_idx]:
            csv_hospital_id = None # If the hospital ID is empty, set it as None
        else:
            csv_hospital_id = data[hospital_id_idx].lower()
        if not data[category_idx]:
            hospital_category = None
        else:
            hospital_category = data[category_idx].lower()
        
        if hospital_category == category.lower():
            hospital_category_dict[csv_hospital_id] = csv_country
    # Process TXT file and create the a dictionary Variance_dict
    country_cancer_cases = {}
    for line in txt_lines:
        # extract data from each line
        parts = line.strip().split(', ')
        # Ensure the parts are correctly formatted
        if len(parts) < 4 or ':' not in parts[0] or ':' not in parts[1] or ':' not in parts[2] or ':' not in parts[3]:
            continue  # Skip lines which format is incorrect
        txt_country = parts[0].split(':')[1].strip().lower()
        txt_hospital_id = parts[1].split(':')[1].strip().lower()
        cancer_cases = int(parts[4].split(':')[1])
        
        # Check if the hospital belongs to the specified category
        if txt_hospital_id in hospital_category_dict and hospital_category_dict[txt_hospital_id] == txt_country:
            if txt_country not in country_cancer_cases:
                country_cancer_cases[txt_country] = []
            country_cancer_cases[txt_country].append(cancer_cases)       
    # Calculate the variance
    for country, cases in country_cancer_cases.items():
        if len(cases) > 1:
            mean = sum(cases) / len(cases)
            squared_deviation = sum((cancer_case - mean) ** 2 for cancer_case in cases)
            variance = squared_deviation / (len(cases) - 1)
        else:
            ## If there's only one hospital in this country, the variance is invalid, so set it to 0.0
            variance = 0.0
        Variance_dict[country] = round(variance, 4)
    return Variance_dict

def Task4(CSVfile, category):
    # Initialize dictionaries
    Category_Country_dict = {}
    
    # Read csvfile using read_csvfile function
    csv_lines = read_csvfile(CSVfile)
    
    # Process CSV file
    header = csv_lines[0].strip().split(',')    
    category_idx = header.index('hospital_category')
    country_idx = header.index('country')
    female_idx = header.index('female_patients')
    staff_idx = header.index('no_of_staff')
    deaths2022_idx = header.index('No_of_deaths_in_2022')
    deaths2023_idx = header.index('No_of_deaths_in_2023')
    
    # Process CSV lines to gather data for each category
    for line in csv_lines[1:]:
        
        data = line.strip().split(',')
        # Check if each line is valid
        # If the data is empty, or the numeric data is less than 1, set it as 0
        if not data[category_idx]:
            hospital_category = None
        else:
            hospital_category = data[category_idx].lower()
        if not data[country_idx]:
            country = None
        else:
            country = data[country_idx].lower()
        if not data[female_idx] or float(data[female_idx]) <= 0:            
            female_patients = 0.0
        else:
            female_patients = float(data[female_idx])
        if not data[staff_idx] or int(data[staff_idx]) <= 0:
            staff_count = 0
        else:
            staff_count = int(data[staff_idx])
        if not data[deaths2022_idx] or float(data[deaths2022_idx]) <= 0:
            deaths_2022 = 0.0
        else:
            deaths_2022 = float(data[deaths2022_idx])
        if not data[deaths2023_idx] or float(data[deaths2023_idx]) <= 0:
            deaths_2023 = 0.0
        else:
            deaths_2023 = float(data[deaths2023_idx])
        
        if hospital_category == category.lower():
            if hospital_category not in Category_Country_dict:
                Category_Country_dict[hospital_category] = {}
            if country not in Category_Country_dict[hospital_category]:
                Category_Country_dict[hospital_category][country] = {} 
                Category_Country_dict[hospital_category][country]['total_female_patients'] = 0
                Category_Country_dict[hospital_category][country]['total_deaths_2023'] = 0
                Category_Country_dict[hospital_category][country]['max_staff'] = 0
                Category_Country_dict[hospital_category][country]['total_deaths_2022'] = 0
                Category_Country_dict[hospital_category][country]['hospital_count'] = 0
                
                '''That's what the structure of Category_Country_dict[hospital_category][country] looks like:
            Category_Country_dict[hospital_category][country] = {
                    'total_female_patients': 0,
                    'max_staff': 0,
                    'total_deaths_2022': 0,
                    'total_deaths_2023': 0,
                    'hospital_count': 0
                }'''
                
            Category_Country_dict[hospital_category][country]['total_female_patients'] += female_patients
            if staff_count > Category_Country_dict[hospital_category][country]['max_staff']:
                Category_Country_dict[hospital_category][country]['max_staff'] = staff_count
            Category_Country_dict[hospital_category][country]['total_deaths_2022'] += deaths_2022
            Category_Country_dict[hospital_category][country]['total_deaths_2023'] += deaths_2023
            Category_Country_dict[hospital_category][country]['hospital_count'] += 1
    
    # Calculate the final value
    for Category in Category_Country_dict:
        inner_dict = {} # Initialise the inner nested dictionary
        for Country in Category_Country_dict[Category]:
            # Execute exception handling for division by zero. Set the output to an empty list. 
            try:
                avg_female_patients = Category_Country_dict[Category][Country]['total_female_patients'] / Category_Country_dict[Category][Country]['hospital_count']
            except ZeroDivisionError:
                inner_dict[Country] = []
            try:
                avg_deaths_2022 = Category_Country_dict[Category][Country]['total_deaths_2022'] / Category_Country_dict[Category][Country]['hospital_count']
                avg_deaths_2023 = Category_Country_dict[Category][Country]['total_deaths_2023'] / Category_Country_dict[Category][Country]['hospital_count']            
                PCAD = ((avg_deaths_2023 - avg_deaths_2022) / avg_deaths_2022) * 100
            except ZeroDivisionError:
                inner_dict[Country] = []
                
                continue # Skip this Coutnry which data is invalid
            inner_dict[Country] = [round(avg_female_patients, 4), Category_Country_dict[Category][Country]['max_staff'], round(PCAD, 4)]
        Category_Country_dict[Category] = inner_dict # Update the output dictionary
    
    return Category_Country_dict

def main(CSVfile, TXTfile, category):
    OP1 = Task1(CSVfile, TXTfile)
    OP2 = Task2(CSVfile, TXTfile)
    OP3 = Task3(CSVfile, TXTfile, category)
    OP4 = Task4(CSVfile, category)
    return OP1, OP2, OP3, OP4