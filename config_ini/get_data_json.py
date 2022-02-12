import os
import configparser
import glob
import chardet
from pprint import pprint
import json
import traceback
import time


def get_file_encoding(file):
	with open(file, 'rb') as f:
		data = f.read()
		encoding = chardet.detect(data)['encoding']
		return encoding


def add_product_types(files):
	data_lst = []
	# 用来查重
	product_type_names = []

	for index, file in enumerate(files):
		encoding = get_file_encoding(file)
		# RawConfigParser可以解决配置文件中有%符号的报错
		config = configparser.RawConfigParser()
		config.read(file, encoding=encoding)
		tmp = {
			'id': str(index+1),
			"ChName": config.get('global', "productTypeCh"),
			"EnName": config.get('global', "productTypeEn"),
			}
		if tmp['EnName'] not in product_type_names:
			data_lst.append(tmp)
			product_type_names.append(tmp['EnName'])

	return data_lst


# s = '1,2,3'
def get_array_from_str(s):
	s = s.lstrip().rstrip()
	s = s.split(',')
	return s


def get_leadTimes_lst_from_start_end_interval(leadTimes):
	start = int(leadTimes[0])
	end = int(leadTimes[1])
	interval = int(leadTimes[2])
	if interval != 0:
		tmp = [*range(start, end + 1, interval)]
		leadTimes_lst = [str(x).zfill(3) for x in tmp]
	else:
		leadTimes_lst = ['000']
	return leadTimes_lst


def if_product_exsit(data_lst, product_type_name, product_name):
	try:
		product_type_json = list(filter(lambda x: x['EnName'] == product_type_name, data_lst))
		products = product_type_json['products']
		for product_ in products:
			if product_['EnName'] == product_name:
				return True
		return False
	except:
		# 假设上述跑不通即没有products，说明还没有任何产品
		return False


def add_products(files, data_lst):
	for index, file in enumerate(files):
		encoding = get_file_encoding(file)
		# RawConfigParser可以解决配置文件中有%符号的报错
		config = configparser.RawConfigParser()
		config.read(file, encoding=encoding)

		product_type_name = config.get('global', "productTypeEn")
		levels_str = config.get('global', "levels")
		leadTimes_str = config.get('global', "leadTimes")
		ChName = config.get('global', "productNameCh")
		EnName = config.get('global', "productNameEn")
		levels_lst = get_array_from_str(levels_str)
		leadTimes_lst = get_leadTimes_lst_from_start_end_interval(get_array_from_str(leadTimes_str))

		tmp = {
			'id': str(index+1),
			"ChName": ChName,
			"EnName": EnName,
			'levels': levels_lst,
			'leadTimes': leadTimes_lst,
			}
		if not if_product_exsit(data_lst, product_type_name, EnName) :
			for index, data_ in enumerate(data_lst):
				if data_['EnName'] == product_type_name:
					try:
						data_lst[index]['products'].append(tmp)
					except:
						data_lst[index]['products'] = [tmp]
	return data_lst


def add_iniTimes(data_lst):
	for index_product_type, data_ in enumerate(data_lst):
		product_type_name = data_['EnName']
		products = data_['products']
		for index_product, product in enumerate(products):
			product_name = product['EnName']
			dates = os.listdir('/data/users/qhyu/ocean_web/products/' + product_type_name + "/" + product_name)
			dates.sort(reverse=True)
			data_lst[index_product_type]['products'][index_product]['iniTimes'] = dates
	return data_lst


def update_data_json():
	files = glob.glob('./config*.ini')
	files.sort()

	data_lst = add_product_types(files)
	data_lst = add_products(files, data_lst)
	data_lst = add_iniTimes(data_lst)

	with open("/data/users/qhyu/ocean_web/ocean_web/src/assets/data/data.json", "w", encoding="utf-8") as fout:
		json.dump(data_lst, fout, )


if __name__ == '__main__':
	while True:
		try:
			update_data_json()
			print("done")
		except:
			print(traceback.format_exc())
		# print("waiting...")
		# time.sleep(5)
