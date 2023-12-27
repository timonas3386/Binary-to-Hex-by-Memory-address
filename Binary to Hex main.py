import csv

binary_file_path = 'mem_miss.csv'
output_csv_path = 'output.csv'

with open(binary_file_path, 'rb') as file:
    binary_data = file.read()
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerow(['Decimal Value', 'Hexadecimal Value'])
        item_length = 8
        for i in range(0, len(binary_data), item_length):
            item = binary_data[i:i+item_length]
            decimal_value = int.from_bytes(item, byteorder='little')
            
            hex_value = hex(decimal_value)
            csv_writer.writerow([decimal_value, hex_value])
            print('Running...[{:.2%}]'.format(i/(len(binary_data))),end = "\r")

print("Success! Save the output data to '{output_csv_path}'")
