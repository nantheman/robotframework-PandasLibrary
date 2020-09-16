*** Settings ***
Documentation   This robot file is for the verification of the Pandas Library
Library    PandasLibrary
Suite Setup    Set Index   data.csv  id   csv


*** Test Cases ***
Test read all content
    [Documentation]   Test to read all rows and columns  from the data
    Log To Console    Start Test
    ${return_data}=    Read all content
    Log to Console    Returned value is ${return_data}

Test read all rows
    [Documentation]   Test to read all rows from the data
    Log To Console    Start Test
    ${return_data}=    Read all rows   first_name
    Log to Console    Returned value is ${return_data}

Test read all column
    [Documentation]   Test to read all columns  from the data
    Log To Console    Start Test
    ${row}=   Set Variable    10
    ${row}=   Convert To Integer    ${row}
    ${return_data}=    Read all columns    ${row}
    Log to Console    Returned value is ${return_data}

Test read row and column
    [Documentation]   Test to read particular rows and columns  from the data
    Log To Console    Start Test
    ${row}=   Set Variable    1
    ${row}=   Convert To Integer    ${row}
    ${return_data}=    Read row and column  ${row}  gender
    Log to Console    Returned value is ${return_data}

Test row and column size
    [Documentation]   Test to get the size of the data
    Log To Console    Start Test
    ${row_size}  ${column_size}    Get Row and Column size
    Log to Console    Row size is ${row_size} and column size is ${column_size}

Test head data
    [Documentation]   Test to get the head data
    Log To Console    Start Test
    ${row}=   Set Variable    5
    ${row}=   Convert To Integer    ${row}
    ${head_data}=   Read Head Data  ${row}
    Log to Console    Available data is ${head_data}

Test tail data
    [Documentation]   Test to get tail data
    Log To Console    Start Test
    ${row}=   Set Variable    5
    ${row}=   Convert To Integer    ${row}
    ${tail_data}=   Read Tail Data  ${row}
    Log to Console    Available data is ${tail_data}

Test row index
    [Documentation]   Test to get row index number
    Log To Console    verification of row index number
    ${column_name}=   Set Variable    last_name
    ${column_val}=   Set Variable    Morris
    @{data}=   Get Row Index   ${column_name}  ${column_val}
    Log to Console      Available data is @{data}[0]
	
Test read all content and header
    [Documentation]   Test to read all content and header
    Log To Console    Reading all content and header
    ${data}   ${hdr}   Read all content and header
    Log to Console      ${hdr}
    Log to Console      ${data}

Test Multiple data frame functions
    Log to Console   Start Test
    ${row}=   Set Variable  3
    ${row}=   Convert To Integer    ${row}
    ${rowd}=  Read row by index    ${row}
    Log to Console   ${rowd}
	Log to Console   Update last_name to Moreno
    ${colname}=  Set Variable  last_name
    ${return_data}=  Add or Update Column  ${rowd}  ${colname}  Moreno
    Log to Console   Returned value is ${return_data}
	Log to Console   Add column location as 3rd Column
    ${colname}=  Set Variable  location
    ${colloc}=   Convert To Integer    2
    ${return_data}=  Add or Update Column  ${rowd}  ${colname}  Tokyo  ${colloc}
    Log to Console   Returned value is ${return_data}
