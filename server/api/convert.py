from ofxparse import OfxParser
from os import path
import xlsxwriter
import codecs
import sys
import io
import base64
import pandas as pd

def convert_file(instance, encoding='utf-8'):
    filename = instance['filename'].split('.')[0]
    content = instance['base64content']
    format = instance['format']
    file_io = decode_string_to_byte_io(content)
    new_io = get_csv_from_bytes(file_io)
    result = {"filename": f'{filename}{format}', "base64content": encode_byte_io_to_string(new_io)}
    return result

def get_csv_from_bytes(bytes):
    data = get_array_from_ofx(bytes)
    new_io = get_csv_from_data_frame(data)
    return new_io

def get_array_from_ofx(ofx_file):
    obj = OfxParser.parse(ofx_file)
    account = obj.account
    statement = account.statement
    transactions = statement.transactions
    columns = list(transactions[0].__dict__.keys())
    result = []
    for transaction in transactions:
        values = list(transaction.__dict__.values())
        result.append(values)

    return pd.DataFrame(result, columns=columns)

def get_csv_from_data_frame(df):
    output = io.BytesIO()
    df.to_csv(output)
    output.seek(0)
    return output

def create_sheet_from_array(data):
	output = io.BytesIO()
	workbook = xlsxwriter.Workbook(output)
	worksheet = workbook.add_worksheet()

	for row in range(len(data)):
		for col in range(len(data[row])):
			value = data[row][col]
			worksheet.write(row, col, value)

	workbook.close()
	output.seek(0)
	return output

def decode_string_to_byte_io(string, encoding='utf-8'):
    return io.BytesIO(base64.b64decode(string))

def encode_byte_io_to_string(bytes_io, encoding='utf-8'):
    return base64.b64encode(bytes_io.getvalue()).decode()
