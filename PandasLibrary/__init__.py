#!/usr/bin/env python
###################################################################################################
# PandasLibrary is the library design to execute the pandas command to fetch data from the csv file.
###################################################################################################
import os
import datetime
import pandas as pd


class PandasLibrary(object):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self.index_name = None
        pass


    def set_index(self, file_name, index_name, file_type):
        '''
        Method to read the csv file and return the pandas dataframe.

        :param filename:  Name of CSV file
        :return  dataframe: Pandas dataframe of the csv file
        '''
        self.filename = file_name
        self.file_type = file_type
        self.index_name = index_name

    def read_all_rows(self, column):
        '''
        This get_message keyword "read_all_rows" which will return the data based on
        all the row datas and column names.

        :param column:  Name of column
        :return available_data: Return the data present in the row and column in the csv file.
        '''
        if self.file_type == 'xls':
            data_frame = pd.read_excel(self.filename, index_col=self.index_name)
        elif self.file_type == 'csv':
            data_frame = pd.read_csv(self.filename, index_col=self.index_name)
        else:
            return  "Please set index with filename and file type"

        available_data = data_frame.loc[:][column]
        return available_data

    def read_all_columns(self, row):
        '''
        This get_message keyword "read_all_columns" which will return the data
        based on row and all the column data.

        :param row:   Name of row
        :return available_data: Return the data present in the row and column in the csv file.
        '''
        if self.file_type == 'xls':
            data_frame = pd.read_excel(self.filename, index_col=self.index_name)
        elif self.file_type == 'csv':
            data_frame = pd.read_csv(self.filename, index_col=self.index_name)
        else:
            return  "Please set index with filename and file type"

        available_data = data_frame.loc[row][:]
        return available_data

    def read_all_content(self):
        '''
        This get_message keyword "read_all_content" which will return the data of all rows and
        columns of the file specified as a argument

        :param filename:  CSV fileName
        :return available_data: Return the data present in all the rows and columns from the file
        '''
        if self.file_type == 'xls':
            data_frame = pd.read_excel(self.filename, index_col=self.index_name)
        elif self.file_type == 'csv':
            data_frame = pd.read_csv(self.filename, index_col=self.index_name)
        else:
            return  "Please set index with filename and file type"

#        available_data = data_frame.loc[:][:]
#        return available_data

        return data_frame

    def read_all_content_and_header(self):
        '''
        This get_message keyword "read_all_content" which will return the data of all rows and
        columns including the column headers (as list) of the file specified as a argument

        :param filename:  CSV fileName
        :return available_data: Return the data present in all the rows and columns from the file
                                and a list of column names
        '''
        if self.file_type == 'xls':
            data_frame = pd.read_excel(self.filename, index_col=self.index_name)
        elif self.file_type == 'csv':
            data_frame = pd.read_csv(self.filename, index_col=self.index_name)
        else:
            return  "Please set index with filename and file type"

        return data_frame,data_frame.columns.tolist() 

    def read_row_and_column(self, row, column):
        '''
        This get_message keyword "read_row_and_column" which will return the
        data of particular rows and particular columns of the file specified as a argument.

        :param filename:  CSV fileName
        :param row:  Row name/number
        :param column: Column name/number
        :return available_data: Return the data present in row and column of the file
        '''
        if self.file_type == 'xls':
            data_frame = pd.read_excel(self.filename, index_col=self.index_name)
        elif self.file_type == 'csv':
            data_frame = pd.read_csv(self.filename, index_col=self.index_name)
        else:
            return  "Please set index with filename and file type"
        available_data = data_frame.loc[row][column]
        return available_data
    
    def get_row_and_column_size(self):
        '''
        This get_message keyword "get_row_and_column_size" which will return the
        number of rows and columns present in the file

        :param filename:  CSV fileName
        :return current_shape: Return the shape of the csv
        '''
        if self.file_type == 'xls':
            data_frame = pd.read_excel(self.filename, index_col=self.index_name)
        elif self.file_type == 'csv':
            data_frame = pd.read_csv(self.filename, index_col=self.index_name)
        else:
            return  "Please set index with filename and file type"
        current_shape = data_frame.shape
        return current_shape

    def read_head_data(self, head_value):
        '''
        This get_message keyword "read_head_data" which will return the
        data of particular rows and particular columns of the file specified as a argument.

        :param filename:  CSV fileName
        :param row:  Row name/number
        :param column: Column name/number
        :return available_data: Return the data present in row and column of the file
        '''
        if self.file_type == 'xls':
            data_frame = pd.read_excel(self.filename, index_col=self.index_name)
        elif self.file_type == 'csv':
            data_frame = pd.read_csv(self.filename, index_col=self.index_name)
        else:
            return  "Please set index with filename and file type"
        available_data = data_frame[:head_value]
        return available_data

    def read_tail_data(self, head_value):
        '''
        This get_message keyword "read_head_data" which will return the
        data of particular rows and particular columns of the file specified as a argument.

        :param filename:  CSV fileName
        :param row:  Row name/number
        :param column: Column name/number
        :return available_data: Return the data present in row and column of the file
        '''
        if self.file_type == 'xls':
            data_frame = pd.read_excel(self.filename, index_col=self.index_name)
        elif self.file_type == 'csv':
            data_frame = pd.read_csv(self.filename, index_col=self.index_name)
        else:
            return  "Please set index with filename and file type"
        available_data = data_frame[-head_value:]
        return available_data

    def upload_to_csv(self, testcase_id, status, testinfo=None, filename='test_report.csv'):
        '''
        This get_message keyword "upload_to_csv" which will
        upload the results into the csv file.

        :param testcase_id: Test Case ID
        :param status:   Test STATUS
        :param testinfo: Test Description

        example:-
        13 December 2019-  18:54:59	123	Pre-setup PASS

        '''
        # check the file status
        if not os.path.isfile(filename):
            new_frame = pd.DataFrame(columns=['TestCase', 'Test_status',
                                              'Execution_Time', 'Test_Info'])
            new_frame.to_csv(filename, index=False)
        # capture the current time
        today = datetime.datetime.now()
        current_time = str(today.strftime("%d %B %Y-  %H:%M:%S"))
        test_data = {'TestCase': [testcase_id], 'Test_status': [status],
                     'Execution_Time': [current_time], 'Test_Info': [testinfo]}
        data_frame = pd.DataFrame(test_data)
        data_frame.to_csv(filename, mode='a', index=False, header=False)
   
    def write_to_csv(self, data_frame, filename, writeheader=False):
        '''
        This get_message keyword "write_to_csv" which will append the dataframe into the csv file.
        :param data_frame: data frame with curated output
        :param filename:   Output file name
        :writeheader:      Useful when doing incremental writes. 

        '''
        # check the file status
        if not os.path.isfile(filename):
            data_frame.to_csv(filename, mode='w', index=False)
        else:
            data_frame.to_csv(filename, mode='a', index=False,header=False)

    def add_or_update_column(self, data_row, column_name, column_new_value, column_position=None):
        '''
        This get_message keyword "add_or_update_column" which will update the
        data of particular rows and particular columns of the file specified as a argument.

        :param filename:  CSV fileName
        :param data_row:  Row as dataframe
        :param column_name:  Column name
        :param column_new_value: Column value
        :column_position: Leave blank for last column (append) else column is inserted within frame
        :return amended data row
        '''
        if not column_position:
            data_row[column_name] = column_new_value
        else:
            data_row.insert(column_position,column_name,column_new_value)
        return data_row

    def get_column_value(self, data_row, column_name ):
        '''
        This get_message keyword "get_column_value" which will update the
        data of particular rows and particular columns of the file specified as a argument.

        :param data_row:  Single Row of data
        :param column_name: Column name
        :return column value: Return column value as a scalar 
        '''

        return data_row.iloc[0][column_name]
    
    def read_row_by_index(self, row_index):
        '''
        Keyword "read_row_by_index" returns the row as a dataframe for a row_index

        :param filename:  CSV fileName
        :param row_index:  Row index
        :return available_data: Data row as data_frame
        '''
        if self.file_type == 'xls':
            data_frame = pd.read_excel(self.filename, index_col=self.index_name)
        elif self.file_type == 'csv':
            data_frame = pd.read_csv(self.filename, index_col=self.index_name)
        else:
            return  "Please set index with filename and file type"
        return data_frame[data_frame.index == row_index]

    def get_index_value(self, data_row ):
        '''
        Keyword "get_index_value" returns the index value
        :param filename:  CSV fileName
        :param data_row: Row as data frame
        :return Row index
        '''
        return data_row.index
    
    def get_index_as_list(self):
        '''
        Keyword "get_index_as_list" returns the index column as a list which can be used 
        through the rows
        :param filename:  CSV fileName
        :return index values as list 

        '''
        if self.file_type == 'xls':
            data_frame = pd.read_excel(self.filename, index_col=self.index_name)
        elif self.file_type == 'csv':
            data_frame = pd.read_csv(self.filename, index_col=self.index_name)
        else:
            return  "Please set index with filename and file type"
        return data_frame.index.tolist()
		
    def add_to_dataframe(self, data_frame, data_row):
        '''
        Keyword "add_to_dataframe" builds a cumulative dataframe 
                (adds row to an existing data frame or builds a new one)
        :param filename:  CSV fileName
        :param data_frame: Data frame that was already built
        :param data_row: Data row (structure must match Data frame)
        :return: Cumulative data frame
        '''
        try:
            return data_frame.append(data_row)
        except:
            return data_row
        	
    def get_row_index(self, column_name, column_value):
        if self.file_type == 'xls':
            data_frame = pd.read_excel(self.filename, index_col=self.index_name)
        elif self.file_type == 'csv':
            data_frame = pd.read_csv(self.filename, index_col=self.index_name)
        else:
            return  "Please set index with filename and file type"

        available_data = data_frame.index[data_frame[column_name] == column_value].tolist()
        return available_data

    def _test():        
        print("Test pandas functions for csv/xls file read/update for use with robotframework")
        command = PandasLibrary()
        filename = 'data.csv'
        command.set_index(file_name="data.csv", index_name='id', file_type='csv')
        print("Reading all the contents:- ")
        print(command.read_all_content())
        print("Reading all the rows:-  ")
        print(command.read_all_rows('first_name'))
        print("Reading all the columns:-  ")
        print(command.read_all_columns(1))
        print("Reading particular row and columns:-  ")
        print(command.read_row_and_column(1, 'gender'))
        print("Reading CSV size")
        print(command.get_row_and_column_size())
        print("Reading CSV head data")
        print(command.read_head_data(10))
        print("Reading CSV tail data")
        print(command.read_tail_data(10))
        testcase_id= 1
        status='Fail'
        testinfo='test failed'
        command.upload_to_csv(testcase_id, status, testinfo)
		
        print("get_index_as_list " + str(command.get_index_as_list()))
        print("get the row index " + str(command.get_row_index('last_name', 'Morris')))
        print("read row by index (index=3)")
        tdf = command.read_row_by_index(3)
        print(tdf)
        print("add or update column - Update column value")
        print(command.add_or_update_column(tdf,'last_name','Moreno'))
        print("add or update column - Add column 'location' as 3rd column")
        print(command.add_or_update_column(tdf,'location','Tokyo',2))
        print("add_to_dataframe - df1 + df2")
        tdf3 = pd.DataFrame()
        print("add_to_dataframe - df1")
        tdf1 = command.read_row_by_index(1)
        print("add_to_dataframe - df2")
        tdf2 = command.read_row_by_index(2)
        tdf3 = command.add_to_dataframe(tdf3,tdf1)
        print("df1 + df2")
        print(command.add_to_dataframe(tdf3,tdf2))

        print("Modify data frame information and write to csv")
        tdf3 = pd.DataFrame()
        tdf = command.read_row_by_index(3)
        print(tdf)
        print("add or update column - Update column value")
        print(command.add_or_update_column(tdf,'last_name','Moreno'))
        print("add or update column - Add column 'location' as 3rd column")
        print(command.add_or_update_column(tdf,'location','Tokyo',2))
        tdf3 = command.add_to_dataframe(tdf3,tdf)
        tdf = command.read_row_by_index(2)
        print(tdf)
        print("add or update column - Add column 'location' as 3rd column")
        print(command.add_or_update_column(tdf,'location','Sao Paulo',2))
        tdf3 = command.add_to_dataframe(tdf3,tdf)
        print(tdf3)
        command.write_to_csv(tdf3, "test_cumreport.csv", writeheader=True)

if __name__ == '__main__':
    print(__main__)
    _test()
